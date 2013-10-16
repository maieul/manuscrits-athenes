#les paramètres
base="http://www.corgialenios.gr/files/medium/7/48547ep_{nombre}_KAT_{nombre}.pdf"
extension = ".pdf"
min = 156
max = 196
romain = False
i = min
dossier="2490"
# les imports
import urllib.request
import roman
while i <= max:
    try:   
        if romain:
            url = base.format(nombre=roman.toRoman(i).lower)
            name = roman.toRoman(i).lower()
        else:
            url = base.format(nombre=str(i).zfill(3))
            name = str(i).zfill(3)
        fichier =  dossier+"/"+name+extension
        print (fichier)
        print (url)
        
        http = urllib.request.urlopen(url)
        file = open(fichier,"wb")
        file.write(http.read())
        file.close()
    except:
        pass
    i = i + 1