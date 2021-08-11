#!/usr/bin/env python
from re import template
import unittest
from main import app
import flask

class BasicTestCase(unittest.TestCase):
    def test_home(self):
            tester = app.test_client(self)
            response = tester.get('/about', content_type='html/text')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data, b'About')

    def test_other(self):
            tester = app.test_client(self)
            response = tester.get('a', content_type='html/text')
            self.assertEqual(response.status_code, 404)
            self.assertTrue(b'does not exist' in response.data)

if __name__ == '__main__':
    unittest.main()
