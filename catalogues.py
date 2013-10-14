#les paramètres
base="http://xeir.nlg.gr/images/15/"
min = 2
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
        else:
            url = base + str(i).zfill(3)+extension
        print (url)
        http = urllib.request.urlopen(url)
        file = open(dossier+"/"+str(i).zfill(3)+extension,"wb")
        file.write(http.read())
        file.close()
    except:
        pass
    i = i + 1