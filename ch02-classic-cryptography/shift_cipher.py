def decrypt_shift_cipher(c):
    # capital alphabet -> range from 65 ~ 90
    for k in range(1, 26):
        print(f"shift key : {k}, plaintext : " + "".join(list(map(lambda x : chr((ord(x) - 65 + k) % 26 + 65), c))))


if __name__ == "__main__":
    c = "KZAXLAKWSKQXGJEWLGVWUJQHL"
    decrypt_shift_cipher(c)

    # shift key : 8, plaintext : SHIFTISEASYFORMETODECRYPT