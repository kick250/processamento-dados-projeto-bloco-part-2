from actions.close_program import CloseProgram
from actions.create_distributor import CreateDistributor
from actions.show_distributor import ShowDistributor
import helper


def read_option():
  options = (
    { 'option': '0 - Sair', 'exec': CloseProgram.build() },
    { 'option': '1 - Ver distribuidor', 'exec': ShowDistributor.build() },
    { 'option': '2 - Criar distribuidor', 'exec': CreateDistributor.build() },
    { 'option': '3 - Apagar distribuidor', 'exec': CloseProgram.build() },
    { 'option': '4 - Ver produto', 'exec': CloseProgram.build() },
    { 'option': '5 - Criar produto', 'exec': CloseProgram.build() },
    { 'option': '6 - Apagar produto', 'exec': CloseProgram.build() },
    { 'option': '7 - Ver pedido', 'exec': CloseProgram.build() },
    { 'option': '8 - Criar pedido', 'exec': CloseProgram.build() },
    { 'option': '9 - Apagar pedido', 'exec': CloseProgram.build() },
  )
  print()
  for option in options:
    print(option['option'])

  option_index = helper.read_int("Digite a opção: ", range(0, 10))
  return options[option_index]['exec']


while True:
  option = read_option()
  option.execute()