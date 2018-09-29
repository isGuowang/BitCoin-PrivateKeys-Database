import bitcoin
import requests
from .btc_api import btcApi
from .models import Address


def balanceApi(address):
    data = address
    response = requests.get("https://blockchain.info/q/addressbalance/" + data).text

    return response


def KeyToAddress(key):

    private_key = str(key)
    decoded_private_key = bitcoin.decode_privkey(private_key.encode("utf-8"), 'hex')
    valid_private_key =  0 < decoded_private_key < bitcoin.N

    wif_encoded_private_key = bitcoin.encode_privkey(decoded_private_key, 'wif')
    keys =  wif_encoded_private_key

    public_key = bitcoin.fast_multiply(bitcoin.G, decoded_private_key)

    (public_key_x, public_key_y) = public_key
    if (public_key_y % 2) == 0:
        compressed_prefix = '02'
    else:
        compressed_prefix = '03'
    hex_compressed_public_key = compressed_prefix + bitcoin.encode(public_key_x, 16)

    address1 = bitcoin.pubkey_to_address(public_key)
    #address2 = bitcoin.pubkey_to_address(hex_compressed_public_key.encode("utf-8"))

    #balance1 = balanceApi(address1)
    #balance1 = btcApi(address1)
    #if balance1 ==None:
    #    balance1 = 0

    if Address.objects.filter(address=address1):
        balance = "可能有余额"

    else:
        balance = "没有"

    return keys, address1, balance