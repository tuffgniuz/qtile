from libqtile import widget
from libqtile.bar import Bar
from libqtile.config import Screen

from colors import seiun
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
                    highlight_color=seiun['fg'],
                    block_highlight_text_color=seiun['bg'],
                    highlight_method='line'),

                right_arrow(seiun['dark-gray'], seiun['bg']),
                # display the current wm layout
                widget.CurrentLayout(
                    background=seiun['dark-gray'],
                    fmt='[{}]',
                    padding=10),

                right_arrow(seiun['gray'], seiun['dark-gray']),
                widget.WindowCount(
                    background=seiun['gray'],
                    foreground=seiun['bg'],
                    padding=5,
                    fmt=' {}'),
                right_arrow(seiun['bg'], seiun['gray']),
                widget.WindowName(
                    padding=10),

                left_arrow(seiun['bg'], seiun['gray1']),
                # display total available updates
                widget.CheckUpdates(
                    distro='Arch',
                    margin=30,
                    padding=10,
                    colour_have_updates=seiun['cyan'],
                    colour_no_updates=seiun['fg'],
                    no_update_string='No updates',
                    display_format='累 {updates} updates',
                    background=seiun['gray1']),

                left_arrow(seiun['gray1'], seiun['gray2']),
                # display memory usage 
                widget.Memory(
                    background=seiun['gray2'],
                    foreground=seiun['bg'],
                    padding=10,
                    measure_mem='G',
                    format=' {MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}'),

                left_arrow(seiun['gray2'], seiun['gray3']),
                # display cpu usage
                widget.CPU(
                    background=seiun['gray3'],
                    foreground=seiun['bg'],
                    padding=10,
                    format=' {freq_current}GHz {load_percent}%'),

                left_arrow(seiun['gray3'], seiun['gray4']),
                # Display essid and connection strength
                widget.Wlan(
                    background=seiun['gray4'],
                    foreground=seiun['bg'],
                    padding=10,
                    format='直 {essid} {percent:2.0%}',
                    interface='wlp2s0'),

                left_arrow(seiun['gray4'], seiun['gray5']),
                widget.PulseVolume(
                    background=seiun['gray5'],
                    foreground=seiun['bg'],
                    fmt=' {}',
                    padding=10,
                    volume_app='pavucontrol'),

                left_arrow(seiun['gray5'], seiun['gray6']),
                widget.Clock(
                    format='%Y-%m-%d %a %I:%M %p',
                    background=seiun['gray6'],
                    foreground=seiun['bg'],
                    padding=10),

                left_arrow(seiun['gray6'], seiun['fg']),
                widget.Systray(
                    background=seiun['fg'],
                    padding=10),

                widget.Spacer(
                    length=10,
                    background=seiun['fg']
                ),

                left_arrow(seiun['fg'], seiun['red']),
                widget.QuickExit(
                    background=seiun['red'],
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
