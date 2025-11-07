def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if 'a' <= char <= 'z':
            decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            plaintext += decrypted_char
        elif 'A' <= char <= 'Z':
            decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

cipher = "odroboewscdrolocdcwkbdmyxdbkmdzvkdpybwyeddrobo"

print("Caesar Cipher using Brute Force\n")
for key in range(1, 26):
    decrypted_text = caesar_decrypt(cipher, key)
    print(f"Key = {key:02}: {decrypted_text}\n")
