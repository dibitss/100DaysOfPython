from subprocess import call
import os

from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def clear():
    _ = call('clear' if os.name =='posix' else 'cls')
    print(logo)

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char.isalpha():
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position % len(alphabet)]
    else: 
        end_text += char
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

run_again = "yes"
while run_again == "yes":
    clear()
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    run_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")