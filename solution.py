# Non-deaf telephone problem solution
# Read a number from INPUT.TXT and write it to OUTPUT.TXT unchanged

with open('INPUT.TXT', 'r') as f:
    number = f.read().strip()

with open('OUTPUT.TXT', 'w') as f:
    f.write(number)
