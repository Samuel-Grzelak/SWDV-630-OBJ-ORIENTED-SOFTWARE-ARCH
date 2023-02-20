# Composite pattern example - Hotel Management System
# Hotel Staff List and Hierarchy

# Declare class for sub level employees (child/leaflets)

class DepartmentStaff:

	def __init__(self, *args):

        # assigns first positional argument to member variable "position"

		self.position = args[0]

	def showDetails(self):
        
        # print element's position

		print("\t", end ="")
		print(self.position)

# Declare class for department leads (parent/ branch)
class DepartmentHead:

	def __init__(self, *args):

        # assigns first positional argument to member variable "position"
        # initialize list of child elements

		self.position = args[0]
		self.children = []

	def add(self, child):

        # add specified child element to list

		self.children.append(child)

	def remove(self, child):

        # remove specified child element to list

		self.children.remove(child)

	def showDetails(self):

		# display department heads (parent/branch) and sub level employees (chile/leaflets)
		print(self.position)
		for child in self.children:
			print("\t", end ="")
			child.showDetails()


"""main method"""

if __name__ == "__main__":

    # instantiate department roles
	topOfList = DepartmentHead("General Manager")
	subListItem1 = DepartmentHead("Hotel Manager")
	subListItem2 = DepartmentHead("Restaraunt Manager")
	subListItem101 = DepartmentStaff("Receptionist")
	subListItem102 = DepartmentStaff("Housekeeper")
	subListItem201 = DepartmentStaff("Server")
	subListItem202 = DepartmentStaff("Cook")

    # add department roles under department leads
	subListItem1.add(subListItem101)
	subListItem1.add(subListItem102)
	subListItem2.add(subListItem201)
	subListItem2.add(subListItem202)

    # add department leads (and their sub list of roles) under general management
	topOfList.add(subListItem1)
	topOfList.add(subListItem2)

    # display hotel staff hierachy
	topOfList.showDetails()
