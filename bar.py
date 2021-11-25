from libqtile import widget
from libqtile.bar import Bar
from libqtile.config import Screen

from colors import nord_fox, nord
from unicodes import left_arrow, right_arrow, lower_left_triangle

widget_defaults = dict(
    font='VictorMono Nerd Font Mono',
    fontsize=12,
    background=nord_fox['bg'],
    foreground=nord_fox['fg']
)

extension_defaults = widget_defaults.copy()



screens = [
    Screen(
        top=Bar(
             [
                # display groups
                # lower_left_triangle('bg', 'fg_gutter'),
                widget.GroupBox(
                    active=nord_fox['fg'],
                    inactive=nord_fox['fg_gutter'],
                    disable_drag=True,
                    borderwidth=0,
                    margin_x=0,
                    padding_x=10,
                    highlight_method='line',
                    block_highlight_text_color=nord_fox['red'],
                    highlight_color=nord_fox['bg']),

                lower_left_triangle(nord_fox['bg'], nord_fox['magenta']),
                widget.CurrentLayout(
                    foreground=nord_fox['bg'],
                    background=nord_fox['magenta'], 
                    fmt='[{}]',
                    padding=10),

                lower_left_triangle(nord_fox['magenta'], nord_fox['bg']),
                widget.WindowCount(
                    foreground=nord_fox['yellow'], 
                    padding=5,
                    fmt=' {}'),
                # right_arrow(nord_fox['bg'], nord_fox['black']),
                widget.WindowName(
                    foreground=nord_fox['white'],
                    padding=10),

                lower_left_triangle(nord['nord0'], nord['nord2']),
                widget.CheckUpdates(
                    distro='Arch',
                    background=nord['nord2'],
                    margin=30,
                    padding=10,
                    colour_have_updates=nord_fox['cyan'],
                    colour_no_updates=nord_fox['red'],
                    no_update_string='No updates',
                    display_format='累 {updates} updates'),

                lower_left_triangle(nord['nord2'], nord['nord3']),
                widget.Memory(
                    foreground=nord_fox['white'],
                    background=nord['nord3'],
                    padding=10,
                    measure_mem='G',
                    format=' {MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}'),

                lower_left_triangle(nord['nord3'], nord['nord4']),
                widget.CPU(
                    foreground=nord['nord0'],
                    background=nord['nord4'],
                    padding=10,
                    format=' {freq_current}GHz {load_percent}%'),

                lower_left_triangle(nord['nord4'], nord['nord5']),
                widget.Wlan(
                    foreground=nord['nord0'],
                    background=nord['nord5'],
                    padding=10,
                    format='直 {essid} {percent:2.0%}',
                    interface='wlp2s0'),

                lower_left_triangle(nord['nord5'], nord['nord6']),
                widget.Net(
                    foreground=nord['nord0'],
                    background=nord['nord6'],
                    interface='wlp2s0',
                    format='{down} ↓↑ {up}'),

                lower_left_triangle(nord['nord6'], nord['nord7']),
                widget.Clock(
                    foreground=nord['nord0'],
                    background=nord['nord7'],
                    format=' %Y-%m-%d %a %I:%M %p',
                    padding=10),

                lower_left_triangle(nord['nord7'], nord_fox['black']),
                widget.Systray(
                    background=nord_fox['black'],
                    padding=10),

                widget.Spacer(length=20, background=nord_fox['black'])
            ],
            size=24,
            background=nord_fox['bg']
        ),
    ),
]
