# WSCS

Wireless Signal Coverter System
based on github.com/homeworkc/lazycast and https://github.com/FD-/RPiPlay

how to use ? 
1. ./requirement.sh
2. cd lazycast
3. ./makefile.sh
4. ./all.sh 

if you want it to start on boot 
Append this line to /etc/xdg/lxsession/LXDE-pi/autostart:

<code>
@lxterminal -l --working-directory=<absolute path of lazycast> -e ./all.sh
</code>
  
For example, if lazycast is placed under ~/ (which corresponds to /home/pi/), append the following line to the file:

<code>
@lxterminal -l --working-directory=/home/pi/lazycast -e ./all.sh
</code>

