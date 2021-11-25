from libqtile import extension
from libqtile.lazy import lazy
from libqtile.config import Key

from colors import nord_fox

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

    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "o", lazy.layout.maximize()),

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
            background=nord_fox['bg'],
            foreground=nord_fox['fg'],
            selected_background=nord_fox['fg_gutter'],
            selected_foreground=nord_fox['fg'],
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
        lazy.spawn(f'{terminal} nnn -d -C')),
    Key([mod], 'v',
        lazy.spawn(f'{terminal} vtop'),
        desc="Launch vtop"),
    
    # toggle scratchpad dropdowns
    Key([], "F1", lazy.group['scratchpad'].dropdown_toggle('fm')),
    Key([], "F2", lazy.group['scratchpad'].dropdown_toggle('ncmpcpp')),
    Key([], "F3", lazy.group['scratchpad'].dropdown_toggle('term')),
]

