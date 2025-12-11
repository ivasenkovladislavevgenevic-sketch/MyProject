# Read input from INPUT.TXT
with open('INPUT.TXT', 'r') as f:
    number = f.read().strip()

# Write output to OUTPUT.TXT
with open('OUTPUT.TXT', 'w') as f:
    f.write(number)
