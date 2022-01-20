from django.test import TestCase


class MockupTestClass(TestCase):
    def test_tests_works(self):
        print('tests working!')
        self.assertEqual(333, int('333'))
