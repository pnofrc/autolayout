# November 2021, copyleft || Funix || Zine Camp, Worm, Rotterdam
# 
# This script is to generate a zine from a telegram group chat
# 
# import json # to read the json file

import json # to use json in python

d = open('result.json','r') #open the json file
dictio = json.load(d) # and make it load
m = dictio['messages'] # then declare the array "m" that take all the 'messages' keys 

contents = ''

n = 0
for x in m:
    if 'photo' in x:
        contents += f"<img src={x['photo']}>"
        n = n+1
        print(f"<img src={x['photo']}>")

    elif 'text' in x:
        if x['text'] != '':
           contents += f'<p>{x["text"]}</p>'
        else:
            continue

intro = '''<html>
                    <head>
                        <meta charset="UTF-8">
                        <link rel="stylesheet" href="../../script/interface.css">
                        <script src="../../script/paged.polyfill.js"></script>
                        <link rel="stylesheet" href="./style.css">
                        <title>📡 💻📘</title>
                    </head>

                    <body>
                    
                    '''

outro = '''         </div></body>
              </html>'''


with open("index.html", "w") as file:
    
    file.write(intro)

    file.write(contents)
    
    file.write(outro)
    
    file.close()
    