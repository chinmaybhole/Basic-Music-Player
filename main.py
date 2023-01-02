import pygame
import tkinter as tk
from tkinter.filedialog import askdirectory
from PIL import Image, ImageTk
import os

# Using tkinter to make music player screen interface
music_player = tk.Tk()
# music_player = tk.PhotoImage()
bg1 = tk.PhotoImage(
    file='img/dcn4blc-a137d2e9-6b30-4faf-ae8d-1de83a8de0ac.png')

music_player.title("Life is one grand sweet song")
music_player.geometry('380x250')

# With the help of os we are going to make directory that prompts the user to choose folder of music
directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()
# todo add label to music player
play_list = tk.Listbox(music_player, font='Courier',
                       bg='purple', fg='white', width=37, selectmode=tk.SINGLE)
play_list.grid(columnspan=5)
listofsong = []
for song in song_list:
    pos = 0
    listofsong.append(song)
    play_list.insert(pos, song)
    pos += 1

pygame.init()
pygame.mixer.init()


# pygame.mixer.music.load(listofsong[2])
# pygame.mixer.music.play()


def playsong():
    currentsong = play_list.get(tk.ACTIVE)
    print(currentsong)
    pygame.mixer.music.load(currentsong)
    songstatus.set("Playing")
    pygame.mixer.music.play()


def pausesong():
    songstatus.set("Paused")
    pygame.mixer.music.pause()


def stopsong():
    songstatus.set("Stopped")
    pygame.mixer.music.stop()


def resumesong():
    songstatus.set("Resuming....")
    pygame.mixer.music.unpause()


songstatus = tk.StringVar()
songstatus.set("choosing")
song_title = tk.Label(
    music_player, font="img/balloons.ttf", textvariable=songstatus)

playbtn = tk.Button(music_player, text="Play", command=playsong)
playbtn.config(font=('img/balloons.ttf', 20),
               bg="black", fg="white", padx=0, pady=0)
playbtn.grid(row=1, column=0)

playpause = tk.Button(music_player, text="Pause", command=pausesong)
playpause.config(font=('img/balloons.ttf', 20),
                 bg="black", fg="white", padx=0, pady=0)

playpause.grid(row=1, column=1)

playresume = tk.Button(music_player, text="Resume", command=resumesong)
playresume.config(font=('img/balloons.ttf', 20),
                  bg="black", fg="white", padx=0, pady=0)
playresume.grid(row=1, column=2)

playstop = tk.Button(music_player, text="Stop", command=stopsong)
playstop.config(font=('img/balloons.ttf', 20),
                bg="black", fg="white", padx=0, pady=0)
playstop.grid(row=1, column=3)

music_player.mainloop()
