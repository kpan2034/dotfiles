import os

ban_artist = os.popen('banshee --query-artist').read()
ban_title = os.popen('banshee --query-title').read()

artist = ban_artist[8:-1]
title = ban_title[7:]

output = '  ' + artist + ' - ' + title 

print(output)