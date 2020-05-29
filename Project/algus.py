fail = open("albumid.txt", encoding = "UTF-8")

album = []

for rida in fail:
    album.append(rida)
    
    
fail.close()

nimi = input("Sisestage albumi või artisti nimi: ")
x = nimi.title()

for str in album:
    if x in str:
        print(str)