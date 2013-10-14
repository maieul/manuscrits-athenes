#les paramètres
base="http://xeir.nlg.gr/images/11/"
min = 1
max = 6
romain = True
i = min
extension = ".gif"
dossier="437"
# les imports
import urllib.request
import roman
while i <= max:
    try:   
        if romain:
            url = base + roman.toRoman(i).lower()+extension
            name = roman.toRoman(i).lower()
        else:
            url = base + str(i).zfill(3)+extension
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