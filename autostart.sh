#!/bin/sh

# auto start fctix
fcitx5 -d %

# auto start redshift
redshift -l -6.175110:106.865036 -m randr &

# restore background with feh
~/.fehbg &

# mpd daemon start (if no other user instance exist)
# [ ! -s ~/.config/mpd/pid ] && mpd

# start mopidy
mopidy &

xcompmgr -c -l10 -t10 &

# blueman-applet
blueman-applet &
