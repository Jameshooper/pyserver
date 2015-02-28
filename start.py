import sys, time
from daemon import Daemon
import os
class fade_lamp(Daemon):
        def run (self):
                while True:
                        os.system("sudo python /var/www/pyserver/fade.py")
fade = fade_lamp ('tmp/fade.pid')
fade.start()

