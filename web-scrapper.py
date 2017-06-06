##### webscrapper

from tkinter import *
from bs4 import BeautifulSoup
import urllib.request
from prettytable import PrettyTable
import csv

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.button = Button(frame, text="SUCHE", fg="blue", command=self.search)
        self.button.pack(side=LEFT)
        self.entry = Entry(root)
        self.entry.pack()

    def search(self):
        self.entry_get = self.entry.get()
        print("Suchanfrage angenommen:", self.entry_get)

        self.sub_url = "https://www.gelbeseiten.de/{}/stuttgart/s".format(self.entry_get)

        iterator_page = 0
        multiple_url = []
        for iterator_page in range(20):
            iterator_page = iterator_page + 1
            multiple_url.append("".join([self.sub_url, str(iterator_page)]))

        # self.wall_output = Label(root,compound = CENTER,text=multiple_url)
        # self.wall_output.pack()

        parser = 0
        # while parser < len(multiple_url):
        #  print(multiple_url[parser])
        # parser += 1

        text_file = open("Output3.txt", "w")
        csv_file = open("test.csv", "w")
        table = PrettyTable(['Namen', 'Adressen'])

        with urllib.request.urlopen("file:///C:/Users/HDALICI/Desktop/test.html") as url:
            soup = BeautifulSoup(url, "html.parser")

            names = [name.get_text().strip() for name in soup.findAll("div", {"class": "name m08_name"})]
            street = [address.get_text().strip() for address in soup.findAll(itemprop="streetAddress")]
            plz = [address.get_text().strip() for address in soup.findAll(itemprop="postalCode")]
            city = [address.get_text().strip() for address in soup.findAll(itemprop="addressLocality")]

            for line in zip(names, street, plz , city):
                print("%s;%s;%s;%s;\n" % line)
                text_file.write("%s;%s;%s;%s;\n" % line)


            text_file.close()
            print("Prozess finish")


root = Tk()
app = App(root)

wall_label = Label(root, text="Gelbe Seiten durchsuchen")

wall_label.pack()

root.mainloop()
