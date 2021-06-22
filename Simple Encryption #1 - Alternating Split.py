def decrypt(encrypted_text, n):
    # for None and ''
    if not encrypted_text: return encrypted_text

    mid = len(encrypted_text) // 2
    for _ in range(n):
        arr1 = encrypted_text[:mid]
        arr2 = encrypted_text[mid:]
        encrypted_text = ''.join([arr2[i] + arr1[i] for i in range(len(arr1))]) + ('', arr2[-1])[len(encrypted_text) % 2 == 1]
        '''
        encrypted_text = ''.join([  \
            encrypted_text[i // 2 + ((0,-mid) [i % 2 == 0])] \
            for i, j in enumerate(encrypted_text)])
        '''
    return encrypted_text            
        


def encrypt(text, n):
    # for None and ''
    if not text: return text

    for _ in range(n):
        text = text[1::2] + text[::2]
        '''
        text = ''.join(  \
            [j for i, j in enumerate(text) if i % 2 == 1] + \
            [j for i, j in enumerate(text) if i % 2 == 0] \
            )
        '''
    return text

a = encrypt('This is a test!', 1)
b = decrypt(a, 1)
print(*(a, b), sep = '\n')


'''
test.assert_equals(encrypt("This is a test!", 0), "This is a test!")
test.assert_equals(encrypt("This is a test!", 1), "hsi  etTi sats!")
test.assert_equals(encrypt("This is a test!", 2), "s eT ashi tist!")
test.assert_equals(encrypt("This is a test!", 3), " Tah itse sits!")
test.assert_equals(encrypt("This is a test!", 4), "This is a test!")
test.assert_equals(encrypt("This is a test!", -1), "This is a test!")
test.assert_equals(encrypt("This kata is very interesting!", 1), "hskt svr neetn!Ti aai eyitrsig")

test.assert_equals(decrypt("This is a test!", 0), "This is a test!")
test.assert_equals(decrypt("hsi  etTi sats!", 1), "This is a test!")
test.assert_equals(decrypt("s eT ashi tist!", 2), "This is a test!")
test.assert_equals(decrypt(" Tah itse sits!", 3), "This is a test!")
test.assert_equals(decrypt("This is a test!", 4), "This is a test!")
test.assert_equals(decrypt("This is a test!", -1), "This is a test!")
test.assert_equals(decrypt("hskt svr neetn!Ti aai eyitrsig", 1), "This kata is very interesting!")

test.assert_equals(encrypt("", 0), "")
test.assert_equals(decrypt("", 0), "")
test.assert_equals(encrypt(None, 0), None)
test.assert_equals(decrypt(None, 0), None)
'''
#hsi  etTi sats!
# [-8, 0, -7, 1, -6, 2, -5, 3, -4, 4, -3, 5, -2, 6, -1]

#s eT ashi tist!

# 15 len 
'''
if len(text) is pair so odd and pair leeter is equal and 
first leeter in position len(text) // 2
'''


''' 
This is a test!
#hsi  etTi sats
'''