from pytubefix import YouTube
from pytubefix.contrib.search import Filter
from art import *
from Color_Console import ctext
from termcolor import colored
import datetime
from pynput import keyboard
import os
import time
import sys, subprocess

def main():
    def on_press1(key):
        if key == keyboard.Key.esc:
            os._exit(0)

    def on_press2(key):
        if key == keyboard.Key.esc:
            subprocess.run('clear', shell=True)
            os.execv(sys.executable, ['python'] + sys.argv)

    listener1 = keyboard.Listener(on_press=on_press1)
    def start_listener1():
        if not listener1.running:
            listener1.start()
    start_listener1()

    listener2 = keyboard.Listener(on_press=on_press2)
    def start_listener2():
        if not listener2.running:
            listener2.start()

    def stop_listener1():
        if listener1.running:
            listener1.stop()

    def stop_listener2():
        if listener2.running:
            listener2.stop()
    stop_listener2()


    art1 = text2art("Youtube")
    art2 = text2art("downloader")
    ctext(art1,"red","black")
    time.sleep(0.15)
    ctext(art2,"red","black")
    time.sleep(0.15)
    ctext('=' * 68,"blue","black")
    time.sleep(0.15)
    ctext("Made By: opponet    |    press Esc to exit","green","black")
    time.sleep(0.15)
    ctext('=' * 68,"blue","black")


    while True:
        try:
            time.sleep(0.15)
            link = input("Please Enter Vidoe URL: ")
            yt = YouTube(link)
        except:
            ctext("❌ URL is not correct try again.","red","black")
        else: break

    time.sleep(0.15)
    ctext('=' * 68,"blue","black")
    time.sleep(0.15)
    print("Video name: ", end="")
    time.sleep(0.15)
    ctext(yt.title,"cyan","black")
    time.sleep(0.15)
    print("Video channel: ", end="")
    time.sleep(0.15)
    ctext(yt.author, "cyan","black")
    time.sleep(0.15)
    print("Video length: ", end="")
    time.sleep(0.15)
    ctext(datetime.timedelta(seconds=yt.length), "cyan","black")


    videos = yt.streams.filter(file_extension="mp4",only_video=True)
    resolutions = [video.resolution for video in videos]
    resolutionlist = list(set(resolutions))
    if None in resolutionlist:
        resolutionlist.remove(None)
    resolutionlist.sort(key=lambda r: int(r.rstrip("p")))
    time.sleep(0.15)
    print("Available resolutions: ", end="")
    time.sleep(0.15)
    ctext((resolutionlist),"green","black")
    time.sleep(0.15)
    ctext("Press Esc to return back","red","black")
    ctext('=' * 68,"blue","black")
    time.sleep(0.15)
    stop_listener1()
    start_listener2()


    while True:
        try:
            res = input("Choose a quality: ")
            if (res not in resolutionlist):
                raise ValueError("❌ Not valid value")
        except:
            ctext("Please choose a quality from the list above 👆","red","black")
        else: break

    for video in yt.streams.filter(file_extension="mp4",only_video=True):
        if video.resolution == res:
            choose = video


    time.sleep(0.15)
    print("Video size: ",end="")
    time.sleep(0.15)
    ctext(f"{choose.filesize_mb}MB","green","black")
    time.sleep(0.15)
    ctext('=' * 68, "blue","black")
    time.sleep(0.15)


    print("The download will be in your current file.",end="")
    time.sleep(0.15)
    confirm = input("Do you want to continue? [Y/n]")
    time.sleep(0.15)

    if confirm.upper() in ["N", "NO"]:
        os._exit(0)

    if confirm == "" or confirm.upper() in ["Y", "YES"]:
        try:
            time.sleep(1), ctext("Wait for download.","cyan","black"), ctext("This will take some time.","cyan","black")
            choose.download()
            ctext("Download successfully ✅","green","black")
            ctext("Thanks for using tool","green","black")
            os._exit(1)
        except:
            ctext("Failed to download ❌. Try again!","red","black")
    else:
        ctext("Error ❌","red","black")
main()

# add shorts youtube
# https://youtu.be/WEMqvdvGttQ?si=Jacc2Y_Fqr9ic-_C