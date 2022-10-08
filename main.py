
import keyboard
import time

def openConsole():
    keyboard.press('/')
    time.sleep(0.05)
    keyboard.release('/')

def typeCommand():
    # Use a breakpoint in the code line below to debug your script.
    while(True):
        print('Waiting for & input')  # Press Ctrl+F8 to toggle the breakpoint.
        keyboard.wait('`')
        openConsole()
        keyboard.write("fill ~1 ~-1 ~-5 ~10 ~5 ~5 minecraft:stone hollow\n")
        openConsole()
        keyboard.write("fill ~1 ~0 ~0 ~1 ~1 ~0 air\n")
        #openConsole()
        #keyboard.write("setblock ~1 ~0 ~0 minecraft:acacia_door\n")
        #openConsole()
        #keyboard.write("setblock ~1 ~1 ~0 minecraft:acacia_door\n")


        #Add in flooring
        openConsole()
        keyboard.write("fill ~2 ~-1 ~-4 ~9 ~-1 ~4 minecraft:acacia_planks\n")

        # Front Windows
        openConsole()
        keyboard.write("fill ~1 ~1 ~2 ~1 ~3 ~4 minecraft:glass_pane\n")
        openConsole()
        keyboard.write("fill ~1 ~1 ~-2 ~1 ~3 ~-4 minecraft:glass_pane\n")
        # Back Windows
        openConsole()
        keyboard.write("fill ~10 ~1 ~2 ~10 ~3 ~4 minecraft:glass_pane\n")
        openConsole()
        keyboard.write("fill ~10 ~1 ~-2 ~10 ~3 ~-4 minecraft:glass_pane\n")
        #Right Window
        openConsole()
        keyboard.write("fill ~3 ~1 ~5 ~8 ~3 ~5 minecraft:glass_pane\n")
        openConsole()
        keyboard.write("fill ~3 ~1 ~-5 ~8 ~3 ~-5 minecraft:glass_pane\n")

        # Lights
        openConsole()
        keyboard.write("setblock ~2 ~3 ~-4 minecraft:torch\n")
        openConsole()
        keyboard.write("setblock ~9 ~3 ~-4 minecraft:torch\n")
        openConsole()
        keyboard.write("setblock ~2 ~3 ~4 minecraft:torch\n")
        openConsole()
        keyboard.write("setblock ~9 ~3 ~4 minecraft:torch\n")
        openConsole()
        keyboard.write("setblock ~0 ~2 ~1 minecraft:torch\n")
        openConsole()
        keyboard.write("setblock ~0 ~2 ~-1 minecraft:torch\n")

        # Roof
        for i in range(0, 5):
            openConsole()
            output = "fill" +  " ~" + str(0+i) + " ~" + str(5+i) + " ~" + str(-6+i) + " ~" + str(11-i) + " ~" + str(5+i) + " ~" + str(6-i) + " minecraft:acacia_planks\n"
            keyboard.write(output)
        for i in range(1, 15):
            for j in range(0, 15):
                openConsole()
                output = "clone" + " ~" + str(0) +  " ~" + str(-1) + " ~" + str(-8) + " ~" + str(11) + " ~" + str(11) + " ~" + str(10) + " ~" + str(0 + (25 * j)) + " ~" + str(-1) + " ~" + str((-25 * i)) + " replace force\n"
                keyboard.write(output)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    typeCommand()


