
"""
screens.py

Author: Kyle Crandall
Date: July 2020

generates screens including widgets and Bar
"""

from libqtile.config import Screen
from libqtile import widget, bar

from .defaults import colors, font, default_apps

# Setup Bar
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
        widget.Image(
            filename="~/.config/qtile/theme/icons/terminal.png",
            margin=6,
            mouse_callbacks = {"Button1":lambda qtile: qtile.cmd_spawn(default_apps["terminal"])}
        ),
        widget.Image(
            filename="~/.config/qtile/theme/icons/browser.png",
            margin=6,
            mouse_callbacks = {"Button1":lambda qtile: qtile.cmd_spawn(default_apps["browser"])}
        ),
        widget.Image(
            filename="~/.config/qtile/theme/icons/editor.png",
            margin=6,
            mouse_callbacks = {"Button1":lambda qtile: qtile.cmd_spawn(default_apps["editor"])}
        ),
        widget.Sep(
            linewidth=1,
            padding=10
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
            filename="~/.config/qtile/theme/icons/update.png",
            background=colors["themecolor2"],
            margin=6,
            #mouse_callbacks = {"Button1": lambda qtile: qtile.cmd_spawn(default_apps['terminal'] + " -e ~/.config/qtile/update_all.bash")}
        ),
        widget.Pacman(
            background=colors["themecolor2"],
            foreground=colors["foreground1"],
            unavailable=colors["foreground2"]
        ), 
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
