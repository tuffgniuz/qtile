from libqtile.bar import Bar
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
from colors import gruvbox

bar = Bar([
    GroupBox(
        disable_drag=True,
        active=gruvbox['gray'],
        inactive=gruvbox['dark-gray'],
        highlight_method='line',
        block_highlight_text_color=gruvbox['cyan'],
        borderwidth=0,
        highlight_color=gruvbox['bg'],
        background=gruvbox['bg']
    ),
    right_arrow(gruvbox['fg0'], gruvbox['bg']),
    CurrentLayout(
        background=gruvbox['fg0'],
        foreground=gruvbox['fg9']
    ),
    right_arrow(gruvbox['bg0'], gruvbox['fg0']),

    WindowCount(
        text_format='缾 {num}',
        background=gruvbox['bg0'],
        foreground=gruvbox['fg9'],
        show_zero=True,
    ),

    right_arrow(gruvbox['bg'], gruvbox['bg0']),
    WindowName(foreground=gruvbox['fg']),

    left_arrow(gruvbox['bg'], gruvbox['fg1']),
    CPU(
        format=' {freq_current}GHz {load_percent}%',
        background=gruvbox['fg1'],
        foreground=gruvbox['dark-green']
    ),

    left_arrow(gruvbox['fg1'], gruvbox['fg2']),
    Memory(
        format=' {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
        background=gruvbox['fg2'],
        foreground=gruvbox['yellow']
    ),

    left_arrow(gruvbox['fg2'], gruvbox['fg3']),
    Net(
        background=gruvbox['fg3'],
        foreground=gruvbox['dark-blue']
    ),

    left_arrow(gruvbox['fg3'], gruvbox['bg0']),
    Clock(
        background=gruvbox['bg0'],
        foreground=gruvbox['dark-magenta'],
        format=' %Y-%m-%d %a %I:%M %p'
    ),

    left_arrow(gruvbox['bg0'], gruvbox['fg0']),
    Systray(
        background=gruvbox['fg0']
    ),

    Spacer(length=20, background=gruvbox['fg0'])
], background=gruvbox['bg'], size=26, margin=9)
