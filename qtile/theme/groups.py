"""
groups.py

Author: Kyle Crandall
Date: July 2020

Sets up qtile groups
"""

from libqtile.config import Key, Group
from libqtile.lazy import lazy

from .defaults import group_names, mod_key

def gen_groups(keys):
    groups = []
    for i, name in enumerate(group_names):
        # Add group
        groups.append(Group(name=name))

        # Add shortcuts
        keys.append(Key([mod_key], "%d"%(i+1),
                        lazy.group[name].toscreen(),
                        desc="Switch to %s"%(name,)))
        keys.append(Key([mod_key, "shift"], "%d"%(i+1),
                        lazy.window.togroup(name, switch_group=True),
                        desc="Move focused window to %s"%(name,)))
    return groups, keys
