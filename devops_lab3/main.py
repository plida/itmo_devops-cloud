def calculate(a, b, oper):
      try:
            a = int(a)
            b = int(b)
            if oper == "+":
                  return a + b
            if oper == "-":
                  return a - b
            if oper == "*":
                  return a * b
            if oper == "/" and b != 0:
                  return a / b
            return False
      except TypeError:
            return False


if __name__ == "__main__":
      a = input("Input a: ")
      b = input("Input b: ")
      oper = input("Input operation (+-*/): ")
      res = calculate(a, b, oper)
      if res:
            print(f"Result {a} {oper} {b} = {calculate(a, b, oper)}")
      else:
            print("ERR")
