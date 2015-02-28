import sys, time
from daemon import Daemon

class fade_lamp(Daemon):
	def run (self):
		while True:
			time.sleep(1)

fade = fade_lamp ('tmp/fade.pid')
fade.stop()
