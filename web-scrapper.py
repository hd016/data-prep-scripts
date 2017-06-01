##### webscrapper

from tkinter import *

##### basic_url ####
basic_url = "https://www.gelbeseiten.de/arzt/stuttgart/s"
iterator_page = 0
multiple_url = []
for iterator_page in range(20):
    iterator_page = iterator_page + 1
    multiple_url.append("".join([basic_url,str(iterator_page),"\n"]))
##### basic_url ####


class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.button = Button(frame, text="SUCHE", fg ="blue", command=self.write_slogan)
        self.button.pack(side=LEFT)

    def write_slogan(self):
        print ("Suchanfrage angenommen")
        self.wall_output = Label(root,
          compound = CENTER,
          text=multiple_url)
        self.wall_output.pack()
      

root = Tk()
app = App(root)

entry = Entry(root)

wall_label = Label(root, text="Gelbe Seiten durchsuchen")

wall_label.pack()
entry.pack()

root.mainloop()
