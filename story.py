# story of life

print('''***Some useful info: type 'y' for yes and 'n' for no in response to yes or no questions. Once you reach an ending, it will reset
back to the last decision point. If you want to exit the game (like when you reach an ending) enter a letter that isn't 'y' or 'n' into
an input function that asks for 'y' or 'n' ''')

# this is where class info will be

class Human(object):

    def __init__(self, name, action, health, dep_level):
        self.name = name
        self.action = action
        self.health = health
        self.dep_level = dep_level

    def say_name(self):
        print(f'{self.name}')

    def action(self):
        print(f'{self.action}')

    def take_damage(self, damage = 20):
        self.health -= damage
        print(f'''You are now at {self.health} health. Ouch. Git gud.''')

    def dep_level_inc(self, damage = 10):
        self.dep_level += damage
        print(f'''You are now at {self.dep_level} depression level.''')

    def dep_level_dec(self, dec = 20):
        self.dep_level -= dec
        print(f'''You are now at {self.dep_level} depression level.''')

    def fight(self, damage = 10):
        self.health -= damage
        print(f'''Your enemy is now at {self.health} health. But I didn't hear no bell!''')

    def fatality(self, damage = 1000):
        self.health -= damage
        print(f'''Your enemy is now at {self.health} health. Damn, you didn't have to do him like that!''')


while True:
    human1 = Human(input('''What is your name? '''), 100, 0, 0)
    teacher = Human(input('''What is your favorite teacher's name? '''), 100, 0, 0)
    person = Human(input('''Who do you hate the most? '''), 100, 0, 0)
    person1 = Human(input('''Who is someone you like? '''), 100, 0, 0)
    person2 = Human(input('''Who is just some random person? '''), 100, 0, 0)
    print('''Alrighty then, let the story begin!''')
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
                                while True:
                                    # branch 5
                                    if ans5 == 'y':
                                        print(f'''You asked for it. So, as time passes by, you see some gangsters coming toward you. You look 'em in the eye and know they're after you.
                                        One of the kind African-American members approaches you and takes out his bat. He beats the crap out of you. First hit.''')
                                        human1.take_damage()
                                        print('''Second hit.''')
                                        human1.take_damage()
                                        print('''He keeps hitting you.''')
                                        human1.take_damage()
                                        human1.take_damage()
                                        human1.take_damage()
                                        print(f'''You are now dead. Gg. This is an ending, kind of. But you can take a different route now.''')
                                        break

                                    # branch 5
                                    if ans5 == 'n':
                                        print('''Alright, I'm glad you finally came to your senses. No one likes the shadow realm.''')
                                        # <insert 2nd branch 1 after finishing that branch>
                            # branch 4
                            if ans4 == 'n':
                                print('''Good, don't ever think about doing that.''')
                                # <insert 2nd branch 1 after finishing that branch>
                    # branch 2
                    if ans2 == 'n':
                        print('''Good, anthropoid. No trouble for you today!''')
                        ans6 = input(f'''Years go by, and you're in middle school. Your favorite teacher, {teacher.name}, is teaching there. {teacher.name}
                        never gives any homework or tests. One day, you walk into the classroom to retrieve your forgotten notebook. But before you go in,
                        you see {teacher.name} making out with another teacher. Do you tell on them? ''')
                        while True:
                            # branch 6
                            if ans6 == 'y':
                                print(f'''Good, that was the right thing to do. {teacher.name} may have been your favorite teacher, but no one is above the law.''')
                                print(f'''Unfortunately, since your favorite teacher was fired, the new teacher is terrible. You're getting homework every day and
                                even pop quizzes! The person you hate the most, {person.name}, approaches you one day and doesn't look happy about the new teacher.
                                And s/he knows you're the reason why there's a new teacher.''')
                                ans7 = input('''S/he's ready to throw hands. You're ready to throw hands. But do you? ''')
                                # branch 7
                                if ans7 == 'y':
                                    print('''You throw the first punch.''')
                                    human1.fight()
                                    print('''Do another, come on, give him/her the ol one two!''')
                                    for x in range(2):
                                        human1.fight()
                                    print('''Give him/her an uppercut, finish him/her off!''')
                                    human1.fatality()
                                    break
                            # branch 6
                            if ans6 == 'n':
                                print(f'''Well, at least you're not a snitch. Now, since you decided not to rat {teacher.name} out, he goes on with his sexual adventures. However,
                                you become''')
                                break

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
                        it's time to get back to the story! Well, it's that time now. High School. I skipped middle school since it's boring and saves me some time. Because of your decision
                        to be a good, hard-working student, you got into Magnet. Unfortunately, depression settles in.''')
                        human1.dep_level_inc()
                        print('''Feels bad, and now you're a junior. And you have to do a 20-40 minute presentation on a boring subject. Somehow you manage to do it, but
                        in the process your depression increases. And you're deciding on which college to go to, but you know you're not good enough to get into the one you want.
                        Depression increases.''')
                        human1.dep_level_inc()
                        print('''Senior year, ayyy. Finally you don't have to stress about anything. You survived.''')
                        human1.dep_level_dec()
                        ans8 = input('''You're finally an adult now. Would you like to work at an office where you're financially secure but bored af? ''')
                        while True:
                            # branch 8
                            if ans8 == 'y':
                                print(f'''Alright, I guess you have no ambition to do something more with your life. You sit at your office
                                chair going through the piles of documents on your desk. You don't even know what you're doing exactly, all
                                you're doing is scribbling some stuff on each paper then putting it on another pile. There is no value to
                                what you are doing at all. It might as well just be busywork. So much for that degree.You don't like the
                                other people in the office. They're all just as boring as you. You go home to your spouse, {person1.name}.
                                {person1.name} grows tired of you after all the years of a stale marriage.{person1.name} leaves you for
                                {person2.name} since s/he is much more interesting and exciting than you. All you have left in your life is
                                your job, and we all know how that's going...You're 80 now. Nothing really happened in your adult life besides
                                {person1.name} leaving you for {person2.name}. It's pretty much the end of the road now. Everything that happened in your life seemed pretty pointless as you reach the
                                end. Goodbye...''')
                                break
                            # branch 8
                            if ans8 == 'n':
                                print(f'''You decided to ditch the office job and go for something different. You're struggling for money right now, but it doesn't matter since you're
                                happy. You make your spouse, {person1.name}, happy ;), and life seems purposeful. The unfortunate thing is your spouse gets hit by a car and is murdered.
                                That's just how it goes sometimes. The circle of life.''')
                                human1.dep_level_dec
                                print(f'''Rip. You're so depressed you go through life with no purpose. You don't even like what you do anymore. {person1.name} meant everything to you and
                                you lost him/her. End of the line...''')
                                break
                    # branch 3
                    if ans3 == 'n':
                        print('''Well, it's your choice. Nothing I can do about it. Throw away your life if you want. Too bad cuz now you're 40 and work at McDonalds. It's a miracle you can
                        afford your rent. You have no one in your life since they all moved on to bigger and better things. But things finally turn around. As you go into your local flea
                        market, you buy a lottery ticket like you do every day. You get a nickel and scratch the card. A cherry, a banana, and a strawberry. Then you get hit by a truck and die.
                        ¯\_(ツ)_/¯''')
                        break

    # will loop back to y
    if ans == 'n':
        print('Come on, you know you wanna go toward the light. That is the only way the story will progress.')
        input('It is pitch-black except for the small circle of light in the distance. Go toward the light? ')
