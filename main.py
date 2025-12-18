import splash
import home
import calendar
import tasks
import events
import shortcuts
import power
import settings

import curses
import sys
import getpass
import time
import datetime

def start():
    curses.initscr()
    curses.curs_set(0)
    if "--help" in sys.argv or "-h" in sys.argv:
        print("Usage: zeropda [args]\n\nArguments:\n--splash / -s: show splash screen\n--help / -h: show this message")
    elif "--splash" in sys.argv or "-s" in sys.argv:
        splash.run()
    curses.wrapper(main)

def main(stdscr):
    h, w = stdscr.getmaxyx()
    curses.start_color()
    curses.use_default_colors()

    top_margin = 1
    bottom_margin = 1
    
    left_w = w // 4
    
    items = ["Home", "Calendar", "Tasks", "Events", "Shortcuts", "Settings", "Power"]
    views = {
        "Home": home,
        "Calendar": calendar,
        "Tasks": tasks,
        "Events": events,
        "Shortcuts": shortcuts,
        "Settings": settings,
        "Power": power
    }

    focused = 0 # 0 = left, 1 = right
    
    left_pane = curses.newwin(h - top_margin - bottom_margin, left_w, 0 + top_margin, 0)
    right_pane = curses.newwin(h - top_margin - bottom_margin, w - left_w, 0 + top_margin, left_w)
    
    selected = 0

    while True:
        view_name = items[selected]
        draw_topbar(stdscr)
        draw_bottombar(stdscr)
        draw_left(left_pane, items, selected, focused)
        draw_right(right_pane, views, view_name, focused)

        key = stdscr.getch()
        if key == curses.KEY_UP and selected > 0 and focused == 0:
            selected -= 1
        elif key == curses.KEY_DOWN and selected < len(items) - 1 and focused == 0:
            selected += 1

        if key == 9 and focused != 1:
            focused = 1
        elif key == 9 and focused != 0:
            focused = 0
        
        

        
def draw_topbar(stdscr):
    date = datetime.datetime.now()
    topbar = "| ZeroPDA | Current user: " + getpass.getuser() + " | Date: " + date.strftime("%A %d %B %Y") + " | Time: " + date.strftime("%H:%M") + " |" 
    stdscr.addstr(0, 0, topbar,)
    stdscr.refresh()

def draw_bottombar(stdscr):
    h, w = stdscr.getmaxyx()
    bottombar = "| Tab: Switch Panes | Left, Up, Down, Right/HJKL: Navigation | Enter: Select |"
    stdscr.addstr(h - 1, 0, bottombar)

def draw_left(win, items, selected, focused):
    win.clear()
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    if focused == 0:
        win.attron(curses.color_pair(1))
        win.box()
        win.attroff(curses.color_pair(1))
    else:
        win.attron(curses.color_pair(2))
        win.box()
        win.attroff(curses.color_pair(2))

    win.addstr(0, 2, " Main Menu ")
    
    for i, item in enumerate(items):
        attr = curses.A_REVERSE if i == selected else 0
        win.addstr(1 + i, 2, item, attr)
    win.refresh()

def draw_right(win, views, view_name, focused):
    win.clear()
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

    if focused == 1:
        win.attron(curses.color_pair(1))
        win.box()
        win.attroff(curses.color_pair(1))
    else:
        win.attron(curses.color_pair(2))
        win.box()
        win.attroff(curses.color_pair(2))

    win.addstr(0, 2, " " + view_name + " ")
    views[view_name].draw(win, focused)

if __name__ == "__main__":
    start()