Implementing the Vigenère Cipher. 

It's a bit more complex than the Caesar Cipher and provides better security through the use of a keyword to shift letters.

How the Vigenère Cipher Works
Keyword: Unlike the Caesar Cipher which uses a single shift value, the Vigenère Cipher uses a keyword where each letter of the keyword represents a shift value.
Encryption Process:
Repeat the keyword so that it matches the length of the plaintext.
Shift each letter of the plaintext by the corresponding letter of the repeated keyword.
Decryption Process:
Reverse the process by shifting in the opposite direction using the keyword.
Example
Let's encrypt the word "HELLO" using the keyword "KEY".

Original Alphabet:

A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Keyword: "KEY"

Repeat to match the length of plaintext: "KEYKE"
Encryption:

H (shifted by K, which is 10) -> R
E (shifted by E, which is 4) -> I
L (shifted by Y, which is 24) -> J
L (shifted by K, which is 10) -> V
O (shifted by E, which is 4) -> S
Encrypted text: "RIJVS"
Decryption:

Reverse the process using the same keyword.
Implementing Vigenère Cipher in Python
Here’s a simple implementation of the Vigenère Cipher for both encryption and decryption:


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
Explanation of the Code
Keyword Repetition:

The keyword is repeated to match the length of the plaintext.
Encrypt and Decrypt:

For each character in the text, the corresponding shift value from the keyword is applied.
For encryption, the shift is added.
For decryption, the shift is subtracted.
ASCII Handling:

