import Tkinter
import tkMessageBox
import os
import re

def getFilesInDir(path):
   return os.listdir(path)

def deleteAllRars(path):
   for root, subFolders, files in os.walk(path):
      path = root
      for f in files:
         if(f.endswith(".rar") or re.search(r'\.r\d+$', f)):
            filepath = os.path.join(root, f)
            os.remove(filepath)
            print "deleted file: "+filepath
   refreshText()
         
def getAllFiles(path):
   for root, subFolders, files in os.walk(path):
      t.insert(Tkinter.INSERT,root+"\n", "DGREEN")
      for f in files:
         t.insert(Tkinter.INSERT, f+"\n")

def deleteRarInFolder(path):
   files = getFilesInDir(path)
   for f in files:
      if(f.endswith(".rar") or re.search(r'\.r\d+$', f)):
         filepath = os.path.join(path, f)
         os.remove(filepath)
         print "deleted file: "+filepath
   refreshText()

def promptAll():
   answer = tkMessageBox.askyesno( "Delete all .rar files", "Are you sure?")
   if(answer):
      deleteAllRars(rootPath)
   else:
      return

def promptRoot():
   answer = tkMessageBox.askyesno( "Delete .rar files in folder", "Are you sure?")
   if(answer):
      deleteRarInFolder(rootPath)
   else:
      return

def refreshText():
   t.config(state="normal")
   t.delete(1.0, Tkinter.END)
   getAllFiles(rootPath)
   t.config(state="disabled")

top = Tkinter.Tk()
rootPath = "."
rootFiles = getFilesInDir(rootPath)

#set up scrollable text window
scrollbar = Tkinter.Scrollbar(top)
scrollbar.pack(side = Tkinter.RIGHT, fill=Tkinter.Y)
t = Tkinter.Text(top, yscrollcommand = scrollbar.set, height="50", width="150")
scrollbar.config( command = t.yview )

#get intial filetree
getAllFiles(rootPath)
b = Tkinter.Button(top, text ="Delete all .rar files in this folder.", command=lambda: promptRoot())
bAll = Tkinter.Button(top, text ="Delete all .rar files in this folder and subdirectories.", command=lambda: promptAll())
t.config(state="disabled")
b.pack()
bAll.pack()
t.tag_config('DGREEN', foreground='darkgreen')
t.pack()
top.mainloop()
