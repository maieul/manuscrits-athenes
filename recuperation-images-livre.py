#les paramètres
base="http://babel.hathitrust.org/cgi/imgsrv/image?id=mdp.39015012425404;seq={nombre}"
extension = ".jpg"
min = 1
max = 776
romain = False

dossier="Schlumberger1884"
complete = 0
# les imports
import urllib.request
import roman

# le code
i = min
while i <= max:
    try:   
        if romain:
            url = base.format(nombre=roman.toRoman(i).lower)
            name = roman.toRoman(i).lower()
        else:
            url = base.format(nombre=str(i).zfill(complete))
            name = str(i).zfill(len(str(max)))
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