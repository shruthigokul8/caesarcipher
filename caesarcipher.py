class CaesarCipher:
    def __init__(self, shift, mod, alphabet, foreign_chars, letter_case):
        self.shift = shift
        self.mod = mod
        self.alphabet = alphabet.lower()
        self.foreign_chars = foreign_chars
        self.letter_case = letter_case

    def remove_foreign_chars(self, text):
        """Remove non-letter and non-digit characters."""
        import re
        return re.sub(r'[^a-zA-Z0-9 ]', '', text)

    def apply_cipher(self, decode, text):
        """Apply Caesar Cipher to the input text."""
        if decode == "decode":
            self.shift = -self.shift
        
        if self.foreign_chars == "1":
            text = self.remove_foreign_chars(text)
        
        result = ""
        for char in text:
            index = self.alphabet.find(char.lower())
            if index != -1:
                new_index = (index + self.shift) % self.mod
                if new_index < 0:
                    new_index += self.mod
                if char.isupper():
                    result += self.alphabet[new_index].upper()
                else:
                    result += self.alphabet[new_index]
            else:
                result += char
        
        return result

    def transform_case(self, text):
        """Transform the case of the output based on the letter_case setting."""
        if self.letter_case == "2":  # Lowercase
            return text.lower()
        elif self.letter_case == "3":  # Uppercase
            return text.upper()
        return text

def main():
    # Inputs to the cipher
    input_text = input("Enter text: ")
    option = input("Choose 'encode' or 'decode': ")
    shift_value = int(input("Enter shift value: "))
    modulo_value = int(input("Enter modulus value: "))
    alphabet_value = input("Enter alphabet (e.g. 'abcdefghijklmnopqrstuvwxyz'): ")
    letter_case_value = input("Choose case: 1 (default), 2 (lower), 3 (upper): ")
    foreign_chars_value = input("Remove foreign characters? Enter 1 for Yes, 0 for No: ")

    # Initialize the CaesarCipher
    cipher = CaesarCipher(
        shift=shift_value,
        mod=modulo_value,
        alphabet=alphabet_value,
        foreign_chars=foreign_chars_value,
        letter_case=letter_case_value
    )

    # Apply the cipher
    cipher_output = cipher.apply_cipher(option, input_text)
    cipher_output = cipher.transform_case(cipher_output)

    # Display the result
    print("Output:", cipher_output)

if __name__ == "__main__":
    main()
