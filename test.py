#!/usr/bin/env python3
import unittest
from vec2 import Vec2
from person import Person
from unittest.mock import patch

class TestVec2(unittest.TestCase):
    def setUp(self):
        print("setup")

    def tearDown(self):
        print("teardown")

    @classmethod
    def setUpClass(cls):
        print('setup class')

    @classmethod
    def tearDownClass(cls):
        print('teardown class')

    def test_add(self):
        a = Vec2(5, 3)
        a.add(Vec2(3, 7))
        self.assertEqual(a.x, 8)
        self.assertEqual(a.y, 10)

    def test_scale(self):
        a = Vec2(5, -2)
        a.scale(4)
        self.assertEqual(a.x, 20)
        self.assertEqual(a.y, -8)

    def test_divide(self):
        a = Vec2(15, -6)
        a.divide(3)
        self.assertEqual(a.x, 5)
        self.assertEqual(a.y, -2)

    def test_divide_zero(self):
        a = Vec2(15, -6)
        with self.assertRaises(ValueError):
            a.divide(0)

class TestPerson(unittest.TestCase):
    def test_fetch(self):
        with patch('person.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "{ \"age\": 20 }"

            marco = Person("marco2")
            self.assertEqual(marco.name, "marco2")
            self.assertEqual(marco.age, 20)
            mocked_get.assert_called_with("https://api.agify.io/?name=marco2")

            mocked_get.return_value.ok = False
            polo = Person("polo")
            self.assertEqual(polo.name, "polo")
            self.assertEqual(polo.age, None)
            mocked_get.assert_called_with("https://api.agify.io/?name=polo")

if __name__ == "__main__":
    unittest.main()
