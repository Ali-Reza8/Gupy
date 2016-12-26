#!/usr/bin python
# -*- coding:utf-8 -*-
"""
button.25.25.SOMETEXT
label.30.35.SOMETEXT
alert.SOMETEXT
"""


import script
import re
import sys
import os
import io
from time import sleep
import PythonColorize as _

def compiler(path):
	if re.findall(r'^~/+\.gupy', path):
		with open(path, 'r') as f:
			exec(f)
			
