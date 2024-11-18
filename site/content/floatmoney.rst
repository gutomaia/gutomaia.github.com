Why You Should Never Use Floats/Doubles Primitives for Money
############################################################

:date: 2024-11-16 21:00
:modified: 2024-11-16 21:00
:tags: python finance
:Category: finance
:slug: floatmoney
:authors: Guto Maia
:sumary: Why you should never use Floats or Double primitives for Money

.. figure:: {static}/images/gus_streach.png
    :align: center
    :alt: superman 3: Gus streaching to reach computer
    :scale: 50%


Handling real numbers in computer science is a complex task, especially for fields like finance and astronomy, where precision is critical. Standard floating-point arithmetic is optimized for speed, often at the expense of exact precision. This trade-off has a particularly problematic impact on financial calculations, where even tiny rounding errors can add up to substantial discrepancies. Consequently, many programming languages provide special libraries or data types for precise decimal handling, specifically for applications where exactness is paramount.


Understanding the Problem
=========================

How does IEEE 754 Represent Floating Points?
--------------------------------------------

Most programming languages, if not all, represent floating-point numbers according to the IEEE 754 standard, which specifies how to encode decimal numbers in binary format for compatibility across systems. This standard uses scientific notation within a fixed number of bits, trading some accuracy for speed.

For example, the decimal number ``0.1`` (i.e., :math:`1 \times 10^{-1}`) cannot be represented precisely in binary, so IEEE 754 provides an approximation. In the 32-bit IEEE 754 format, the number is broken down as follows:

- The first bit is for the sign.
- The next 8 bits represent the exponent.
- The remaining 23 bits store the mantissa.

In 64-bit format, the exponent uses 11 bits, and the mantissa uses 52 bits. Due to this finite bit length, rounding errors can occur in even simple arithmetic operations.

Floating Point in Action
------------------------

To see IEEE 754's limitations in Python, open a Python 3 terminal and try:

.. code-block:: python

    >>> 100.3 + 0.1 == 100.4

You might expect `True`, but you'll see `False` because:

.. code-block:: python

    >>> 100.3 + 0.1
    100.39999999999999



We can delve further by examining the binary representation of floating-point numbers in Python:

.. code-block:: python

    import struct

    BLUE = "\033[1;34m"
    CYAN = "\033[1;36m"
    GREEN = "\033[0;32m"
    RESET = "\033[0;0m"

    def binary(num, ctype):
        return [bin(c).replace('0b', '').rjust(8, '0') for c in struct.pack(ctype, num)]

    def binary_str(num, exponent=8, mantissa=23, ctype='!f'):
        bits = ''.join(binary(num, ctype))
        end_exponent = exponent + 1
        start_mantissa = end_exponent + 1
        end_mantissa = start_mantissa + mantissa + 1
        return ''.join([BLUE, bits[:1], GREEN, bits[1:end_exponent], CYAN, bits[start_mantissa:end_mantissa], RESET])

    def binary_str_fp64(num, exponent=11, mantissa=52, ctype='!d'):
        return binary_str(num, exponent, mantissa, ctype)

Try it out:

.. code-block:: python

    >>> print(binary_str_fp64(2.1))
    010000000000000110011001100110011001100110011001100110011001101

The sign bit appears in blue, the exponent bits in green, and the mantissa in cyan.

To observe the full decimal value without truncation, Python's `Decimal` type is helpful:

.. code-block:: python

    from decimal import Decimal
    >>> Decimal(2.1)
    Decimal('2.100000000000000088817841970012523233890533447265625')


What may seem like an error is actually by design—it's a standard behavior resulting from how floating-point numbers are stored and rounded in memory. This limitation is not unique to Python; it affects many programming languages due to the IEEE 754 standard.

Javascript and TypeScript example
*********************************

.. code-block:: javascript

    console.log(100.3 + 0.1 === 100.4);  // False!

Java example
************

In Java, floating-point precision issues are also evident when using the float or double types:

.. code-block:: java

    public class FloatPrecision {
        public static void main(String[] args) {
            double result = 100.3 + 0.1;
            System.out.println(result == 100.4); // false
            System.out.println(result);          // 100.39999999999999
        }
    }

C example
*********

C also exhibits precision issues with floating-point arithmetic, using the float or double types:

.. code-block:: c

    #include <stdio.h>

    int main() {
        double result = 100.3 + 0.1;
        printf("%d\n", result == 100.4);  // 0 (false)
        printf("%.17f\n", result);        // 100.3999999999999915
        return 0;
    }

C# Example
**********

In C#, the double type produces similar rounding errors, as shown here:

.. code-block:: csharp

    using System;

    class FloatPrecision {
        public static void Main() {
            double result = 100.3 + 0.1;
            Console.WriteLine(result == 100.4); // False
            Console.WriteLine(result);          // 100.39999999999999
        }
    }

PHP Example
***********

In PHP, floating-point numbers are also subject to the same precision issues. Here's how it looks in PHP:

.. code-block:: php

    <?php
    $result = 100.3 + 0.1;
    var_dump($result == 100.4); // bool(false)
    echo $result;               // 100.39999999999999
    ?>

This small error can impact financial calculations significantly. It arises because of inherent rounding in floating-point representation, which is a trade-off between speed and exactness.


A More Precise Solution: Using Decimal for Financial Calculations
=================================================================

For precise financial calculations, Python provides the `Decimal` type. Unlike floats, `Decimal` maintains exact values, which is critical for financial data.

**Note**: Always input numbers as strings when using `Decimal` to avoid loading imprecise float values into it.

.. code-block:: python

    >>> Decimal('100.3') + Decimal('0.1')
    Decimal('100.4')

Going Further: The Money Class
------------------------------

While `Decimal` handles the numeric precision, financial calculations often require a bit more structure, such as tracking currency. To address this, we can create a `Money` class that uses `Decimal` for value representation and includes a currency attribute.

.. code-block:: python

    from decimal import Decimal
    from enum import Enum

    class Currency(Enum):
        USD = 'USD'
        EUR = 'EUR'
        BRL = 'BRL'

    class Money:
        def __init__(self, amount: Decimal, currency: Currency=Currency.USD):
            self.amount = Decimal(str(amount))
            self.currency = currency

        def __str__(self):
            return f"{self.currency.value} {self.amount:.2f}"

        # Additional operations and validation can be added here.

Now, creating a `Money` instance is straightforward:

.. code-block:: python

    >>> price = Money('100.30', Currency.BRL)
    >>> print(price)
    BRL 100.30

The `Money` class helps keep calculations precise and provides a natural place to implement any additional methods or validation rules necessary for financial operations.


Most programming languages offer libraries or specific data types to handle precise decimal calculations, especially for financial applications. Let's take a look on some.


JavaScript and TypeScript: `decimal.js` Library
-----------------------------------------------

JavaScript and TypeScript don't have built-in decimal types, but the `decimal.js` library offers precise decimal arithmetic.

.. code-block:: bash
    
    # install decimal.js
    npm install decimal.js


.. code-block:: javascript

    // JavaScript const Decimal = require('decimal.js'); 
    const money1 = new Decimal('100.3'); 
    const money2 = new Decimal('0.1'); 
    const total = money1.plus(money2); 
    console.log(total.toString()); // Outputs: 100.4

Java: BigDecimal
----------------

Java's BigDecimal class is ideal for precise decimal calculations, as it avoids the rounding issues of floating-point numbers.

.. code-block:: java

    import java.math.BigDecimal;

    public class MoneyCalculation {
        public static void main(String[] args) {
            BigDecimal money1 = new BigDecimal("100.3");
            BigDecimal money2 = new BigDecimal("0.1");
            BigDecimal total = money1.add(money2);
            System.out.println(total); // Outputs: 100.4
        } 
    }


PHP: BCMath Extension
---------------------

PHP's BCMath extension provides functions for arbitrary-precision arithmetic, perfect for handling money.

.. code-block:: php

    <?php 
    $money1 = "100.3"; $money2 = "0.1"; 
    $total = bcadd($money1, $money2, 2); 
    echo $total; // Outputs: 100.4 
    ?>


C++: boost::multiprecision::cpp_dec_float
-----------------------------------------

C++ lacks a built-in decimal type, but the Boost library provides cpp_dec_float for precise decimal calculations.


.. code-block:: cpp

    #include <iostream> 
    #include <boost/multiprecision/cpp_dec_float.hpp>

    using namespace boost::multiprecision;

    int main() {
        cpp_dec_float_50 money1("100.3");
        cpp_dec_float_50 money2("0.1");
        cpp_dec_float_50 total = money1 + money2;
        std::cout << total << std::endl; // Outputs: 100.4 return 0;
    }

Real-World Scenarios: The Madness in Practice
=============================================

In practice, I have observed several fintech companies—yes, not just one or two—that fail to use precise data types to represent monetary values. Instead, they rely on standard floating-point primitive numbers (float), which are not designed for exact representation of decimal values, as demonstrated.

The result? Rounding errors accumulate across transactions, silently affecting balances. These errors may initially seem negligible but can snowball into significant discrepancies over millions of transactions. Now consider taxes and commissions: when each value is calculated as a percentage of an imprecise number representation, the errors compound. Inaccurate tax/commission calculations not only affect business bottom lines but can also lead to compliance issues and legal penalties.

It's madness that many fintechs, which handle billions in assets, skip the basics of numerical representation—it's indded a ground basic topic taught in the first semester of computer science or finance courses. This negligence can lead to reputational damage, regulatory fines, and a lack of trust from users.

Conclusion: Precision is Non-Negotiable in Financial Systems
============================================================

Using Decimal instead of float is not just a best practice—it's a necessity for financial applications where precision is non-negotiable. Floating-point arithmetic is inherently imprecise for base-10 operations, making it unsuitable for handling currency. The errors might start small, but in systems managing high volumes of transactions, they can rapidly escalate to unacceptable levels.

By adopting Decimal and encapsulating it within a Money class, developers gain a double advantage:

* Accuracy: Decimal ensures precise arithmetic and eliminates rounding errors inherent in float operations.
* Abstraction: A Money class allows you to enforce domain-specific rules, such as currency conversions, formatting, and rounding policies, providing a cleaner and more maintainable codebase.

Ignoring precision is not an option. Financial systems deal with people's money, trust, and livelihoods. A lack of attention to these details can cause significant harm—not just to your application, but to your reputation and your customers. As engineers, we have a responsibility to choose the right tools and practices for the job.

In the world of fintech, where small margins and high stakes are the norms, precision is paramount. The question isn't whether you can use floats—it's whether you're willing to gamble with the accuracy and reliability of your financial systems. And that's a bet no responsible engineer or organization should take.

