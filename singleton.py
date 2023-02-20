# Singleton pattern example - Hotel Management System
# House Keeping - Room State (Available (default), Dirty, Clean, or Out of Order)

# Declare parent class for hotel rooms 
class Room:

	# state shared by each instance
	__shared_state = dict()

	# constructor method
	def __init__(self):

		self.__dict__ = self.__shared_state
		self.state = 'Available'

	def __str__(self):

		return self.state

# Decalre class for each hotel room as a child of Room
# Hotel Room # 001
class Room_001(Room):
    pass

# main method
if __name__ == "__main__":
    
    print(Room_001()) # Output: Available

    # Three HouseKeeper instances created that have access to the shared state of Room # 001
    HouseKeeper1 = Room_001()
    HouseKeeper2 = Room_001() 
    HouseKeeper3 = Room_001() 

    HouseKeeper1.state = 'Clean'    #changed the shared state
    HouseKeeper2.state = 'Dirty'    #changed the shared state

    print(HouseKeeper1) # Output: Dirty
    print(HouseKeeper2) # Output: Dirty

    HouseKeeper3.state = 'Out of order' # changed the shared state

    print(HouseKeeper1) # Output: Out of order
    print(HouseKeeper2) # Output: Out of order
    print(HouseKeeper3) # Output: Out of order
