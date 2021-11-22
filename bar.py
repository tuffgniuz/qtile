from libqtile import widget
from libqtile.bar import Bar
from libqtile.config import Screen

from colors import gruvbox
from unicodes import left_arrow, lower_left_triangle, right_arrow

widget_defaults = dict(
    font='VictorMono Nerd Font Mono',
    fontsize=12,
    background=gruvbox['bg'],
    foreground=gruvbox['fg']
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=Bar(
             [
                # widget.TextBox(
                #     text='', # arch logo
                #     fontsize=22,
                #     padding=10,
                #     background=gruvbox['dark-red'],
                #     foreground=gruvbox['fg']),
                #  # right_arrow(gruvbox['bg'], gruvbox['dark-red']),
                #  lower_left_triangle(gruvbox['dark-red'], gruvbox['bg']),

                # display groups
                widget.GroupBox(
                    active=gruvbox['fg'],
                    inactive=gruvbox['dark-gray'],
                    disable_drag=True,
                    borderwidth=0,
                    margin_x=0,
                    padding_x=10,
                    highlight_method='line',
                    block_highlight_text_color=gruvbox['red'],
                    highlight_color=gruvbox['bg']),

                right_arrow(gruvbox['dark-yellow'], gruvbox['bg']),
                # display the current wm layout
                widget.CurrentLayout(
                    background=gruvbox['dark-yellow'],
                    fmt='[{}]',
                    padding=10),

                right_arrow(gruvbox['yellow'], gruvbox['dark-yellow']),
                widget.WindowCount(
                    background=gruvbox['yellow'],
                    padding=5,
                    fmt=' {}'),
                right_arrow(gruvbox['bg'], gruvbox['yellow']),
                widget.WindowName(
                    foreground=gruvbox['cyan'],
                    padding=10),

                 # left_arrow(gruvbox['bg'], gruvbox['red']),
                # widget.Pomodoro(
                 #    background=gruvbox['red'],
                 #    color_active=gruvbox['fg'],
                 #    color_inactive=gruvbox['fg'],
                 #    color_break=gruvbox['fg'],
                 #    prefix_active=' ',
                 #    prefix_inactive=' pomodoro',
                 #    padding=10),
                left_arrow(gruvbox['bg'], gruvbox['fg0']),
                # display total available updates
                widget.CheckUpdates(
                    distro='Arch',
                    margin=30,
                    padding=10,
                    colour_have_updates=gruvbox['fg'],
                    colour_no_updates=gruvbox['bg'],
                    no_update_string='No updates',
                    display_format='累 {updates} updates',
                    background=gruvbox['fg0']),

                left_arrow(gruvbox['fg0'], gruvbox['bg0']),
                # display memory usage 
                widget.Memory(
                    background=gruvbox['bg0'],
                    padding=10,
                    measure_mem='G',
                    format=' {MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}'),

                left_arrow(gruvbox['bg0'], gruvbox['fg1']),
                # display cpu usage
                widget.CPU(
                    background=gruvbox['fg1'],
                    padding=10,
                    format=' {freq_current}GHz {load_percent}%'),

                left_arrow(gruvbox['fg1'], gruvbox['fg2']),
                # Display essid and connection strength
                widget.Wlan(
                    background=gruvbox['fg2'],
                    padding=10,
                    format='直 {essid} {percent:2.0%}',
                    interface='wlp2s0'),

                left_arrow(gruvbox['fg2'], gruvbox['fg3']),
                widget.Net(
                    background=gruvbox['fg3'],
                    interface='wlp2s0',
                    format='{down} ↓↑ {up}',
                ),

                left_arrow(gruvbox['fg3'], gruvbox['fg4']),
                widget.Clock(
                    format=' %Y-%m-%d %a %I:%M %p',
                    background=gruvbox['fg4'],
                    padding=10),

                left_arrow(gruvbox['fg4'], gruvbox['fg9']),
                widget.Systray(
                    background=gruvbox['fg9'],
                    padding=10),

                widget.Spacer(
                    length=10,
                    background=gruvbox['fg9']
                ),

                left_arrow(gruvbox['fg9'], gruvbox['cyan']),
                widget.QuickExit(
                    background=gruvbox['cyan'],
                    foreground=gruvbox['bg'],
                    default_text='',
                    fontsize=17,
                )
            ],
            size=24,
            margin=10,
            background=gruvbox['bg']
        ),
    ),
]
