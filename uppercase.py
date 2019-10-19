def uppercase(astring):
  
  i = 0
  count = 0

  for letter in astring:
    if letter == "." or letter == "," or letter == " ":
        continue
    if letter == letter.upper():
        count += 1
    i += 1 
    if i == 3:
        break

  if count != 0:
    return astring.upper()
  else:
    return astring