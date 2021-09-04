from os import linesep
from googletrans import Translator  
translator = Translator()  


filename = "chapter_chinese.txt"


#translation not 100% accurate some phrase can be added  to replacesword.txt to help
replaces = {}
with open("replacesword.txt", encoding="utf8") as re:
    con = re.readlines()
    for line in con:
        if line != "\n":
            arr = line.split(" ")
            if  len(arr) == 2:
                arr[1] = arr[1].replace("\n", "") 
                replaces[arr[0]] = arr[1]
            else:
                strong = ""
                for s in range(len(arr)-1,0,-1):
                    strong =  arr[s] + " "+strong
                strong = strong.replace("\n", "")
                replaces[arr[0]] = strong

newf = open('replaced_chapter.txt', 'a', encoding="utf8")

with open(filename, encoding="utf8") as f:
    content = f.readlines()
    for line in content:
        if line != "\n":
            line = line.replace("    ", "")
            for key,val in replaces.items():
                if key in line:
                    line = line.replace(key, val)
            newf.write(translator.translate(line).text+"\n")
            #newf.write(translator.translate(line).text+"\n")
f.close()


