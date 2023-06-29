import os
from guizero import App, ListBox

path = "wallpapers/"
dir_list = os.listdir(path)

app = App(title="PictoPaper", width= 300, height=400) 
def setpic(value):
    os.system('pcmanfm --set-wallpaper ' + os.path.abspath("wallpapers/"+ value) )
    
pics = ListBox(app, items=dir_list, command=setpic, width = 275, height=400)
app.display()