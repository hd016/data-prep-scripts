##### webscrapper

basic_url = "https://www.gelbeseiten.de/arzt/stuttgart/s"
iterator_page = 20
for iterator_page in range(21):
    multiple_url = "".join([basic_url,str(iterator_page)])
    print (multiple_url)
