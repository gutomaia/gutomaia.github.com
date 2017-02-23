wedNESday #3
############

:date: 2017-01-18 23:00
:modified: 2017-01-21 17:34
:tags: nes, emulator, python
:Category: nes
:slug: wednesday_3
:authors: Guto Maia
:sumary: write a NES emulator


Goals and Detours
=================

One of goals this week was to create a fake PPU, so that we can start testing it and playing with it and create a Pull Request in the py65 project with some tests. Although, while writing some tests in order to reach the first goal, I thought that I could do better.

Running some ASM snippets
=========================

For the fake PPU, I need some tests that calls it. All the tests that I had so far, dealed only with CPU. Then using `nesasm_py <https://github.com/gutomaia/nesasm_py>`_ I've managed to run some ASM code snippets within a test in a very readable way. I took some code snippets, some of them, like
`load palettes <https://github.com/gutomaia/wedNESday/blob/9d162406bb01144b9339284801f4cd2e5c1ba352/wednesday/tests/nes_snippet_test.py#L104>`_ uses the PPU. Then the detours started.

Those tests open the possibility to run some book and tutorials codesnippets without much effort. I've started some demos from `6502.org's compare beyond <http://www.6502.org/tutorials/compare_beyond.html>`_, now I'm playing with some codesnippets from the book `Machine Language for Beginners <https://www.amazon.com/Machine-Language-Beginners-Richard-Mansfield/dp/0942386116>`_ by Richard Mansfield.

Divide and Conquer
==================

I though, that not only py65 deserve some pull requests, but those demos might be useful for other projects. I'm thinking in creating kind of a 'guide' project/module just filled with tests in the most generic way. If anyone could think of a catch name, please tweet me!


As usual, you can checkout the progress at `wedNESday repository <https://github.com/gutomaia/wedNESday>`_.

Next wedNESday
==============

 * It will be a holiday on São Paulo-Brasil, thefore I might have more time to evolve on the PPU.
 * Code Snippets from `Machine Language for Beginners <https://www.amazon.com/Machine-Language-Beginners-Richard-Mansfield/dp/0942386116>`_'s book.
 * Split the tests into a Guide project.
