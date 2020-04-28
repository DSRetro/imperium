from imperium.errors import ArgumentError
from imperium.commands import getCommands
import imperium.version as version
import argparse, datetime, platform, sys, os

def main():
    parser = argparse.ArgumentParser(description='Imperium Interpreter')
    parser.add_argument('-f', '--file', action='store', dest='filepath', help='Path of .imp or .impc file to perform action on.')
    parser.add_argument('-e', '--exec', action="store_true", help='Execute the file specified.', default=False)
    parser.add_argument('-c', '--comp', action="store_true", help='Compile .imp file to .impc.', default=False)
    args = parser.parse_args()

    if (args.exec and args.comp):
        raise ArgumentError("Too many arguments provided")
        return
    if (args.exec and not args.filepath):
        raise ArgumentError("No file to execute provided")
        return
    if (args.comp and not args.filepath):
        raise ArgumentError("No file to compile provided")
        return
    if (args.exec and args.filepath):
        execute()
        return
    if (args.comp and args.filepath):
        compil()
        return
    if not (args.exec and args.comp and args.filepath):
        run_console()
        return

def now():
    return str(datetime.datetime.now()).split('.')[0]

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    if platform.system() == 'Darwin':
        os.system('clear')
    if platform.system() == 'Linux':
        os.system('clear')
    dstring = ('ImperiumConsole v{} ({}) [{} | {}]'.format(version.getVersion(), now(), str(sys.platform).capitalize(), platform.machine()))
    div = '~' * len(dstring)
    print(dstring + '\n' + div)

def run_console():
    clear()
    while True:
        command = input('>> ')
        if(command == 'help'):
            print(getCommands())
        if(command == 'clear'):
            clear()
        if(command == 'exit'):
            exit()
            

def execute():
    pass

def compil():
    pass

if __name__ == "__main__":
    main()
