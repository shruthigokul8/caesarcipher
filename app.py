from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

class CaesarCipher:
    def __init__(self, shift, mod, alphabet, foreign_chars, letter_case):
        self.shift = shift
        self.mod = mod
        self.alphabet = alphabet.lower()
        self.foreign_chars = foreign_chars
        self.letter_case = letter_case

    def remove_foreign_chars(self, text):
        import re
        return re.sub(r'[^a-zA-Z0-9 ]', '', text)

    def apply_cipher(self, decode, text):
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
                result += self.alphabet[new_index].upper() if char.isupper() else self.alphabet[new_index]
            else:
                result += char
        return result

    def transform_case(self, text):
        if self.letter_case == "2":
            return text.lower()
        elif self.letter_case == "3":
            return text.upper()
        return text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cipher', methods=['POST'])
def cipher():
    data = request.json
    cipher = CaesarCipher(
        shift=int(data['shift']),
        mod=int(data['mod']),
        alphabet=data['alphabet'],
        foreign_chars=data['foreign_chars'],
        letter_case=data['letter_case']
    )
    result = cipher.apply_cipher(data['operation'], data['text'])
    result = cipher.transform_case(result)
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)


