import socket
import sys
import select
from datetime import datetime as time
from xiangqi import XiangqiGame as Game

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

class GameSocket:
    """A base class for our client and server"""

    def __init__(self, port):
        """construct specify port to try to connect to"""
        self.sockfd = None
        self.port = port
        self.host = "127.0.0.1"
        self.address = (self.host, self.port)
        self.connection = None
        self.createSocket()
        self.game = None
        self.turn = False
        

    def createSocket(self):
        """create an IPv4 TCP socket"""
        self.sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0, None)


    def exit_connection(self):
        self.connection.close()
        self.connection = None
        sys.exit()

    def print_help(self):
         print("Welcome to Xiangqi central.")
         print("To learn how to play visit")
         print("https://en.wikipedia.org/wiki/Xiangqi")
         print("General   = \u265A")
         print("Adviser   = \u265D")
         print("Elephant  = \u252B")
         print("Horse     = \u265E")
         print("Chariot   = \u265C")
         print("Cannon    = \u25CE")
         print("Soldier   = \u265F")
         print("\n\n Enter commands as coordinates delimited by a comma")
         print("Example: a0,a1")
         print("The game initiator is player red")

    def run_input_loop(self):
        while self.connection:

            """
            For the idea of how to get around the blocking input call by including stdin in reads fd list
            Author: Pontus
            URL : https://stackoverflow.com/questions/1335507/keyboard-input-with-timeout
            """
            
            reads = [self.connection, sys.stdin]
            writes = [self.connection, sys.stdout]
            execs = []
            
            reads, writes, execs = select.select(reads, writes, execs, 10)
            if reads:
                if self.connection in reads and sys.stdout in writes:
                    self.receive()
                
            if writes:
                if sys.stdin in reads:
                    request = input("")
                    self.send(request)
                    

    def prompt(self):
        print("Type \\q to quit")
        print("Type \\h for directions")
        print("Type \\game to start a game")
        print("Type \\board to print the game board")

        
    def make_move(self, request):
         try:
             x, y = None, None
             x, y = request.split(",")

             if x and y:

                 if not self.turn:
                     print("Hey, it's not your turn")
                     return
                 alpha = [chr(x) for x in range(ord('a'), ord('i') + 1)]
                 nume = [str(x) for x in range(1, 11)]
                 if x[0] in alpha and y[0] in alpha and x[1] in nume and y[1] in nume:
                     if(self.game.make_move(x, y)):
                         print("Your move %s to %s" % (x, y))
                         self.game.victory_check()
                         print(self.game)
                         self.turn = False
                         
                         self.connection.send(request.encode())
                     else:
                         print("illegal move, try again")
                 else:
                     print("invalid move format, try again")
         except:
             self.connection.send(request.encode())

        
    def send(self, request):
        """encode message and send it over the socket fd"""
       
        if not request:
            return 
                    
        if request == "\q":
            self.connection.send(request.encode())
            print("terminating connection")
            self.exit_connection()
                
        elif request == "\h":
            self.print_help()
            return
            
        elif request == '\\board':
            print(self.game)
            return
            
        elif request == '\game':
            self.game = Game()
            print("You go first!\n\n")
            print(self.game)
            self.connection.send(request.encode())
            self.turn = True
            return 
        
        if self.game:
            self.make_move(request)
            return
            
        else:
            self.connection.send(request.encode())

                                
    def receive(self, size=1024):
        """receive response from the socket fd and decode them"""
        
        response = self.connection.recv(size).decode()

        if response == "\q":
            print("peer terminated connection")
            self.exit_connection()

        elif response == "\game":
            print("Your peer requested a new game of Xiangqi!")
            print("They will be going first")
            self.game = Game()
            print(self.game)
            self.turn = False


        else:
            try:
                x, y = response.split(",")
                alpha = [chr(x) for x in range(ord('a'), ord('i') + 1)]
                nume = [str(x) for x in range(1, 11)]
                if x[0] in alpha and y[0] in alpha and x[1] in nume and y[1] in nume:
                    self.game.make_move(x, y)
                    print("Your Opponent moved: %s to %s" % (x, y))
                    print(self.game)
                    self.turn = True
            except:
                now = time.now()
                print(">>>peer @%s:%s:%s ----> %s" % (now.hour, now.minute, now.second,response))
        
