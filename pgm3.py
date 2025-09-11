s = input("Enter a string:")
first_char =s[0]
rest = s[1:].replace(first_char,'$')
modified = first_char + rest
print("Modified String :", modified)