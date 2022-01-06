#!/bin/sh

# notification server

deadd-notification-center &

# auto start redshift
redshift -l -6.175110:106.865036 -m randr &

# restore background with feh
~/.fehbg &

# mpd daemon start (if no other user instance exist)
# [ ! -s ~/.config/mpd/pid ] && mpd

# start mopidy
# mopidy &


##################
# systray applets
#################

# networkmanager
nm-applet &

# picom
picom -cCGfF -o 0.38 -O 200 -I 200 -t 0 -l 0 -r 3 -D2 -m 0.88 --experimental-backend &

# mic and volumectl
mictray &
pasystray &


