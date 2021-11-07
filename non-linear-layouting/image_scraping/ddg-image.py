# November 2021, copyleft || Funix || Zine Camp, Worm, Rotterdam

# Scrape and download images in local from DuckDuckGo 

# with DuckDuckGoImages!

import DuckDuckGoImages as ddg          # import the library for scrape
import os                               # to manipulate the file system
import shutil                           # same but powerfull >:D
import time                             # to create delays :: for having a few seconds to check the console
import random                           # to get random numbers 
from urllib.request import urlopen      # to request urls usage


 # start the layouting :: html + css + paged.js >>    
                                                                           
                                        # declare the first part of the text of the html, we will fill it
                                        # in the process with loops
html = '''                                
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="../../script/interface.css">
        <script src="../../script/paged.polyfill.js"></script>
        <link rel="stylesheet" href="./style.css">
        <title>📡 💻📘</title>
    </head>
<body>

    <div class="firstP">
        <h1 style="position: absolute; top: 0; left:0; color: black;">Title!</h1>
        
        <p style="position: absolute; bottom: 0; right:0;">Authors!</p>
    </div>

    <div class="contents"><p>
'''                                  
   

                                        # Prepare the local folder :: where the images will be saved >>

if os.path.isdir('./images/'):          # check if the folder "images" exists
     shutil.rmtree('./images/')         # if yes, delete it

os.mkdir('./images/')                   # and then create a fresh new one

                                    

url = 'https://pad.xpub.nl/p/ddg/export/txt'
response = urlopen(url)
qq = response.read().split()

print(qq)                        # print the array!


time.sleep(2)                            # check qq in the console!

                                        
                                      # Elaborate each word :: process every element of the array qq
for q in qq:
    
    q = q.decode()

    print(q)                            # print the q!

    os.mkdir(f'./images/{q}/')     # create the folder

      


                                        # Scrape images  with ddg.download()! :: we imported DuckDuckGoImages *as* ddg, 
                                        # it's just compacted the name

                                        # q is, indeed, the query for DuckDuckGo
                                        # folder=(../path/to/download)
                                        # max_urls=(how many results attempt to scrape
                                        # thumbnails=(True/False, to download thumbnails or bigger images)

    ddg.download(q, folder= f"./images/{q}/", max_urls=5, thumbnails=True) 


    picc = os.listdir(f"./images/{q}/")   # get the contents of the folder
                                                    # each downloaded image will have a randomic UUIDv4 name so next step is 
                                                    # to change its name with the name of the current q

    if len(picc) == 0:                          # if the the list is empty..
        html += f'{q}' # ..add now the <html> for just the text, since there are no images downloaded..
        html += "\n"
        os.rmdir(f'./images/{q}/')            # ..and delete the folder created, since is useless..
        continue                                    # ..from now on this q can't do anything more, let's go to the next iteration



                                                    # Layout q and its pic!
    pic = picc[0]                               # let's take a random picture from the array

    os.rename(f'./images/{q}/{pic}', f'./images/{q}/{q}.jpg')  # This is to rename the pic with qBinded + the .jpg extension
    os.replace(f'./images/{q}/{q}.jpg', f'./images/{q}.jpg')   # This is to move the pic to the main folder
    shutil.rmtree(f'./images/{q}/')                                        # and it's time to delete the folder of this q

    html += f"""    {q}"""                        # Now let's fill the html with text and the pic
    html += "\n"
    html += f"""    <span><img src="./images/{q}.jpg"></span>"""
    html += "\n"

    



                
                                                      # Close the html text
html += ''' </p><div>
    </body>                                                              
</html>'''

with open('index.html','w') as index: # Save the <html> file!
    index.write(html)