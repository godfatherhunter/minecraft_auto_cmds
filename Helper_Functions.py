"""
This is a file that contains wrapper functions for sending in commands to minecraft.

"""
import keyboard
import time


def type_to_console(command):
    """
    Types a command to the minecraft console using the keyboard library.

    :param command: string type that is the command that will be sent to the minecraft console
    :return: none
    """
    # This opens the console so the command can be typed to it.
    keyboard.press('/')
    time.sleep(0.05)
    keyboard.release('/')

    # Mocks te keyboard typing in the command
    output = command + '\n'  # Format the output so it has an enter at the end. This will allow the command to be ran.
    keyboard.write(output)
