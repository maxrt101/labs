import unittest

from .. import ShoesManager, Shoes, ShoeType, Sneakers, Boots, FlipFlops

shoes = [
  Sneakers(10, 'Adidas'),
  FlipFlops(20, 'Adidas'),
  Sneakers(20, 'Nike'),
  Boots(10, 'Adidas'),
  Sneakers(30, 'Nike'),
  FlipFlops(17, 'Nike'),
  Boots(14, 'Adidas')
]

class FindTest(unittest.TestCase):
  def test_find_by_type(self):
    mngr = ShoesManager()
    mngr.add_shoes(shoes)

    for shoe_type in ShoeType:
      self.assertListEqual(mngr.find_by_type(shoe_type), [x for x in shoes if x.type == shoe_type])

  def test_find_by_size(self):
    mngr = ShoesManager()
    mngr.add_shoes(shoes)

    sizes = [x.size for x in shoes]

    for size in sizes:
      self.assertListEqual(mngr.find_by_size(size), [x for x in shoes if x.size == size])

