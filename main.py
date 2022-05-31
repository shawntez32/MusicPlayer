import tkinter as tk
import pygame

root = tk.Tk()
root.title('LocalsOnly')
root.geometry("800x400")

#Initiliaze Pygame Mixer
pygame.mixer.init()

#SongBox
song_box = tk.Listbox(root, bg='black',fg='green',width=80)
song_box.pack(pady=20)

#Create Player Control Buttons
back_btn_img = tk.PhotoImage(file="images/back_btn2.png")
forward_btn_img = tk.PhotoImage(file="images/forward_btn2.png")
play_btn_img = tk.PhotoImage(file="images/play_btn2.png")
pause_btn_img = tk.PhotoImage(file="images/pause_btn2.png")
stop_btn_img = tk.PhotoImage(file="images/stop_btn2.png")

#Control Frame
control_frame = tk.Frame(root,height=50,bg='#000')
control_frame.pack()

back_btn = tk.Button(control_frame, image=back_btn_img, borderwidth=0)
forward_btn = tk.Button(control_frame, image=forward_btn_img, borderwidth=0)
play_btn = tk.Button(control_frame, image=play_btn_img, borderwidth=0)
pause_btn = tk.Button(control_frame, image=pause_btn_img, borderwidth=0)
stop_btn = tk.Button(control_frame, image=stop_btn_img, borderwidth=0)

back_btn.grid(row=0,column=0,padx=10)
forward_btn.grid(row=0,column=1,padx=10)
play_btn.grid(row=0,column=2,padx=10)
pause_btn.grid(row=0,column=3,padx=10)
stop_btn.grid(row=0,column=4,padx=10)

root.mainloop()
