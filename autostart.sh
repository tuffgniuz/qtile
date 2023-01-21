#!/bin/sh

# wallpaper
~/.fehbg &
#
# systemtray
blueman-applet &
nm-applet &
pasystray &

# programs
# mullvad connect 
picom &
redshift -l -6.21462:106.84513 &
deadd-notification-center &

