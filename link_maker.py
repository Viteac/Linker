logo='''  _____      _            __        ____    ____         __
 |_   _|    (_)          [  |  _   |_   \  /   _|       [  |  _
   | |      __   _ .--.   | | / ]    |   \/   |   ,--.   | | / ] .---.  _ .--.
   | |   _ [  | [ `.-. |  | '' <     | |\  /| |  `'_\ :  | '' < / /__\\[ `/'`\]
  _| |__/ | | |  | | | |  | |`\ \   _| |_\/_| |_ // | |, | |`\ \| \__., | |
 |________|[___][___||__][__|  \_] |_____||_____|\'-;__/[__|  \_]'.__.'[___] \n Ver 1.0 by Viteac viteac.blogspot.com\n'''
def create_link():
    add = input('Enter the address:\n>>> ')
    sec = input('Enter a section:\n>>> ')
    tit = input('Enter a Title:\n>>>')
    ne = input('Open link in new window Y/N?:\n>>>').lower()
    if ne == 'y':
        ne = '_blank'
    else:
        ne = 'self'
    lead = f'<a href="https://{add}"'
    trail = '</a>'
    new = f'target="{ne}"'
    titlead = f'title={tit}"'
    tittrail = '>'
    if ne == '_blank':
        link = f'{lead}{new}{titlead}{tittrail}{sec}{trail}'
        if tit == "":
            link = f'{lead} {new}{tittrail}{sec}{trail}'

    else:
        link = f'{lead} {titlead}{tittrail}{sec}{trail}'
        if tit == "":
            link = f'{lead}{tittrail}{sec}{trail}'

    print(link)
    choice = False
    while choice not in ['1', '2']:
        choice = input(f'1. Another Hyperlink\n 2. Main Menu\n >>> ')
    if choice == '1':
        create_link()
    elif choice == '2':
        menu()


def image_link():

    image_add = input('Enter image file name with extension.\n>>> ').lower()
    alter = input('Enter alternative text.\n>>> ')
    image_lin = f' <img src="{image_add}" alt="{alter}"> '
    print(image_lin)

    atributs = False
    while atributs not in ['y', 'n']:
        atributs = input('Do you want to add size atributes width and height?\n>>> ').lower()

    if atributs == 'y':
        while True:
            try:
                width = int(input('Enter width of the image.\n>>> '))
                height = int(input('Enter height of the image.\n>>> '))
            except ValueError:
                print('Try again. Enter numeric value')
            else:
                break

        print(f' <img src="{image_add}" alt="{alter}" width="{width}" height="{height}">')

    choice = False
    while choice not in ['1', '2']:
        choice = input(f'1. Another image link\n 2. Main Menu\n >>> ')
    if choice == '1':
        return image_link()


def menu():
    print(logo)
    options = False
    while options not in ['1', '2', '3']:
        options = input(f'What do yo want to do?\n1. Create Hyperling.\n2. Create image link.\n3. Exit\n>>> ')
    if options == '1':
        create_link()
    elif options == '2':
        image_link()

while True:
    menu()
