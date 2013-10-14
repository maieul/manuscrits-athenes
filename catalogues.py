#les paramètres
base="http://xeir.nlg.gr/images/15/"
min = 1
max = 39
romain = True
i = min
extension = ".gif"
dossier="435"
# les imports
import urllib.request
import roman
while i <= max:
    try:   
        if romain:
            url = base + roman.toRoman(i).lower()+extenstion
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