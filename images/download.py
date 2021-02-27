import os

#Open Twitter Images 
data = open("images.txt","r").read().split("'");

#Download each image
for i in data:
    if "https://pbs.twimg.com" in i:
        os.system("wget " + i)