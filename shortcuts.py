import curses
import getpass

def draw(win, focused):

    h, w = win.getmaxyx()

    win.addstr(1, 2, "Shortcuts")
    
    win.refresh()
