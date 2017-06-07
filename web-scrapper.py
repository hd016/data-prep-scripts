##### webscrapper ######
# Author: Harun D.
# Project: Gelbe Seiten Webscrapper
# Auftrag: **************
# Status: aktiv

from tkinter import *
from bs4 import BeautifulSoup
import urllib.request
import os


### Start der Main App ###
class App:
    def __init__(self, master):
        ### Hauptelemente in der Main###
        wall_label = Label(root, text="Gelbe Seiten durchsuchen")
        wall_label.pack()
        frame = Frame(master)
        frame.pack()

        ### Main Buttons und Aufnehmen in den Root ###
        self.button_complete = Button(frame, text="Komplette Suche", fg="blue", command=self.search_complete)
        self.button_iterate = Button(frame, text="Einzelne Suche", fg="blue", command=self.search_iterate)
        self.button_complete.pack(side=LEFT)
        self.button_iterate.pack(side=RIGHT)


        ### Die komplette Suchfunktion, kommt von dem Button: button_complete
        ### Leitet die Frage an search_complete_inner weiter
    def search_complete(self):
        self.entry = Entry(root)
        self.entry.pack()
        self.button_complete_inner = Button(text="Suche", fg="blue", command=self.search_complete_inner)
        self.button_complete_inner.pack()
    def search_complete_inner(self):
        self.entry_get = self.entry.get()
        print("Suchanfrage angenommen:", self.entry_get)
        self.sub_url = "https://www.gelbeseiten.de/{}/stuttgart/s".format(self.entry_get)

        ### Iterator für den Zähler am Stringende. S1, S2, S3 ...
        multiple_url = []
        for iterator_page in range(20):
                iterator_page = iterator_page + 1
                multiple_url.append("".join([self.sub_url, str(iterator_page)]))

        ### Schleife für das durchgehen aller 20 Seiten ###
        parser = 0
        # while parser < len(multiple_url):
        #  print(multiple_url[parser])
        # parser += 1

        ### Ausschreiben von dem aktuellen Pfad + die Formatierung (kein Hardcode!) Hauptelement: cwd_out_final
        cwd = os.getcwd()
        text_file = open("Ergebnisse-von-{}.txt".format(self.entry_get), "w")
        cwd_out = "\{}".format(text_file.name)
        cwd_out_final = cwd + cwd_out

        ### Öffnen der Urllib, aktuell: OFFLINE
        ### urlopen(multiple_url[parser]) ist standard parameter
        with urllib.request.urlopen("file:///C:/Users/HDALICI/Desktop/test.html") as url:
            soup = BeautifulSoup(url, "html.parser")

        ### Parsen von HTML Tags in Tuples # -> siehe Anfrage in Stackoverflow
            names = [name.get_text().strip() for name in soup.findAll("div", {"class": "name m08_name"})]
            street = [address.get_text().strip() for address in soup.findAll(itemprop="streetAddress")]
            plz = [address.get_text().strip() for address in soup.findAll(itemprop="postalCode")]
            city = [address.get_text().strip() for address in soup.findAll(itemprop="addressLocality")]

        ### Zippen und das Schreiben von Ergebnissen.
            for line in zip(names, street, plz , city):
                    print("%s;%s;%s;%s;\n" % line)
                    text_file.write("%s;%s;%s;%s;\n" % line)


            text_file.close()

        ### Die Ausgaben als Labels.
            self.wall_output_line = Label(root,compound=CENTER, text="Die Datei wurde hier abgespeichert:")
            self.wall_output = Label(root,compound = CENTER,text=cwd_out_final)
            self.wall_output_line.pack()
            self.wall_output.pack()
