import splash
import curses
import sys

def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        print("Usage: zeropda [args]\n\nArguments:\n--splash / -s: show splash screen\n--help / -h: show this message")
    elif "--splash" in sys.argv or "-s" in sys.argv:
        splash.run()

def home():
    return


if __name__ == "__main__":
    main()