# videoDownload.py
#
# This module provides tools for downloading
# videos off of the internet.
import pathlib
import random
import regex as re
# standard libraries
import urllib.request
import yt_dlp

socialMediaFile = "SocialMedia.txt"


class VideoConnectionError(Exception):
    def __init__(self):
        print("Connection Error......")


class NotSocialMediaVideo(Exception):
    def __init__(self):
        print("Not a Social Media Video")


def generateRandomNumber(min_value: int, max_value: int):
    """
    :param min_value:
    :param max_value:
    :return: random Number to be concatenated with the file name
    """
    return random.randint(min_value, max_value)


def generteRandomFileName(extension: str = '.mp4', delimiter: str = '/', url: str = " ") -> str:
    """

    :param url:
    :param extension:
    :param delimiter:
    :param url:
    :return:
    """
    folder_path: str = 'Downloads/'
    video_name = re.sub('[^A-Za-z0-9]+', '', url.split(delimiter)[-1])
    output_file = "{0}{1}{2}".format(folder_path, video_name, extension)
    while pathlib.Path(output_file).exists():
        video_name = video_name.join(str(generateRandomNumber(0, 99)))
        output_file = "{0}{1}{2}".format(folder_path, video_name, extension)
    print("Downloading {0}".format(output_file.split(delimiter)[1]))
    return output_file


def checkSocialMediaVideo(url: str, delimiter: str = '/', www: str = 'www') -> bool:
    if url.split(delimiter)[2].split('.')[0] == www:
        sm = url.split(delimiter)[2].split('.')[1]
    else:
        sm = url.split(delimiter)[2].split('.')[0]
    with open(socialMediaFile, 'r') as file:
        if sm in file:
            print("{0} video.".format(sm))
            return True
        else:
            return False


if __name__ == '__main__':
    print('>>> Running in DEV MODE...')
    user_input = input('Enter a URL:')
    if checkSocialMediaVideo(user_input):
        file_name = generteRandomFileName(url=user_input)
        try:
            urllib.request.urlopen(user_input)
        except Exception:
            VideoConnectionError()

        # Download
        try:
            ydl_opts = {'outtmpl': file_name}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([user_input])
        except yt_dlp.utils.DownloadError:
            VideoConnectionError()
    else:
        NotSocialMediaVideo()
