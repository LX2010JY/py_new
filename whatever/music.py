import mp3play
import time

filename = 'http://111.206.239.14/m10.music.126.net/20170112171100/8354a3be86fa0de62ac8dde98ebcfe65/ymusic/3e07/b25f/f79e/6e51d26005008a129e70ea52e0e9de7d.mp3?wshc_tag=1&wsts_tag=58774249&wsid_tag=72f9d2f7&wsiphost=ipdbm'
mp3 = mp3play.load(filename)
mp3.play()
# Let it play for up to 30 seconds, then stop it.
time.sleep(min(30, mp3.seconds()))
mp3.stop()