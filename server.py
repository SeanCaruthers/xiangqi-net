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

    Python Select Documentation
    Author: https://docs.python.org/3/library/select.html
    URL : https://docs.python.org/3/library/select.html

    Networking: A Top Down Approach
    Authors: James Kurose, Keith Ross
    C 2017, pearson
    URL: https://www.pearson.com/us/higher-education/program/Kurose-Computer-Networking-A-Top-Down-Approach-7th-Edition/PGM1101673.html

"""


class Server(GameSocket):
    """A basic server class 

    lifecycle = socket->bind->listen->loop(accept->recv->send->close)

    """

    def __init__(self, port):
        """construct server and begin server lifecycle"""
        super().__init__(port)
        self.player = "blue"
        self.sockfd.bind(self.address)
        self.sockfd.listen(1)
        print("Listening at: {0}".format(self.address))

        while not self.connection:
            self.connection, address = self.sockfd.accept()

        print("Connected by: {0}".format(address))

        self.prompt()
        self.run_input_loop()
                    
        self.sockfd.close()


if __name__ == "__main__":
    import sys

    port = int(sys.argv[1])
    server = Server(port)
