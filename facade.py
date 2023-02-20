# Facade pattern example - Hotel Management System
# User booking a room

class SearchingRoom:
	# Subsystem # 1 - Search for a room that matches filter

	def search(self):
		print("Searching...")


class RequestingRoom:
	# Subsystem # 2 - Request to book a room

	def request(self):
		print("Requesting...")


class BookingRoom:
	# Subsystem # 3 - Inform guest whether booking was approved or denied

	def book(self):
		print("Your reservation request has been approved and booked!")


class RoomReservation:
	# Facade - Subsystems combined efforts to complete room reservation process

	def __init__(self):
		self.searching = SearchingRoom()
		self.requesting = RequestingRoom()
		self.booking = BookingRoom()

	def BookARoom(self):
		self.searching.search()
		self.requesting.request()
		self.booking.book()

#  main method 
if __name__ == "__main__":

	roomReservation = RoomReservation()
	roomReservation.BookARoom()
