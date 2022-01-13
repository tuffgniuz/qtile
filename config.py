import os
import subprocess
from typing import List  # noqa: F401

from libqtile import hook

# import layout objects
from libqtile.layout.columns import Columns
from libqtile.layout.xmonad import MonadTall
from libqtile.layout.stack import Stack
from libqtile.layout.floating import Floating

# import widgets and bar
from libqtile.bar import Bar
from libqtile.widget.groupbox import GroupBox
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.window_count import WindowCount
from libqtile.widget.windowname import WindowName
from libqtile.widget.prompt import Prompt
from libqtile.widget.cpu import CPU
from libqtile.widget.memory import Memory
from libqtile.widget.net import Net
from libqtile.widget.systray import Systray
from libqtile.widget.clock import Clock
from libqtile.widget.spacer import Spacer

from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from colors import gruvbox
from unicodes import left_half_circle, right_half_circle


mod = "mod4"
terminal = guess_terminal()

keys = [
    # Launch applications
    Key([mod], "w", lazy.spawn('firefox'), desc="Launch browser"),
    Key([mod], "d", lazy.spawn('discord'), desc="Launch discord"),
    Key([mod], "s", lazy.spawn('obs'), desc="Launch OBS"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Command prompt
    Key([mod], "p", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    # Toggle floating and fullscreen
    Key([mod], "f", lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen mode"),
    Key([mod, "shift"], "space", lazy.window.toggle_floating(),
        desc="Toggle fullscreen mode"),

    # Keybindings for resizing windows in MonadTall layout
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "o", lazy.layout.maximize()),
    Key([mod, "control"], "space", lazy.layout.flip()),

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]

groups = [
    Group('1', label="一", matches=[
          Match(wm_class='firefox')], layout="stack"),
    Group('2', label="二", layout="monadtall"),
    Group('3', label="三", layout="columns"),
    Group('4', label="四", matches=[
          Match(wm_class='discord'), Match(wm_class='zoom')], layout="stack"),
    Group('5', label="五", matches=[Match(wm_class="obs")], layout="stack"),
    Group('6', label="六", layout="monadtall"),
    Group('7', label="七", layout="monadtall"),
    Group('8', label="八", layout="monadtall"),
    Group('9', label="九", layout="monadtall"),
]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # Or, use below if you prefer not to switch to that group.
        # mod1 + shift + letter of group = move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    Columns(
        border_normal=gruvbox['dark-gray'],
        border_focus=gruvbox['gray'],
        border_width=2,
        border_normal_stack=gruvbox['dark-gray'],
        border_focus_stack=gruvbox['dark-blue'],
        border_on_single=2,
        margin=10,
        margin_on_single=10,
    ),
    MonadTall(
        border_normal=gruvbox['dark-gray'],
        border_focus=gruvbox['gray'],
        margin=10,
        border_width=2,
        single_border_width=2,
        single_margin=10,
    ),
    Stack(
        border_normal=gruvbox['dark-gray'],
        border_focus=gruvbox['gray'],
        border_width=2,
        num_stacks=1,
        margin=10,
    )
]

floating_layout = Floating(
    border_normal=gruvbox['dark-gray'],
    border_focus=gruvbox['magenta'],
    border_width=4,
    float_rules=[
        *Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry
        Match(wm_class="pavucontrol"),
        Match(wm_class="zoom"),
    ])

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]
widget_defaults = dict(
    font='TerminessTTF Nerd Font',
    fontsize=13,
    padding=10,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=Bar(
            [

                left_half_circle(gruvbox['dark-blue']),
                CurrentLayout(
                    background=gruvbox['dark-blue'],
                ),
                right_half_circle(gruvbox['dark-blue']),

                Spacer(length=5),

                left_half_circle(gruvbox['dark-magenta']),
                WindowCount(
                    background=gruvbox['dark-magenta'],
                    show_zero=True
                ),
                right_half_circle(gruvbox['dark-magenta']),

                Spacer(length=5),

                left_half_circle(gruvbox['dark-cyan']),
                Clock(
                    background=gruvbox['dark-cyan'],
                    format='%Y-%m-%d %a %I:%M %p'),
                right_half_circle(gruvbox['dark-cyan']),

                Spacer(length=5),

                Prompt(),
                WindowName(),
                # Spacer(length=400),


                left_half_circle(gruvbox['bg']),
                GroupBox(
                    disable_drag=True,
                    active=gruvbox['gray'],
                    inactive=gruvbox['dark-gray'],
                    highlight_method='line',
                    block_highlight_text_color=gruvbox['red'],
                    borderwidth=0,
                    highlight_color=gruvbox['bg'],
                    background=gruvbox['bg']
                ),
                right_half_circle(gruvbox['bg']),

                Spacer(length=200),

                Systray(
                    padding=15,
                    background='#00000000'
                ),

                Spacer(length=10),

                left_half_circle(gruvbox['blue']),
                CPU(background=gruvbox['blue']),
                right_half_circle(gruvbox['blue']),

                Spacer(length=5),

                left_half_circle(gruvbox['magenta']),
                Memory(background=gruvbox['magenta']),
                right_half_circle(gruvbox['magenta']),

                Spacer(length=5),

                left_half_circle(gruvbox['cyan']),
                Net(background=gruvbox['cyan']),
                right_half_circle(gruvbox['cyan']),

            ],
            margin=[5, 10, 0, 10],
            background='#00000000',
            opacity=1,
            size=26,
        ),
    ),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = ''
cursor_warp = False
auto_fullscreen = False
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])
