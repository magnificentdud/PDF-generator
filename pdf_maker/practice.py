#class grammar

'''
Phone
: phone number
: cals
: messenger



class Phone:
    def __init__(self,number):
        self.number = number
    def call(self, to):
        print(to, '에게 전화를 겁니다')
    def send_message(self, to):
        print(to, '에게 문자를 보냈습니다')
  
class SmartPhone:
    def __init__(self,number):
        self.number = number
    def call(self, to):
        print(to, '에게 전화를 겁니다')
    def send_message(self, to):
        print(to, '에게 문자를 보냈습니다')
    def surf_internet(self):
        print('인터넷에 접속합니다')
    def kakao(self, to):
        print(to,'에게 카톡을 보냅니다')
    
  
p1 = SmartPhone('010-1234-5678')
p1.call('02-123-4567')
p1.send_message('010-3567-3928')
p1.kakao('Woochan')
p1.surf_internet()


#상속

class Phone:#부모 클래스
    def __init__(self,number):
        self.number = number
    def call(self, to):
        print(to, '에게 전화를 겁니다')
    def send_message(self, to):
        print(to, '에게 문자를 보냈습니다')
  
class SmartPhone(Phone):# 자식 클래스
    def __init__(self, number):
      super().__init__(number)
    def surf_internet(self):
        print('인터넷에 접속합니다')
    def kakao(self, to):
        print(to,'에게 카톡을 보냅니다')
    def game(self, to):
        print('게임',to,'에 접속합니다')
    
  
p1 = SmartPhone('010-1234-5678')
p1.call('02-123-4567')
p1.send_message('010-3567-3928')
p1.kakao('Woochan')
p1.surf_internet()
p1.game('배틀그라운드')

'''

#다른 class 를 attribute 로 가지는 class


class Phone:#부모 클래스
    def __init__(self,number):
        self.number = number
    def call(self, to):
        print(to, '에게 전화를 겁니다')
    def send_message(self, to):
        print(to, '에게 문자를 보냈습니다')

class radio:
  def __init__(self, hz, volume):
    self.hz = hz
    self.volume = volume

  def listen(self):
    print('현재 hz',self.hz)
    print('현재 volume', self.volume)

class SmartPhone(Phone):# 자식 클래스
    def __init__(self, number, hz, volume):
      super().__init__(number)
      
      self.radio = radio(hz, volume)
    def surf_internet(self):
        print('인터넷에 접속합니다')
    def kakao(self, to):
        print(to,'에게 카톡을 보냅니다')
    def game(self, to):
        print('게임',to,'에 접속합니다')
      
    
  
p1 = SmartPhone('010-1234-5678', 100, 0)
p1.call('02-123-4567')
p1.send_message('010-3567-3928')
p1.kakao('Woochan')
p1.surf_internet()
p1.game('배틀그라운드')
p1.radio.listen()