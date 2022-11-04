class Animal:
  def __init__(self, name, species):
    self.name = name
    self.species = species

  def greeting(self):
    print('こんにちは、私の名前は' + self.name + 'です')

tiger = Animal('ココ', '虎')

print(tiger.species)
tiger.greeting()