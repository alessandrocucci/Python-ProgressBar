# Text progress bar tool for your Python scripts.

A text progress bar is typically used to display the progress of a long running operation, providing a visual cue that processing is underway.

The ProgressBar class manages the current progress.

The client could choose the bar width, and how it has to be displayed (percentage and/or steps).



Here's some examples! :+1:

```python
from time import sleep
from progressbar import ProgressBar

print "Progress Bar 1: width 20, steps 25:"
pb = ProgressBar()
pb.set_total(25)
for x in xrange(25):
	pb.advance()
	sleep(0.25)
# OUTPUT: [====================] 100%

print "Progress Bar 2: width 10, steps 100:"
pb = ProgressBar(width=10)
pb.set_total(100)
for x in xrange(100):
	pb.advance()
	sleep(0.1)
# OUTPUT: [==========] 100%

print "Progress Bar 3: width 30, steps 40:"
pb = ProgressBar(width=30, percentage=False, steps=True)
pb.set_total(40)
for x in xrange(40):
	pb.advance()
	sleep(0.25)
# OUTPUT: [==============================] 40/40

```
