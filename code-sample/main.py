from yt_dl import YT_DL

dl = YT_DL()

#single video
dl.dlSingle('https://www.youtube.com/watch?v=jM4QH2SGyGQ')

#playlist
dl.dlPlaylist('Your playlist URL')