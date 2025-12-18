import curses
import getpass

def draw(win, focused):

    win.addstr(1, 2, "Tasks")
    
    win.refresh()
