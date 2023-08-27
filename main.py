from actions.close_program import CloseProgram
from actions.create_distributor import CreateDistributor
from actions.show_distributor import ShowDistributor
from actions.delete_distributor import DeleteDistributor
from actions.show_product import ShowProduct
from actions.create_product import CreateProduct
from actions.delete_product import DeleteProduct
from actions.show_order import ShowOrder
from actions.create_order import CreateOrder
from actions.delete_order import DeleteOrder
import helper


def read_option():
  options = (
    { 'option': '0 - Sair', 'exec': CloseProgram.build() },
    { 'option': '1 - Ver distribuidor', 'exec': ShowDistributor.build() },
    { 'option': '2 - Criar distribuidor', 'exec': CreateDistributor.build() },
    { 'option': '3 - Apagar distribuidor', 'exec': DeleteDistributor.build() },
    { 'option': '4 - Ver produto', 'exec': ShowProduct.build() },
    { 'option': '5 - Criar produto', 'exec': CreateProduct.build() },
    { 'option': '6 - Apagar produto', 'exec': DeleteProduct.build() },
    { 'option': '7 - Ver pedido', 'exec': ShowOrder.build() },
    { 'option': '8 - Criar pedido', 'exec': CreateOrder.build() },
    { 'option': '9 - Apagar pedido', 'exec': DeleteOrder.build() },
  )
  print()
  for option in options:
    print(option['option'])

  option_index = helper.read_int("Digite a opção: ", range(0, 10))
  return options[option_index]['exec']


while True:
  option = read_option()
  option.execute()