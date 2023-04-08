#this is the program to download youtube videos.
from __future__ import unicode_literals
import youtube_dl
import os

class download(object):
    def __init__(self,url):
        self.url = url
        self.save_path = os.path.join(os.path.expanduser('~'), 'downloads')
        self.song()

        def song(self):
            opts = {
                'verbose': true ,
                'fixup' : 'detect_or_warn',
                'format' : 'bestaudio/best',
                'postprocessors' : [ {
                    'key' : 'FFmpegeExtractAudio',
                    'preferredcodec' : 'mp3',
                    'prefferquality' : '1411',
                } ],
                'extractaudio' : true ,
                'outtmpl' : self.save_path + '/%(title)s.&(ext)s',
                'noplaylist ' : True
            }

            ydl = youtube_dl.YoutubeDL(opts)
            ydl.download([self.url])


if __name__ == '__main__' :
    url = input ("enter the url to the song here.\n >>  ")
    download(url)