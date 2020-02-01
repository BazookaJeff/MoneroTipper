import unittest

import helper
from helper import get_xmr_val
from tipbot.withdraw import parse_withdrawl_amount

try:
    from unittest.mock import patch, Mock, MagicMock
except ImportError:
    from mock import patch, Mock

class mainTestCase(unittest.TestCase):
    """
    NOTICE: Some of these testcases rely on coingecko's API when calling method_handler.get_xmr_val.
     It is possible that these tests will fail when the value changes during the assert.
    """

    helper.botname = "MoneroTip"

    def test_parse_withdrawal_amount(self):
        self.assertTrue(parse_withdrawl_amount("withdraw 1.0 xmr") == "1.0")
        self.assertTrue(parse_withdrawl_amount("withdraw 1xmr") == "1")

        self.assertTrue(parse_withdrawl_amount("withdraw 1 mxmr") == "0.001")
        self.assertTrue(parse_withdrawl_amount("withdraw 1mxmr") == "0.001")

        self.assertTrue(parse_withdrawl_amount("withdraw 1.0$") == str(get_xmr_val(1)))
        self.assertTrue(parse_withdrawl_amount("withdraw $1") == str(get_xmr_val(1)))
