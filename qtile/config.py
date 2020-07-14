"""
config.py

Author: Kyle Crandall
Date: July 2020

Qtile config file, loads ktheme
"""

from libqtile.config import Drag, Click
from libqtile.lazy import lazy
from libqtile import layout, hook

from typing import List
import os
import subprocess

from theme.shortcuts import gen_keys
from theme.groups import gen_groups
from theme.layouts import gen_layouts
from theme.screens import gen_screens
from theme.defaults import mod_key

# Setup keyboard shortcuts
keys = gen_keys()

# Setup groups and associated keybindings
groups, keys = gen_groups(keys)

# Setup layouts
layouts = gen_layouts()

# Setup Screens
screens, widget_defaults = gen_screens()
extension_defaults = widget_defaults.copy()

# Drag floating layouts.
mouse = [
    Drag([mod_key], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod_key], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod_key], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "LG3D"

# Startup Hook
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~")
    subprocess.call([home+"/.config/qtile/scripts/autorun.sh"])
