==================
F1 Live timing app
==================

This is a live timing map application for f1 championship races made using
javascript and google maps markers. The live timing data is supplied by
formula1.com.

It’s interactive, you can press over a driver to track him or press into an
empty map zone to untrack and have a general view.
It has also been made with a responsive design to adapt it to mobile browsers
using jquerymobile framework.

How it works:
============

The client side (Already uploaded to github):
Until the race start date a countdown and a demo race is showed.
When the countdown finishes it will connect to server (using ajax) to get the
live timing data from server (every five seconds) and the interface will be
updated using this data.

The server side (Not in github yet):
It uses a Django app for the web page and the static race data (circuit, laps, driver names) is put into the html using the django template system.
For the dynamic data (live timing) I have modified the source of a C program
for the linux terminal called live-f1 to generate a json with the data that the
client requires instead of printing it on terminal screen.

