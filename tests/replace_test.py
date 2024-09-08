import unittest

positive_cases = [
    '[Getting Started with Sandboxie](docs/Content/GettingStarted.md)',
    '[General Usage Tips]( docs/Content/UsageTips.md )'
]
negative_cases = [
    'docs',
    'docs/',
    '/docs/',
    '/docs/',
    'example.com/docs/url'
]


class MyTestCase(unittest.TestCase):
    def test_replace(self):
        from plugin import _replacer
        for x in positive_cases:
            self.assertNotEqual(x, _replacer(x))
        for x in negative_cases:
            self.assertEqual(x, _replacer(x))


if __name__ == '__main__':
    unittest.main()
