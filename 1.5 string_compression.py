def string_compression(string):
  buffer = None
  output = ''
  count = 1
  for char in string:
    if buffer is None:
      output += char
      buffer = char
    if char == buffer:
      count += 1
    else:
      output += str(count)
      output += char
      buffer = char
      count = 1
  output += str(count)

  if len(string) < len(output):
    return string

  return output

print(string_compression('aabbbbcccddaaa'))