
import unittest
from classifyTriangle import classifyTriangle



class TestTriangles(unittest.TestCase):

   


    def testEquilateralTriangles_1(self): 

        self.assertEqual(classifyTriangle(7,7,7),'Equilateral','7,7,7 is a equilateral triangle')


    def testEquilateralTriangles_2(self): 

        self.assertNotEqual(classifyTriangle(10,100,100),'Equilateral','100,100,100 is a equilateral triangle')


   



    def testIsosceles_1(self): 

        self.assertEqual(classifyTriangle(2,2,3),'Isosceles','2,2,3 is a Isosceles triangle')
    

    def testIsosceles_2(self): 

        self.assertEqual(classifyTriangle(4,4,5),'Isosceles','4,4,5 is a Isosceles triangle')


    def testScalene_1(self):

        self.assertEqual(classifyTriangle(10,11,12),'Scalene','10,11,12 is a Scalene triangle')    



    def testScalene_2(self):

        self.assertEqual(classifyTriangle(2,3,4),'Scalene','2,3,4 is a Scalene triangle')    


    
    def testRight_1(self): 

        self.assertEqual(classifyTriangle(9,40,41),'Right','9,40,41 is a Right triangle')
        

    def testRight_2(self): 

        self.assertEqual(classifyTriangle(5,12,13),'Right','5,12,13 is a Right triangle')
    

    def testRight_3(self): 

        self.assertEqual(classifyTriangle(6,8,10),'Right','6,8,10 is a Right triangle')
    


    def testInvalid_1(self):

      self.assertEqual(classifyTriangle(-4,-6,-10),'NotATriangle','Only positive values valid' )
    

    def testInvalid_2(self):

      self.assertEqual(classifyTriangle(-1,1,1),'NotATriangle','Only positive values valid' )


    def testvalid_3(self):

      self.assertEqual(classifyTriangle(-100,-200,100),'NotATriangle','Only positive values valid' )
    
    def testFloatingPoint_1(self):
        self.assertEqual(classifyTriangle(3.0, 4.0, 5.0), "Right")
        #self.assertTrue(math.isclose(5.0, 5.00000000001))
        #self.assertAlmostEqual(classifyTriangle(3.00000000001, 4.00000000001, 5.00000000001), "Right")

    def testFloatingPoint_2(self):
        self.assertEqual(classifyTriangle(5.2, 5.2, 5.2), "Equilateral", "5.2,5.2,5.2 is a equilateral triangle")


    #def testInputsD(self):
        #self.assertEqual(classifyTriangle(10,15,30),'Scalene','Should be Isoceles')
        

    #def testFloatingPoint_3(self):
        #self.assertEqual(math.isclose(1.1,2.1,3.1))


        
        



if __name__ == '__main__':
    print('Tests are running')

    unittest.main()