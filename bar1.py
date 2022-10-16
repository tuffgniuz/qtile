from libqtile.bar import Bar
from libqtile.widget.battery import Battery
from libqtile.widget.clock import Clock
from libqtile.widget.cpu import CPU
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.groupbox import GroupBox
from libqtile.widget.memory import Memory
from libqtile.widget.net import Net
from libqtile.widget.spacer import Spacer
from libqtile.widget.systray import Systray
from libqtile.widget.window_count import WindowCount
from libqtile.widget.windowname import WindowName

from unicodes import right_arrow, left_arrow
from colors import nord_fox

bar = Bar([
    GroupBox(
        disable_drag=True,
        active=nord_fox['blue'],
        inactive=nord_fox['black'],
        highlight_method='line',
        block_highlight_text_color=nord_fox['magenta'],
        borderwidth=0,
        highlight_color=nord_fox['bg'],
        background=nord_fox['bg']
    ),
    right_arrow(nord_fox['blue'], nord_fox['bg']),
    CurrentLayout(
        background=nord_fox['blue'],
        foreground=nord_fox['white']
    ),
    right_arrow(nord_fox['magenta'], nord_fox['blue']),

    WindowCount(
        text_format='缾 {num}',
        background=nord_fox['magenta'],
        foreground=nord_fox['white'],
        show_zero=True,
    ),

    right_arrow(nord_fox['bg'], nord_fox['magenta']),
    WindowName(
        background=nord_fox['bg'],
        foreground=nord_fox['fg']
    ),

    left_arrow(nord_fox['bg'], nord_fox['blue']),
    CPU(
        format=' {freq_current}GHz {load_percent}%',
        background=nord_fox['blue'],
        foreground=nord_fox['white']
    ),

    left_arrow(nord_fox['blue'], nord_fox['magenta']),
    Memory(
        format=' {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
        background=nord_fox['magenta'],
        foreground=nord_fox['white']
    ),

    # # left_arrow(gruvbox['fg2'], gruvbox['fg3']),
    # # # Net(
    # # #     background=gruvbox['fg3'],
    # # #     foreground=gruvbox['dark-blue']
    # # # ),
    # # Battery(
    # #     background=gruvbox['fg3'],
    # #     format='{char} {percent:2.0%} {hour:d}:{min:02d}'
    # # ),

    left_arrow(nord_fox['magenta'], nord_fox['cyan']),
    Clock(
        background=nord_fox['cyan'],
        foreground=nord_fox['white'],
        format=' %Y-%m-%d %a %I:%M %p'
    ),

    left_arrow(nord_fox['cyan'], nord_fox['white']),
    Systray(
        background=nord_fox['white']
    ),

    Spacer(length=20, background=nord_fox['white'])
],
    # background=nord_fox['bg'],
    size=26,
    margin=8
)
