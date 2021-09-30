#! /usr/bin/python
#
# Generates CPU Status for i3blocks
#

import subprocess
import json

BAR_COLOR = "#888888"
BAD_COLOR = "#FF0000"

def main():
    cpu_report = json.loads(subprocess.run("mpstat -P ALL -o JSON", capture_output=True, shell=True, text=True).stdout)
    temp = float(open("/sys/class/thermal/thermal_zone0/temp", "r").read()) / 1000.0

    usage = None

    for stats in cpu_report["sysstat"]["hosts"][0]["statistics"][0]["cpu-load"]:
        if stats["cpu"] == "all":
            usage = 100.0 - stats["idle"]
            break
    
    msg = "CPU: "
    if usage > 90:
        msg += "<span foreground=\"%s\">■■■■■ %.1f%% %.1fC</span>" % (BAD_COLOR, usage, temp)
    elif usage > 80:
        msg += "<span foreground=\"%s\">■■■■■ %.1f%% %.1fC</span>" % (BAR_COLOR, usage, temp)
    elif usage > 60:
        msg += "<span foreground=\"%s\">■■■■  %.1f%% %.1fC</span>" % (BAR_COLOR, usage, temp)
    elif usage > 40:
        msg += "<span foreground=\"%s\">■■■   %.1f%% %.1fC</span>" % (BAR_COLOR, usage, temp)
    elif usage > 20:
        msg += "<span foreground=\"%s\">■■    %.1f%% %.1fC</span>" % (BAR_COLOR, usage, temp)
    elif usage > 0:
        msg += "<span foreground=\"%s\">■     %.1f%% %.1fC</span>" % (BAR_COLOR, usage, temp)
    else:
        msg += "<span foreground=\"%s\">      %.1f%% %.1fC</span>" % (BAR_COLOR, usage, temp)

    print(msg)


if __name__ == "__main__":
    main()
