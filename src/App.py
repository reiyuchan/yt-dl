from turtle import goto
from pytube import YouTube,Playlist

class YT_DL:
    def __init__(self, choice) -> None:
        self.choice = choice

    def dlSingle(self,singleUrl):
        self.yt = YouTube(
            singleUrl,
            use_oauth=False,
            allow_oauth_cache=False
            )
        print(f"Downloading video: {singleUrl}")
        print(f"Download in progress...!")
        self.yt.streams.filter(file_extension='mp4').first().download()

    def setUP(self):
        if self.choice == "s":
            singleUrl = input("Enter the video url: ")
            self.dlSingle(singleUrl)
        elif self.choice == "m":
            playlistUrl = input("Enter the playlist url: ")
            self.dlPlaylist(playlistUrl)

    def dlPlaylist(self,playlistUrl):
        self.plyls = Playlist(playlistUrl)
        for self.url in self.plyls.video_urls:
            try:
                self.yt
            except self.VideoUnavailable:
                print(f"Video {self.url} is unavailable, skipping...!")
            else:
                print(f"Downloading Video: {self.url}")
                print(f"Download in progress...!")
                self.video.streams.filter(file_extension='mp4').first().download()

while True:

    dl = YT_DL(
        input(
            "Do you want to download playlist or single video? (s for single video/m for playlist or alot of videos):"
        )
    )
    dl.setUP()
    c = input('Do you want to continue? (y/n)\n')
    if c == 'n':
        print('Quitting...!')
        input("Press Enter to continue...!")
        break
    elif c == 'y':
        continue
    else:
        print('Invalid..choice')