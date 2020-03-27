import os
import subprocess
import time

from os.path import isfile

SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""

img_num = 0
cwd = f'{os.getcwd()}/img/'

def set_wallpaper(file_path):
    subprocess.Popen(SCRIPT%file_path, shell=True)
    print('Wallpaper set to ' + file_path)


if __name__ == "__main__":
    list_of_files = [f for f in os.listdir(f'{cwd}')]
    while True:
        set_wallpaper(f'{cwd}{list_of_files[img_num]}')
        if img_num != len(list_of_files)-1:
            img_num += 1
        else:
            img_num = 0
        time.sleep(86400)


