import unittest
import convolutions

class TestConvolution(unittest.TestCase):
    
    def testIdentity(self):
        self.assertListEqual([1,2,3,4,0,0,0],list(convolutions.convInput([1,2,3,4],[1,0,0,0])))
    
    def testAmpAndAtt(self):
        self.assertListEqual([0,3.5,7,10.5,14,0,0],list(convolutions.convInput([1,2,3,4],[0,3.5,0,0])))
    
    def testShift(self):
        self.assertListEqual([0,0,1,2,3,4,0],list(convolutions.convInput([1,2,3,4],[0,0,1,0])))
    
    def testEcho(self):
        self.assertListEqual([1,2,4,6,3,4,0],list(convolutions.convInput([1,2,3,4],[1,0,1,0])))
        
    def testCommutativity(self):
        self.assertListEqual(list(convolutions.convInput([1,0,1,0],[1,2,3,4])),list(convolutions.convInput([1,2,3,4],[1,0,1,0])))
    
    
def runTests():
    unittest.main(module="convInput_unittest")
    
if __name__ == "__main__":
    unittest.main()