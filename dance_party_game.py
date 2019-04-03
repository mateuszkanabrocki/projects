from sys import exit

from textwrap import dedent

import random

from os import system

# freeze program execusion for specified time
from time import sleep

# get an OS name
import platform


class Engine(object):

    # download a scenerio and scenes
    def download(self, scenerio):

        self.scenerio = scenerio

    # play a game
    def play(self):

        next_game_name = None

        while next_game_name not in ('game_over', 'last_scene'):
            next_game_name = self.scenerio.next_scene()

        self.scenerio.next_scene()
        exit()

    # run next scene
    def next_scene(self):
        pass


class Scene(object):

    def __init__(self):
        self.time = 1

    # clear IDLE window
    def clear(self):

        # for Windows
        if platform.system() == "Windows":
            system('cls')

        # for Mac and Linux
        else:
            system('clear')


class Game_intro(Scene):

    def run(self):

        self.clear()
        print(dedent("""
            WARNING!!!
            This game is not for the people with weak nerves...
            """))

        sleep(2*self.time)
        self.clear()
        print(dedent("""
                    Today you are Jeff. Recently you've started attending
                    dancing class, brazilian zouk classes more precisely .
                    (it's a dance in couples like salsa or tango)

                    You were always scared of dancing. That's why you
                    started attending these classes. You're doing pretty
                    fine but you're still a little a bit shy when
                    it's a bout dancing in the party.

                    Finally, your friend encouraged you to go to one.

                    Damn, you're scared like a scared mouse!
                    """), end="")

        sleep(4*self.time)
        print(dedent("""
                    But here you are in Pick&Roll Club latino party
                    saturday night! It's 11 p.m.. There is stil only
                    a few people around.
                    That's good. The less the better, right?

                    You hear the song rhytm going like:
                    buuum  cik cik...
                    buuum  cik cik...
                    """))

        return 'waiting'


class Waiting(Scene):

    def run(self):

        wait_number = 0

        while wait_number < 3:

            wait = input("\nWanna wait for the next song?\n(yes/no)\n> ")
            self.clear()

            if 'yes' in wait:
                print("\nLet's wait. Waiting is cool.\n")
                sleep(3*self.time)
                wait_number += 1
                print(random.choice([
                                    "This song is pretty fast.",
                                    "Ahh, it's Kizomba...",
                                    "Ahh, it's Bachata...",
                                    "Ahh, it's Salsa...",
                                    "I don't know this song.",
                                    "I don't like this song.",
                                    "This song is really slow."
                                    ]))

            elif 'no' in wait:
                return 'ask_to_dance'

            else:
                pass

        self.clear()
        print(dedent("""
                    You've been waiting so long for the better song
                    that finally some girl asked you to dance.

                    """))

        sleep(5*self.time)
        return 'start_to_dance'


class Ask_to_dance(Scene):

    def run(self):

        while True:
            self.clear()
            answer = input((dedent("""
                    Ok. Finally you've found enough courage to get yourself
                    on the dance floor. Good for you!

                    Your eyes found a girl at the bar waiting for the dance.
                    You are slowly walking in her direction. She starts to look
                    at you too.

                    What do you do next?

                        a) say something to her
                        b) just keep looking at her
                        c) turn back and run for your life!
                        d) smile and show her your hand

                    (type a, b, c or d)
                    > 
                                """)))

            if answer == 'a':
                said = input("Say something to her:\n> ")
                self.clear()
                said_list = said.split()

                for i in range(len(said_list)):
                    print(random.choice([
                        (f"buuum {said_list[i]}!"),
                        (f"cik {said_list[i]}!")
                                        ]), end="")

                print("\n(The music is too loud!)\n")
                sleep(5*self.time)

            elif answer == 'b':
                sleep(2*self.time)
                self.clear()
                print(dedent("""
                            You've been looking at her so long
                            she got scared and run.

                            Happens...
                            Let's wait for another song then.
                            """))
                sleep(1*self.time)

                return 'waiting'

            elif answer == 'c':
                sleep(1*self.time)
                self.clear()
                print("You are safe now.\n")
                sleep(1*self.time)

                return 'waiting'

            elif answer == 'd':
                self.clear()
                return 'start_to_dance'

            else:
                pass


class Start_to_dance(Scene):

    def run(self):

        try:
            while True:
                for i in range(1, 5):
                    self.clear()
                    print(dedent(f"""
                                Ok. Here we are on the dance floor.
                                Now, just to start in rhythm.

                                Music is quite fast.

                                Try to move on 1.

                                {i}
                                (press 'Ctrl + C' to move)
                                """))

                    sleep(1*self.time)

        except KeyboardInterrupt:
            self.clear()
            print(f"You moved on {i}!")

            if i != 1:
                print("Not the best start...\n", end="")

            else:
                print("Great job!")

        return 'just_dance'


class Just_dance(Scene):

    def just_dancing(self):

        moves = {
            'a': "Going into laterall!",
            'b': "Now a little bit of crusado...",
            'c': "And a bumerang!\n",
            'd': "Taking some breath while leading boneca.",
            'e': "This song is too fast for roasted chicken!\nI don't wanna die!"
                }

        print(dedent("""
                    Ok, the steps.
                    I need to dance some other steps now.

                    What should I dance now?

                    a) laterall
                    b) cruasado
                    c) bumerang
                    d) boneca
                    e) roasted chicken

                    (type a, b, c, d or e)
                    """))

        i = 0

        while i < 5:
            
            steps = input()

            if steps in moves.keys():
                print(moves.get(steps))
                i += 1

            else:
                pass

    def run(self):

        print(dedent("""
                Ok. Here we go. Just keep the rhythm, listen to the music,
                watch the dance floor and lead the steps."""))

        sleep(2*self.time)
        self.just_dancing()

        while True:
            self.clear()
            to_do = input(dedent("""
                                Oh no! While doing a turn girl's hair
                                tungled around my neck!
                                I can't breath!

                                What should I do now?

                                a) turn her again
                                b) turn myself closkwise
                                c) turn myself counterclockwise

                                (type a, b, or c)
                                """))
            worse = None

            if to_do == 'a':
                self.clear()
                print("You fainted.\nNice try though!")
                return 'game_over'

            elif to_do == 'b':

                if worse is None:
                    print("\nOh no! Not in this direction!",
                          "It's getting worse!")
                    sleep(4*self.time)
                    worse = True

                else:
                    self.clear()
                    print("You fainted./n Nice try though!")
                    return 'game_over'

            elif to_do == 'c':
                self.clear()
                print("You are rescued!")
                sleep(2*self.time)
                break

            else:
                pass

        self.just_dancing()

        while True:
            self.clear()
            to_do = input(dedent("""
                                Watch out!
                                One couple is moving very fast towards us.
                                They can't see us!

                                What should I do now?

                                a) step in the their way to block them and
                                    rescue the girl you're dancing with
                                b) jump to the left!

                                (type a or b)
                                """))
            if to_do == 'a':
                print(dedent("""
                            You step in the couple's way.
                            They hit you like a tornado,
                            but you're girl is safe!

                            That hurt."""))

                sleep(3*self.time)
                return 'last_scene'

            elif to_do == 'b':
                print(dedent("""
                            You jump to the left like lion!
                            You avoided the dangerous couple
                            but youbumped into another one.")

                            That hurt."""))
                            
                sleep(3*self.time)
                return 'last_scene'


class Last_scene(Scene):

    def run(self):

        print(dedent("""
                    You did it! The song finished and you're alive!
                    Good job!
                    """))


class Game_over(Scene):

    def run(self):
        print("\nIt could be better. But at least you tried!")


class Scenerio(object):

    def __init__(self, first_scene_name):
        self.current_scene_name = first_scene_name


class Zouk_scenerio(Scenerio):

    # assign strings to scenes
    scenerio = {
        'game_intro': Game_intro(),
        'waiting': Waiting(),
        'ask_to_dance': Ask_to_dance(),
        'start_to_dance': Start_to_dance(),
        'just_dance': Just_dance(),
        'last_scene': Last_scene(),
        'game_over': Game_over()
    }

    # run next scene, return following scene name
    def next_scene(self):
        self.current_scene_name = Zouk_scenerio.scenerio.get(self.current_scene_name).run()
        return self.current_scene_name


# create a zouk_scenerio object
zouk_scenerio = Zouk_scenerio('game_intro')
# create this game engine object
zouk_engine = Engine()
# change so you get a name and the Scenerio class is imported from other file
zouk_engine.download(zouk_scenerio)
# run the game
zouk_engine.play()
