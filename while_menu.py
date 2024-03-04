""" While loop Menu - Guitar Tools"""
menu_option = ''

while menu_option != '3':
    print('Guitar tools:', '1: Fretboard Visualizer', '2: Use Professor Jones\'s app', '3: quit practice', sep="\n")
    menu_option = input("Enter a number for more info or '3' to quit: ")
    if menu_option == '1':
        print("""e |---|---|---|---|---|---|---|---|---|---|---|---|
B |---|---|---|---|---|---|---|---|---|---|---|---|
G |---|---|---|---|---|---|---|---|---|---|---|---|
D |---|---|---|---|---|---|---|---|---|---|---|---|
A |---|---|---|---|---|---|---|---|---|---|---|---|
E |---|---|---|---|---|---|---|---|---|---|---|---|""")
    elif menu_option == '2':
        print("Professor Jones's app is currently under development. Please select a different option at this time.")
