import pyfiglet
from pytube import YouTube
import argparse
import sys
import os


class CLI_Downloader:
    _BANNER = pyfiglet.figlet_format("CLI-Yt")
    _mode = "Video"
    _resolution = "highest"
    _leave_flag = False
    _folder = os.path.join(os.getenv('USERPROFILE'), 'Downloads')

    def _parse_arguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-a", action='store_true',
                            help="Select downloading mode.")
        parser.add_argument("-l", action='store_true',
                            help="Download video with lowest resolution.")
        args = parser.parse_args()
        if args.a:
            self._mode = "Audio"
        if args.l:
            self._resolution = "lowest"

    def _download_video(self, link):
        try:
            video = YouTube(link)
            if self._mode == "Video":
                stream = video.streams.get_highest_resolution(
                ) if self._resolution == "highest" else video.streams.get_lowest_resolution()
                stream.download(output_path=self._folder,
                                filename=video.video_id)
            if self._mode == "Audio":
                video.streams.get_audio_only().download(output_path=self._folder,
                                                        filename=video.video_id + "_audio")
            print("Video downloaded successfully.")
        except Exception as e:
            print("Something went wrong. Printing stack trace.")
            print(e)
        print("Leave? Y - Yes / Other - No")
        _leave_input = input().lower()

        if _leave_input == "y" or _leave_input == "yes":
            self._leave_flag = True
        else:
            return

    def download(self):
        self._parse_arguments()
        print(self._BANNER)
        print("Current mode: " + self._mode + " / Quality: " + self._resolution)
        while self._leave_flag == False:
            print("Please insert the Youtube video link.")
            video_link = input()
            self._download_video(video_link)
        sys.exit()

os.system('cls' if os.name == 'nt' else 'clear')
downloader = CLI_Downloader()
downloader.download()
