fail = open("albumid.txt", encoding = "UTF-8")

album = []

for rida in fail:
    album.append(rida)
    
    
fail.close()


nimi = input("Sisestage albumi või artisti nimi: ")

for str in album:
    if nimi in str:
        print(str)
    