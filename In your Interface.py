class Teams:
    def __init__(self, members):
        self.__myTeam = members

    def __len__(self):
        return len(self.__myTeam)
    
    # 1a) Add the __contains__ protocol
    def __contains__(self, member):
        return member in self.__myTeam
    
    # 2a) Add the __iter__ protocol
    def __iter__(self):
        return iter(self.__myTeam)


def main():
    classmates = Teams(['John', 'Steve', 'Tim'])

    # 1b) show whether or not  'Tim' and 'Sam' are part of our team
    print('─' * 10) 
    possiblemember = ['Tim', 'Sam']
    
    print( "Are " + possiblemember[0] + " and " + possiblemember[1] + " part of our team?")
    
    for member in possiblemember:
        partofteam = classmates.__contains__(member)
        if partofteam:
            print ("Yes, " + member + " is a member.")
        else:
            print ("No, " + member + " is not a member.")
    
    # 2b) show how you can print each member of the classmates object
    print('─' * 10) 
    print ( "Who is part of our team?" )
    for classmate in classmates:
        classmates.__iter__()
        print(classmate)
    
    # 3) Determine if the class classmates implements the __len__ method.
    print( "How large is our team?" )
    print (len(classmates))
    print (classmates.__len__())
    
    """
    Classmates is not a class, but it is an object that references the class Teams.
    Teams implements that __len__ method which the object Classmates has referenced.
    """

    # 4) Explain the difference between interfaces and implementation.
    """
    Implementation is what the user does not need to know. This is the coding, classes, and methods in place to achieve a goal.
    Interface is what the user needs to know. Its job is to make it easier for the user to interact with the equipment or program to achieve the goal.
    """
    
    # 5) Think through the interface-implementation of a large scale storage system.
    # In many systems today, we have the ability to store information from a single application to a variety of storage devices
    # - local storage (hard drive, usb), the cloud and/or some new medium in the future.
    # How would you design an interface structure such that all of the possible implementations could store data effectively.
    """
    A class would be created with the attributes and behaviors that all data storage objects will pocess.
    Then, each type of storage device would be created as their own object in reference to the base class and modified with additional
    attributes and behaviors for their storage needs.
    
    Visual aid: https://drive.google.com/file/d/1r9n9HzUXc5Ad2GYy7wtJrl8Y8kx4YAbc/view?usp=sharing
    """
main()