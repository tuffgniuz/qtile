import os

import subprocess
from typing import List
from libqtile.config import ScratchPad, DropDown, Group, Match, Key
from libqtile import widget
from libqtile import hook, layout
from libqtile import extension
from libqtile.config import Click, Drag
from libqtile.lazy import lazy

from colors import seiun
from bar import widget_defaults, screens
from keys import browser, terminal, keys, mod

groups = [
    Group('1', label='一', matches=[Match(wm_class=[browser])]),
    Group('2', label='二', matches=[Match(wm_class=['gimp'])]),
    Group('3', label='三', matches=[Match(wm_class=['nemo'])]),
    Group('4', label='四', matches=[Match(wm_class=['zoom', 
                                                    'discord', 
                                                    'element-desktop', 
                                                    'slack'])], layout='max'),
    Group('5', label='五'),
    Group('6', label='六'),
    Group('7', label='七'),
    Group('8', label='八'),
    Group('9', label='九'),
]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),
        # mod1 + shift + letter of group = move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            desc="move focused window to group {}".format(i.name)),
    ])


layouts = [
    # layout.Columns(
    #     add_after_last=True,
    #     border_normal='#3c3836',
    #     border_focus=gruvbox['fg'],
    #     border_width=3,
    #     shift_windows=True,
    #     border_on_single=True,
    #     margin=8,
    # ),
    # ),
    # layout.Stack(num_stacks=5),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    layout.Tile(
        ratio=0.55,
        add_after_last=True,
        border_normal=seiun['dark-gray'],
        border_focus=seiun['blue'],
        border_width=3,
        shift_windows=True,
        border_on_single=True,
        margin=10,
    ),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
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
floating_layout = layout.Floating(
    float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class='blueman-manager'),
    Match(wm_class='nemo'),
    Match(wm_class='pavucontrol'),
    Match(wm_class='zoom'),

    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    ],
    border_focus=seiun['blue'],
    border_normal=seiun['dark-gray'],
    border_width=4)
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

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])
