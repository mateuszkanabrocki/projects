import sys
import os
from typing import List, Dict, Union, Optional, Any


this_module = os.path.dirname(os.path.realpath(__file__))
planisphere_gothonweb_path = os.path.join(this_module, __file__)

direction = [] # type: List[str]
do = ['shoot', 'dodge', 'hit', 'kick', 'tell', 'throw', 'place', 'leave', 'kill']
stop = ['the', 'in', 'of', 'from', 'at', 'it', 'a', 'him']
noun = ['joke', 'bomb', 'gothon']


class Room(object):

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description
        self.paths = {} # type: Dict[str, Room]

    def go(self, direction: str) -> Any: # Union[Room, None] throw Room not defined error
        return self.paths.get(direction, None)

    def add_paths(self, paths: Any) -> None: # paths: Dict[str, Room] throw Room not defined error
        self.paths.update(paths)


start_place = Room("Central Corridor",
"""
The Gothons of Planet Percal #25 have invaded your ship and destroyed
your entire crew.  You are the last surviving member and your last
mission is to get the neutron destruct bomb from the Weapons Armory, put
it in the bridge, and blow the ship up after getting into an escape pod.

You're running down the central corridor to the Weapons Armory when a
Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown
costume flowing around his hate filled body.  He's blocking the door to
the Armory and about to pull a weapon to blast you.
""")
    

laser_weapon_armory = Room("Laser Weapon Armory",
"""
Lucky for you they made you learn Gothon insults in the academy.  You
tell the one Gothon joke you know: Lbhe zbgure vf fb sng, jura fur fvgf
nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.  The Gothon stops, tries
not to laugh, then busts out laughing and can't move.  While he's
laughing you run up and shoot him square in the head putting him down,
then jump through the Weapon Armory door.

You do a dive roll into the Weapon Armory, crouch and scan the room for
more Gothons that might be hiding.  It's dead quiet, too quiet.  You
stand up and run to the far side of the room and find the neutron bomb
in its container.  There's a keypad lock on the box and you need the
code to get the bomb out.  If you get the code wrong then the
lock closes forever and you can't get the bomb. 
The code is a 1 digit number from 1 to 3 (so you have any chance ;) ).
""")


the_bridge = Room("The Bridge",
"""
The container clicks open and the seal breaks, letting gas out.  You
grab the neutron bomb and run as fast as you can to the bridge where you
must place it in the right spot.

You burst onto the Bridge with the netron destruct bomb under your arm
and surprise 5 Gothons who are trying to take control of the ship.  Each
of them has an even uglier clown costume than the last.  They haven't
pulled their weapons out yet, as they see the active bomb under your arm
and don't want to set it off.
""")


escape_pod = Room("Escape Pod",
"""
You point your blaster at the bomb under your arm and the Gothons put
their hands up and start to sweat.  You inch backward to the door, open
it, and then carefully place the bomb on the floor, pointing your
blaster at it.  You then jump back through the door, punch the close
button and blast the lock so the Gothons can't get out.  Now that the
bomb is placed you run to the escape pod to get off this tin can.

You rush through the ship desperately trying to make it to the escape
pod before the whole ship explodes.  It seems like hardly any Gothons
are on the ship, so your run is clear of interference.  You get to the
chamber with the escape pods, and now need to pick one to take.  Some of
them could be damaged but you don't have time to look.  There are 2 pods,
which one do you take?
""")


the_end_winner = Room("Happy Ending",
"""
You jump into pod and hit the eject button.  The pod easily slides out
into space heading to the planet below.  As it flies to the planet, you
look back and see your ship implode then explode like a bright star,
taking out the Gothon ship at the same time.  You won!
""")


shoot = Room("Death",
"""
Quick on the draw you yank out your blaster and fire
it at the Gothon.  His clown costume is flowing and
moving around his body, which throws off your aim.
Your laser hits his costume but misses him entirely.
This completely ruins his brand new costume his mother
bought him, which makes him fly into an insane rage
and blast you repeatedly in the face until you are
dead.  Then he eats you.
""")


dodge = Room("Death",
"""
Like a world class boxer you dodge, weave, slip and
slide right as the Gothon's blaster cranks a laser
past your head.  In the middle of your artful dodge
your foot slips and you bang your head on the metal
wall and pass out.  You wake up shortly after only to
die as the Gothon stomps on your head and eats you.
""")


wrong_code = Room("Death",
"""
The lock buzzes one last time and then you hear a
sickening melting sound as the mechanism is fused
together.  You decide to sit there, and finally the
Gothons blow up the ship from their ship and you die.
""")


throw_the_bomb = Room("Death",
"""
In a panic you throw the bomb at the group of Gothons
and make a leap for the door.  Right as you drop it a
Gothon shoots you right in the back killing you.  As
you die you see another Gothon frantically try to
disarm the bomb. You die knowing they will probably
blow up when it goes off.
""")


wrong_pod = Room("Death",
"""
You jump into a random pod and hit the eject button.  The pod escapes
out into the void of space, then implodes as the hull ruptures, crushing
your body into jam jelly.
""")


class Map(object):

    dict = {'shoot': shoot,
            'dodge': dodge,
            'tell a joke': laser_weapon_armory,
            'say joke': laser_weapon_armory,
            'right_code': the_bridge,
            'wrong_code': wrong_code,
            'throw the bomb': throw_the_bomb,
            'slowly place the bomb': escape_pod,
            'right_pod': the_end_winner,
            'wrong_pod': wrong_pod
           }


start_place.add_paths({
    'shoot': Map.dict['shoot'],
    'kill': Map.dict['shoot'],
    'dodge': Map.dict['dodge'],
    'hit': Map.dict['dodge'],
    'kick': Map.dict['dodge'],
    'tell joke': Map.dict['tell a joke']

})

laser_weapon_armory.add_paths({
    'right_code': Map.dict['right_code'], # a testing cheat
    'wrong_code': Map.dict['wrong_code'] # a testing cheat
})

the_bridge.add_paths({
    'throw bomb': Map.dict['throw the bomb'],
    'place bomb': Map.dict['slowly place the bomb'],
    'leave bomb': Map.dict['slowly place the bomb']
})

escape_pod.add_paths({
    'right_pod': Map.dict['right_pod'], # a testing cheat
    'wrong_pod': Map.dict['wrong_pod'] # a testing cheat
})

START = 'start_place'

def load_room(name: str) -> Optional[Any]:
    white_list = ('start_place', 'laser_weapon_armory', 'the_bridge','escape_pod',
                  'the_end_winner', 'wrong_pod', 'generic_death', 'throw_the_bomb',
                  'shoot', 'dodge', 'wrong_code')

    if name not in white_list:
        raise Exception(f'You can\'t run load_room with {name} as a parameter.')
    return globals().get(name)

def name_room(room: Room) -> Union[str, Exception]:
    white_list = ('start_place', 'laser_weapon_armory', 'the_bridge','escape_pod',
                  'the_end_winner', 'wrong_pod', 'generic_death', 'throw_the_bomb',
                  'shoot', 'dodge', 'wrong_code')

    # give room object, get room name
    for key, value in globals().items():
        if value == room and key in white_list:
            return key
    raise Exception(f'You can\'t run name_room with {room} as a parameter.')
