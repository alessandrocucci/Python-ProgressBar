# -*- coding: utf-8 -*-
#
# progressbar.py  - A simple progress bar for your python scripts.
# Copyright (c) 2016 Alessandro Cucci
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

__author__ = 'Alessandro Cucci'
__email__ = 'alessandro.cucci@gmail.com'
__date__ = '06-09-2016'
__version__ = '1.0'

import sys


class ProgressBar(object):
	"""
	Text progress bar tool for Python scripts.

	A text progress bar is typically used to display the progress of a long
	running operation, providing a visual cue that processing is underway.
	The ProgressBar class manages the current progress.

	The client could choose the bar width, and how it has to be displayed
	(percentage and/or steps).
	"""
	def __init__(self, width=20, percentage=True, steps=False):
		self.total = 0
		self.current = 0
		self.finished = False
		self.width = width
		self.widget = {
			'percentage': percentage,
			'steps': steps
		}

	def set_total(self, total):
		self.total = total

	def advance(self):
		self.current += 1
		if self.current > self.total:
			self.finished = True
		if not self.finished:
			self.write_bar()

	def write_bar(self):
		current_width = int((self.width * self.current) / float(self.total))
		current_percentage = int((self.current / float(self.total)) * 100)
		template = "\r[{{0:<{0}}}]".format(self.width)
		output = template.format("=" * current_width)
		if self.widget['percentage']:
			output += " {0}%".format(current_percentage)
		if self.widget['steps']:
			output += " {0}/{1}".format(self.current, self.total)
		sys.stdout.write(output)
		sys.stdout.flush()


if __name__ == '__main__':
	"""
	Here some tests and examples...
	"""

	from time import sleep

	print
	print"Progress Bar di lunghezza 20 per 25 steps:"
	print
	pb = ProgressBar()
	pb.set_total(25)
	for x in xrange(25):
		pb.advance()
		sleep(0.25)

	print
	print
	print "Progress Bar di lunghezza 10 per 100 steps:"
	print
	pb = ProgressBar(width=10)
	pb.set_total(100)
	for x in xrange(100):
		pb.advance()
		sleep(0.1)

	print
	print
	print "Progress Bar di lunghezza 30 in 40 steps:"
	print
	pb = ProgressBar(width=30, percentage=False, steps=True)
	pb.set_total(40)
	for x in xrange(40):
		pb.advance()
		sleep(0.25)

	print
	print
