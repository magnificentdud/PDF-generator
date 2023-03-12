#magic method 매직메소드(함수)

class CarDataset:
  def __init__(self):
    self.samples = ['KIA', 'HYUNDAI', 'BMW', 'TOYOTA', 'MERCEDES' ,'LAMBO','PORSCHE']
    
  def __len__(self):
    print('LEN MAGIC METHOD!')
    return len(self.samples)
    
  def __getitem__(self, idx):
    return self.samples[idx]

obj = CarDataset()

# print(obj.__len__())
print(len(obj))

elem = obj.__getitem__(1)
print(elem)

for elem in obj:
  print(elem)
  