from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(text_to_manipulate, shift_amount, cipher_direction):
  manipulated_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in text_to_manipulate:
      if char not in alphabet:
        manipulated_text += char
      else:
        manipulated_text += alphabet[alphabet.index(char) + shift_amount]
  print(f"The {direction}d text is {manipulated_text}")

play_again = "yes"

while play_again == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26

  caesar(text_to_manipulate=text, shift_amount=shift, cipher_direction=direction)
  play_again = input("Type 'yes' to go again. Otherwise type 'no'\n").lower()
