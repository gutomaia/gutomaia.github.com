wedNESday #1
############

:date: 2017-01-04 23:00
:modified: 2017-01-07 23:00
:tags: nes emulator python
:Category: nes
:slug: wednesday
:authors: Guto Maia
:sumary: write a NES emulator


Forewords
=========

I've been hacking the NES for quite a long time, and since them, I've always been asked for writing an emulator. Although it was never a priority, everytime a question like that stands, I usually answer: "Why not?".

Let's think over. Why should I, and why you should to? There are already several good emulators available, why write another one?

Moreover, googling about the subject "write nes emulator", there are several good stories. I've put the most relevant links at the bottom. I also recomend you to read them.

Therefore. What to tell abount NES emulators that haven't already being told? Well, not saying that I do intend to fishish it, but let's explore more the ideia.


Press Start
===========

In order to write the emulator, we need to keep up with the overall architecture that was involved. For now, let's focus on the CPU. NES had a ‎Ricoh 2A03 CPU with the same instruaction set of the 6502. Since we are talking about code. Let highlight the code
from Niels Widger's `Nintengo <https://github.com/nwidger/nintengo>`_. It's very polished, and more important, it's filled with tests. So as a experiment, I've rewrote the tests and used on the James Tauber's `ApplePy <https://github.com/jtauber/applepy>`_, most impressive, without mush effort, the test spec payoff, and show how well made ApplePy is.

You can checkout the progress at `wedNESday repository <https://github.com/gutomaia/wedNESday>`_.

Next wedNESday
==============

 * Get a better understand on how IRQ and NMI works
 * try to do the same with `py65 <https://github.com/mnaberez/py65>`_.



References
================
`Writing an NES emulator in Go Part 1 <http://nwidger.github.io/blog/post/writing-an-nes-emulator-in-go-part-1/>`_

`Write a NES Emulator with Javascript Part 1 <http://blog.alexanderdickson.com/javascript-nes-emulator-part-1>`_

`Write a NES Emulator with Javascript Part 2 <http://blog.alexanderdickson.com/javascript-nes-emulator-part-2>`_

`I made an NES emulator Heres what I learned about the original Nintendo <https://medium.com/@fogleman/i-made-an-nes-emulator-here-s-what-i-learned-about-the-original-nintendo-2e078c9b28fe#.7535jmlgd>`_
