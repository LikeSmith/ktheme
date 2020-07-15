"""
shortcuts.py

Author: Kyle Crandall
Date: July 2020

Generates key shortcut list
"""

from libqtile.config import Key
from libqtile.lazy import lazy

from .defaults import default_apps, mod_key

import os

def gen_keys():
    keys = [
        # Manage Windows:
        # Switch windows
        Key([mod_key], "Down",
            lazy.layout.down(),
            desc="Shift focus down"),
        Key([mod_key], "Up",
            lazy.layout.up(),
            desc="Shift focus up"),
        Key([mod_key], "Right",
            lazy.layout.right(),
            desc="Shift focus right"),
        Key([mod_key], "Left",
            lazy.layout.left(),
            desc="Shift focus left"),
        
        # Move windows:
        Key([mod_key, "shift"], "Down",
            lazy.layout.shuffle_down(),
            desc="Shift focused window down"),
        Key([mod_key, "shift"], "Up",
            lazy.layout.shuffle_up(),
            desc="Shift focused window up"),
        Key([mod_key, "shift"], "Right",
            lazy.layout.swap_right(),
            desc="Shift focused window right"),
        Key([mod_key, "shift"], "Left",
            lazy.layout.swap_left(),
            desc="Shift focused window left"),
        
        # Resize windows:
        Key([mod_key, "control"], "Up",
            lazy.layout.grow(),
            desc="Increase size of focused window"),
        Key([mod_key, "control"], "Down",
            lazy.layout.shrink(),
            desc="Decrease size of focused window"),
        Key([mod_key, "control", "shift"], "Up",
            lazy.layout.maximize(),
            desc="Maximize focused window"),
        Key([mod_key, "control", "shift"], "Down",
            lazy.layout.normalize(),
            desc="Normalize window sizes"),
        
        # window functions
        Key([mod_key], "q",
            lazy.window.kill(),
            desc="Kill focused window"),
        Key([mod_key], "f",
            lazy.window.toggle_floating(),
            desc="Float focused window"),
        Key([mod_key, "shift"], "f",
            lazy.window.toggle_fullscreen(),
            desc="Fusscreen focused window"),

        # Utilities
        Key([mod_key], "u",
            lazy.spawn(default_apps["terminal"] + " -e %s/.config/qtile/scripts/update_all.bash"%(os.path.expanduser("~"),)),
            desc="Run all updates"),
        Key([mod_key, "shift"], "u",
            lazy.spawn(default_apps["terminal"] + " -e %s/.config/qtile/scripts/update_pacman.bash"%(os.path.expanduser("~"),)),
            desc="Run Pacman updates"),
        Key([mod_key, "control"], "u",
            lazy.spawn(default_apps["terminal"] + " -e %s/.config/qtile/scripts/update_yay.basj"%(os.path.expanduser("~"),)),
            desc="Run yay updates"),

        # App Shortcuts
        Key([mod_key], "Return",
            lazy.spawn(default_apps["terminal"]),
            desc="Spawn terminal"),
        Key([mod_key], "b",
            lazy.spawn(default_apps["browser"]),
            desc="Spawn browser"),
        Key([mod_key], "e",
            lazy.spawn(default_apps["editor"]),
            desc="Spawn editor"),

        # Qtile Shortcuts
        Key([mod_key, "control"], "r",
            lazy.restart(),
            desc="Reload Qtile"),
        Key([mod_key, "control"], "q",
            lazy.shutdown(),
            desc="Logout"),
        Key([mod_key], "r",
            lazy.spawncmd(),
            desc="Run")
    ]
    return keys
