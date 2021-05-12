def convertTextToBin(text):
    return ''.join(format(ord(x), 'b').zfill(8) for x in text)

def convertTextToBigInt(text):
    text_as_bin = convertTextToBin(text)
    return int(text_as_bin, 2)

def convertBigIntToText(num):
    num_as_bin = bin(num)[2:]
    text = ''
    while num_as_bin != '':
        last_8_bit = num_as_bin[-8:]
        num_as_bin = num_as_bin[:-8]
        text += chr(int(last_8_bit, 2))
    return text[::-1]