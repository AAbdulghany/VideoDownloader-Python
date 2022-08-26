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

if __name__ == '__main__':
    print('>>> Running in DEV MODE...')
    user_input = input('Enter a URL:')
    try:
        urllib.request.urlopen(user_input)
    except Exception:
        VideoConnectionError()

    # Download
    try:
        ydl_opts = {'outtmpl': 'file_name.mp4'}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([user_input])
    except yt_dlp.utils.DownloadError:
        VideoConnectionError()
