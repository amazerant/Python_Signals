import scipy.fft as fft

def discreteConvolution(signal1,signal2):
    '''calculates the discrete convolution of two real valued one dimensional arrays
    using fft and ifft functions from scipy.fft'''
    signal1,signal2 = list(signal1),list(signal2)
    LS1,LS2 = len(signal1),len(signal2)
    
    signal1.extend([0]*(LS2-1))
    signal2.extend([0]*(LS1-1))

    return fft.ifft(fft.fft(signal1)*fft.fft(signal2))

if __name__ == "__main__":
    pass
    




