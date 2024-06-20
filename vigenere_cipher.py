def vigenere_cipher(text, keyword, direction):
    result = ""
    keyword_repeated = (keyword * ((len(text) // len(keyword)) + 1))[:len(text)]
    
    for i in range(len(text)):
        if text[i].isalpha():
            ascii_offset = 65 if text[i].isupper() else 97
            shift = ord(keyword_repeated[i].lower()) - 97
            if direction == "decrypt":
                shift = -shift
            shifted = ((ord(text[i]) - ascii_offset + shift) % 26) + ascii_offset
            result += chr(shifted)
        else:
            result += text[i]
    
    return result

# Example usage
text = "HELLO, World!"
keyword = "KEY"
encrypted = vigenere_cipher(text, keyword, "encrypt")
decrypted = vigenere_cipher(encrypted, keyword, "decrypt")

print(f"Original text: {text}")
print(f"Encrypted text: {encrypted}")
print(f"Decrypted text: {decrypted}")
