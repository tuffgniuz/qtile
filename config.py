import os
import subprocess

from typing import List

from libqtile import hook
from libqtile.extension.dmenu import DmenuRun
from libqtile.extension.window_list import WindowList
from libqtile.layout.columns import Columns
from libqtile.layout.xmonad import MonadTall
from libqtile.layout.stack import Stack
from libqtile.layout.floating import Floating
from libqtile.config import Click, Drag, DropDown, Group, Key, Match, ScratchPad, Screen
from libqtile.lazy import lazy

from colors import nord_fox

from bar1 import bar

mod = "mod4"
terminal = "kitty"

#  _  _________   ______ ___ _   _ ____  ____
# | |/ / ____\ \ / / __ )_ _| \ | |  _ \/ ___|
# | ' /|  _|  \ V /|  _ \| ||  \| | | | \___ \
# | . \| |___  | | | |_) | || |\  | |_| |___) |
# |_|\_\_____| |_| |____/___|_| \_|____/|____/

keys = [
    Key([mod, "control"], "1", lazy.to_screen(0)),
    Key([mod, "control"], "2", lazy.to_screen(1)),

    # Launch applications
    Key([mod], "w", lazy.spawn('brave'), desc="Launch browser"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    Key([mod], "p", lazy.spawn('rofi -show drun'), desc="Run rofi"),

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

#   ____ ____   ___  _   _ ____  ____
#  / ___|  _ \ / _ \| | | |  _ \/ ___|
# | |  _| |_) | | | | | | | |_) \___ \
# | |_| |  _ <| |_| | |_| |  __/ ___) |
#  \____|_| \_\\___/ \___/|_|   |____/

groups = [
    Group('1', label="一", matches=[
          Match(wm_class='firefox'), Match(wm_class='thunderbird'), Match(wm_class='qutebrowser')], layout="stack"),
    Group('2', label="二", layout="monadtall"),
    Group('3', label="三", layout="columns"),
    Group('4', label="四", matches=[
          Match(wm_class='discord'), Match(wm_class='zoom'), Match(wm_class="teams"), Match(wm_class="whatsdesk")], layout="stack"),
    Group('5', label="五", matches=[
          Match(wm_class="youtube music")], layout="stack"),
    # Group('6', label="六", layout="monadtall"),
    # Group('7', label="七", layout="monadtall"),
    # Group('8', label="八", layout="monadtall"),
    # Group('9', label="九", layout="monadtall"),
]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            desc="move focused window to group {}".format(i.name)),
    ])

#  ____   ____ ____      _  _____ ____ _   _ ____   _    ____  ____
# / ___| / ___|  _ \    / \|_   _/ ___| | | |  _ \ / \  |  _ \/ ___|
# \___ \| |   | |_) |  / _ \ | || |   | |_| | |_) / _ \ | | | \___ \
#  ___) | |___|  _ <  / ___ \| || |___|  _  |  __/ ___ \| |_| |___) |
# |____/ \____|_| \_\/_/   \_\_| \____|_| |_|_| /_/   \_\____/|____/

groups.append(ScratchPad('scratchpad', [
    DropDown('term', 'kitty', width=0.4, height=0.5, x=0.3, y=0.1, opacity=1),
    DropDown('mixer', 'pavucontrol', width=0.4,
             height=0.6, x=0.3, y=0.1, opacity=1),
    DropDown('blueman', 'blueman-manager', width=0.05,
             height=0.6, x=0.35, y=0.1, opacity=1),
]))

keys.extend([
    Key(["control"], "1", lazy.group['scratchpad'].dropdown_toggle('term')),
    Key(["control"], "2", lazy.group['scratchpad'].dropdown_toggle('mixer')),
    Key(["control"], "3", lazy.group['scratchpad'].dropdown_toggle('blueman')),
])

#  _        _ __   _____  _   _ _____ ____
# | |      / \\ \ / / _ \| | | |_   _/ ___|
# | |     / _ \\ V / | | | | | | | | \___ \
# | |___ / ___ \| || |_| | |_| | | |  ___) |
# |_____/_/   \_\_| \___/ \___/  |_| |____/

layouts = [
    Stack(
        border_normal=nord_fox['black'],
        border_focus=nord_fox['cyan'],
        border_width=2,
        num_stacks=1,
        margin=10,
    ),
    MonadTall(
        border_normal=nord_fox['black'],
        border_focus=nord_fox['cyan'],
        margin=10,
        border_width=2,
        single_border_width=2,
        single_margin=10,
    ),
    Columns(
        border_normal=nord_fox['black'],
        border_focus=nord_fox['cyan'],
        border_width=2,
        border_normal_stack=nord_fox['black'],
        border_focus_stack=nord_fox['cyan'],
        border_on_single=2,
        margin=10,
        margin_on_single=10,
    )
]

floating_layout = Floating(
    border_normal=nord_fox['bg'],
    border_focus=nord_fox['cyan'],
    border_width=2,
    float_rules=[
        *Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry

        # Match(wm_class="protonvpn"),
        Match(title="AICOMS"),
        Match(wm_class="blueman-manager"),
        Match(wm_class="pavucontrol"),
        Match(wm_class="zoom "),
        Match(wm_class="bitwarden"),
        Match(wm_class="nemo"),
        Match(wm_class="xarchiver"),
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
    bacgkround=nord_fox['bg'],
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(top=bar)
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = ''
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"


@ hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])
