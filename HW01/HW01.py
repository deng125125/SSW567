"""
Classify triangles and use an automated test platform, e.g. UnitTest or PyTest, and write test cases to
test your implementation of classifying triangles.
"""
import unittest
import math

def classify_triangle(a, b, c):
    """
    :param a, b, c: the lengths of the sides of a triangle
    :return: a string that specifies whether the triangle is scalene, isosceles,
             or equilateral, and whether it is a right triangle as well.
    """
    if a <= 0 or b <= 0 or c <= 0 or a + b < c or b + c < a or a + c < b:
        return "It's not a triangle!"

    res = ""
    if a == b == c:
        res += "equilateral"
    elif a == b or b == c:
        res += "isosceles"
    else:
        res += "scalene"

    if round(a * a + b * b, 2) == round(c * c, 2) or round(a * a + c * c, 2) == round(b * b, 2) or round(b * b + c * c, 2) == round(a * a, 2):
        res += " and a right triangle."
    else:
        res += " and is not a right triangle."

    return f"It's {res}"


class TestClassifyTriangle(unittest.TestCase):
    """
    Test classify_triangle() method.
    """
    def test_classify_triangle(self):
        """ test classify_trianle() method """
        self.assertEqual(classify_triangle(3, 4, 5), "It's scalene and a right triangle.")
        self.assertEqual(classify_triangle(5, 4, 3), "It's scalene and a right triangle.")
        self.assertEqual(classify_triangle(1, 1, 1), "It's equilateral and is not a right triangle.")
        self.assertEqual(classify_triangle(-3, -4, 5), "It's not a triangle!")
        self.assertEqual(classify_triangle(0, 1, 1), "It's not a triangle!")
        self.assertEqual(classify_triangle(0.3, 0.4, 0.5), "It's scalene and a right triangle.")
        self.assertEqual(classify_triangle(3, 4, 4), "It's isosceles and is not a right triangle.")
        self.assertEqual(classify_triangle(3, 4, 100), "It's not a triangle!")
        self.assertEqual(classify_triangle(math.sqrt(7), math.sqrt(7), math.sqrt(14)), "It's isosceles and a right triangle.")
        self.assertEqual(classify_triangle(math.sqrt(10), math.sqrt(5), math.sqrt(5)), "It's isosceles and a right triangle.")

# Here is the call to run unittest module
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
