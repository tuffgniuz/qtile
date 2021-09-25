from libqtile import widget
from libqtile.bar import Bar
from libqtile.config import Screen

from colors import seiun, red_gray_gradient
from unicodes import left_arrow, right_arrow

widget_defaults = dict(
    font='Terminus',
    fontsize=12,
    background=seiun['bg'],
    foreground=seiun['fg']
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=Bar(
             [
                widget.TextBox(
                    text='', # arch logo
                    fontsize=22,
                    padding=10,
                    foreground=seiun['dark-blue']),
                # display groups
                widget.GroupBox(
                    active=seiun['fg'],
                    inactive=seiun['dark-gray'],
                    disable_drag=True,
                    borderwidth=0,
                    margin_x=0,
                    padding_x=10,
                    highlight_method='line',
                    block_highlight_text_color=seiun['red'],
                    highlight_color=seiun['bg']),

                right_arrow(seiun['dark-yellow'], seiun['bg']),
                # display the current wm layout
                widget.CurrentLayout(
                    background=seiun['dark-yellow'],
                    fmt='[{}]',
                    padding=10),

                right_arrow(seiun['yellow'], seiun['dark-yellow']),
                widget.WindowCount(
                    background=seiun['yellow'],
                    padding=5,
                    fmt=' {}'),
                right_arrow(seiun['bg'], seiun['yellow']),
                widget.WindowName(
                    foreground=seiun['cyan'],
                    padding=10),

                left_arrow(seiun['bg'], seiun['dark-blue']),
                # display total available updates
                widget.CheckUpdates(
                    distro='Arch',
                    margin=30,
                    padding=10,
                    colour_have_updates=seiun['cyan'],
                    colour_no_updates=seiun['fg'],
                    no_update_string='No updates',
                    display_format='累 {updates} updates',
                    background=seiun['dark-blue']),

                left_arrow(seiun['dark-blue'], seiun['blue']),
                # display memory usage 
                widget.Memory(
                    background=seiun['blue'],
                    padding=10,
                    measure_mem='G',
                    format=' {MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}'),

                left_arrow(seiun['blue'], seiun['dark-magenta']),
                # display cpu usage
                widget.CPU(
                    background=seiun['dark-magenta'],
                    padding=10,
                    format=' {freq_current}GHz {load_percent}%'),

                left_arrow(seiun['dark-magenta'], seiun['magenta']),
                # Display essid and connection strength
                widget.Wlan(
                    background=seiun['magenta'],
                    padding=10,
                    format='直 {essid} {percent:2.0%}',
                    interface='wlp2s0'),

                left_arrow(seiun['magenta'], seiun['dark-cyan']),
                widget.PulseVolume(
                    background=seiun['dark-cyan'],
                    fmt=' {}',
                    padding=10,
                    volume_app='pavucontrol'),

                left_arrow(seiun['dark-cyan'], seiun['cyan']),
                widget.Clock(
                    format='%Y-%m-%d %a %I:%M %p',
                    background=seiun['cyan'],
                    padding=10),

                left_arrow(seiun['cyan'], seiun['fg']),
                widget.Systray(
                    background=seiun['fg'],
                    padding=10),

                widget.Spacer(
                    length=10,
                    background=seiun['fg']
                ),

                left_arrow(seiun['fg'], seiun['green']),
                widget.QuickExit(
                    background=seiun['green'],
                    foreground=seiun['bg'],
                    default_text='',
                    fontsize=17,
                )
            ],
            size=24,
            margin=10,
            background=seiun['bg']
        ),
    ),
]
