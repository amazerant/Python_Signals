import timeit
import tracemalloc
import logging
import argparse
import matlab.engine
import matplotlib.pyplot as plt
import numpy as np
import unittest

import convolutions
import convInput_unittest
import convOutput_unittest

convInput = convolutions.convInput
convOutput = convolutions.convOutput

def testFunction(function,input_signal,kernel,number,logger):
    '''executes {function} with given {input_signal} and {kernel}, measures total execution time of {number} executions and memory usage'''
    
    #checking whether input arguments make sense and measuring memory usage  
    try:
        tracemalloc.start()
        convolution = eval(function)(eval(input_signal),eval(kernel))
        memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()
    except Exception as e:
        logger.error(msg=f"function name: {function}\ninput_signal signal: {input_signal}\nkernel: {kernel}\n",exc_info=e)
        return 

    #measuring time of executions
    czas = timeit.timeit(
        "eval(function)(eval(input_signal),eval(kernel))",
        globals={"function":function,"input_signal":input_signal,"kernel":kernel},
        number = number,
        setup=f"from __main__ import {function}"
    )
    
    input_signal = eval(input_signal)
    kernel = eval(kernel)
    n = len(input_signal)
    m = len(kernel)  
    
    #creating csv file used to run Matlab code
    with open('thisFileWillRemoveItself.csv','w',newline='') as csvfile:
        csvfile.write(f"{n},"+str(input_signal).replace(' ','').replace('[','').replace(']','').replace(')','').replace('(','')+'\n')
        csvfile.write(f"{m},"+str(kernel).replace(' ','').replace('[','').replace(']','').replace(')','').replace('(','')+'\n')
        
    #writing output to file "convolutions_tests.log"
    logger.info(f"function name: {function}\ninput_signal signal: {input_signal}\nkernel: {kernel}\nreturned: {convolution}\ntotal execution time: {czas}\nnumber of executions: {number}\nmemory usage: {memory}")
    
    #running unit tests
    ###right now results of tests aren't shown in the console###
    suite = unittest.TestLoader().loadTestsFromTestCase(eval(f"{function}_unittest.TestConvolution"))
    with open("convolutions_tests.log","a") as logFile:
        unittest.TextTestRunner(stream=logFile,verbosity=2).run(suite)
        
    #creating and saving plots
    x_inp = range(0,len(input_signal),1)
    x_ker = range(0,len(kernel),1)
    x_conv = range(0,len(convolution),1)
    plt.subplot(2,3,1)
    plt.stem(x_inp,np.real(input_signal),basefmt='black',markerfmt='s')
    plt.xticks(x_inp)
    plt.title('Input signal (real part)')
    plt.subplot(2,3,2)
    plt.stem(x_ker,np.real(kernel),basefmt='black',markerfmt='s')
    plt.xticks(x_ker)
    plt.title('Kernel (real part)')
    plt.subplot(2,3,3)
    plt.stem(x_conv,np.real(convolution),basefmt='black',markerfmt='s')
    plt.xticks(x_conv)
    plt.title('Convolution (real part)')
    plt.subplot(2,3,4)
    plt.stem(x_inp,np.imag(input_signal),basefmt='black',markerfmt='s')
    plt.xticks(x_inp)
    plt.title('Input signal (imaginary part)')
    plt.subplot(2,3,5)
    plt.stem(x_ker,np.imag(kernel),basefmt='black',markerfmt='s')
    plt.xticks(x_ker)
    plt.title('Kernel (imaginary part)')
    plt.subplot(2,3,6)
    plt.stem(x_conv,np.imag(convolution),basefmt='black',markerfmt='s')
    plt.xticks(x_conv)
    plt.title('Convolution (imaginary part)')
    figure = plt.gcf()
    figure.set_size_inches(16,12)
    plt.savefig("plotPython.png",dpi=100)
    
    #executing Matlab code
    eng = matlab.engine.start_matlab()
    eng.convolutions_tests(nargout=0)
    eng.quit()
if __name__ == "__main__":   
    #creating logger
    logging.basicConfig(filemode="w",level="INFO")
    logger = logging.getLogger(__name__)
    handler = logging.FileHandler("convolutions_tests.log")
    formatter = logging.Formatter('--- Test from %(asctime)s\n%(message)s',datefmt="%d/%m/%Y %I:%M:%S %p---")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    #creating parser
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('function',metavar='function',type=str,help='enter name of function you want to execute (convInput, convOutput)')
    parser.add_argument('input_signal',metavar='input_signal',type=str,help='enter an array representing input signal signal (for example [1,2,3])')
    parser.add_argument('kernel',metavar='kernel',type=str,help='enter an array representing kernel (for example [1,2,3])')
    parser.add_argument('number',metavar='number',type=int,help='enter how many times should function be ran')
    args = parser.parse_args()
    function = args.function
    input_signal = args.input_signal
    kernel = args.kernel
    number = args.number
    
    testFunction(function,input_signal,kernel,number,logger)

    
