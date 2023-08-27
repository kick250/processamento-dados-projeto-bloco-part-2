def read_int(message, options = None, positive = False):
  while True:
    try:
      value = int(input(message))

      if options != None and value not in options:
        print("Valor não incluido nas opções.")
        continue

      if positive and value <= 0:
        print("Valor invalido.")
        continue

      return value
    except ValueError:
      print("Valor invalido.")

def read_float(message, options = None, positive = False):
  while True:
    try:
      value = float(input(message))

      if options != None and value not in options:
        print("Valor não incluido nas opções.")
        continue

      if positive and value <= 0:
        print("Valor invalido.")
        continue

      return value
    except ValueError:
      print("Valor invalido.")

def read_string(message, empty_valid = True):
  while True:
    value = input(message)

    if not empty_valid and len(value) == 0:
      print("Valor invalido.")
      continue

    return value