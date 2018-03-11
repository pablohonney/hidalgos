import unittest

from hypothesis import strategies as st, given

from src.algorithms.compression import tunstall


class TestTunstall(unittest.TestCase):

    # http://balapon.blogspot.am/2014/11/tunstall-code-python.html
    def test_abc(self):
        plain_text = 7 * 'a' + 2 * 'b' + 1 * 'c'
        expected_table = [
            ['b', '000'], ['c', '001'], ['ab', '010'], ['ac', '011'], ['aaa', '100'], ['aab', '101'], ['aac', '110']
        ]
        expected_keys = sorted(key for key, _ in expected_table)

        actual_table = tunstall(plain_text, 3)
        actual_keys = sorted(actual_table.keys())

        self.assertListEqual(actual_keys, expected_keys)

    # https://en.wikipedia.org/wiki/Tunstall_coding
    def test_hello_world(self):
        plain_text = 'hello, world'
        table = tunstall(plain_text, 5)
        # print(table)

    @unittest.skip('TODO tunstall codecs')
    @given(st.text())
    def test_data_driven(self, plain_text):
        encoding_table = tunstall(plain_text)
        code = ''.join(list(encode(plain_text, encoding_table)))
        restored = decode(code, encoding_table)

        self.assertEqual(plain_text, restored)
