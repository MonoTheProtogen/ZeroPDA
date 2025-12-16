import curses
import time
import getpass

logo = [                                            
    r" _______                      ______  _____   _______ ",
    r"|__     |.-----..----..-----.|   __ \|     \ |   _   |",
    r"|     __||  -__||   _||  _  ||    __/|  --  ||       |",
    r"|_______||_____||__|  |_____||___|   |_____/ |___|___|",                                                       
    "",
    "",
    " Welcome " + getpass.getuser() + "!",                                              
]

def splash(stdscr, duration=10):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.nodelay(True)
    curses.start_color()
    curses.use_default_colors()

    rows, cols = stdscr.getmaxyx()
    art_height = len(logo)
    art_width = max(len(line) for line in logo)
    start_y = (rows - art_height) // 2
    start_x = (cols - art_width) // 2

    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

    for i, line in enumerate(logo):
        if i > 4:
            stdscr.addstr(start_y + i, start_x, line, curses.color_pair(2))
        else:
            stdscr.addstr(start_y + i, start_x, line, curses.color_pair(1))

    bar_width = 20
    block_width = 5
    bar_y = start_y + art_height + 2
    bar_x = (cols - bar_width) // 2
    pos = 0

    start_time = time.time()

    bar_start = "╺"
    bar_mid = "╍"
    bar_end = "╸"

    message = "Loading..."
    message_y = bar_y + 2
    message_x = (cols - len(message)) // 2

    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    while time.time() - start_time < duration:
        stdscr.addstr(bar_y, bar_x, " " * bar_width, curses.color_pair(3))
        stdscr.addstr(bar_y, bar_x - 1, bar_start, curses.color_pair(3)) 
        stdscr.addstr(bar_y, bar_x + bar_width, bar_end, curses.color_pair(3)) 

        if(time.time() - start_time > 7):
            message = "All done! "
            stdscr.addstr(message_y, message_x, message, curses.color_pair(2))
        else:
            stdscr.addstr(message_y, message_x, message, curses.color_pair(1))

        

        for i in range(block_width):
            stdscr.addstr(bar_y, bar_x + (pos + i) % bar_width, bar_mid, curses.color_pair(3))

        stdscr.refresh()
        stdscr.border()
        pos = (pos + 1) % bar_width
        time.sleep(0.1)

    curses.curs_set(1)
    stdscr.clear()
    stdscr.refresh()

def run():
    curses.wrapper(splash)