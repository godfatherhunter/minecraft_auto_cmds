import keyboard
import time
from Helper_Functions import *

#  This program is meant to run in the background while your game is running. The commands work by using your
#  character's location so you should move while commands are running. I was running the Java version of minecraft but
#  the Windows version should work fine. (Some commands can be different though)
#  For more commands search for "Minecraft console commands" and there and tons of site that give details

# This is the character that the code will what for before typing out the commands.
# You don't want to change this to a key that you'll use in game.
KEY_BIND = '`'
CLONE = False  # Set this to True if you want to make a whole village with one button


def build_house():
    """
    This is an example function that builds a house by sending commands to minecraft using the console
    """
    # Loops to allow for the house

    while (True):
        print('Waiting for the ' + KEY_BIND + ' input')
        #  The loops waits for the specified input before it runs
        keyboard.wait(KEY_BIND)

        #  The fill command fills an area from point <x, y, z> to point <x, y, z> (So it can be a line, plane, or cube)
        #  The ~ in the command means relative to the player. (Your character stands at point <~0, ~0, ~0>)
        #  point <~1, ~0, ~0> is one cube way from your character in the x direction.
        type_to_console("fill ~1 ~-1 ~-5 ~10 ~5 ~5 minecraft:stone hollow")
        type_to_console("fill ~1 ~0 ~0 ~1 ~1 ~0 air")

        # Add in flooring
        type_to_console("fill ~2 ~-1 ~-4 ~9 ~-1 ~4 minecraft:acacia_planks")

        # Front Windows
        type_to_console("fill ~1 ~1 ~2 ~1 ~3 ~4 minecraft:glass_pane")
        type_to_console("fill ~1 ~1 ~-2 ~1 ~3 ~-4 minecraft:glass_pane")

        # Back Windows
        type_to_console("fill ~10 ~1 ~2 ~10 ~3 ~4 minecraft:glass_pane")
        type_to_console("fill ~10 ~1 ~-2 ~10 ~3 ~-4 minecraft:glass_pane")
        # Right Window
        type_to_console("fill ~3 ~1 ~5 ~8 ~3 ~5 minecraft:glass_pane")
        type_to_console("fill ~3 ~1 ~-5 ~8 ~3 ~-5 minecraft:glass_pane")

        # Lights
        type_to_console("setblock ~2 ~3 ~-4 minecraft:torch")  # setblock is used to set one block
        type_to_console("setblock ~9 ~3 ~-4 minecraft:torch")
        type_to_console("setblock ~2 ~3 ~4 minecraft:torch")
        type_to_console("setblock ~9 ~3 ~4 minecraft:torch")
        type_to_console("setblock ~0 ~2 ~1 minecraft:torch")
        type_to_console("setblock ~0 ~2 ~-1 minecraft:torch")

        # Roof
        for i in range(0, 5):
            output = "fill" + " ~" + str(0 + i) + " ~" + str(5 + i) + " ~" + str(-6 + i) + " ~" + str(
                11 - i) + " ~" + str(5 + i) + " ~" + str(6 - i) + " minecraft:acacia_planks"
            type_to_console(output)

        #  This Clones the house into many many houses
        if CLONE:
            for i in range(1, 4):
                for j in range(0, 4):
                    output = "clone" + " ~" + str(0) + " ~" + str(-1) + " ~" + str(-8) + " ~" + str(11) + " ~" + str(
                        11) + " ~" + str(10) + " ~" + str(0 + (25 * j)) + " ~" + str(-1) + " ~" + str(
                        (-25 * i)) + " replace force"
                    type_to_console(output)


if __name__ == '__main__':
    build_house()
