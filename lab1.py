# lab1.py/20 by maxrt101

class Farm:
  farm_count: int = 0

  __location = ''
  __animal_count = 0
  __vents_power = 0
  __area = 0
  __monthly_income = 0 
  __animal_species = [] 

  def __init__(self, location: str = "", animal_count: int = 0, vents_power: int = 0, area: int = 0, monthly_income: int = 0, animal_species: list[str] = []) -> None:
    self.__location = location
    self.__animal_count = animal_count
    self.__vents_power = vents_power
    self.__area = area
    self.__monthly_income = monthly_income
    self.__animal_species = animal_species
    Farm.farm_count += 1

  def __del__(self):
    Farm.farm_count -= 1

  def __str__(self) -> str:
    return f"Farm:\n  location: {self.__location}\n  animal count: {self.__animal_count}\n  vents power: {self.__vents_power}\n  area: {self.__area}\n  monthly income: {self.__monthly_income}\n  animal species: {self.__animal_species}"

  @classmethod
  def get_count(cls) -> int:
    return cls.farm_count


def main() -> None:
  farms: list[Farm] = [
    Farm("Lviv",     150, 400, 10000, 3000000, ["monkeys", "shraks"]),
    Farm("Kyiv",     250, 700, 20000, 4500000, ["cows", "rabbits"]),
    Farm("Ternopil", 100, 300, 7000,  2100000, ["pigs", "chickens"])
  ]
  for farm in farms:
    print(farm)


if __name__ == "__main__":
  main()

