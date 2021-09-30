from libqtile.widget import TextBox

def lower_left_triangle(bg_color, fg_color):
    return TextBox(
                    text='\ue0be',
                    padding=0,
                    fontsize=22,
                    font='Iconsolata for Powerline',
                    background=bg_color,
                    foreground=fg_color)


def left_arrow(bg_color, fg_color):
    return TextBox(
                    text='\uE0B2',
                    padding=0,
                    fontsize=22,
                    background=bg_color,
                    foreground=fg_color)

def right_arrow(bg_color, fg_color):
    return TextBox(
                    text='\uE0B0',
                    padding=0,
                    fontsize=22,
                    background=bg_color,
                    foreground=fg_color)
