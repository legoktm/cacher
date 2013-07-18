#!/usr/bin/env python
"""
Copyright (C) 2013 Legoktm

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
IN THE SOFTWARE.
"""

import cache
import os
import time
import unittest


class TestEverything(unittest.TestCase):

    def assertBackend(self, backend, timer=True):
        c = cache.Cache(backend=backend)
        c.set('abc', 'def')
        self.assertEqual(c.get('abc'), 'def')
        self.assertIn('abc', c)
        c.delete('abc')
        self.assertNotIn('abc', c)
        if timer:
            c.set('abc', 'def', 2)
            time.sleep(3)
            self.assertNotIn('abc', c)

    def testMemcache(self):
        self.assertBackend('memcache')

    def testRedis(self):
        self.assertBackend('redis')

    def testPickle(self):
        self.assertBackend('pickle', timer=False)

    def testJSON(self):
        self.assertBackend('json', timer=False)

    def tearDown(self):
        files = ['cache.json', 'cache.pickle']
        for f in files:
            if os.path.exists(f):
                os.unlink(f)