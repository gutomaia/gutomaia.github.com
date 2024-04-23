wedNESday #8 - A long delay
###########################

:date: 2024-04-19 23:00
:modified: 2024-04-19 23:00
:tags: 6502, nes, python, wedNESday
:Category: nes
:slug: wednesday_8
:authors: Guto Maia
:sumary: More than just coding

A Long Time Ago
===============

It's been a while since my last update, and if you've been visiting this page eagerly awaiting news, thank you for your patience. Let's dive right in. Recently, I've been using the "wedNESday" project to thoroughly test NES emulators and improve them.

In a Galaxy Far Far Away
========================

Emulators are being tested using a CPU specification derived from `Nintego <https://github.com/nwidger/nintengo/blob/master/m65go2/instructions_test.go>`_. Here are the emulators I've been putting through their paces:

- `Arbne <https://github.com/ergoadams/arbne>`_: Discovered in a serendipitous encounter within a `Reddit thread <https://www.reddit.com/r/EmuDev/comments/gc5w8w/a_really_bad_nes_emulator_in_python_feedback/>`_, a call for feedback that demands an answer.
- `ApplePy <https://github.com/jtauber/applepy>`_: An Apple 2 emulator by James Tauber, although not a NES emulator, it relies on the 6502 architecture.
- `JSnes <https://github.com/bfirsh/jsnes>`_: A NES emulator written in Javascript, pivotal for my experiments in nodeNES.
- `Py3NES <https://github.com/PyAndy/Py3NES>`_: Constructed amidst live streaming sessions, Py3NES offers a fascinating insight into NES emulation, with its entire development journey documented on `YouTube <https://www.youtube.com/channel/UCT0oEArSloMLL_URLyy2HfA>`_.
- `Py65 <https://github.com/mnaberez/py65>`_: A Python-based 6502 emulator, serving as a critical component in the testing arsenal.
- `Pyntendo <https://github.com/jameskmurphy/nes>`_: Implemented also CPython, Pyntendo promises an intriguing exploration into NES emulation.
- `6502js <https://github.com/Torlus/6502.js>`_: Gregory Estrade's 6502 emulator, a very interesting for quest for accuracy and reliability.


The Goal is to improve the overwall accuracy

Summary of Results
==================

The following table succinctly summarizes the outcomes gleaned from the 6502 instruction tests:

.. include:: ../includes/special.rst
.. include:: ../includes/cpu_spec_failed_results.rst
 
You can find an updated version of this table at `ẁedNESday's documentation <https://gutomaia.net/wedNESday/0.0.x/instructions.html#cpu-failed-tests>`_.

Result Details
===============

NES emulators typically do not implement the decimal mode, rendering ADC and SEC operations with BCD optional, whereas these functionalities are essential for 6502 emulators. Currently, my focus lies on refining the interrupt specification. That's explain why irq, nmi, and reset interruption tests fail across all emulators.

- **PLP Instruction Issue:** Across all emulators, the PLP instruction presents a notable issue, which will be addressed in further detail in a dedicated topic.
- **ApplePy Limitations:** ApplePy lacks implementations for math operations with BCD and interrupts.
- **Arbne Quirk:** Arbne exhibits a minor issue with the BRK instruction, specifically concerning the return of the Program Counter, resulting in a peculiar plus one offset.
- **JSnes Challenges:** JSnes faces challenges with all branch instructions, JSR, and RTS due to issues with instructions that alter the Program Counter position. This may stem from underlying logic in the bridge.
- **Py3NES BRK Issue:** Py3NES encounters an issue with the BRK instruction.
- **Py65 Differences:** Py65 demonstrates discrepancies in the behavior of jump instructions.
- **Pyntendo**, Pytendo has only a minor issue with invalid opcodes.
- **6502js Procedure Call:** The 6502.js emulator encounters issues with the JSR (Jump to Subroutine) and RTS (Return from Subroutine) instructions. These issues impact the proper execution of subroutine calls and returns.
- **Number of Cycles:** Across all emulators, I found it necessary to disable cycle checking in certain instructions to ensure proper functionality. I will be publishing a new table documenting these instances where cycle checking had to be skipped.

In response to these findings, I've initiated forks of each emulator to address the some of the identified issues. The goal is to synchronize the behavior of all emulators, ensuring consistency and compatibility. To achieve this, I'm focusing on improving the test cases for instructions such as BRK, JSR, PLP, and RST, which are crucial for accurate emulation.

PLP Instruction
---------------

The PLP instruction, short for "Pull Processor Status from Stack," retrieves the last value from the stack and updates the Status register accordingly. It affects all flags except the Break (B) and Unused (U) flags.

Essentially, this means that whatever value the B flag had before the PLP execution will remain unchanged afterward, as will the U flag. According to the `Nintego PLP Test <https://github.com/nwidger/nintengo/blob/f173d610a4acece3bb01a6564fe0f35b1a0ed7ac/m65go2/instructions_test.go#L1210>`_, if the value 0xFF is pushed onto the stack, PLP will pull 0xCF into the Status register.

However, giving the Nintengo example, it's worth noting that although fetching the U flag will always return "1", although the corresponding bit in the status register is now set to 0 (0xCF). Further testing on real hardware may be necessary to validate this behavior.


.. code-block:: asm
   
   STX $FF
   TXS
   PLP
   JSR print_p_reg
   JSR print_flags

Testing Specification
---------------------

I often emphasize that a good test is built upon a solid specification. Following the principles of Model Driven Architecture (MDA), I consider a specification to be effective when it exhibits the following characteristics:

- **Self-contained:** A good specification should be self-contained, meaning it doesn't rely on any external references. It defines the scope of the problem within itself, providing clear boundaries for testing.

- **Platform Independent:** A specification should be platform independent, meaning it can be applied uniformly across different environments and architectures. This ensures consistency and compatibility, regardless of the underlying technology stack or infrastructure.

- **Abstracted:** A specification should be abstracted, avoiding implementation details or reliance on concrete methods. This ensures flexibility and adaptability, allowing for changes or enhancements without impacting the overall testing framework.

- **Extendable:** An ideal specification is designed to be extendable, capable of accommodating future requirements or modifications. This flexibility enables the testing framework to evolve alongside the project it supports.

- **Readable:** Perhaps most importantly, a specification must be readable by humans. Clear and concise documentation ensures that the intent and requirements of the system under test are easily understood, facilitating collaboration and maintenance efforts.

While the CPU specs still lack complete abstraction due to explicit calls to assert methods from the unittest.TestCase mixin, efforts are underway to further abstract these specifications in alignment with these principles.

Aside from the `abstracted`, which the CPU specs still lacks since it does explicit calls assert methods from the unittest.TestCase as a mixin. 
