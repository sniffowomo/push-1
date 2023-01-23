#!/usr/bin/env python3
'''
Base 64 image decoder taken from this link
https://www.geeksforgeeks.org/python-convert-image-to-string-and-vice-versa/
'''

import base64

file = open('encoder.bin', 'rb')
byte = file.read()
file.close()

decodeit = open('i.png', 'wb')
decodeit.write(base64.b64decode((byte)))
decodeit.close()
