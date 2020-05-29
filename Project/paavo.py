fail = open("albumid.txt", encoding="UTF-8")

albumid = []

def Albumite_kriipsud():
    for rida in fail:
        elemendid = rida.split("\t")
        esineja = elemendid[0]
        album = elemendid[1]
        albumid.append(album)
        aasta = elemendid[2]
        laul = elemendid[3]
        if len(albumid) > 1:
            if albumid[-2] != albumid[-1]:
                print()
                print("--------------------------------------------")
                print()
        print(rida)
        
Albumite_kriipsud()

fail.close()