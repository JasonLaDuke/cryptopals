import binascii


hex_string = "49276d206b696c6c696e6720796f75722062726" \
             "1696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"


def hex_to_base64(hex_string):
    base64_string = binascii.b2a_base64(bytearray.fromhex(hex_string), newline=False)
    return base64_string

print(hex_to_base64(hex_string))
