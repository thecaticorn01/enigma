import argparse
parser = argparse.ArgumentParser(description="Caesar Cipher")
parser.add_argument("text", help="The text to encode or decode")
parser.add_argument("shift", help="The shift value", type=int)
parser.add_argument("direction", help="The direction to encode or decode", choices=["encode", "decode"])
args = parser.parse_args()
Shifted = []
for i in args.text:
  if i.isalpha():
    if args.direction == "encode":
      if i.isupper():
        Shifted.append(chr((ord(i) + args.shift - 65) % 26 + 65))
      elif i.islower():
        Shifted.append(chr((ord(i) + args.shift - 97) % 26 + 97))
    elif args.direction == "decode":
      if i.isupper():
        Shifted.append(chr((ord(i) - args.shift - 65) % 26 + 65))
      elif i.islower():
        Shifted.append(chr((ord(i) - args.shift - 97) % 26 + 97))
  elif i.isnumeric() and int(i) in range(1, 26):
      if args.direction == "encode":
        Shifted.append(chr(int(i) + args.shift + 64))
      elif args.direction == "decode":
        Shifted.append(chr(int(i) - args.shift + 90))
print("".join(Shifted))