wedNESday #2
############

:date: 2017-01-11 23:00
:modified: 2017-01-14 17:34
:tags: nes, emulator, python
:Category: nes
:slug: wednesday_2
:authors: Guto Maia
:sumary: write a NES emulator


Keep up
=======

I've refactored the tests and extracted to `CPU6502Spec <https://github.com/gutomaia/wedNESday/blob/68e17dff9ec06215c53f05c5069c3c06aadc8816/wednesday/tests/cpu_6502_spec.py>`_, and them start playing with py65. Didn't take long to have most of the test working. Now I have the same test spec running with either ApplyPy or Py65 6502, and that's amazing. Although, let's keep in mind that the goal is a Ricoh 2A03 CPU, the NES CPU. And that lead us to deal with interrupts.


IRQ and NMI
===========

IRQ stands for "Interrupt Request" and NMI for "Non-Masked Interrupt". As far as I know, and please someone correct me if I got it wrong. Interrupts are used for event handling. On the NES, you have two CPUs (Main and PPU for graphics) that runs in parallel. There fore, to accurately emulate a NES, we need to deal with several race conditional on the hardware. Or, for start, we can make then serial (`NMI Thread <https://wiki.nesdev.com/w/index.php/NMI_thread>`_ on NESDev gives good tips in NMI only), and be able to run Super Mario Bros.

As usual, you can checkout the progress at `wedNESday repository <https://github.com/gutomaia/wedNESday>`_.

Next wedNESday
==============

 * Create a fake PPU and a memory bridge and try to run a simple waitvblank program.
 * Create a pull request with CPUSpec and send to `py65 <https://github.com/mnaberez/py65>`_.
