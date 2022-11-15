from tkinter import *
from tkinter.filedialog import *
from gtts import gTTS
from pygame import *
import os 

def new_file():
    root.title("제목없음- TTS")
    file = None 
    tb.delete(1.0,END)

def open_file():
    file = askopenfilename(title = "파일 선택", filetypes = (("텍스트 파일", "*.txt"),("모든 파일", "*.*")))
    root.title(os.path.basename(file) + " - 메모장")
    e1.delete(0,END)
    e1.insert(0,file)
    tb.delete(1.0, END)
    f = open(file,"r")
    tb.insert(1.0,f.read())
    f.close()

def save_file():
    f = asksaveasfile(mode = "w", defaultextension=".txt")
    if f is None:
        return
    ts = str(tb.get(1.0, END))
    f.write(ts)
    f.close()

   
def create():
   text = e1.get()
   f = open(text, "r")
   tts = gTTS(f.read())
   tts.save(text+".mp3")

def play_file():
   music_file = e1.get()+".mp3"   

   mixer.init(24000)
   mixer.music.load(music_file)
   mixer.music.play()

def stop_file():

   mixer.quit()

def p_save():
   word = e2.get()
   tts = gTTS(word)
   tts.save(word+".mp3")
   
def p_play():
   music_file = e2.get()+".mp3"   # mp3 or mid file

   mixer.init()
   mixer.music.load(music_file)
   mixer.music.play()

def create_help():
   window = Toplevel(root)
   window.title("Help")
   w = Label(window, text="파일 이름")
   w.grid(row=0, column=0)
   w = Label(window, text="내용")
   w.grid(row=0, column=1)
   w = Label(window, text="travel1")
   w.grid(row=1, column=0)
   w = Label(window, text="공항에서")
   w.grid(row=1, column=1)
   w = Label(window, text="hotel1")
   w.grid(row=2, column=0)
   w = Label(window, text="호텔에서")
   w.grid(row=2, column=1)

   
def create_about():
   window = Toplevel(root)
   window.title("About")
   w = Label(window, text="scyan TTS 1.0 \n"
                         +"®www.scyan.com")
   w.grid(row=0, column=0)   


root = Tk()
root.title("Scyan TTS")
root.wm_iconbitmap("speaker.ico") 
root.geometry("400x400")



menubar = Menu(root)

menu_1 = Menu(menubar, tearoff=0)
menu_1.add_command(label="새파일",command=new_file)
menu_1.add_command(label="열기",command=open_file)
menu_1.add_command(label="저장", command=save_file)
menu_1.add_separator()
menu_1.add_command(label="종료", command=root.destroy)
menubar.add_cascade(label="파일", menu=menu_1)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="파일목록", command=create_help)
helpmenu.add_command(label="정보", command=create_about)
menubar.add_cascade(label="도움말", menu=helpmenu)

root.config(menu=menubar)


w = Label(root, text="TXT 파일 읽기")
w.grid(row=0, column=0)
e1 = Entry(root)
e1.grid(row=0, column=1)
w = Button(root, text="MP3 생성", command=create)
w.grid(row=0, column=2)
w = Button(root, text="▶", command=play_file)
w.grid(row=0, column=3)
w = Button(root, text="■", command=stop_file)
w.grid(row=0, column=4)

w = Label(root, text="Phrase 읽기 ")
w.grid(row=1, column=0)
e2 = Entry(root)
e2.grid(row=1, column=1)
w = Button(root, text="구문 저장", command=p_save)
w.grid(row=1, column=2)
w = Button(root, text="구문 읽기", command=p_play)
w.grid(row=1, column=3, columnspan=2)

frame = Frame(root)
frame.grid(row=2, column=0, columnspan=4, sticky='W')  
tb = Text(frame, width=50)
tb.pack(side='left', fill='both', expand=True)
scrollbar = Scrollbar(frame)
tb.config(yscrollcommand=scrollbar.set)
scrollbar.config(command= tb.yview)
scrollbar.focus_set()

scrollbar.pack(side='right', fill='y')


mainloop()
