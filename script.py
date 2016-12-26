# -*- coding: utf-8 -*-
import sys
import os
import re
import io
import compiler
from time import sleep
import PythonColorize as _

init_code = """#!/usr/bin/python

import Tkinter
top = Tkinter.Tk()

#####################
# Your Code Should be here :)
#####################

top.mainloop()"""

def init(path):
	if re.findall(r'^~/+', path):
		print _.colorize(text='[*] init project Started...', color='yellow')
		print _.colorize(text='[*] change current dir to {}'.format(path), color='yellow')
		os.system('touch {path}/gui.gupy && subl {path}/gui.gupy'.format(path=path))
		this_script_dir = os.path.dirname(__file__)
		rel_path = path + '/gui.gupy'
		path_for_new_file = os.path.join(this_script_dir, rel_path)
		with io.FileIO(path_for_new_file, "w") as file:
			file.write(init_code)
			sleep(3)
			print _.colorize(text='[+] Your Request Succefully Finished!', color='cyan')
	else:
		print _.colorize(text='[!] Please start your path with ~', color='red')


def main():
	# print cmd
	# arg = cmd.split(' ')[1]
	while True:
		try:
			cmd = raw_input(_.colorize(text="> ", color='red'))
			if cmd == str("init"):
				try:
					AskForPath = raw_input(_.colorize(text="Path (start with ~): ", color='green'))
					init(path=AskForPath)
				except KeyboardInterrupt:
					print _.colorize(text='\n[*] Stopping Script...', color='red')
					sleep(2)
					print "\nBye ;)"
					break
			if cmd == str("compile"):
				AskForcompile = raw_input(_.colorize(text="Path (start with ~ and End with 'name.gupy'): ", color='green', style='bold'))
				compiler(path=AskForcompile)
		except KeyboardInterrupt:
			print _.colorize(text='\n[*] Stopping Script...', color='red')
			sleep(2)
			print "\nBye ;)"
			break


if __name__ == '__main__':
	main()
