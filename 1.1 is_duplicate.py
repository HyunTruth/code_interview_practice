def is_duplicate(str):
  hash = {}
  for i in range(256):
    hash[i] = False
  for char in str:
    if hash[ord(char)] is True:
      return True
    if hash[ord(char)] is False:
      hash[ord(char)] = True
  return False


print(is_duplicate('abcda'))
