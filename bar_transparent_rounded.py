from libqtile.bar import Bar

from libqtile.widget.groupbox import GroupBox
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.window_count import WindowCount
from libqtile.widget.windowname import WindowName
from libqtile.widget.cpu import CPU
from libqtile.widget.memory import Memory
from libqtile.widget.net import Net
from libqtile.widget.systray import Systray
from libqtile.widget.clock import Clock
from libqtile.widget.spacer import Spacer

from colors import gruvbox
from unicodes import left_half_circle, right_half_circle

bar = Bar([
    left_half_circle(gruvbox['blue']),
    CurrentLayout(
        background=gruvbox['blue'],
    ),
    right_half_circle(gruvbox['blue']),

    Spacer(length=10),

    left_half_circle(gruvbox['magenta']),
    WindowCount(
        text_format='缾 {num}',
        background=gruvbox['magenta'],
        show_zero=True
    ),
    right_half_circle(gruvbox['magenta']),

    Spacer(length=10),

    left_half_circle(gruvbox['cyan']),
    Clock(
        background=gruvbox['cyan'],
        format=' %Y-%m-%d %a %I:%M %p'),
    right_half_circle(gruvbox['cyan']),

    Spacer(length=10),

    # Prompt(foreground=gruvbox['fg']),

    WindowName(foreground=gruvbox['fg']),

    left_half_circle(gruvbox['bg']),
    GroupBox(
        disable_drag=True,
        active=gruvbox['gray'],
        inactive=gruvbox['dark-gray'],
        highlight_method='line',
        block_highlight_text_color=gruvbox['magenta'],
        borderwidth=0,
        highlight_color=gruvbox['bg'],
        background=gruvbox['bg']
    ),
    right_half_circle(gruvbox['bg']),

    Spacer(length=100),

    Systray(
        padding=15,
        # background='#00000000'
    ),

    Spacer(length=10),

    left_half_circle(gruvbox['dark-cyan']),
    CPU(
        format=' {freq_current}GHz {load_percent}%',
        background=gruvbox['dark-cyan']),
    right_half_circle(gruvbox['dark-cyan']),

    Spacer(length=10),

    left_half_circle(gruvbox['dark-magenta']),
    Memory(
        format=' {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
        background=gruvbox['dark-magenta']),
    right_half_circle(gruvbox['dark-magenta']),

    Spacer(length=10),

    left_half_circle(gruvbox['dark-blue']),
    Net(
        background=gruvbox['dark-blue']
    ),
    right_half_circle(gruvbox['dark-blue'])
],
    margin=[10, 10, 5, 10],
    background='#00000000',
    opacity=1,
    size=25,
)
