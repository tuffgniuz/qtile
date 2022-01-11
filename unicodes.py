from libqtile.widget.textbox import TextBox


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
