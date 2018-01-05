# story of life

print('***Some useful info: type y for yes and n for no in response to yes or no questions')

ans = input('It is pitch-black except for the small circle of light in the distance. Go toward the light? ')

# first decision
if ans == 'y':
    print('''The light is getting bigger, until you are completely enveloped in the light. Congrats! You just made it out of the womb!
You are very slimy though...''')


# second decision, dead end
if ans == 'n':
    print('Come on, you know you wanna go toward the light. That is the only way the story will progress.')
    input('It is pitch-black except for the small circle of light in the distance. Go toward the light? ')
    if ans == 'n':
        print('Well, you just broke the game. Restart this somehow and choose yes.')
