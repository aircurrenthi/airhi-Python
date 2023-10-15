import string

def encrypt(text,encryDict):
    cipher = []
    for i in text:
        v = encryDict[i]
        cipher.append(v)
    return " ".join(cipher)

abc = string.printable[:-5]
subText = abc[-3:] + abc[:-3]
encry_dict = dict(zip(subText, abc))
print("列印編碼字典\n",encry_dict)

msg = "If the implementation is easy to expalain, it may be a good idea."
ciphertext = encrypt(msg,encry_dict)

print("原始字串 ",msg)
print("加密字串 ",ciphertext)