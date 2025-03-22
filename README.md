# Scout Law LED Sign
This project serves as a template for anyone who wants to make a custom Scout Law sign with a Raspberry PI Pico (RP2040) micro controller.  Cub Scouts (Lions and Tigers in particular) learn the fundamentals of scouting through things like the "Scout Law", "Scout Oath", and "Cub Scout Motto".  This project started as a simple way to help younger Cub Scouts learn the Scout Law.

## Basic Behavior
The sign itself is 24"x36".  Into the facade are cut outs for each letter of the words in the Scout Law.  Those words are then illuminated in correct sequence to "time" scouts reciting the Scout Law out-loud, with the word fading in and out.  The duration / timing of the lighting is done corresponding to syllable length of the word.  This should help to keep everyone at the same pace and to help younger scouts learn to read the sign.

The mechanism is triggered via a push-button on the back of the sign though future iterations might allow for remote-control.

## Requirements
The primary requirements I decided on for this project are:
- Helps teach the Scout Law
- Fun
- Portable
  - Lightweight
  - Easy to handle
- Inexpensive (relatively)
- Somewhat durable

As a result, there is always a trade-off between weight, durability, and cost.  This repository goes over the details of those decisions and provides the reasoning behind them.

## This Repo
I decided to open-source this repo as a means to share the project with others and to document my progress as much of this is a journey into the unknown for me.  Feel free to use this to build your own version, use parts of it, or even enhance it as you see fit.

[TODO]

# Physical Design
A laminated set of different materials for structure, aesthetic, and function.  The sign is essentially words cut through a material with each word being back-lit with LEDs.  Here is a concept model to show the basic lamination:
![Scout Law Layers](/assets/sign_mockup.PNG)

[TODO]

# Electrical Design
Component listing:
[TODO]

# Software Design
The project uses a MicroPython OS image flashed to the Pico that runs Python natively to control GPIOs on the Pico.
[TODO]

# External Links
- Pico Pinout (https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf)
- Pico W Pintout (https://datasheets.raspberrypi.com/picow/PicoW-A4-Pinout.pdf)
- Pico Datasheet (https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf)
- Pico W Datasheet (https://datasheets.raspberrypi.com/picow/pico-w-datasheet.pdf)
- MicroPython (https://micropython.org/)