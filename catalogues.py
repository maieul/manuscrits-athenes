#les paramètres
base="http://xeir.nlg.gr/images/1/"
min = 1
max = 11
romain = True
i = min
extension = ".gif"
dossier="430"
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
        print (url)
        print (name)
        http = urllib.request.urlopen(url)
        file = open(dossier+"/"+name+extension,"wb")
        file.write(http.read())
        file.close()
    except:
        pass
    i = i + 1