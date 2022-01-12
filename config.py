from typing import List  # noqa: F401

from libqtile import bar, widget

from libqtile.layout.columns import Columns
from libqtile.layout.xmonad import MonadTall
from libqtile.layout.floating import Floating

from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from colors import gruvbox

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

    # Launch browser
    Key([mod], "w", lazy.spawn('firefox'), desc="Launch browser"),
    Key([mod], "d", lazy.spawn('discord'), desc="Launch discord"),
    Key([mod], "s", lazy.spawn('obs'), desc="Launch OBS"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    Key([mod], "f", lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen mode"),
    Key([mod, "shift"], "space", lazy.window.toggle_floating(),
        desc="Toggle fullscreen mode"),

    # Keybinding for MonadTall
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
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
]

# groups = [Group(i) for i in "123456789"]

groups = [
    Group('1', label="一", matches=[
          Match(wm_class='firefox')], layout="monadtall"),
    Group('2', label="二", layout="monadtall"),
    Group('3', label="三", layout="columns"),
    Group('4', label="四", layout="monadtall"),
    Group('5', label="五", matches=[Match(wm_class="obs")], layout="monadtall"),
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
        border_focus=gruvbox['dark-yellow'],
        border_normal_stack=gruvbox['dark-gray'],
        border_focus_stack=gruvbox['yellow'],
        border_width=4,
        border_on_single=2,
        margin=10,
        margin_on_single=0,
    ),
    MonadTall(
        border_normal=gruvbox['dark-gray'],
        border_focus=gruvbox['dark-yellow'],
        margin=10,
        border_width=4,
        single_border_width=2,
        single_margin=0,
    ),
]

floating_layout = Floating(
    border_normal=gruvbox['dark-gray'],
    border_focus=gruvbox['blue'],
    border_width=2,
    float_rules=[
        *Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry
        Match(wm_class="pavucontrol"),
    ])

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(),
                widget.CurrentLayout(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
                widget.Systray(),
                widget.QuickExit(),
            ],
            background=gruvbox['bg'],
            size=24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
