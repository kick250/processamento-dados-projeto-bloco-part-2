from actions.close_program import CloseProgram
import helper


def read_option():
  options = (
    { 'option': '0 - Sair', 'exec': CloseProgram() },
    { 'option': '1 - Ver distribuidor', 'exec': CloseProgram() },
    { 'option': '2 - Criar distribuidor', 'exec': CloseProgram() },
    { 'option': '3 - Apagar distribuidor', 'exec': CloseProgram() },
    { 'option': '4 - Ver produto', 'exec': CloseProgram() },
    { 'option': '5 - Criar produto', 'exec': CloseProgram() },
    { 'option': '6 - Apagar produto', 'exec': CloseProgram() },
    { 'option': '7 - Ver pedido', 'exec': CloseProgram() },
    { 'option': '8 - Criar pedido', 'exec': CloseProgram() },
    { 'option': '9 - Apagar pedido', 'exec': CloseProgram() },
  )
  for option in options:
    print(option['option'])

  option_index = helper.read_int("Digite a opção: ", range(0, 10))
  return options[option_index]['exec']


while True:
  option = read_option()
  option.execute()