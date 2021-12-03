import os

import subprocess
from typing import List
from libqtile.config import ScratchPad, DropDown, Group, Match, Key
from libqtile import widget
from libqtile import hook, layout
from libqtile import extension
from libqtile.config import Click, Drag
from libqtile.lazy import lazy

from colors import nord_fox
from bar import widget_defaults, screens
from keybindings import browser, terminal, keys, mod


groups = [
    Group('1', label='一', matches=[Match(wm_class=[browser])]),
    Group('2', label='二', matches=[Match(wm_class=['gimp'])]),
    Group('3', label='三', matches=[Match(wm_class=['DesktopEditors',
                                                    'nemo',
                                                    'Thunderbird'])]),
    Group('4', label='四', matches=[Match(wm_class=['zoom', 
                                                    'discord', 
                                                    'element-desktop', 
                                                    'slack'])], layout='max'),
    Group('5', label='五', matches=[Match(wm_class=['qbittorrent'])]),
    Group('6', label='六'),
    Group('7', label='七'),
    Group('8', label='八'),
    Group('9', label='九'),
]

for group in groups:
    keys.extend([
        Key([mod], group.name, lazy.group[group.name].toscreen(),
            desc=f"Switch to group {group.name}"),
        Key([mod, "shift"], group.name, lazy.window.togroup(group.name),
            desc=f"move focused window to group {group.name}"),
    ])

# append scratchpad to list of groups
groups.append(
    ScratchPad('scratchpad', [
        # nnn file manager
        DropDown("fm", 
                f"{terminal} nnn -d -C", 
                y=0.1,
                x=0.25,
                width=0.5,
                height=0.6,
                opacity=1,
                ),
        # ncmpcpp music player
        DropDown('ncmpcpp', 
                f'{terminal} ncmpcpp', 
                y=0.1,
                x=0.25,
                width=0.5,
                height=0.6,
                opacity=1),
        # term
        DropDown('term',
                f'{terminal}',
                y=0.1,
                x=0.25,
                width=0.5,
                height=0.6,
                opacity=1),
        DropDown('discord',
                 'discord',
                 y=0.1,
                 x=0.25,
                 opacity=1)
        ])
        )

layouts = [
    # layout.Columns()j
    # layout.Stack(num_stacks=5),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(
        margin=10,
        border_normal=nord_fox['black'],
        border_focus=nord_fox['fg_gutter'],
        border_width=2,
        single_border_width = 2
        ),
    # layout.MonadWide(),
    # # layout.RatioTile(),
    # layout.Tile() 
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
    Match(wm_class='thunar'),
    Match(wm_class='pavucontrol'),
    Match(wm_class='zoom'),
    Match(wm_class='Msgcompose'),

    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    ],
    border_focus=nord_fox['fg_gutter'],
    border_width=2)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])
