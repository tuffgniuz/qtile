from libqtile import extension
from libqtile.lazy import lazy
from libqtile.config import Key

from colors import seiun

mod = 'mod4'
browser = 'firefox'
terminal = 'kitty'

keys = [
    # Switch between windows
    Key([mod], "h", 
        lazy.layout.left(), 
        desc="Move focus to left"),
    Key([mod], "l", 
        lazy.layout.right(), 
        desc="Move focus to right"),
    Key([mod], "j", 
        lazy.layout.down(), 
        desc="Move focus down"),
    Key([mod], "k", 
        lazy.layout.up(), 
        desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", 
        lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", 
        lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", 
        lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", 
        lazy.layout.shuffle_up(), 
        desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", 
        lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", 
        lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", 
        lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", 
        lazy.layout.grow_up(), 
        desc="Grow window up"),
    Key([mod], "n", 
        lazy.layout.normalize(), 
        desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    # toggle floating mode
    Key([mod, 'shift'], 'space',
        lazy.window.toggle_floating()),
    
    # Toggle between different layouts as defined below
    Key([mod], "Tab", 
        lazy.next_layout(), 
        desc="Toggle between layouts"),
    Key([mod, "shift"], "c", 
        lazy.window.kill(), 
        desc="Kill focused window"),

    Key([mod, "shift"], "r", 
        lazy.restart(), 
        desc="Restart Qtile"),
    # Key([mod, "control"], "q", 
    #     lazy.shutdown(), 
    #     desc="Shutdown Qtile"),

    # Spawn apps
   Key([mod], "p", 
        lazy.run_extension(extension.DmenuRun(
            dmenu_prompt='',
            dmenu_font='Terminus',
            dmenu_height=22,
            dmenu_lines=15,
            background=seiun['bg'],
            foreground=seiun['dark-gray'],
            selected_background=seiun['dark-gray'],
            selected_foreground=seiun['fg'],
        )),
        desc="Spawn a command using a prompt widget"),
    Key([mod], "Return", 
        lazy.spawn(terminal), 
        desc="Launch terminal"),
    Key([mod], "w",
        lazy.spawn(browser),
        desc="Launch browser"),
    Key([mod], 'd',
        lazy.spawn('discord'),
        desc='Launch discord client'),
    Key([mod], "z",
        lazy.spawn('zoom'),
        desc="Launch zoom"),
    Key([mod], "e",
        lazy.spawn(terminal + ' -e nnn -d -C')),
    Key([mod, 'shift'], 'm',
        lazy.spawn(terminal + ' -e neomutt'),
        desc='Launches neomut in terminal'),
    Key([mod], 'v',
        lazy.spawn(terminal + ' -e vtop'),
        desc="Launch vtop"),
    Key([mod], 't',
        lazy.spawn(terminal + ' -e rtorrent'))
]

