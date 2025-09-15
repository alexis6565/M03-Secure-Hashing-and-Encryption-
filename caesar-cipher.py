#caesar cipher tha encrypts and decrypts a given text
def caesar_cipher(text, shift, mode= 'encrypt'):    
    result = ""
    if mode == 'decrypt':
        shift = -shift #reverse the shift for decryption
    for char in text:
        if char.isalpha(): #check if character is a letter
            ascii_offset = ord('a') if char.islower() else ord('A')
            #shift the character and wrap around the alphabet using modulo operation
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char #non-alphabetic characters are added unchanged
    return result
# Example usage
text = "Hello, World!"  
shift = 3   

encrypted_text = caesar_cipher(text, shift, mode='encrypt')
print(f"Encrypted: {encrypted_text}")

decrypted_text = caesar_cipher(encrypted_text, shift, mode='decrypt')
print(f"Decrypted: {decrypted_text}")