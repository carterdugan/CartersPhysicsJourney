from vectormath import *
import unittest as ut

class TestVectorMath(ut.TestCase):

    v1 = (1, 2)
    v2 = (3, 4)
    v3 = (1, 2, 3)
    v4 = (3, 4, 5)
    matrix1 = ( (1, 2), (3, 4) )
    matrix2 = ( (1, 2, 3), (4, 5, 6), (7, 8, 9) )

    def testCheckEqualSize(self):
        with self.assertRaises(Exception):
            addVectors(self.v1, self.v3)
        with self.assertRaises(Exception):
            addVectors(self.v3, self.v1)

    def testAddVector(self):
        self.assertEqual(addVectors(self.v1, self.v2), (4, 6))
        self.assertEqual(addVectors(self.v3, self.v4), (4, 6, 8))

    def testScaleVector(self):
        self.assertEqual(scaleVector(5, self.v1), (5, 10))
        self.assertEqual(scaleVector(5, self.v3), (5, 10, 15))

    def testDotProduct(self):
        self.assertEqual(dotProduct(self.v1, self.v2), 11)
        self.assertEqual(dotProduct(self.v3, self.v4), 26)

    def testDeterminant(self):
        self.assertEqual(determinant(self.matrix1), -2)
        self.assertEqual(determinant(self.matrix2), 0)

if __name__ == '__main__':
    ut.main()