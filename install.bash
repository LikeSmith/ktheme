#! /usr/bin/bash
#
# install ktheme
#

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

if [[ $1 == "-u" ]]; then
    echo "Uninstalling..."
    if [ -L ~/.config/i3 ]; then
        echo "Removing i3 config"
        rm ~/.config/i3
    fi
    if [ -L ~/.config/i3blocks ]; then
        echo "Removing i3blocks config"
        rm ~/.config/i3blocks
    fi
    if [ -L ~/.config/i3status ]; then
        echo "Removing i3status config"
        rm ~/.config/i3status
    fi
    if [ -L ~/.config/termite ]; then
        echo "Removing termite config"
        rm ~/.config/termite
    fi
elif [[ $1 == "" ]]; then
    echo "Installing..."
    if [[ ! -L ~/.config/i3 ]]; then
        echo "installing i3 config"
        ln -sn ${DIR}/i3 ~/.config/i3
    else
        echo "i3 config already exists"
    fi
    if [[ ! -L ~/.config/i3blocks ]]; then
        echo "installing i3blocks config"
        ln -sn ${DIR}/i3blocks ~/.config/i3blocks
    else
        echo "i3blocks config already exists"
    fi
    if [[ ! -L ~/.config/i3status ]]; then
        echo "installing i3status config"
        ln -sn ${DIR}/i3status ~/.config/i3status
    else
        echo "i3status config already exists"
    fi
    if [[ ! -L ~/.config/termite ]]; then
        echo "installing termite config"
        ln -sn ${DIR}/termite ~/.config/termite
    else
        echo "termite config already exists"
    fi
fi
