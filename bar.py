from libqtile import widget
from libqtile.bar import Bar
from libqtile.config import Screen

from colors import nord_fox, nord
from unicodes import lower_left_triangle

widget_defaults = dict(
    font="TerminessTTF Nerd Font Mono",
    fontsize=13,
    background=nord_fox["bg"],
    foreground=nord_fox["fg"],
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=Bar(
            [
                # display groups
                # lower_left_triangle('bg', 'fg_gutter'),
                widget.GroupBox(
                    active=nord_fox["fg"],
                    inactive=nord_fox["fg_gutter"],
                    disable_drag=True,
                    borderwidth=0,
                    margin_x=0,
                    padding_x=10,
                    highlight_method="line",
                    block_highlight_text_color=nord_fox["red"],
                    highlight_color=nord_fox["bg"],
                ),
                lower_left_triangle(nord_fox["bg"], nord_fox["blue"]),
                widget.CurrentLayout(
                    foreground=nord_fox["white"],
                    background=nord_fox["blue"],
                    fmt="[{}]",
                    padding=10,
                ),
                lower_left_triangle(nord_fox["blue"], nord_fox["bg"]),
                widget.WindowCount(
                    foreground=nord_fox["yellow"], padding=5, fmt=" {}"
                ),
                widget.WindowName(foreground=nord_fox["white"], padding=10),

                lower_left_triangle(nord_fox['bg'], nord_fox['black']),
                widget.DF(
                    format=" {p} {uf}",
                    visible_on_warn=False,
                    foreground=nord_fox["magenta"],
                    background=nord_fox['black']
                ),
                # lower_left_triangle(nord_fox['magenta'], nord_fox['pink']),
                widget.Memory(
                    foreground=nord_fox["pink"],
                    padding=10,
                    measure_mem="G",
                    format=" {MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}",
                    background=nord_fox['black']
                ),
                # lower_left_triangle(nord_fox['pink'], nord['nord4']),
                widget.CPU(
                    foreground=nord_fox["yellow"],
                    padding=10,
                    format=" {freq_current}GHz {load_percent}%",
                    background=nord_fox['black']
                ),
                # lower_left_triangle(nord['nord4'], nord['nord6']),
                widget.Net(
                    foreground=nord_fox["green"],
                    interface="wlp2s0",
                    format="{down} ↓↑ {up}",
                    background=nord_fox['black']
                ),
                # lower_left_triangle(nord['nord6'], nord['nord7']),
                widget.Clock(
                    foreground=nord_fox["red"],
                    format=" %Y-%m-%d %a %I:%M %p",
                    padding=10,
                    background=nord_fox['black']
                ),
                lower_left_triangle(nord_fox["black"], nord_fox["fg_gutter"]),
                widget.Systray(background=nord_fox["fg_gutter"], padding=10),
                lower_left_triangle(nord_fox["fg_gutter"], nord_fox["bg"]),
                widget.QuickExit(
                    background=nord_fox["bg"],
                    foreground=nord_fox["white"],
                    fontsize=18,
                    default_text="  ",
                ),
            ],
            size=26,
            background=nord_fox["bg"],
        ),
    ),
]
