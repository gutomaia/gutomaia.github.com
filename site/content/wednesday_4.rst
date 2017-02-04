wedNESday #4
############

:date: 2017-01-25 23:00
:modified: 2017-01-28 17:35
:tags: nes emulator python
:Category: nes
:slug: wednesday_4
:authors: Guto Maia
:sumary: write a NES emulator

.. figure:: {filename}/images/blender_brain.jpg
    :align: center
    :alt: Blender Brain
    :scale: 50%

    Blender Brain*

Split and Share
===============

I'm splitting the project wedNESday into a guide project. Unfortunelly, it does not have a catch name yet. The goal of this sidekick project is to serve as a lighthouse for thouse who attempt to create an emulator. It's filled with abstract test case scenarios. Well, for now the sameone I already have on wedNESday (yep, mostly,just copy and clip).


The Real Deal
=============

As I had more time, due to a local holiday, I've spent a lot of time with an actual 6502 microprocessor, thanks to `Toshimitsu Kamei <https://twitter.com/salexkidd>`_, who bought that for me sended it to Brazil from Japan. The MPU is a `W65C02S <http://datasheets.chipdb.org/Western%20Design/W65C02S.pdf>`_. I'm using the RaspberryPi's GPIO to interract with it. So far, haven't done much. Still reading the manual and how to actially send and data and memory addresses. Also dealing with pinout flags, to understand when I should read from data and address and when I should write.

Trivia fact
-----------
- Matt Groening's Futurama showed that Blender uses a 6502 CPU.

.. figure:: {filename}/images/futurama.jpg
    :align: center
    :alt: Futurama

Next wedNESday
==============

 * Don't know yet. I'll certainly have less time available this week. How about some GUI?
