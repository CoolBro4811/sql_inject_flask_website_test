def caesar_encrypt(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            # Shift character within alphabet
            start = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - start + shift) % 26 + start)
        else:
            # Non-alphabet characters remain unchanged
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)  # Decrypt is just the inverse of encryption

# Example usage
if __name__ == "__main__":
    text = input("Enter text: ")
    shift = int(input("Enter shift value: "))
    
    encrypted = caesar_encrypt(text, shift)
    print(f"Encrypted: {encrypted}")
    
    decrypted = caesar_decrypt(encrypted, shift)
    print(f"Decrypted: {decrypted}")

