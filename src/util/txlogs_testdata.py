from web3 import Web3,HTTPProvider,Contract
import sys
import os
import pickle
import json

settings = json.loads(open('%s/../settings.json' % os.path.dirname(__file__)).read())
web3 = Web3(HTTPProvider('https://mainnet.infura.io/v3/%s' % settings['infra_key']))
#web3 = Web3(HTTPProvider('https://mainnet.infura.io/v3/4dd320ab0cae40978f1e6419283c982d'))

def main():
  tx_hash = sys.argv[1].lower()
  #tx_detail = web3.eth.waitForTransactionReceipt(tx_hash)
  tx_detail = web3.eth.get_transaction(tx_hash)
  print(tx_detail)
  print(tx_detail.input)
  print(Contract.decode_function_input(tx_detail.input))
  with open('testdata.bin', mode='wb') as f:
    pickle.dump(tx_detail, f)


if __name__== '__main__':
    main()
