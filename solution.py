# Read a number from INPUT.TXT and write it unchanged to OUTPUT.TXT

with open('INPUT.TXT', 'r') as f:
    number = f.read().strip()

with open('OUTPUT.TXT', 'w') as f:
    f.write(number)
