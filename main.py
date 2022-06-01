from tkinter import *
import pygame
from tkinter import filedialog

root = Tk()
root.title('LocalsOnly')
root.geometry("800x400")

#Initiliaze Pygame Mixer
pygame.mixer.init()

def add_song():
    song = filedialog.askopenfilename(initialdir='audio/',title='Choose a file',filetypes=(('mp3 Files', '*.mp3'), ('wav Files', '*.wav')))
    song_box.insert(END, song)

def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir='audio/',title='Choose a file',filetypes=(('mp3 Files', '*.mp3'), ('wav Files', '*.wav')))
    for song in songs:
        song_box.insert(END, song)

def play():
    song = song_box.get(ACTIVE)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)

#Create Global Pause
global paused
paused = False

def pause(is_paused):
    global paused
    paused = is_paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True

def next_song():
    next_one = song_box.curselection()
    try:
        next_one = next_one[0] + 1
    except:
        pass
    song = song_box.get(next_one)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    song_box.selection_clear(0, END)
    song_box.activate(next_one)
    song_box.selection_set(next_one, last=None)

def previous_song():
    previous_one = song_box.curselection()
    try:
        previous_one = previous_one[0] - 1
    except:
        pass
    song = song_box.get(previous_one)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    song_box.selection_clear(0, END)
    song_box.activate(previous_one)
    song_box.selection_set(previous_one, last=None)

def delete_song():
    song_box.delete(ANCHOR)
    pygame.mixer.music.stop()

#SongBox
song_box = Listbox(root, bg='blue',fg='green',width=80, selectbackground='gray',selectforeground='black')
song_box.pack(pady=20)

#Create Player Control Buttons
back_btn_img = PhotoImage(file="images/back_btn2.png")
forward_btn_img = PhotoImage(file="images/forward_btn2.png")
play_btn_img = PhotoImage(file="images/play_btn2.png")
pause_btn_img = PhotoImage(file="images/pause_btn2.png")
stop_btn_img = PhotoImage(file="images/stop_btn2.png")

#Control Frame
control_frame = Frame(root,height=50)
control_frame.pack()

back_btn = Button(control_frame, image=back_btn_img, command=previous_song)
forward_btn = Button(control_frame, image=forward_btn_img, command=next_song)
play_btn = Button(control_frame, image=play_btn_img, command=play)
pause_btn = Button(control_frame, image=pause_btn_img, command=lambda: pause(paused))
stop_btn = Button(control_frame, image=stop_btn_img, command=stop)

back_btn.grid(row=0,column=0,padx=10)
forward_btn.grid(row=0,column=1,padx=10)
play_btn.grid(row=0,column=2,padx=10)
pause_btn.grid(row=0,column=3,padx=10)
stop_btn.grid(row=0,column=4,padx=10)

#Create Menu
my_menu = Menu(root)
root.config(menu=my_menu, bg="#000")

add_song_menu = Menu(my_menu, tearoff=0)
add_many_songs_menu = Menu(my_menu)
delete_song_menu = Menu(my_menu)


my_menu.add_cascade(label='Add Songs',menu=add_song_menu)
my_menu.add_cascade(label='Add many songs',menu=add_many_songs_menu)
my_menu.add_cascade(label='Delete songs',menu=delete_song_menu)

add_song_menu.add_command(label='Add one song to playlist', command=add_song)
delete_song_menu.add_command(label='Delete song from playlist', command=delete_song)
add_many_songs_menu.add_command(label='Add multiple songs to playlist', command=add_many_songs)

root.mainloop()
