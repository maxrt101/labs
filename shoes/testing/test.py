from ..manager import ShoesManager
from .. import ShoeType, Sneakers, Boots, FlipFlops

class ShoesTest:
  def __init__(self) -> None:
    pass

  def main(self) -> None:
    shop = ShoesManager()
    shop.add_shoes([
      Sneakers(10, 'Adidas'),
      FlipFlops(20, 'Adidas'),
      Sneakers(20, 'Nike'),
      Boots(10, 'Adidas'),
      Sneakers(30, 'Nike'),
      FlipFlops(17, 'Nike'),
      Boots(14, 'Adidas')
    ])

    print('Unsorted:\n\t', '\n\t'.join([str(x) for x in shop.shoes]), '\n')
    print('Sorted by size:\n\t', '\n\t'.join([str(x) for x in shop.sort_by_size(True)]), '\n')
    print('Sorted by type:\n\t', '\n\t'.join([str(x) for x in shop.sort_by_type()]), '\n')
    print('Sorted by manufacturer:\n\t', '\n\t'.join([str(x) for x in shop.sort_by_manufacturer()]), '\n')

    print('All sportwear sorted by size:\n\t',
          '\n\t'.join([str(x) for x in shop.sort_by_size(False, shop.find_by_type(ShoeType.SPORT))]),
          '\n')


