"""
layouts.py

Author: Kyle Crandall
Date: July 2020

sets up layouts
"""

from libqtile import layout

from .defaults import colors

def gen_layouts():
    layouts = [
        layout.MonadTall(
            align=layout.MonadTall._left,
            border_focus=colors["themecolor1"],
            border_normal=colors["background"],
            border_width=3,
            margin=5
        )
    ]
    return layouts
