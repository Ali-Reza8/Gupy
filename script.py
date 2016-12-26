# -*- coding: utf-8 -*-
import sys
import os
import re
import io
# import compiler
from time import sleep
import PythonColorize as _
import Tkinter
from Tkinter import *

print _.colorize(text="""  ,ad8888ba,                                          
 d8"'    `"8b                                         
d8'                                                   
88             88       88  8b,dPPYba,   8b       d8  
88      88888  88       88  88P'    "8a  `8b     d8'  
Y8,        88  88       88  88       d8   `8b   d8'   
 Y8a.    .a88  "8a,   ,a88  88b,   ,a8"    `8b,d8'    
  `"Y88888P"    `"YbbdP'Y8  88`YbbdP"'       Y88'     
                            88               d8'      
                            88              d8'       """, color='cyan', style='bold')
			print _.colorize(text='\r[About] an gui Generator written in python', color='green')


# Syntax Doc:
"""
 *
 * 
 * button(arg*)
 * label(arg*)
 * alert(Text)
 *
 * 
"""


def compiler(path):
	if re.findall(r'^~/+\.gupy', path):
		with open(path, 'r').read() as f:
			EXEC_compile = """import Tkinter
top = Tkinter.Tk()
{f}
top.mainloop()""".format(f=f)
			exec(EXEC_compile)


def init(path):
	if re.findall(r'^~/+', path):
		print _.colorize(text='[*] init project Started...', color='yellow')
		print _.colorize(text='[*] change current dir to {}'.format(path), color='yellow')
		os.system('touch {path}/gui.gupy && subl {path}/gui.gupy'.format(path=path))
		print _.colorize(text='[+] Your Request Succefully Finished!', color='cyan')
	else:
		print _.colorize(text='[!] Please start your path with ~', color='red')


def main():
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
				AskForcompile = str(raw_input(_.colorize(text="Path (start with ~ and End with 'name.gupy'): ", color='green', style='bold')))
				compiler(path=AskForcompile)
		except KeyboardInterrupt:
			print _.colorize(text='\n[*] Stopping Script...', color='red')
			sleep(2)
			print "\nBye ;)"
			break


if __name__ == '__main__':
	main()
