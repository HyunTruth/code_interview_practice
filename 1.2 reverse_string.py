def reverse_string(str):
  stack = list(str)
  result = []
  while len(stack) > 0:
    result.append(stack.pop())
  return ''.join(result)


print(reverse_string('abcde'))
