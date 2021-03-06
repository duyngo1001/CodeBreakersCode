  def evalRPN(self, tokens: List[str]) -> int:
      stack = []
      operations = {
          '+': lambda x, y: x + y,
          '-': lambda x, y: x - y,
          '*': lambda x, y: x * y,
          '/': lambda x, y: int(x / y)
      }
      for token in tokens:
          if token in operations:
              second, first = stack.pop(), stack.pop()
              result = operations[token](first, second)
              stack.append(result)
          else:
              stack.append(int(token))
      return stack.pop()
