import matlab.engine
import csv
import python_convolution

def test_discreteConvolution():
    '''Tests whether or not discreteConvolution from python_convolution
    returns the same result as conv from Matlab
    
    (with the maximal relative error equal to 1e-4,
    treating Matlab value as the exact value)'''

    eng = matlab.engine.start_matlab()
    eng.matlab_convolution(nargout=0)
    eng.quit()

    signal1 = []
    signal2 = []
    signal3 = []

    FILE_PATH = ''

    with open(FILE_PATH,'r') as csvfile:
        reader = csv.reader(csvfile,delimiter=' ',quotechar='|')
        for row in reader:
            row = row[0].split(',')
            if row[0] != 'NaN':
                signal1.append(eval(row[0].replace('i','j')))
            if row[1] != 'NaN':
                signal2.append(eval(row[1].replace('i','j')))
            if row[2] != 'NaN':
                signal3.append(eval(row[2].replace('i','j')))
                
                
    conv = python_convolution.discreteConvolution(signal1,signal2)

    assert (abs(signal3-conv)/abs(conv) <= 1e-4).all()
    




