import os 

path = os.path.abspath(os.path.dirname(__file__)).replace("\\","/")

for root,dirs,files in os.walk(path+"/ideas"):
    for file in files:
        print(file)