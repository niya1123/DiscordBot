import sys, subprocess

args = sys.argv

url = args[1]
file_name = url[-5:]
cmd = 'youtube-dl -xo "./Music/' + file_name + '.%(ext)s" --audio-format mp3 ' + url
subprocess.call(cmd, shell=True)
