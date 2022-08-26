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


class VideoConnectionError(Exception):
    def __init__(self):
        print("Connection Error......")


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
        video_name = (str(generateRandomNumber(0, 999))).join(video_name)
        output_file = "{0}{1}{2}".format(folder_path, video_name, extension)
    print(output_file)
    return output_file


if __name__ == '__main__':
    print('>>> Running in DEV MODE...')
    user_input = input('Enter a URL:')
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
