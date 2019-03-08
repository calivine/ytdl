from __future__ import unicode_literals
import youtube_dl
import os
from sys import argv

# Download data and config

download_options = {
	'outtmpl': '%(title)s.%(ext)s',
	'nocheckcertificate': True
}

# Video directory

if not os.path.exists('Videos'):
	os.mkdir('Videos')
else:
	os.chdir('Videos')

# Download videos

with youtube_dl.YoutubeDL(download_options) as dl:
	with open(argv[1], 'r') as f:
		for video_url in f:
			dl.download([video_url])
