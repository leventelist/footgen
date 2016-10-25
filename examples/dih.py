#!/usr/bin/python

from footgen import *

f = Footgen("header_40")

f.dih(pitch=2.54, pins=40, width=2.54, drill=1, diameter=1.5)
f.finish();

f = Footgen("header_40f")

f.dihf(pitch=2.54, pins=40, width=2.54, drill=1, diameter=1.5)
f.finish();


