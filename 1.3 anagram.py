def is_anagram(str1, str2):
  str1 = ''.join(sorted(str1.lower())).strip()
  str2 = ''.join(sorted(str2.lower())).strip()
  return str1 == str2

print(is_anagram('abcd e','dcbae'))