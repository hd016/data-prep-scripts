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

        ### Inner und Outer Frames (-> Panel -> GWT - OK )
        self.frame = Frame(master)
        self.frame_inner = Frame()
        self.frame_outer = Frame()
        self.frame.pack()
        self.frame_inner.pack()
        self.frame_outer.pack()

        ### Main Buttons und Aufnehmen in den Root ###
        self.button_complete = Button(self.frame_inner, text="Komplette Suche", fg="blue", command=self.search_complete)
        self.button_iterate = Button(self.frame_inner, text="Einzelne Suche", fg="blue", command=self.search_iterate)
        self.button_complete.pack(side=LEFT)
        self.button_iterate.pack(side=RIGHT)


        ##################################################################################
        #
        #   Funktionen: Komplette Suche, Einzelne Suche
        #
        ##################################################################################

        ### Die komplette Suchfunktion, kommt von dem Button: button_complete
        ### Leitet die Frage an search_complete_inner weiter
    def search_complete(self):
        self.entry_search_complete = Entry(root)
        self.entry_search_complete.pack()
        self.button_complete_inner = Button(text="Suche", fg="blue", command=self.search_complete_inner)
        self.button_complete_inner.pack()
    def search_complete_inner(self):
        self.entry_search_complete_get = self.entry_search_complete.get()
        print("Suchanfrage angenommen:", self.entry_search_complete_get)
        self.sub_url = "https://www.gelbeseiten.de/{}/stuttgart/s".format(self.entry_search_complete_get)

        ### Iterator für den Zähler am Stringende. S1, S2, S3 ...
        multiple_url = []
        for iterator_page in range(20):
                iterator_page = iterator_page + 1
                multiple_url.append("".join([self.sub_url, str(iterator_page)]))

        ### Schleife für das durchgehen aller 20 Seiten ###
        parser = 0
        #while parser < len(multiple_url):
        #print(multiple_url[parser])
        #parser += 1

        ### Ausschreiben von dem aktuellen Pfad + die Formatierung (kein Hardcode!) Hauptelement: cwd_out_final
        cwd = os.getcwd()
        text_file = open("Ergebnisse-von-{}.txt".format(self.entry_search_complete_get), "w")
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
                    #print("%s;%s;%s;%s;\n" % line)
                    print("ALLES OK")
                    text_file.write("%s;%s;%s;%s;\n" % line)


            text_file.close()

        ### Die Ausgaben als Labels.
            self.wall_output_line_search_complete = Label(self.frame_outer,compound=CENTER, text="Die Datei wurde hier abgespeichert:")
            self.wall_output_search_complete = Label(self.frame_outer,compound = CENTER,text=cwd_out_final)
            self.wall_output_line_search_complete.pack()
            self.wall_output_search_complete.pack()
            print("BITTI")

    #### ------------------------ Komplette Suche zu Ende ------------------------ ####


    ### Die komplette Suchfunktion, kommt von dem Button: button_complete
        ### Leitet die Frage an search_complete_inner weiter


    def search_iterate(self):
    ### Eingabe für PLZ ###
        self.frame_outer.forget()
        self.label_plz_search_iterate = Label(self.frame_outer,compound = CENTER,text="Postleitzahl")
        self.entry_plz_search_iterate = Entry(self.frame_outer)

        self.label_plz_search_iterate.pack()
        self.entry_plz_search_iterate.pack()

    ### Eingabe für Stadt
        self.label_city_search_iterate = Label(self.frame_outer,compound = CENTER,text="Stadt")
        self.entry_city_search_iterate = Entry(self.frame_outer)

        self.label_city_search_iterate.pack()
        self.entry_city_search_iterate.pack()

    ### Button für Suche
        self.button_iterate_inner = Button(self.frame_outer, text="Suche", fg="blue", command=self.search_iterate_inner)
        self.button_iterate_inner.pack()



    def search_iterate_inner(self):
        self.entry_search_iterate_get = self.entry_search_iterate.get()
        print("Suchanfrage angenommen:", self.entry_search_iterate_get)
        self.sub_url = "https://www.gelbeseiten.de/{}/stuttgart/s".format(self.entry_search_iterate_get)

        ### Iterator für den Zähler am Stringende. S1, S2, S3 ...
        multiple_url = []
        for iterator_page in range(20):
                iterator_page = iterator_page + 1
                multiple_url.append("".join([self.sub_url, str(iterator_page)]))

        ### Schleife für das durchgehen aller 20 Seiten ###
        parser = 0
        #while parser < len(multiple_url):
        #print(multiple_url[parser])
        #parser += 1

        ### Ausschreiben von dem aktuellen Pfad + die Formatierung (kein Hardcode!) Hauptelement: cwd_out_final
        cwd = os.getcwd()
        text_file = open("Ergebnisse-von-{}.txt".format(self.entry_search_complete_get), "w")
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
                    #print("%s;%s;%s;%s;\n" % line)
                    print("ALLES OK")
                    text_file.write("%s;%s;%s;%s;\n" % line)


            text_file.close()

        ### Die Ausgaben als Labels.
            self.wall_output_line_search_complete = Label(self.frame_outer,compound=CENTER, text="Die Datei wurde hier abgespeichert:")
            self.wall_output_search_complete = Label(self.frame_outer,compound = CENTER,text=cwd_out_final)
            self.wall_output_line_search_complete.pack()
            self.wall_output_search_complete.pack()
            print("BITTI")




root = Tk()
root.geometry('450x450')
root.title('Gelbe Seiten Scrapper')
app = App(root)
root.mainloop()
