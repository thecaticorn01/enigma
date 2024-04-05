def caesar_cipher(text, shift, direction):
  Shifted = []
  for i in text:
    if i.isalpha():
      if direction == "encode":
        if i.isupper():
          Shifted.append(chr((ord(i) + shift - 65) % 26 + 65))
        elif i.islower():
          Shifted.append(chr((ord(i) + shift - 97) % 26 + 97))
      elif direction == "decode":
        if i.isupper():
          Shifted.append(chr((ord(i) - shift - 65) % 26 + 65))
        elif i.islower():
          Shifted.append(chr((ord(i) - shift - 97) % 26 + 97))
    elif i.isnumeric() and int(i) in range(1, 26):
        if direction == "encode":
          Shifted.append(chr(int(i) + shift + 64))
        elif direction == "decode":
          Shifted.append(chr(int(i) - shift + 90))
    else:
      raise ValueError("Invalid direction. Please choose 'encode' or 'decode'.")
  return "".join(Shifted)