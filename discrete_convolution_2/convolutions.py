import numpy as np

def convInput(input_signal,kernel):
    '''algorithm taken from the chapter 6 of the book:
    "The Scientist and Engineer's Guide to Digital Signal Processing" by Steven W. Smith, Ph.D. http://www.dspguide.com/ch6.htm'''
    try:
        n,m = len(input_signal),len(kernel)
        if n==0 or m==0:
           raise ValueError("input_signal and kernel must be non-zero length arrays of numbers")
    except:
        raise ValueError("input_signal and kernel must be non-zero length arrays of numbers")
    y = np.zeros(n+m-1,dtype='complex_')  
    for i in range(n):
        for j in range(m):
            try:
                y[i+j] += complex(input_signal[i])*complex(kernel[j])
            except ValueError:
                raise ValueError("input_signal and kernel must be non-zero length arrays of numbers")
    return y

def convOutput(input_signal,kernel):
    '''algorithm taken from the chapter 6 of the  book:
    "The Scientist and Engineer's Guide to Digital Signal Processing" by Steven W. Smith, Ph.D. http://www.dspguide.com/ch6.htm'''
    try:
        n,m = len(input_signal),len(kernel)
        if n==0 or m==0:
           raise ValueError("input_signal and kernel must be non-zero length arrays of numbers") 
    except:
        raise ValueError("input_signal and kernel must be non-zero length arrays of numbers")
    y = np.zeros(n+m-1,dtype='complex_') 
    for i in range(n+m-1):
        for j in range(m):
            if i<j:
                pass
            elif i-j>n-1:
                pass
            else:
                try:
                    y[i] += complex(kernel[j])*complex(input_signal[i-j])
                except ValueError:
                    raise ValueError("input_signal and kernel must be non-zero length arrays of numbers")
    return y

if __name__ == "__main__":
    pass
