#! /usr/bin/python
#
# Generates Battery Status for i3blocks
#

import subprocess

DISCHARGING = 0
CHARGING = 1
AC = 2
FULL = 3
UNKNOWN = 4


def main():
    acpi_str = subprocess.run(["acpi"], stdout=subprocess.PIPE, text=True, input="battery").stdout

    batteries = []
    
    for line in acpi_str.split("\n"):
        if len(line) == 0:
            continue
        lab = line.split(": ")[0]
        line = line[len(lab)+1:]
        line = line.split(", ")

        # get state
        if "Discharging" in line[0]:
            status = DISCHARGING
        elif "Charging" in line[0]:
            status = CHARGING
        elif "AC" in line[0]:
            status = AC
        elif "Full" in line[0]:
            status = FULL
        else:
            status = UNKNOWN
        
        if status == DISCHARGING or status == CHARGING:
            # get percentage
            percentage = int(line[1][:-1])

            # get remaining
            time = [int(s) for s in line[2].split(" ")[0].split(":")]
        else:
            percentage = None
            time = None
        
        batteries.append((lab, status, percentage, time))

    msg = ""
    for lab, status, percentage, time in batteries:
        if len(batteries) > 1:
            msg += "%s: " % lab

        if status == AC:
            msg += "AC"
            continue
        elif status == CHARGING:
            msg += "CHG: "
            color = "#FFFF00"
        elif status == FULL:
            msg += "FUL:"
            color = "#FF00FF"
        elif status == DISCHARGING:
            msg += "BAT: "
            if percentage < 15:
                color = "#FF0000"
            else:
                color = "#00FF00"
        else:
            msg += "?"
            color = "#0000FF"
            continue

        if percentage is not None:
            # if percentage > 88:
            #     msg += "<span foreground=\"%s\">█ %d%%</span>" % (color, percentage)
            # elif percentage > 75:
            #     msg += "<span foreground=\"%s\">▇ %d%%</span>" % (color, percentage)
            # elif percentage > 63:
            #     msg += "<span foreground=\"%s\">▆ %d%%</span>" % (color, percentage)
            # elif percentage > 50:
            #     msg += "<span foreground=\"%s\">▅ %d%%</span>" % (color, percentage)
            # elif percentage > 38:
            #     msg += "<span foreground=\"%s\">▄ %d%%</span>" % (color, percentage)
            # elif percentage > 25:
            #     msg += "<span foreground=\"%s\">▃ %d%%</span>" % (color, percentage)
            # elif percentage > 13:
            #     msg += "<span foreground=\"%s\">▂ %d%%</span>" % (color, percentage)
            # else:
            #     msg += "<span foreground=\"%s\">▁ %d%%</span>" % (color, percentage)
            if percentage > 80:
                msg += "<span foreground=\"%s\">■■■■■ %d%%</span>" % (color, percentage)
            elif percentage > 60:
                msg += "<span foreground=\"%s\">■■■■  %d%%</span>" % (color, percentage)
            elif percentage > 40:
                msg += "<span foreground=\"%s\">■■■   %d%%</span>" % (color, percentage)
            elif percentage > 20:
                msg += "<span foreground=\"%s\">■■    %d%%</span>" % (color, percentage)
            elif percentage > 0:
                msg += "<span foreground=\"%s\">■     %d%%</span>" % (color, percentage)
            else:
                msg += "<span foreground=\"%s\">      %d%%</span>" % (color, percentage)

        if time is not None:
            msg += " (%02d:%02d)" % (time[0], time[1])

        if lab is not batteries[-1][0]:
            msg += "|"

    print(msg)

if __name__ == "__main__":
    main()
