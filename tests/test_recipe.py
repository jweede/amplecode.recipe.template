import os
import unittest

import zc.buildout.buildout

class TemplateTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_simple(self):
        zc.buildout.buildout.main(["-o", "install","simple_test"])

        f = open("test.out")
        self.assertEquals("root\n", f.read())

    def test_filter(self):
        zc.buildout.buildout.main(["-o", "install","filter_test"])

        f = open("test.out")

        self.assertEquals('    "root",\n    "toor"\n', f.read())

    def tearDown(self):
        os.remove("test.out")

if "__main__" == __name__:
    unittest.main()
