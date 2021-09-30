#! /usr/bin/python
#
# Generates Volume Status for i3blocks
#

import subprocess

BAR_COLOR = "#888888"
MUTE_COLOR = "#555555"

def main():
    vol = int(subprocess.run("amixer get Master | awk '/%/ {print $4}' | tr -d []%", capture_output=True, shell=True, text=True).stdout)
    mute = subprocess.run("amixer get Master | awk '/%/ {print $6}' | tr -d []", capture_output=True, shell=True, text=True).stdout == "off\n"
    
    msg = "VOL: "
    if mute:
        msg += "<span foreground=\"%s\">MUTE</span>" % MUTE_COLOR
    elif vol > 80:
        msg += "<span foreground=\"%s\">■■■■■ %d%%</span>" % (BAR_COLOR, vol)
    elif vol > 60:
        msg += "<span foreground=\"%s\">■■■■  %d%%</span>" % (BAR_COLOR, vol)
    elif vol > 40:
        msg += "<span foreground=\"%s\">■■■   %d%%</span>" % (BAR_COLOR, vol)
    elif vol > 20:
        msg += "<span foreground=\"%s\">■■    %d%%</span>" % (BAR_COLOR, vol)
    elif vol > 0:
        msg += "<span foreground=\"%s\">■     %d%%</span>" % (BAR_COLOR, vol)
    else:
        msg += "<span foreground=\"%s\">      %d%%</span>" % (BAR_COLOR, vol)
    
    print(msg)


if __name__ == "__main__":
    main()
