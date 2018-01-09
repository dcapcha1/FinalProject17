# story of life

print('''***Some useful info: type 'y' for yes and 'n' for no in response to yes or no questions''')

# this is where class info will be

class Human(object):

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def say_name(self):
        print(f'{self.name}')

    def take_damage(self, damage = 20):
        self.health -= damage
        print(f'''You are now at {self.health} health. Ouch. Git gud.''')

while True:
    human1 = Human(input('''What is your name? '''), 100)
    # first decision, only answer is y
    ans = input(f'''It is pitch-black except for the small circle of light in the distance. Go toward the light, {human1.name}? ''')
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
                        ans4 = input('''You're jealous, so you destroy it, right? ''')
                        while True:
                            # branch 4
                            if ans4 == 'y':
                                ans5 = input('''If you continue to say yes, you will be banished to the shadow realm, do you want that? ''')
                                while ans5 == 'y':
                                    # branch 5
                                    if ans5 == 'y':
                                        print(f'''You asked for it. So, as time passes by, you see some gangsters coming toward you. You look 'em in the eye and know they're after you.
                                        One of the kind African-American members approaches you and takes out his bat. He beats the crap out of you. First hit.''')
                                        human1.take_damage()
                                        print('''Second hit.''')
                                        human1.take_damage()
                                        print('''He keeps hitting at you.''')
                                        human1.take_damage()
                                        human1.take_damage()
                                        human1.take_damage()

                                        print(f'''You are now dead. Gg no re, {human1.name}. Actually nvm, re cuz I don't know how else to make this code work.''')
                                        break

                                    # branch 5
                                    if ans5 == 'n':
                                        print('''Alright, I'm glad you changed your ways.''')






                    # branch 2
                    if ans2 == 'n':
                        print('''Good, anthropoid. No trouble for you today!''')



            # branch 1
            if ans1 == 'n':
                print('''That's a good boy/girl/thing/object/gender fluid humanoid!''')
                ans3 = input('''Some time passes now, and you're in elementary school. Fractions and equations, yay. Back when life was simpler... but anyway,
                you have a major decision to make right now. Will you be a good, hard-working student (y) or a lazy, good-for-nothing (n)? ''')
                while True:
                    # branch 3
                    if ans3 == 'y':
                        print('''That's what I like to hear! You may not realize it now, but you're setting yourself up for success in the future. Hopefully when
                        the time comes, you realize that what you did in this moment was the most important decision you could have ever made. Now enough with my spiel,
                        it's time to get back to the story!''')

                    # branch 3
                    if ans3 == 'n':
                        print('''Well, it's your choice. Nothing I can do about it. Throw away your life if you want.''')


    # will loop back to y
    if ans == 'n':
        print('Come on, you know you wanna go toward the light. That is the only way the story will progress.')
        input('It is pitch-black except for the small circle of light in the distance. Go toward the light? ')

