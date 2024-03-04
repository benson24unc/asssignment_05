""" While loop Nested Menu - Guitar Tools"""
menu_option = ''

while menu_option != '3':
    print(f'''
Guitar tools:
1: Fretboard Visualizer
2: Use Professor Jones's app
3: Quit practice
''')
    menu_option = input("Enter a number for more info or '3' to quit: ")
    if menu_option == '1':
        print("""e |---|---|---|---|---|---|---|---|---|---|---|---|
B |---|---|---|---|---|---|---|---|---|---|---|---|
G |---|---|---|---|---|---|---|---|---|---|---|---|
D |---|---|---|---|---|---|---|---|---|---|---|---|
A |---|---|---|---|---|---|---|---|---|---|---|---|
E |---|---|---|---|---|---|---|---|---|---|---|---|""")
    elif menu_option == '2':
        anticipation_response = input("Are you looking forward to Professor Jones's app? Enter (y or n): ")
        if anticipation_response == 'y':
            print("Let's hope it is out soon!")
        else:
            print("Understandable, we weren't all meant to be guitar heros!")