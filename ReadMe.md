A library of animations in Circuit Python

This will hopefully build up to a set of animations of different things that you can use in RBG LED matrices. Each animation will output an 8x8 (this may be adjustable in some) array of (R, G, B) tuples that can be written to your grid.

As much as possible, I've tried to introduce some randomization so the animations are a little more interesting -- this works particularly well on flame and lightening.

I hope that there'll be a common interface for each on, but I want to get a few animations up and running first -- looks like I'm converging around frame as the current frame and calc_next_frame() to move on. Need to update flame though as this was created first.

The examples are all tested on a circuit playground express running on a crickit, but it should work on most Circuit Python hardware.

Animations
==========

* flame.py -- this is a simple flame effect. It's a long way from perfect, both in look and performance, but it's a start! 
* wine.py -- a simple animation of a wine glass being drunk
* rainbow.py -- attempt at a rainbow (with rain and sun) but this is pretty tricky on an 8x8 grid - it bight be worth adding some sparkle to the rainbow
* rain.py -- a cloud with rain
* lightening.py -- rain but with added pazzaz
* heart.py -- a stylised heartbeat

Todo:
====
* twinkle
* PacMan
* Smily
* looking eyes
* Maybe heart with ecg trace
* Add images of each one -- need a nice setup with a diffuser.
* Would be really cool to add some data outputs -- graphs and the like -- a scrolling chart, a falling heatmap perhaps, a radar chart, a 'speedometer'-stype guage if it works.

License
=======
GPLv3 -- you know where to find it -- or contact me if you want a comercial license.

