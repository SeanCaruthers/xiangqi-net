from game import GameSocket


"""
     Author : Sean Caruthers

    Citations : The python socket documentation, python socket HOWTO and examples from chapter 2 of Networking a top down approach were used as references
    
    Socket HOWTO - 
    Author : Gordon McMillan, 
    URL : https://docs.python.org/3/library/socket.html#socket.AF_UNIX

    Python Socket Documentation
    Author : Python Software Foundation
    URL : https://docs.python.org/3/library/socket.html#socket.AF_UNIX

    Networking: A Top Down Approach
    Authors: James Kurose, Keith Ross
    C 2017, pearson
    URL: https://www.pearson.com/us/higher-education/program/Kurose-Computer-Networking-A-Top-Down-Approach-7th-Edition/PGM1101673.html

"""


class Client(GameSocket):
    """ a client for our chat game"""

    def __init__(self, port):
        """Build base socket and connect client"""
        super().__init__(port)
        self.player = "red"
        self.sockfd.connect(self.address)

        self.connection = self.sockfd

        if not self.connection:
            print("maybe you didn't start the server?")
            sys.exit()

        print("Connected at {0}".format(self.connection.getpeername()))
        self.prompt()
        self.run_input_loop()


if __name__ == "__main__":
    import sys

    port = int(sys.argv[1])
    client = Client(port)
