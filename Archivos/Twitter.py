#Javier Pascal Flores
import requests

url = "https://twitter.com/katyperry"
info = requests.get(url)
if info.status_code == 200: #Correct reading


    lines = info.text.split("\n")
    index = 0
    line = lines[index]
    while 'u-hiddenVisually">Seguidores' not in line:
        index+=1
        line = lines[index]
    line =lines[index+1]

    print("*****", line, "++++")
    tokens = line.split()
    print (tokens)
    datos =  tokens[2].split("=")
    followers = int(datos[1])
    print("Seguidores:", (followers))

    for line in lines:
        if "TweetTextSize" in line:
            new= (line[line.index('">')+2:])

            if "<img" in line:
                second = (new[new.index('">')+2:])
                print (second)
