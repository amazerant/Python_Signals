File convolutions.py contains functions convInput and convOutput based on the algorithms from the chapter 6 of the book: "The Scientist and Engineer's Guide to Digital Signal Processing" By Steven W. Smith, Ph.D. http://www.dspguide.com/ch6.htm
Algorithms were adapted to Python and edited by Mazerant Adam https://github.com/amazerant

File convolutions_tests.py contains function test that allows user to execute selected function with given input_signal and kernel, measure total time of executing function given number of times and to measure memory usage.
It will also save plots of both real and imaginary parts of input_signal, kernel and calculated convolution and execute file convolutions_tests.m, which will save more plots, that can be compared.

Usage (when executing from console):

python convolutions_tests.py function input_signal kernel number

For example:

python convolutions_tests.py convInput [1,2,3,4,5] [6,7,8] 100

