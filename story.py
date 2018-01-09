# story of life

print('***Some useful info: type y for yes and n for no in response to yes or no questions')

while True:
    # first decision, only answer is y
    ans = input('It is pitch-black except for the small circle of light in the distance. Go toward the light? ')
    if ans == 'y':
        print('''The light is getting bigger, until you're completely enveloped in the light. Congrats! You just made it out of the womb!
        You're very slimy though. Someone's holding you, probably the doctor. Everything is starting to get clearer now.''')
        # second decision, branches
        ans1 = input('''Days pass by and you are in a crib. Would you like to cry? ''')
        while True:
            # branch 1
            if ans1 == 'y':
                print('''Be quiet! You've just woken the parents! Oh no, they're coming now. Try not to anger them afterwards, they work hard
                really hard for you, after all.''')
                # third decision, only answer is n
                ans2 = input('''...It's your first day in pre-school! You can see the teacher reading a book to all the children. After story time, you play with blocks
                and try to build a car. It fails, but at least you tried. Look at that human over there, he's built a large tower of blocks. You're jealous, so you
                destroy it, right? ''')
                while True:
                    # branch 2
                    if ans2 == 'y':
                        print('''You're better than that. Don't do it.''')
                        ans2

                    # branch 2
                    if ans2 == 'n':
                        print('''Good, anthropoid. No trouble for you today!''')



            # branch 1
            if ans1 == 'n':
                print('''That's a good boy/girl/thing/object/gender fluid humanoid!''')
    # will loop back to y
    if ans == 'n':
        print('Come on, you know you wanna go toward the light. That is the only way the story will progress.')
        input('It is pitch-black except for the small circle of light in the distance. Go toward the light? ')

