from datetime import datetime


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

def read_date(message):
  time = None
  while time == None:
    try:
      time = datetime.strptime(input(message), "%d/%m/%Y")
    except ValueError:
      print("Valor invalido.")
  return time.date()

def confirm(message):
  while True:
    response = read_string(message)
    if response.upper() == "S":
      return True
    elif response.upper() == "N":
      return False
    else:
      print("A resposta deve ser S ou N.")


