import unittest
from lib.util import format_satoshis, parse_URI

class TestUtil(unittest.TestCase):

    def test_format_satoshis(self):
        result = format_satoshis(1234)
        expected = "0.00001234"
        self.assertEqual(expected, result)

    def test_format_satoshis_diff_positive(self):
        result = format_satoshis(1234, is_diff=True)
        expected = "+0.00001234"
        self.assertEqual(expected, result)

    def test_format_satoshis_diff_negative(self):
        result = format_satoshis(-1234, is_diff=True)
        expected = "-0.00001234"
        self.assertEqual(expected, result)

    def _do_test_parse_URI(self, uri, expected_address, expected_amount, expected_label, expected_message, expected_request_url):
        address, amount, label, message, request_url = parse_URI(uri)
        self.assertEqual(expected_address, address)
        self.assertEqual(expected_amount, amount)
        self.assertEqual(expected_label, label)
        self.assertEqual(expected_message, message)
        self.assertEqual(expected_request_url, request_url)

    def test_parse_URI_address(self):
        self._do_test_parse_URI('clam:xD4xDTs85aVjYxCm5MG4P7VyEgNXTaySTp', 'xD4xDTs85aVjYxCm5MG4P7VyEgNXTaySTp', '', '', '', '')

    def test_parse_URI_only_address(self):
        self._do_test_parse_URI('xD4xDTs85aVjYxCm5MG4P7VyEgNXTaySTp', 'xD4xDTs85aVjYxCm5MG4P7VyEgNXTaySTp', None, None, None, None)


    def test_parse_URI_address_label(self):
        self._do_test_parse_URI('clam:xD4xDTs85aVjYxCm5MG4P7VyEgNXTaySTp?label=scallop%20test', 'xD4xDTs85aVjYxCm5MG4P7VyEgNXTaySTp', '', 'scallop test', '', '')

    def test_parse_URI_address_message(self):
        self._do_test_parse_URI('clam:xD4xDTs85aVjYxCm5MG4P7VyEgNXTaySTp?message=scallop%20test', 'xD4xDTs85aVjYxCm5MG4P7VyEgNXTaySTp', '', '', 'scallop test', '')

    def test_parse_URI_address_amount(self):
        self._do_test_parse_URI('clam:xD4xDTs85aVjYxCm5MG4P7VyEgNXTaySTp?amount=0.0003', 'xD4xDTs85aVjYxCm5MG4P7VyEgNXTaySTp', 30000, '', '', '')

    def test_parse_URI_address_request_url(self):
        self._do_test_parse_URI('clam:xD4xDTs85aVjYxCm5MG4P7VyEgNXTaySTp?r=http://domain.tld/page?h%3D2a8628fc2fbe', 'xD4xDTs85aVjYxCm5MG4P7VyEgNXTaySTp', '', '', '', 'http://domain.tld/page?h=2a8628fc2fbe')

    def test_parse_URI_ignore_args(self):
        self._do_test_parse_URI('clam:xD4xDTs85aVjYxCm5MG4P7VyEgNXTaySTp?test=test', 'xD4xDTs85aVjYxCm5MG4P7VyEgNXTaySTp', '', '', '', '')

    def test_parse_URI_multiple_args(self):
        self._do_test_parse_URI('clam:xD4xDTs85aVjYxCm5MG4P7VyEgNXTaySTp?amount=0.00004&label=scallop-test&message=scallop%20test&test=none&r=http://domain.tld/page', 'xD4xDTs85aVjYxCm5MG4P7VyEgNXTaySTp', 4000, 'scallop-test', 'scallop test', 'http://domain.tld/page')

    def test_parse_URI_no_address_request_url(self):
        self._do_test_parse_URI('clam:?r=http://domain.tld/page?h%3D2a8628fc2fbe', '', '', '', '', 'http://domain.tld/page?h=2a8628fc2fbe')

    def test_parse_URI_invalid_address(self):
        self.assertRaises(AssertionError, parse_URI, 'clam:invalidaddress')

    def test_parse_URI_invalid(self):
        self.assertRaises(AssertionError, parse_URI, 'notclam:xD4xDTs85aVjYxCm5MG4P7VyEgNXTaySTp')

    def test_parse_URI_parameter_polution(self):
        self.assertRaises(Exception, parse_URI, 'clam:xD4xDTs85aVjYxCm5MG4P7VyEgNXTaySTp?amount=0.0003&label=test&amount=30.0')

