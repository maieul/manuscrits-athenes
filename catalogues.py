#les paramètres
base="http://xeir.nlg.gr/images/9/"
min = 1
max = 27

i = min
import urllib.request
while i <= max:
    try:   
        url = base + str(i).zfill(3)+".gif"
        print (url)
        http = urllib.request.urlopen(url)
        file = open(str(i).zfill(3)+".gif","wb")
        file.write(http.read())
        file.close()
    except:
        pass
    i = i + 1
