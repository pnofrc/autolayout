# November 2021, copyleft || Funix || Zine Camp, Worm, Rotterdam


# NLTK (Natural Language ToolKit) is a library for Natural Language Process.
# We will use it to get the Part Of Speech (POS) of the speech-to-text results.
#
# What does it mean?
#
# It works as grammar tagging: for instance, the sentence "Around the clouds"
# would have this output:
#
#       [('Around', 'IN'), ('the', 'DT'), ('clouds', 'NN')]
#
# 'IN' means 'preposition' - 'DT' means 'determiner' - 'NN' means 'noun, common, singular or mass'


import nltk                             # to use NLTK
from urllib.request import urlopen      # to request urls usage

url = 'https://pad.xpub.nl/p/grammar/export/txt'
response = urlopen(url)
text = response.read().decode('UTF-8')

tokens = nltk.word_tokenize(text)       # Tokenize the words :: split each word

# Elaborate the Part of Speech! It will create an array, a list
pos = nltk.pos_tag(tokens)


# print(pos)                              # print the array!
# time.sleep(2)                           # check it in the console!


# To see all the POS tags, open the terminal and copy:
#
#       python3
#       import nltk
#       nltk.help.upenn_tagset()

#       see also:
#       https://cheatography.com/deacondesperado/cheat-sheets/nltk-part-of-speech-tags/


# start the layouting :: html + css + paged.js >>
#
# declare html :: we will fill it in the process with loops
# declare the first part of the text for two html files with different CSS

html = ''

html = '''
<!DOCTYPE html>
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

    <div class="contents">
'''

# Process each element of the list

for e in pos:                           # e is the current element, pos is the array to process

    print(e)
    if e[0] == '.':                     # if e is a dot, its class will be 'dot'
        html += "   <span class='dot'>.</span><br> \n"

    else:                               # fill the html with each word and assign it as class its POS
        html += "   <span class='"+e[1]+"'> "+e[0]+" </span>\n"

        # Close the html text
html += ''' </div>
    </body>                  
</html>'''

# to tidy wrong " . " and " ' " position
html = html.replace(' .', '.').replace(" '", "'")

# Save the <html> files!

with open('./index.html', 'w', encoding='utf-8') as index:
    index.write(html)
    index.close()

