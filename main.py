from actions.close_program import CloseProgram
from actions.create_distributor import CreateDistributor
from actions.show_distributor import ShowDistributor
from actions.update_distributor import UpdateDistributor
from actions.delete_distributor import DeleteDistributor
from actions.show_product import ShowProduct
from actions.create_product import CreateProduct
from actions.update_product import UpdateProduct
from actions.delete_product import DeleteProduct
from actions.show_order import ShowOrder
from actions.update_order import UpdateOrder
from actions.create_order import CreateOrder
from actions.delete_order import DeleteOrder
import helper


def read_option():
  options = (
    { 'option': '0 - Sair', 'exec': CloseProgram.build() },
    # distributors CRUD
    { 'option': '1 - Ver distribuidor', 'exec': ShowDistributor.build() },
    { 'option': '2 - Criar distribuidor', 'exec': CreateDistributor.build() },
    { 'option': '3 - Atualizar distribuidor', 'exec': UpdateDistributor.build() },
    { 'option': '4 - Apagar distribuidor', 'exec': DeleteDistributor.build() },
    # products CRUD
    { 'option': '5 - Ver produto', 'exec': ShowProduct.build() },
    { 'option': '6 - Criar produto', 'exec': CreateProduct.build() },
    { 'option': '7 - Atualizar produto', 'exec': UpdateProduct.build() },
    { 'option': '8 - Apagar produto', 'exec': DeleteProduct.build() },
    # orders CRUD
    { 'option': '9 - Ver pedido', 'exec': ShowOrder.build() },
    { 'option': '10 - Criar pedido', 'exec': CreateOrder.build() },
    { 'option': '11 - Atualizar pedido', 'exec': UpdateOrder.build() },
    { 'option': '12 - Apagar pedido', 'exec': DeleteOrder.build() },
  )
  print()
  for option in options:
    print(option['option'])

  option_index = helper.read_int("Digite a opção: ", range(0, 13))
  return options[option_index]['exec']


while True:
  option = read_option()
  option.execute()