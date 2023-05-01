import timeit
import tracemalloc
import numpy as np
import python_convolution

values = [(np.random.random(size=int(1e+1))+1j*np.random.random(size=int(1e+1)),np.random.random(size=int(1e+1))+1j*np.random.random(size=int(1e+1))),
          (np.random.random(size=int(1e+3))+1j*np.random.random(size=int(1e+3)),np.random.random(size=int(1e+3))+1j*np.random.random(size=int(1e+3))),
          (np.random.random(size=int(1e+5))+1j*np.random.random(size=int(1e+5)),np.random.random(size=int(1e+5))+1j*np.random.random(size=int(1e+5))),
          (np.random.random(size=int(1e+3))+1j*np.random.random(size=int(1e+3)),np.random.random(size=int(1e+5))+1j*np.random.random(size=int(1e+5)))]

### speed comparison between python_convolution.discreteConvolution and numpy.convolve for different sizes of one dimensional arrays ###

time1_a = timeit.timeit(
    "discreteConvolution(*value)",
    globals = {"value": values[0]},
    number = int(1e+6),
    setup="from python_convolution import discreteConvolution"
)

time1_b = timeit.timeit(
    "convolve(*value)",
    globals = {"value": values[0]},
    number = int(1e+6),
    setup = "from numpy import convolve"
)

time2_a = timeit.timeit(
    "discreteConvolution(*value)",
    globals = {"value": values[1]},
    number = int(1e+3),
    setup="from python_convolution import discreteConvolution"
)

time2_b = timeit.timeit(
    "convolve(*value)",
    globals = {"value": values[1]},
    number = int(1e+3),
    setup = "from numpy import convolve"
)

time3_a = timeit.timeit(
    "discreteConvolution(*value)",
    globals = {"value": values[2]},
    number = int(1e+1),
    setup="from python_convolution import discreteConvolution"
)

time3_b = timeit.timeit(
    "convolve(*value)",
    globals = {"value": values[2]},
    number = int(1e+1),
    setup = "from numpy import convolve"
)

time4_a = timeit.timeit(
    "discreteConvolution(*value)",
    globals = {"value": values[3]},
    number = int(1e+1),
    setup="from python_convolution import discreteConvolution"
)

time4_b = timeit.timeit(
    "convolve(*value)",
    globals = {"value": values[3]},
    number = int(1e+1),
    setup = "from numpy import convolve"
)

print(f"\npython_convolution.discreteConvolution:\narray sizes = 1e+1 and 1e+1\nnumber of executions = 1e+6\ntime = {time1_a}\n")
print(f"\nnumpy.convolve time:\narray sizes = 1e+1 and 1e+1\nnumber of executions = 1e+6\ntime = {time1_b}\n")

print(f"\npython_convolution.discreteConvolution:\narray sizes = 1e+3 and 1e+3\nnumber of executions = 1e+3\ntime = {time2_a}\n")
print(f"\nnumpy.convolve:\narray sizes = 1e+3 and 1e+3\nnumber of executions = 1e+3\ntime = {time2_b}\n")

print(f"\npython_convolution.discreteConvolution:\narray sizes = 1e+5 and 1e+5\nnumber of executions = 1e+1\ntime = {time3_a}\n")
print(f"\nnumpy.convolve:\narray sizes = 1e+5 and 1e+5\nnumber of executions = 1e+1\ntime = {time3_b}\n")

print(f"\npython_convolution.discreteConvolution:\narray sizes = 1e+3 and 1e+5\nnumber of executions = 1e+1\ntime = {time4_a}\n")
print(f"\nnumpy.convolve:\narray sizes = 1e+3 and 1e+5\nnumber of executions = 1e+1\ntime = {time4_b}\n")

### memory usage comparison between python_convolution.discreteConvolution and numpy.convolve for different sizes of one dimensional arrays ###

tracemalloc.start()

python_convolution.discreteConvolution(*values[0])

print(f"\npython_convolution.discreteConvolution:\narray sizes = 1e+1 and 1e+1\nmemory usage (current,peak) ={tracemalloc.get_traced_memory()}\n")

tracemalloc.stop()

tracemalloc.start()

np.convolve(*values[0])

print(f"\nnumpy.convolve:\narray sizes = 1e+1 and 1e+1\nmemory usage (current,peak) ={tracemalloc.get_traced_memory()}\n")

tracemalloc.stop()

tracemalloc.start()

python_convolution.discreteConvolution(*values[1])

print(f"\npython_convolution.discreteConvolution:\narray sizes = 1e+3 and 1e+3\nmemory usage (current,peak) ={tracemalloc.get_traced_memory()}\n")

tracemalloc.stop()
tracemalloc.start()

np.convolve(*values[1])

print(f"\nnumpy.convolve:\narray sizes = 1e+3 and 1e+3\nmemory usage (current,peak) ={tracemalloc.get_traced_memory()}\n")

tracemalloc.stop()
tracemalloc.start()

python_convolution.discreteConvolution(*values[2])

print(f"\npython_convolution.discreteConvolution:\narray sizes = 1e+5 and 1e+5\nmemory usage (current,peak) ={tracemalloc.get_traced_memory()}\n")

tracemalloc.stop()
tracemalloc.start()

np.convolve(*values[2])

print(f"\nnumpy.convolve\narray sizes = 1e+5 and 1e+5\nmemory usage (current,peak) ={tracemalloc.get_traced_memory()}\n")

tracemalloc.stop()
tracemalloc.start()

python_convolution.discreteConvolution(*values[3])

print(f"\npython_convolution.discreteConvolution:\narray sizes = 1e+3 and 1e+5\nmemory usage (current,peak) ={tracemalloc.get_traced_memory()}\n")

tracemalloc.stop()
tracemalloc.start()

np.convolve(*values[3])

print(f"\nnumpy.convolve:\narray sizes = 1e+3 and 1e+5\nmemory usage (current,peak) ={tracemalloc.get_traced_memory()}\n")

tracemalloc.stop()
