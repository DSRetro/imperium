import argparse

def main():
    parser = argparse.ArgumentParser(description='Imperium Interpreter')
    parser.add_argument('filepath', action='store', help='Path of .imp or .impc file to perform action on.')
    parser.add_argument('-e', '--exec', action="store_true", help='Execute the file specified.', default=False)
    parser.add_argument('-c', '--comp', action="store_true", help='Complile .imp file to .impc.', default=False)
    args = parser.parse_args()

if __name__ == "__main__":
    main()
