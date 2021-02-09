import os


def filer():
    while True:
        print('Enter the file name if file exists in working directory otherwise enter a full path.'
              '\nLink maker is working with .txt files')

        file = input('>>>')
        if os.path.isfile(file) is True:
            if file.endswith('.txt') is True:
                print('You want to change')
                return file
            else:
                print('Wrong')

file= filer()

with open(file)as f:
    read = f.readlines()


link = []

for i,v in enumerate(read):
    if read[i] == '\n':
        read.pop(i)

for i,v in enumerate(read):
    read[i] = v.rstrip('\n')


for i,v in enumerate(read):
    link.insert(i, f'<a href="#{v}">{v}</a><br />\n')

with open('set_desc.txt') as f:
    set_desc = f.readlines()

for i,v in enumerate(set_desc):
    set_desc[i] = v.rstrip('\n')

comb=[]

for i,v in enumerate(read):
    comb.insert(int(i), f'<div id="{v}"><b>{v}</b><br />{set_desc[i]}&nbsp;</div><br />\n')

co = 0
k = file.find(".")
saver = file[:k]+"_links.txt"

def save(saver,c):

    while True:
        if os.path.isfile(saver) is True:
            c +=1
            saver = f'{file[:k]}_links{c}.txt'
            return save(saver,c)
        else:
            return saver

savers= save(saver,co)

with open(savers, 'a') as f:
    for x in link:
        f.writelines(x)

    f.writelines('\n' *2)
    for y in comb:
        f.writelines(y)

print(f'Your links are saved in: {saver}')

