import timeit
import tracemalloc
import logging
import argparse

import convolutions

convInput = convolutions.convInput
convOutput = convolutions.convOutput

def test(function,input_signal,kernel,number,logger):
    '''executes {function} with given {input_signal} and {kernel}, measures total execution time of {number} executions and memory usage'''
    try:
        tracemalloc.start()
        result = eval(function)(eval(input_signal),eval(kernel))
        memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()
    except Exception as e:
        logger.error(msg=f"function name: {function}\ninput_signal signal: {input_signal}\nkernel: {kernel}\n",exc_info=e)
        return 
    czas = timeit.timeit(
        "eval(function)(eval(input_signal),eval(kernel))",
        globals={"function":function,"input_signal":input_signal,"kernel":kernel},
        number = number,
        setup=f"from __main__ import {function}"
    )
    logger.info(f"function name: {function}\ninput_signal signal: {input_signal}\nkernel: {kernel}\nreturned: {result}\ntotal execution time: {czas}\nnumber of executions: {number}\nmemory usage: {memory}")
        
if __name__ == "__main__":
    logging.basicConfig(filemode="w",level="INFO")

    logger = logging.getLogger(__name__)
    handler = logging.FileHandler("convolutions_tests.log")
    formatter = logging.Formatter('--- Test from %(asctime)s\n%(message)s',datefmt="%d/%m/%Y %I:%M:%S %p---")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
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
    
    test(function,input_signal,kernel,number,logger)

    