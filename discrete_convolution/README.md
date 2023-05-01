File python_convolution.py contains function discreteConvolution designed to calculate convolution of two discrete, one dimensional signals.
It uses fft and ifft from scipy.fft.


File comparison.py compares execution time and memory usage between python_convolution.discreteConvolution and numpy.convolve for
different sizes of discrete, one dimensional signals. Results are as follows:

- numpy.convolve is faster for shorter signals (both of size: 1e+1 [circa 13,5 times faster], 1e+3 [circa 2 times faster])
- python_convolution.discreteConvolution is faster for longer signals (both of size 1e+5 [circa 76 times faster])
- numpy.convolve is faster when one signal is shorter and the other one is longer (respectively 1e+3 and 1e+5 [circa 2 times faster])

- python_convolution.discreteConvolution peak memory usage is circa 3, 4, 4 and 6 times the numpy.convolve peak memory usage for 
  signals both of size 1e+1, 1e+3, 1e+5 and for signals with mixed sizes of 1e+3 and 1e+5 respectively


File test.py tests whether or not convolution calculated using python_convolution.discreteConvolution is almost equal to the
convolution calculated using conv in Matlab (almost equal means that the relative error of every element of convolution
is lesser than 1e-4, with Matlab conv treated as exact value). It is designed for pytest.

WARNING: before executing test.py please make sure to specify the path to the csv file (FILE_PATH) in both
matlab_convolution.m and test.py. FILE_PATH should be the same in both cases. matlab_convolution.m will create this csv file
and it is required for the test.py to work.
