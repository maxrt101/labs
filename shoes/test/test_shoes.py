import unittest

from .. import Shoes, ShoeType, Sneakers, Boots, FlipFlops


class ShoesTest(unittest.TestCase):
    def test_shoe(self):
        shoe = Shoes(ShoeType.WINTER, 44, "abibas")

        self.assertEqual(shoe.type, ShoeType.WINTER)
        self.assertEqual(shoe.size, 44)
        self.assertEqual(shoe.manufacturer, "abibas")

        str_must_contain = [str(shoe.type.name), str(shoe.size), str(shoe.manufacturer)]
        self.assertEqual(all(map(str(shoe).__contains__, str_must_contain)), True)

    def test_sneakers(self):
        sneakers = Sneakers(50, "nike")

        self.assertEqual(sneakers.size, 50)
        self.assertEqual(sneakers.manufacturer, "nike")

    def test_boots(self):
        boots = Boots(39, "some-company")

        self.assertEqual(boots.size, 39)
        self.assertEqual(boots.manufacturer, "some-company")

    def test_flip_flops(self):
        flip_flops = FlipFlops(41, "Hmelnytskiy Bazar Ltd")

        self.assertEqual(flip_flops.size, 41)
        self.assertEqual(flip_flops.manufacturer, "Hmelnytskiy Bazar Ltd")
