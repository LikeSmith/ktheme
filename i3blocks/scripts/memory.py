#! /usr/bin/python
#
# Generates CPU Status for i3blocks
#

import subprocess

BAR_COLOR = "#888888"
BAD_COLOR = "#FF0000"


def main():
    mem_free = float(subprocess.run("free -b | awk '/Mem/ {print $4}'", capture_output=True, shell=True, text=True).stdout)
    mem_totl = float(subprocess.run("free -b | awk '/Mem/ {print $2}'", capture_output=True, shell=True, text=True).stdout)
    swp_free = float(subprocess.run("free -b | awk '/Swap/ {print $4}'", capture_output=True, shell=True, text=True).stdout)
    swp_totl = float(subprocess.run("free -b | awk '/Swap/ {print $2}'", capture_output=True, shell=True, text=True).stdout)

    mem_usage = (mem_totl - mem_free) / mem_totl * 100.0
    swp_usage = (swp_totl - swp_free) / swp_totl * 100.0

    msg = "MEM: "
    if mem_usage > 90:
        msg += "<span foreground=\"%s\">■■■■■ %.1f%% Swap: %.1f%%</span>" % (BAD_COLOR, mem_usage, swp_usage)
    elif mem_usage > 80:
        msg += "<span foreground=\"%s\">■■■■■ %.1f%% Swap: %.1f%%</span>" % (BAR_COLOR, mem_usage, swp_usage)
    elif mem_usage > 60:
        msg += "<span foreground=\"%s\">■■■■  %.1f%% Swap: %.1f%%</span>" % (BAR_COLOR, mem_usage, swp_usage)
    elif mem_usage > 40:
        msg += "<span foreground=\"%s\">■■■   %.1f%% Swap: %.1f%%</span>" % (BAR_COLOR, mem_usage, swp_usage)
    elif mem_usage > 20:
        msg += "<span foreground=\"%s\">■■    %.1f%% Swap: %.1f%%</span>" % (BAR_COLOR, mem_usage, swp_usage)
    elif mem_usage > 0:
        msg += "<span foreground=\"%s\">■     %.1f%% Swap: %.1f%%</span>" % (BAR_COLOR, mem_usage, swp_usage)
    else:
        msg += "<span foreground=\"%s\">      %.1f%% Swap: %.1f%%</span>" % (BAR_COLOR, mem_usage, swp_usage)

    print(msg)

if __name__ == "__main__":
    main()
