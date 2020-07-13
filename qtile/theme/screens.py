
"""
screens.py

Author: Kyle Crandall
Date: July 2020

generates screens including widgets and Bar
"""

from libqtile.config import Screen
from libqtile import widget, bar

from .defaults import colors, font

def gen_widget_defaults():
    widget_defaults = {
        "font":font["font"],
        "fontsize":font["size"],
        "padding":font["padding"],
        "foreground":colors["foreground1"]
    }
    return widget_defaults

def gen_bar():
    bar_widgets = [
        widget.Sep(
            linewidth=0,
            padding=10,
        ),
        widget.GroupBox(
            active=colors["foreground1"],
            inactive=colors["foreground2"]
        ),
        widget.Prompt(),
        widget.Sep(
            linewidth=1,
            padding=10
        ),
        widget.WindowName(),
        widget.Image(
            filename="~/.config/qtile/theme/icons/speaker.png",
            background=colors["themecolor1"],
            margin=6
        ),
        widget.Volume(
            background=colors["themecolor1"]
        ),
        widget.Image(
            filename="~/.config/qtile/theme/icons/battery.png",
            background=colors["themecolor2"],
            margin=6
        ),
        widget.Battery(
            background=colors["themecolor2"]
        ),
        widget.Clock(
            format='[%Y-%m-%d %a %I:%M %p]',
            background=colors["themecolor1"]
        ),
        widget.Sep(
            linewidth=0,
            padding=10,
            background=colors["themecolor1"]
        )
    ]
    return bar.Bar(
        bar_widgets,
        24,
        background=colors["background"],
        opacity=colors["transparency"]
    )

def gen_screens():
    screens = [
        Screen(
            wallpaper="~/.config/qtile/theme/background.jpg",
            wallpaper_mode="fill",
            top = gen_bar()
        )
    ]
    return screens, gen_widget_defaults()
