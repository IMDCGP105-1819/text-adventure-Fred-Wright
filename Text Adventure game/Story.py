import cmd
import textwrap
import sys
import os
import time
import random



#text.

def Town_Hall():
    line1 = "Although carrying it was a pain, you reach the town hall.\nAlfred notices you and immideately waves his son to take the plank off you.\n"
    line2 = "His wife comes out of the house and while he is fixing, smiles glow over all faces.\n"
    line3 = "Alfred turns around gleefully and shouts: Alfred and sons is back in action! \nWhen he leans back on the stall a quiet but noticeable nail drops from below.\n"
    line4 = "The whole stall falls to pieces with Alfred lying on top.. Soon after, Alfred and his wife have a bad divorce.\n"
    line5 = "I guess you cant fix it all.\n"
    for character in line1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in line2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in line3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in line4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    for character in line5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)

def Home_Text():
    line1 = "You pick out from your pocket the glasses and ask your mother to use them.\n"
    line2 = "Within seconds you realise tears running down her face, you ask: whats wrong?\n"
    line2 = "Mother: For years ive been pretending to read these papers just so I dont have to talk to your miserable father..\nBut even though he's in prison, i now still do it out of habit!\n"
    line3 = "This is the best gift anyones ever given to me, thank you son.\n"
    for character in line1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in line2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in line3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.09)

def Hellish_Path():
    line1 = "Seeing the back of someone in agony, you offer to help them by offering your shovel\n"
    line2 = "Suprised by your presence, he turns around, revealing that he is a demon.\nHe angrily takes the shovel, and starts digging...\n"
    line3 = "You get a wierd tingling feeling...\n"
    for character in line1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in line2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.08)
    for character in line3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.15)

def Unknown_Place():
    line1 = "Noticing the mystical ball fits snugly in the spot on the floor, OCD drives you to place it down.\n"
    line2 = "A red laser comes out forming a wierd dark object looking like the letter P, it floats, unaffected by gravity.\n"
    line3 = "Suddenly lots of these objects appear, all floating and when lines up, looks like the letters of the alphabet!\n"
    line4 = "They all, in sync, jiggle their bodies in a waving-like fashion and all fade into the mist.\n"
    line5 = "What?...\n"
    for character in line1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.07)
    for character in line2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.09)
    for character in line3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.12)
    for character in line4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.15)
    for character in line5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)

def City_Cells():
    line1 = "While walking through the cells, you simply flash your key at your dad.\n"
    line2 = "He simply gives you a note.\nThe note reads the plan of breaking out.\n"
    line3 = "At 1pm, the plan begins, you sneak in and open his cell, you end up making it out with relative ease.\n"
    line4 = "However rather suspiciously, your father decides to go to the town hall instead of reuniting with your mother...\n"
    for character in line1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in line2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.08)
    for character in line3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in line4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)

def River_Text():
    line1 = "In a simple kind guesture, you give your jug to the man who requires it, he fills it up, and heads back home.\n"
    for character in line1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)

def Waterfall_Text():
    line1 = "While walking up to the woman, she turns around, she immediately notices the bone in your hand\n"
    line2 = "She screams for it not to be true wailing at the thought that her beloved son is gone...\n"
    line3 = "You turn to head back, and let her grieve however when you turn around, she is nowhere to be seen\n"
    line4 = "The waves crash down, you realise you will never see her again.\n"
    for character in line1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.07)
    for character in line2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.09)
    for character in line3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.12)
    for character in line4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.15)

def Highgarden_Text():
    line1 = "While walking through the fields of flowers the mystical fiery bolt begins to heat up in your pocket..\n"
    line2 = "It heats up so much that when you take it out it burns your fingers. \nIt glows brighter and brighter, and you notice small sparks come off it..\n"
    line3 = "Those sparks lead to flares, these flares catch fire on the flowers engulfing the meadow.\nThe Flares get bigger, and more frequent, you slowly begin to walk away.\n"
    line4 = "Slowly turns to quickly as the flares spew like a volcano around it, quickly walking turns to flat out running.\n"
    line5 = "Locals notice and begin to run with you, the flares become fireballs that explode on the castles.\nCausing explosions, these fireballs melt all in their way, causing utter carnage and consume the lands.\n"
    line6 = "As you reach the outer rivers you look back...\n"
    line7 = "Castles crumbling, whole farms in flames and only a few survivng... this catastrophic wreckage is... horrible.\n"
    for character in line1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in line2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in line3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.07)
    for character in line4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in line5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in line6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    for character in line7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.15)

def GameOver():
    line1 = "While walking back to home you feel a strange presence, before you know it, you body has fainted and through the bump of your head on the floor, you wake up..\n"
    line2 = "The floor is smouldering, heat covers your body, when you arise to your feet, the demon is looking at you.\n"
    line3 = "Demon: You know why you're here?\nPetrified, You shake your head from side to side...\n"
    line4 = "Demon: You've completed the game, restored balance to your world.\n"
    line14 = "Actually.. no you havent.\n"
    line5 = "I serve the god of death, Hades and he is displeased with your actions.\nYour father was condemned to death, however you saved him, taking him from Hades.\n"
    line6 = "He was inprisoned for breaking the stall of a man called Alfred.\nHe did this because your mother and him slept together.\n"
    line7 = "Hades originally wanted Alfred dead, however your father was weak, just like you.\nHades then hoped that Alfred's wife would kill him, however that did not happen.\n"
    line8 = "Hades had condemned another family, starving and dehydrating them. \nThrough your actions they killed a mystical being, by the shape of a P, and they drunk from the river, with help of your jug.\n"
    line9 = "By my math you have taken 6 lives from hades, the 6th being your mother.\n"
    line15 = "My mother!?\n"
    line16 = "Demon: Yes, she was Hades-bound from suicide due to depression.\n"
    line10 = "However you did return one, with the woman at the waterfall.\n"
    line11 = "You ask, what about the thousands at highgarden?\n"
    line12 = "Demon: Well, i was just on my way to do it.\n But you helped my little quest of digging... A grave.\n"
    line13 = "For.... You......"
    for character in line1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.08)
    for character in line2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    for character in line3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.07)
    for character in line4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in line14:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.3)
    for character in line5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.13)
    for character in line6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    for character in line7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.12)
    for character in line8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.07)
    for character in line9:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)
    for character in line15:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.3)
    for character in line16:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.12)
    for character in line10:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    for character in line11:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in line12:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.25)
    for character in line13:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.5)
    sys.exit(0)
