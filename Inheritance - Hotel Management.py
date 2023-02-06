class HotelRoom:
  def __init__(self, number, rent):
    self.number = number
    self.rent = rent
    
  def __str__(self):
    return self.number + ': $' + str(self.rent) + " per night" + '\n' + self.get_bookings()

  def get_bookings(self):
    return 'No bookings'

  def execute(self):
    print(self.number)

class Rm1(HotelRoom):
  def __init__(self):
    HotelRoom.__init__(self, 'Room 1', 100)

class Rm2(HotelRoom):
  def __init__(self):
    HotelRoom.__init__(self, 'Room 2', 150)
    
  def get_bookings(self):
    return 'March 1st, 2023 - March 3rd, 2023'

class Rm3(HotelRoom):
  def __init__(self):
    HotelRoom.__init__(self, 'Room 3', 120)
    
  def get_bookings(self):
    return 'April 1st, 2023 - April 3rd, 2023'
    
def room_info(room):
  print(room)

room = Rm1()
room.execute()
room_info(room)
room_info(Rm2())
room_info(Rm3())
    
