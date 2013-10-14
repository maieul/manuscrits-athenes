#les paramètres
base="http://xeir.nlg.gr/images/15/"
min = 1
max = 39
romain = True
i = min
import urllib.request
import roman
while i <= max:
    try:   
        if romain:
            url = base + roman.toRoman(i).lower()+".gif"
        else:
            url = base + str(i).zfill(3)+".gif"
        print (url)
        http = urllib.request.urlopen(url)
        file = open("435/"+str(i).zfill(3)+".gif","wb")
        file.write(http.read())
        file.close()
    except:
        pass
    i = i + 1