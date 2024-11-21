class helperClass:
    """
    Just a dummy class without a special meaning
    """
    def __init__(self, name="Nobody"):
        """
        The constructor where a name can be set. Default name: "Nobody"
        """
        self.name = name

    def hi(self):
        """ Greeting """
        print("Hi,", self.name)

    def bye(self):
        """" Bye """
        print("Bye,", self.name)

    def getName(self):
        """ Returns the name """
        return self.name

    def setName(self, new_name):
        """ Allows changing the name after instantiation """
        self.name = new_name