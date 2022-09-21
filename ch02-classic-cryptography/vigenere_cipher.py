def decrypt(c, key):
    m = len(key)
    q, r = divmod(len(c), m)
    key_along = key * q + key[:r]
    p = ""

    for i in range(len(c)):
        p += chr((((ord(c[i]) - 65)-(ord(key_along[i]) - 65)) % 26) + 65)

    return p


def key_gen():
    # Hint: the plaintext starts with 'Y', since Ciphertext starts with 'D', first letter in the key should start with 'F'
    keys = []
    for i in range(26):
        for j in range(26):
            keys.append("F"+chr(65+i)+chr(65+j))
    return keys


if __name__ == "__main__":
    c = "DIHKCAFFYDGNIYVYWBSAEFNHQUGNIAX"
    keys = key_gen()
    for key in keys:
        print(f"key : {key} || plaintext : {decrypt(c, key)}")
    
    # key : FUN || plaintext : YOUFINALLYMADEITCONGRATULATIONS