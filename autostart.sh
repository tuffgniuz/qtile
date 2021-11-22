#!/bin/sh


# auto start fctix
# fcitx5 -d %

# auto start redshift
redshift -l -6.175110:106.865036 -m randr &

# restore background with feh
~/.fehbg &

# mpd daemon start (if no other user instance exist)
# [ ! -s ~/.config/mpd/pid ] && mpd

# start mopidy
mopidy &

# xcompmgr -c -l10 -t10 &

##################
# systray applets
#################

# networkmanager
nm-applet &

# picom
picom &

# blueman-applet
blueman-applet &

# volctl - per-application  systemtray applet for PulseAudio
volctl &

# MicTray - lightweight sys tray application to control the microphone state and volume using PulseAudio
mictray &

# vpn
nordvpn connect Singapore &
