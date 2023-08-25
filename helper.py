def read_int(message, options = None):
  while True:
    try:
      value = int(input(message))

      if options != None and value not in options:
        print("Valor não incluido nas opções.")
        continue

      return value
    except ValueError:
      print("Valor invalido.")