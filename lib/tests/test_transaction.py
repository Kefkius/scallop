import unittest

from lib.transaction import (
    Transaction
)

class Test_Transaction(unittest.TestCase):

    def setUp(self):
        super(Test_Transaction, self).setUp()
        self.coinstake_tx = '02000000704d4a5501faaac09e923eb154c4a1692a69f40c6c7570ee508c5cef1d85325a5caeabd8f74a0100008a47304402205b628da48fe51c0d33fdb496b942690b1c0a6f8b295c431fe80c296b4e19af8702203e33521e4b3cb36e0f82f75930c8eeb5cd28d5189ac10a9b119e967f8cee0d53014104be46fb68e65df4b60ccf5503eed8ccbd0939543205f0ecaaf2343fd2301e4ef7bce423461bee2912f438466a95d125bd43d4b55bf809bd3efb9614bac9fe7b25ffffffff0200000000000000000040e1a65500000000434104be46fb68e65df4b60ccf5503eed8ccbd0939543205f0ecaaf2343fd2301e4ef7bce423461bee2912f438466a95d125bd43d4b55bf809bd3efb9614bac9fe7b25ac000000001568747470733a2f2f4a7573742d446963652e636f6d'

    def test_parse(self):
        tx = Transaction(self.coinstake_tx)
        self.assertEquals(tx.raw, self.coinstake_tx)

    def test_deserialize(self):
        tx = Transaction(self.coinstake_tx)
        tx.deserialize()

        self.assertEquals(tx.output_value(), 1437000000)
        self.assertEquals(tx.version, 2)
        self.assertEquals(tx.time, 1430932848)
        self.assertEquals(tx.clamspeech, 'https://Just-Dice.com')

    def test_coinstake_marker(self):
        raw_tx = '02000000704d4a55010000000000000000000000000000000000000000000000000000000000000000ffffffff04033df406ffffffff010000000000000000000000000000'
        tx = Transaction(raw_tx)
        tx.deserialize()

        self.assertEquals(tx.inputs[0]['is_coinbase'], True)

    def test_coinstake(self):
        tx = Transaction(self.coinstake_tx)
        tx.deserialize()

        self.assertEquals(tx.is_coinstake, True)
