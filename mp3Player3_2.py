from tkinter import *
from tkinter.filedialog import *
from pygame import *
import os
from PIL import ImageTk

top = Tk()
top.title("MP3 플레이어")
top.geometry("384x360")


ls_music = []
index = 0
lb_string = StringVar()
v_size= 0.30


def music_list():
    global index
    dir = askdirectory()
    os.chdir(dir)

    for files in os.listdir(dir):
        ls_music.append(files)

    mixer.init()
    #mixer.music.load(ls_music[index])
    #mixer.music.play(-1)
    #lb_update()

    def list_select(event):
        global index
        index = int(lb.curselection()[0])
        mixer.music.load(ls_music[index])
        mixer.music.play(-1)
        lb_update()

    def list_insert():
        i = 0

        for song in ls_music:
             lb.insert(i, song)
             i += 1
        

    win = Toplevel(top)
    win.title("목록")
    sb = Scrollbar(win)
    sb.pack(side = RIGHT, fill = Y)
    lb = Listbox(win, width = 50, yscrollcommand = sb.set)
    lb.pack(side = LEFT)
    sb.config(command = lb.yview)
    song_lb = Label(textvariable=lb_string)
    song_lb.place(x = 0, y = 0)
    list_insert()
    


    lb.bind("<<ListboxSelect>>", list_select)
            

def play_song(event):
    mixer.music.play(-1)
    lb_update()

def stop_song(event):
    mixer.music.stop()
    

def lb_update():
    global index
    lb_string.set(ls_music[index])

def pre_song(event):
    global index
    if index == 0:
        return
    index -=1
    mixer.music.load(ls_music[index])
    mixer.music.play(-1)
    lb_update()

def next_song(event):
    global index
    if index == len(ls_music[index]) -1:
        return
    index += 1
    mixer.music.load(ls_music[index])
    mixer.music.play(-1)
    lb_update()

def v_up(event):
    global v_size
    mixer.music.set_volume(v_size)
    v_size += 0.10

def v_down(event):
    global v_size
    mixer.music.set_volume(v_size)
    v_size -= 0.10

def quit_music():
    mixer.music.stop()
    top.destroy()
    
                     

#wall = PhotoImage(file = "/Users/2sh7842/capde/tkinter/md_w.gif")
#w_lb = Label(image = wall)
#w_lb.place(x = 0, y = 0)

img_p = PhotoImage(file = "/Users/2sh7842/capde/tkinter/md_p.gif")
b_p = Button(top,height = 30, width = 30, image=img_p)
b_p.place(x = 155, y =166)

img_s = PhotoImage(file = "/Users/2sh7842/capde/tkinter/md_s.gif")
b_s = Button(top, height = 30, width = 30, image=img_s)
b_s.place(x = 195, y = 166)

img_b = PhotoImage(file = "/Users/2sh7842/capde/tkinter/md_b.gif")
b_b = Button(top, height = 30, width = 40, image=img_b)
b_b.place(x = 50, y = 166)

img_n = PhotoImage(file = "/Users/2sh7842/capde/tkinter/md_n.gif")
b_n = Button(top, height = 30, width = 40, image=img_n)
b_n.place(x = 290, y = 166)

img_u = PhotoImage(file = "/Users/2sh7842/capde/tkinter/md_u.gif")
b_u = Button(top, height = 30, width = 30, image=img_u)
b_u.place(x = 176, y = 48)

img_d = PhotoImage(file = "/Users/2sh7842/capde/tkinter/md_d.gif")
b_d = Button(top, height = 30, width = 30, image=img_d)
b_d.place(x = 176, y = 288)

img_l = PhotoImage(file = "/Users/2sh7842/capde/tkinter/md_l.gif")
b_l = Button(top, height = 47, width = 30, image=img_l, command=music_list)
b_l.place(x = 326, y = 24)

b_p.bind("<Button-1>", play_song)
b_s.bind("<Button-1>", stop_song)
b_b.bind("<Button-1>", pre_song)
b_n.bind("<Button-1>", next_song)
b_u.bind("<Button-1>", v_up)
b_d.bind("<Button-1>", v_down)

top.protocol('WM_DELETE_WINDOW', quit_music)


top.mainloop()
