##### webscrapper ######
# Author: Harun D.
# Project: Gelbe Seiten Webscrapper
# Auftrag: **************
# Status: aktiv

from tkinter import *
from bs4 import BeautifulSoup
import urllib.request
import os
import time



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

        ### Start Time ###
        start_time = time.time()

        self.entry_get = self.entry.get()
        self.suchanfrage = ("Suchanfrage angenommen:", self.entry_get)
        print(self.suchanfrage)

        self.sub_url = "https://www.gelbeseiten.de/{}/stuttgart/s".format(self.entry_get)


        text_file = open("Ergebnisse-von-{}.txt".format(self.entry_get), "w")

        ### Iterator für den Zähler am Stringende. S1, S2, S3 ...
        multiple_url = []
        for iterator_page in range(20):
                iterator_page = iterator_page + 1
                multiple_url.append("".join([self.sub_url, str(iterator_page)]))

        ### Schleife für das durchgehen aller 20 Seiten ###
        parser = 0
        while parser < len(multiple_url):
            print(multiple_url[parser])
            with urllib.request.urlopen(multiple_url[parser]) as url:
                parser += 1
                soup = BeautifulSoup(url, "html.parser")

        ### Parsen von HTML Tags in Tuples # -> siehe Anfrage in Stackoverflow
                names = [name.get_text().strip() for name in soup.findAll("div", {"class": "name m08_name"})]
                street = [address.get_text().strip() for address in soup.findAll(itemprop="streetAddress")]
                plz = [address.get_text().strip() for address in soup.findAll(itemprop="postalCode")]
                city = [address.get_text().strip() for address in soup.findAll(itemprop="addressLocality")]
                branches = [branche.get_text().strip() for branche in soup.findAll("div", {"class":"branchen m08_branchen "})]

        ### Zippen und das Schreiben von Ergebnissen.
                for line in zip(names, street, plz , city, branches):
                    print("%s;%s;%s;%s;%s\n" % line)
                    text_file.write("%s;%s;%s;%s;%s\n" % line)


        ### Ausschreiben von dem aktuellen Pfad + die Formatierung (kein Hardcode!) Hauptelement: cwd_out_final
        cwd = os.getcwd()
        cwd_out = "\{}".format(text_file.name)
        cwd_out_final = cwd + cwd_out




        text_file.close()
        print("File geschlossen")
        print("--- %s seconds ---" % (time.time() - start_time))


        ### Die Ausgaben als Labels.
        self.wall_output_line = Label(root,compound=CENTER, text="Die Datei wurde hier abgespeichert:")
        self.wall_output = Label(root,compound = CENTER,text=cwd_out_final)
        self.wall_output_line.pack()
        self.wall_output.pack()

    def search_iterate(self):
        ### Branchen Label und Entry ###
        self.label_branche = Label(root, text="Bitte tippen Sie hier die Branche ein.")
        self.entry_branche = Entry(root)
        self.label_branche.pack()
        self.entry_branche.pack()

        ### PLZ Label und Entry ###
        self.label_plz = Label(root, text="Bitte tippen Sie hier die PLZ ein.")
        self.entry_plz = Entry(root)
        self.label_plz.pack()
        self.entry_plz.pack()

        ### Suche Iterate Button ###
        self.button_iterate_inner = Button(text="Suche", fg="blue", command=self.search_iterate_inner)
        self.button_iterate_inner.pack()

    def search_iterate_inner(self):
        self.entry_branche_get = self.entry_branche.get()
        self.entry_plz_get = self.entry_plz.get()

        print("Suchanfrage angenommen:", self.entry_branche_get, self.entry_plz_get)

        self.sub_iterate_url = "https://www.gelbeseiten.de/{}/stuttgart,,{}/s".format(self.entry_branche_get, self.entry_plz_get)


        text_file = open("Ergebnisse-von-{}-{}.txt".format(self.entry_branche_get, self.entry_plz_get), "w")

        ### Iterator für den Zähler am Stringende. S1, S2, S3 ...
        multiple_url = []
        for iterator_page in range(20):
                iterator_page = iterator_page + 1
                multiple_url.append("".join([self.sub_iterate_url, str(iterator_page)]))

        ### Schleife für das durchgehen aller 20 Seiten ###
        parser = 0
        while parser < len(multiple_url):
            print(multiple_url[parser])
            with urllib.request.urlopen(multiple_url[parser]) as url:
                parser += 1
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

        ### Ausschreiben von dem aktuellen Pfad + die Formatierung (kein Hardcode!) Hauptelement: cwd_out_final
        cwd = os.getcwd()
        cwd_out = "\{}".format(text_file.name)
        cwd_out_final = cwd + cwd_out

        text_file.close()
        print("File geschlossen")

        ### Die Ausgaben als Labels.
        self.wall_output_line = Label(root,compound=CENTER, text="Die Datei wurde hier abgespeichert:")
        self.wall_output = Label(root,compound = CENTER,text=cwd_out_final)
        self.wall_output_line.pack()
        self.wall_output.pack()

root = Tk()
root.geometry('450x450')
root.title('Gelbe Seiten Scrapper')
app = App(root)
root.mainloop()
