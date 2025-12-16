import splash
import curses
import sys
import time

def main():
    curses.initscr()
    curses.curs_set(0)
    if "--help" in sys.argv or "-h" in sys.argv:
        print("Usage: zeropda [args]\n\nArguments:\n--splash / -s: show splash screen\n--help / -h: show this message")
    elif "--splash" in sys.argv or "-s" in sys.argv:
        splash.run()
    curses.wrapper(home)

def home(stdscr):
    h, w = stdscr.getmaxyx()
    
    left_w = w // 4
    
    items = ["Home", "Calendar", "Tasks", "Events", "Shortcuts", "Power"]
    views = []
    
    left_pane = curses.newwin(h, left_w, 0, 0)
    right_pane = curses.newwin(h, w - left_w, 0, left_w)
    
    selected = 0

    while True:
        draw_left(left_pane, items, selected)

        view_name = items[selected]

        key = stdscr.getch()
        if key == curses.KEY_UP and selected > 0:
            selected -= 1
        elif key == curses.KEY_DOWN and selected < len(items) - 1:
            selected += 1

def draw_left(win, items, selected):
    win.clear()
    win.box()
    for i, item in enumerate(items):
        attr = curses.A_REVERSE if i == selected else 0
        win.addstr(1 + i, 2, item, attr)
    win.refresh()


if __name__ == "__main__":
    main()