from imperium.util import getFile

def getCommands():
    with open(getFile("commands.txt"), "r") as file:
        data = file.read()
    return data
