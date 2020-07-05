#! /usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

if [[ $1 == "-u" ]]; then
    echo "Unistalling..."
    if [ -L ~/.config/awesome ]; then
        echo "Removing Awesome config"
        rm ~/.config/awesome
    fi
    if [ -L ~/.config/termite ]; then
        echo "Removing Termite config"
        rm ~/.config/termite
    fi
elif [[ $1 == "" ]]; then
    echo "Installing..."
    if [[ ! -L ~/.config/awesome ]]; then
        echo "Installing Awesome Config..."
        ln -s ${DIR}/awesome ~/.config/awesome
    else
        echo "Awesome Config already installed."
    fi

    if [[ ! -L ~/.config/termite ]]; then
        echo "Installing Termite config..."
        ln -s ${DIR}/termite ~/.config/termite
    else
        echo "Termite Config already installed"
    fi
else
    echo "unknown option."
fi