import unittest
import os
import pickle
from erc20transfer import *

class TestERC20Transfer(unittest.TestCase):
    """verify merge_weth_transfer works fine
    """

    def test_merge_weth_transfer(self):
      with open('%s/../testdata/in_weth_out_erc20.bin' % os.path.dirname(__file__), mode='rb') as f:
        tx = pickle.load(f)

      merged = ERC20Transfer._ERC20Transfer__merge_weth_transfer(tx['logs'], '0xa288d96671f3b951de8c04a5dbaa9820651d2e09')
      self.assertEqual('0xa288d96671f3b951de8c04a5dbaa9820651d2e09', '0x' + merged[1]['topics'][1].hex().lower()[26:])

      with open('%s/../testdata/in_erc20_out_weth.bin' % os.path.dirname(__file__), mode='rb') as f:
        tx = pickle.load(f)

      merged = ERC20Transfer._ERC20Transfer__merge_weth_transfer(tx['logs'], '0x1be78eaaf029930b9558cf58a6f7ee6aa7bb0848')
      self.assertEqual('0x1be78eaaf029930b9558cf58a6f7ee6aa7bb0848', '0x' + merged[3]['topics'][2].hex().lower()[26:])

    def test_get_erc20_transfers(self):
        """verify get_erc20_transfers works fine
        """

        with open('%s/../testdata/in_erc20_out_erc20.bin' % os.path.dirname(__file__), mode='rb') as f:
          tx = pickle.load(f)

        result = ERC20Transfer.get_erc20_transfers(tx, ERC20Transfer.SEND)
        self.assertEqual(Decimal('247.470406'), result[0].get_erc20_amount())
        self.assertEqual('0xdac17f958d2ee523a2206206994597c13d831ec7', result[0].get_erc20_address())
        self.assertEqual('0xc578e5ba6962f59746261b507aee8b9520acf674', result[0].get_erc20_from())
        self.assertEqual('0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852', result[0].get_erc20_to())
        self.assertEqual('USDT', result[0].get_erc20_symbol())


        result = ERC20Transfer.get_erc20_transfers(tx, ERC20Transfer.RECEIVE)
        self.assertEqual(Decimal('54'), result[0].get_erc20_amount())
        self.assertEqual('0xa2881f7f441267042f9778ffa0d4f834693426be', result[0].get_erc20_address())
        self.assertEqual('0x98d266c51fc3c0a0b5a285c481d40b689d18e6f1', result[0].get_erc20_from())
        self.assertEqual('0xc578e5ba6962f59746261b507aee8b9520acf674', result[0].get_erc20_to())
        self.assertEqual('HUSL', result[0].get_erc20_symbol())

        with open('%s/../testdata/in_erc20_out_weth.bin' % os.path.dirname(__file__), mode='rb') as f:
          tx = pickle.load(f)

        result = ERC20Transfer.get_erc20_transfers(tx, ERC20Transfer.SEND)
        self.assertEqual(Decimal('502123362170.914563541208283316'), result[0].get_erc20_amount())
        self.assertEqual('0x15874d65e649880c2614e7a480cb7c9a55787ff6', result[0].get_erc20_address())
        self.assertEqual('0x1be78eaaf029930b9558cf58a6f7ee6aa7bb0848', result[0].get_erc20_from())
        self.assertEqual('0xb6ca52c7916ad7960c12dc489fd93e5af7ca257f', result[0].get_erc20_to())
        self.assertEqual('eMax', result[0].get_erc20_symbol())

        result = ERC20Transfer.get_erc20_transfers(tx, ERC20Transfer.SEND)
        self.assertEqual(Decimal('16553517434.205974622237635713'), result[1].get_erc20_amount())
        self.assertEqual('0x15874d65e649880c2614e7a480cb7c9a55787ff6', result[1].get_erc20_address())
        self.assertEqual('0x1be78eaaf029930b9558cf58a6f7ee6aa7bb0848', result[1].get_erc20_from())
        self.assertEqual('0x000000000000000000000000000000000000dead', result[1].get_erc20_to())
        self.assertEqual('eMax', result[1].get_erc20_symbol())

        result = ERC20Transfer.get_erc20_transfers(tx, ERC20Transfer.RECEIVE)
        self.assertEqual(Decimal('3.646517991624968994'), result[0].get_erc20_amount())
        self.assertEqual('0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2', result[0].get_erc20_address())
        self.assertEqual('0xb6ca52c7916ad7960c12dc489fd93e5af7ca257f', result[0].get_erc20_from())
        self.assertEqual('0x1be78eaaf029930b9558cf58a6f7ee6aa7bb0848', result[0].get_erc20_to())
        self.assertEqual('WETH', result[0].get_erc20_symbol())

        with open('%s/../testdata/in_weth_out_erc20.bin' % os.path.dirname(__file__), mode='rb') as f:
          tx = pickle.load(f)

        result = ERC20Transfer.get_erc20_transfers(tx, ERC20Transfer.SEND)
        self.assertEqual(Decimal('0.105000179112250614'), result[0].get_erc20_amount())
        self.assertEqual('0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2', result[0].get_erc20_address())
        self.assertEqual('0xa288d96671f3b951de8c04a5dbaa9820651d2e09', result[0].get_erc20_from())
        self.assertEqual('0x1b9d2d38a43e29223e4716f49b48547820760a6a', result[0].get_erc20_to())
        self.assertEqual('WETH', result[0].get_erc20_symbol())

        result = ERC20Transfer.get_erc20_transfers(tx, ERC20Transfer.RECEIVE)
        self.assertEqual(Decimal('47880081009752.103915723'), result[0].get_erc20_amount())
        self.assertEqual('0x9f91d9f9070b0478abb5a9918c79b5dd533f672c', result[0].get_erc20_address())
        self.assertEqual('0x1b9d2d38a43e29223e4716f49b48547820760a6a', result[0].get_erc20_from())
        self.assertEqual('0xa288d96671f3b951de8c04a5dbaa9820651d2e09', result[0].get_erc20_to())
        self.assertEqual('CENT', result[0].get_erc20_symbol())

if __name__ == '__main__':
    unittest.main()
