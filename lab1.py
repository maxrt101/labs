# lab1.py/20 by maxrt101

class Farm:
  farm_count: int = 0

  def __init__(self, location: str = "", animal_count: int = 0, vents_power: int = 0, area: int = 0, monthly_income: int = 0, animal_species: list[str] = []) -> None:
    self.location = location
    self.animal_count = animal_count
    self.vents_power = vents_power
    self.area = area
    self.monthly_income = monthly_income
    self.animal_species = animal_species
    Farm.farm_count += 1

  def __del__(self):
    Farm.farm_count -= 1

  def __str__(self) -> str:
    return f"Farm({self.location}, {self.animal_count}, {self.vents_power}. {self.area}, {self.monthly_income}, {self.animal_species})"

  @classmethod
  def get_count(cls) -> int:
    return cls.farm_count


def main():
  farms: list[Farm] = [Farm("Lviv", 150, 400, 10000, 3000000, ["monkeys", "shraks"]), Farm("Kyiv", 250, 700, 20000, 4500000, ["cows", "rabbits"]), Farm("Ternopil", 100, 300, 7000, 2100000, ["pigs", "chickens"])]
  for farm in farms:
    print(farm)


if __name__ == "__main__":
  main()

