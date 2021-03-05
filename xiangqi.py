# Author - Sean Caruthers
# Date - 2/20/19 -- Updated on 3/3/21
# Description - A XiangqiGame emulator


# game variables to make sure that I don't spell anything incorrectly
RED = "RED"
BLACK = "BLACK"
GENERAL = "GENERAL"
ADVISER = "ADVISER"
ELEPHANT = "ELEPHANT"
HORSE = "HORSE"
CHARIOT = "CHARIOT"
CANNON = "CANNON"
SOLDIER = "SOLDIER"
UNFINISHED = 'UNFINISHED'
RED_VICTORY = 'RED_WON'
BLUE_VICTORY = 'BLUE_WON'
CAPTURED = 'CAPTURED'
red = "\u001b[31m"
blue = "\u001b[36m"
white = "\u001b[37m"


def convert_vector(vector, start):
    """A function for converting from a vector to board positions"""
    return chr(vector[0] + int(ord(start[0]))), vector[1] + start[1]


def create_board(chr1, chr2, int1, int2):
    """public method create board for creating game boards of any size"""
    # return the range 1 to n and alphanumeric range a to a maximum of z
    return [(chr(x), y)
            for x in range(int(ord(chr1)), int(ord(chr2)) + 1)
            for y in range(int1, int2 + 1)]


class XiangqiGame:
    """Our L0 game object"""

    def __init__(self):
        """Our class constructor"""

        # initialize the game state
        self._game_state = UNFINISHED

        # a coordinate template for our board
        self._coords = create_board('a', 'i', 1, 10)

        # setup the two players in the game
        self._red = Red(self._coords)
        self._black = Black(self._coords)

        self._turn = self._red

        # initialize the game board to none
        self._board = {}
        for coord in self._coords:
            self._board[coord] = None

        # setup the player pieces
        self.setup_red()
        self.setup_black()

    def __repr__(self):
        return self.get_game_state() + "\n" + self.string_board()
    

    def get_turn(self):
        """get function for the XiangqiGame's turn variables"""
        return self._turn

    def set_turn(self, value):
        """get function for the XiangqiGame's turn variables"""
        self._turn = value

    def get_game_state(self):
        """get function for the XiangqiGame's game_state variable"""
        return "game state = %s" % self._game_state

    def set_game_state(self, value):
        """set function for the XiangqiGame's game_state variable"""
        self._game_state = value

    def get_coords(self):
        """get function for the XiangqiGame's coords variable"""
        return self._coords

    def get_board(self):
        """get function for the XiangqiGame's board variable"""
        return self._board

    def get_red(self):
        """get function for the XiangqiGame's red player variable"""
        return self._red

    def get_black(self):
        """get function for the XiangqiGame's black player variable"""
        return self._black

    def get_pos(self, pos):
        """A function for getting the value at a position on our board"""
        try:
            return self.get_board()[pos]
        except KeyError:
            return None

    def set_pos(self, pos, value):
        """A function for setting the value at a position on our board"""
        try:
            self.get_board()[pos] = value
        except KeyError:
            return None

    def setup_red(self):
        """A function for initializing the black pieces on the board"""

        player = self.get_red()
        coord = ('e', 1)
        piece = General(player, coord)
        player.add_piece(piece)
        player.set_general(piece)
        self.set_pos(coord, piece)

        coord = ('f', 1)
        piece = Adviser(player, coord)
        player.add_piece(piece)
        self.set_pos(coord, piece)

        coord = ('d', 1)
        piece = Adviser(player, coord)
        player.add_piece(piece)
        self.set_pos(coord, piece)

        coord = ('c', 1)
        piece = Elephant(player, coord)
        player.add_piece(piece)
        self.set_pos(coord, piece)

        coord = ('g', 1)
        piece = Elephant(player, coord)
        player.add_piece(piece)
        self.set_pos(coord, piece)

        coord = ('b', 1)
        piece = Horse(player, coord)
        player.add_piece(piece)
        self.set_pos(coord, piece)

        coord = ('h', 1)
        piece = Horse(player, coord)
        player.add_piece(piece)
        self.set_pos(coord, piece)

        coord = ('a', 1)
        piece = Chariot(player, coord)
        player.add_piece(piece)
        self.set_pos(coord, piece)

        coord = ('i', 1)
        piece = Chariot(player, coord)
        player.add_piece(piece)
        self.set_pos(coord, piece)

        coord = ('b', 3)
        piece = Cannon(player, coord)
        player.add_piece(piece)
        self.set_pos(coord, piece)

        coord = ('h', 3)
        piece = Cannon(player, coord)
        player.add_piece(piece)
        self.set_pos(coord, piece)

        coord = ('a', 4)
        piece = Soldier(player, coord)
        player.add_piece(piece)
        self.set_pos(coord, piece)

        coord = ('c', 4)
        piece = Soldier(player, coord)
        player.add_piece(piece)
        self.set_pos(coord, piece)

        coord = ('e', 4)
        piece = Soldier(player, coord)
        player.add_piece(piece)
        self.set_pos(coord, piece)

        coord = ('g', 4)
        piece = Soldier(player, coord)
        player.add_piece(piece)
        self.set_pos(coord, piece)

        coord = ('i', 4)
        piece = Soldier(player, coord)
        player.add_piece(piece)
        self.set_pos(coord, piece)

    def setup_black(self):
        """A function for initializing the red pieces on the board"""
        player = self.get_black()
        coord = ('e', 10)
        piece = General(player, coord)
        player.add_piece(piece)
        player.set_general(piece)
        self.set_pos(coord, piece)

        coord = ('f', 10)
        piece = Adviser(player, coord)
        player.add_piece(piece)
        self.set_pos(coord, piece)

        coord = ('d', 10)
        piece = Adviser(player, coord)
        player.add_piece(piece)
        self.set_pos(coord, piece)

        coord = ('c', 10)
        piece = Elephant(player, coord)
        player.add_piece(piece)
        self.set_pos(coord, piece)

        coord = ('g', 10)
        piece = Elephant(player, coord)
        player.add_piece(piece)
        self.set_pos(coord, piece)

        coord = ('b', 10)
        piece = Horse(player, coord)
        player.add_piece(piece)
        self.set_pos(coord, piece)

        coord = ('h', 10)
        piece = Horse(player, coord)
        player.add_piece(piece)
        self.set_pos(coord, piece)

        coord = ('a', 10)
        piece = Chariot(player, coord)
        player.add_piece(piece)
        self.set_pos(coord, piece)

        coord = ('i', 10)
        piece = Chariot(player, coord)
        player.add_piece(piece)
        self.set_pos(coord, piece)

        coord = ('b', 8)
        piece = Cannon(player, coord)
        player.add_piece(piece)
        self.set_pos(coord, piece)

        coord = ('h', 8)
        piece = Cannon(player, coord)
        player.add_piece(piece)
        self.set_pos(coord, piece)

        coord = ('a', 7)
        piece = Soldier(player, coord)
        player.add_piece(piece)
        self.set_pos(coord, piece)

        coord = ('c', 7)
        piece = Soldier(player, coord)
        player.add_piece(piece)
        self.set_pos(coord, piece)

        coord = ('e', 7)
        piece = Soldier(player, coord)
        player.add_piece(piece)
        self.set_pos(coord, piece)

        coord = ('g', 7)
        piece = Soldier(player, coord)
        player.add_piece(piece)
        self.set_pos(coord, piece)

        coord = ('i', 7)
        piece = Soldier(player, coord)
        player.add_piece(piece)
        self.set_pos(coord, piece)

    def string_board(self):
        """A function for printing our board for debugging"""

        count = 0
        printer = self.get_board()
        board = ""
        x = 0
        y = 0
        board += "   "
        for x in range(1, 11):
            board += " %s  " % x
        board += "\n"
        for key in self.get_coords():
            if not count:
                board += " %s " % chr(ord("a") + y)
                y += 1
                
            count += 1
            if count == 10:
                if printer[key] is None:
                    board += " x \n"
                    count = 0
                else:
                    player = printer[key].get_owner().get_name()[:1]
                    piece = printer[key]
                    board += " %s \n" % (piece)
                    count = 0
            else:
                if printer[key] is None:
                    board += " x ,"
                else:
                    player = printer[key].get_owner().get_name()[:1]
                    piece = printer[key]
                    board += " %s ," % (piece)
            
        return board

    def print_board(self):
        """A function for printing our board for debugging"""

        count = 0
        printer = self.get_board()
        for key in self.get_coords():
            count += 1
            if count == 10:
                if printer[key] is None:
                    print(" x ")
                    count = 0
                else:
                    player = printer[key].get_owner().get_name()[:1]
                    piece = printer[key]
                    print("%s" % (piece))
                    count = 0
            else:
                if printer[key] is None:
                    print(" x ", end=",")
                else:
                    player = printer[key].get_owner().get_name()[:1]
                    piece = printer[key]
                    print(" %s " % (piece), end=",")

    def get_horse_blocks(self, piece, start):
        """A function that returns the blocked moves if a horse if blocked"""

        blocked = []
        count = 0

        # load the blocking positions from the horse class
        blockers = sorted(piece.get_blocks()*2)

        # iterate through blocking positions
        for vector in blockers:

            # if the blocking position is taken, add the necessary values to the blocked array
            if self.get_pos(convert_vector(vector, start)):
                new_vector = [0, 0]
                if vector[0] == 0:
                    if count % 2 == 0:
                        new_vector[0] = 1
                    else:
                        new_vector[0] = -1
                else:
                    new_vector[0] = vector[0] * 2
                if vector[1] == 0:
                    if count % 2 == 0:
                        new_vector[1] = 1
                    else:
                        new_vector[1] = -1
                else:
                    new_vector[1] = vector[1] * 2

                blocked.append(convert_vector(new_vector, start))
                count += 1

        return blocked

    def get_elephant_blocks(self, piece, start):
        """A function that returns the blocked moves if an elephant if blocked"""

        blocked = []
        count = 0

        # load the blocking positions from the elephant class
        blockers = sorted(piece.get_blocks()*2)

        # iterate through blocking positions
        for vector in blockers:

            # if the blocking position is taken, add the necessary values to the blocked array
            if self.get_pos(convert_vector):
                new_vector = [vector[0] * 2, vector[1] * 2]
                blocked.append(convert_vector(new_vector, start))
                count += 1

        return blocked

    def get_chariot_blocks(self, piece, start):
        """A function that returns the blocked moves if an chariot if blocked"""

        blocked = []

        # load the blocking positions into different quadrants
        pos_x = [x for x in piece.get_moves() if x[0] > 0]
        pos_y = [x for x in piece.get_moves() if x[1] > 0]
        neg_x = [x for x in piece.get_moves() if x[0] < 0]
        neg_y = [x for x in piece.get_moves() if x[1] < 0]

        # sort by absolute value
        neg_x = sorted(neg_x, key=lambda x: abs(x[0]))
        neg_y = sorted(neg_y, key=lambda x: abs(x[1]))

        # if a collision is detected, add pieces behind the collision to blocked
        for quadrant in [pos_x, pos_y, neg_x, neg_y]:
            collision = False
            for vector in quadrant:

                if collision:
                    blocked.append(convert_vector(vector, start))
                if self.get_pos(convert_vector(vector, start)):
                    collision = True

        return blocked

    def get_cannon_blocks(self, piece, start, capturing):
        """A function that returns the blocked moves if an cannon if blocked"""

        blocked = []

        # load the valid vectors into different quadrants
        pos_x = [x for x in piece.get_moves() if x[0] > 0]
        pos_y = [x for x in piece.get_moves() if x[1] > 0]
        neg_x = [x for x in piece.get_moves() if x[0] < 0]
        neg_y = [x for x in piece.get_moves() if x[1] < 0]

        # sort the negative vectors by absolute value
        neg_x = sorted(neg_x, key=lambda x: abs(x[0]))
        neg_y = sorted(neg_y, key=lambda x: abs(x[1]))

        # if a collision is detected, add pieces behind the collision to blocked
        if capturing:
            for quadrant in [pos_x, pos_y, neg_x, neg_y]:
                collision = 0
                for vector in quadrant:
                    if self.get_pos(convert_vector(vector, start)):
                        collision += 1
                        blocked.append(convert_vector(vector, start))
                    if collision == 2:
                        if convert_vector(vector, start) in blocked:
                            blocked.remove(convert_vector(vector, start))

        else:
            for quadrant in [pos_x, pos_y, neg_x, neg_y]:
                collision = False
                for vector in quadrant:
                    if self.get_pos(convert_vector(vector, start)):
                        collision = True
                    if collision:
                        blocked.append(convert_vector(vector, start))

        return blocked

    def general_eye_contact(self):
        """A function to test whether generals can see each other"""

        # start at the position of the red general and
        # iterate up on the y axis
        start = self.get_red().get_general().get_position()
        start = [start[0], start[1]]
        while (start[0], start[1]) in self.get_board():
            start[1] += 1

            # if the piece that is hit first is a general return true
            piece = self.get_pos((start[0], start[1]))
            if piece:
                if piece.get_name() == GENERAL:
                    return True
                else:
                    return False
        return False

    def find_valid_moves(self, piece, piece_2):
        """A function for finding the valid moves one turn out"""
        # find each pieces starting position and valid moves
        start = piece.get_position()

        # find the places that they could move to in one turn
        valid = [convert_vector(vector, start) for vector in piece.get_moves()
                 if convert_vector(vector, start) in piece.get_spaces()]

        # a variable to check if the piece is blocked
        blocked = []

        if piece.get_name() == HORSE:
            blocked = self.get_horse_blocks(piece, start)
        if piece.get_name() == ELEPHANT:
            blocked = self.get_elephant_blocks(piece, start)
        if piece.get_name() == CHARIOT:
            blocked = self.get_chariot_blocks(piece, start)
        if piece.get_name() == CANNON:
            blocked = self.get_cannon_blocks(piece, start, piece_2)

        return [x for x in valid if x not in blocked]

    def is_in_check(self, player):
        """A function to check whether the player is in check"""

        # set the player and the player who would check the other person
        if player.upper() == RED:
            player = self.get_red()
            checker = self.get_black()
        else:
            player = self.get_black()
            checker = self.get_red()

        # find the position of the player's general
        general = player.get_general().get_position()

        # iterate through the checker's pieces
        for piece in checker.get_pieces():

            # find the places that they could move to in one turn
            danger = self.find_valid_moves(piece, general)

            # if the general's position is within these places, return True
            if general in danger:

                return True

        # otherwise return false
        return False

    def victory_check(self):
        player = self.get_turn()
        if not self.is_in_check(player.get_name()):
            return False
        pieces = player.get_pieces()
        for piece in pieces:
            moves = piece.get_moves()
            for move in moves:
                start = piece.get_position()
                end = convert_vector(move, start)
                start = "".join([start[0], str(start[1])])
                end = "".join([end[0], str(end[1])])
                if self.validate_move(start, end):
                    return False
        return True

    def validate_move(self, start, end):
        """Our make move function, returns False if the move is not possible"""

        # Convert the string to coordinates
        start = (start[0], int(start[1:]))
        end = (end[0], int(end[1:]))

        # check if there if a piece at the start position
        piece = self.get_pos(start)
        piece2 = self.get_pos(end)

        # ensure that a piece exists at that position
        if not piece:
            return False

        # ensure that it is the turn of the piece's owner
        if piece.get_owner() != self.get_turn():
            return False

        if start not in piece.get_spaces() or end not in piece.get_spaces():
            return False

        # ensure that the end position is within the piece's valid moves
        if end not in self.find_valid_moves(piece, piece2):
            return False

        # if moving the piece puts the player in check, then cancel the move
        if self.is_in_check(piece.get_owner().get_name()) or self.general_eye_contact():
            return False

        # see if the second piece is a friendly piece
        if piece2:
            if piece2.get_owner() == piece.get_owner():
                return False

        return True

    def make_move(self, start, end):
        """Our make move function, returns False if the move is not possible"""

        # Convert the string to coordinates
        start = (start[0], int(start[1:]))
        end = (end[0], int(end[1:]))

        # check if there if a piece at the start position
        piece = self.get_pos(start)
        piece2 = self.get_pos(end)

        # ensure that a piece exists at that position
        if not piece:
            return False

        # ensure that it is the turn of the piece's owner
        if piece.get_owner() != self.get_turn():
            return False

        # check to see if the captured space holds a friendly piece
        if piece2:
            if piece2.get_owner() == piece.get_owner():
                return False

        if start not in piece.get_spaces() or end not in piece.get_spaces():
            return False

        # ensure that the end position is within the piece's valid moves
        if end not in self.find_valid_moves(piece, piece2):
            return False
        # if moving the piece puts the player in check, then cancel the move
        piece.set_position(end)
        self.set_pos(start, None)
        self.set_pos(end, piece)

        if self.is_in_check(piece.get_owner().get_name()) or self.general_eye_contact():
            self.set_pos(start, piece)
            if piece2:
                self.set_pos(end, piece2)
            else:
                self.set_pos(end, None)
                piece.set_position(start)
            return False

        # check if there is a piece at the end position
        if piece2:
            piece2.set_position(CAPTURED)
            piece2.get_owner().remove_piece(piece2)

        # update the board and remove the captured piece from the player's pieces
        piece.set_position(end)
        self.set_pos(end, piece)
        self.set_pos(start, None)

        # update the current turn
        if self.get_turn() == self.get_red():
            self.set_turn(self.get_black())
        else:
            self.set_turn(self.get_red())
       
        if self.victory_check():
            if self.get_turn() == self.get_red():
                self.set_game_state(BLUE_VICTORY)
            else:
                self.set_game_state(RED_VICTORY)

      

        return True


class Player:
    """Our player class"""
    def __init__(self, game_board):
        self._board = game_board
        self._pieces = []
        self._general = None

        # holder variables for the subclasses
        self._name = None
        self._side = None
        self._castle = None

    def get_general(self):
        """get function for the Player's general"""
        return self._general

    def set_general(self, value):
        """get function for the Player's general"""
        self._general = value

    def get_pieces(self):
        """get function for the Player's pieces list"""
        return self._pieces

    def add_piece(self, piece):
        """A function for adding pieces from the player's pieces list"""
        self.get_pieces().append(piece)

    def remove_piece(self, piece):
        """A function for adding pieces from the player's pieces list"""
        self.get_pieces().remove(piece)

    def get_name(self):
        """get function for the Player's name variable"""
        return self._name

    def get_board(self):
        """get function for the Player's board variable"""
        return self._board

    def get_side(self):
        """get function for the Player's side variable"""
        return self._side

    def get_castle(self):
        """get function for the Player's castle variable"""
        return self._castle


class Black(Player):
    """A class for Black players that inherits from the player class"""
    def __init__(self, *args):
        super().__init__(*args)
        self._name = BLACK

        # valid moves for elephants
        self._side = create_board("a", "i", 6, 10)

        # valid moves generals and advisers
        self._castle = create_board("d", "f", 8, 10)


class Red(Player):
    """A class for Red players that inherits from the player class"""

    def __init__(self, *args):
        """Our class constructor"""
        super().__init__(*args)
        self._name = RED

        # valid moves for elephants
        self._side = create_board("a", "i", 1, 5)

        # valid moves for generals and advisers
        self._castle = create_board("d", "f", 1, 3)


class Piece:
    """a class for Pieces"""

    def __init__(self, owner, position):
        """Our class constructor"""
        # name & moves are initialized in the sub classes
        self._name = None
        self._moves = None
        self._blocks = None
        self._owner = owner
        # spaces may be initialized in the sub classes
        self._spaces = self.get_owner().get_board()
        self._position = position

    def get_blocks(self):
        """get function for the Piece's spaces blocks"""
        return self._blocks

    def get_spaces(self):
        """get function for the Piece's spaces variable"""
        return self._spaces

    def get_moves(self):
        """get function for the Piece's moves variable"""
        return self._moves

    def get_owner(self):
        """get function for the Piece's owner variable"""
        return self._owner

    def get_name(self):
        """get function for the Piece's name variable"""
        return self._name

    def get_position(self):
        """get function for the Piece's position variable"""
        return self._position

    def set_position(self, value):
        """set function for the Piece's position variable"""
        self._position = value

    def __repr__(self):
        if self.get_owner().get_name() == RED:
            return red + self.character + white
        else:
            return blue +  self.character + white


class General(Piece):
    """A class for Generals that inherit from the Piece class"""

    def __init__(self, *args):
        """Our class constructor"""
        super().__init__(*args)
        self._name = GENERAL
        self.character =  "\u265A"

        # valid spots that the general can move within
        self._spaces = self.get_owner().get_castle()

        # our general's valid moves
        self._moves = [(x, 0) for x in range(-1, 2, 2)] + \
            [(0, y) for y in range(-1, 2, 2)]



class Adviser(Piece):
    """A class for Advisers that inherit from the Piece class"""

    def __init__(self, *args):
        """Our class constructor"""
        super().__init__(*args)
        self._name = ADVISER
        self.character =  "\u265D"
        

        # valid spots that the adviser can move within
        self._spaces = self.get_owner().get_castle()

        # our adviser's valid moves
        self._moves = [(x, y) for x in range(-1, 2, 2) for y in range(-1, 2, 2)]


class Elephant(Piece):
    """A class for Elephants that inherit from the Piece class"""

    def __init__(self, *args):
        """Our class constructor"""
        super().__init__(*args)
        self._name = ELEPHANT
        self.character =  "\u252B"

        # spaces that could block our elephant
        self._blocks = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

        # valid spots that the elephant can move within
        self._spaces = self.get_owner().get_side()

        # our elephant's valid moves
        self._moves = [(2*x, 2*y) for x in range(-1, 2, 2) for y in range(-1, 2, 2)]


class Horse(Piece):
    """A class for Horses that inherit from the Piece class"""

    def __init__(self, *args):
        """Our class constructor"""
        super().__init__(*args)
        self._name = HORSE
        self.character =  "\u265E"

        # spaces that could block our horse
        self._blocks = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # our horse's valid moves
        self._moves = [(2*x, y) for x in range(-1, 2, 2) for y in range(-1, 2, 2)] + \
            [(x, 2*y) for x in range(-1, 2, 2) for y in range(-1, 2, 2)]


class Chariot(Piece):
    """A class for Chariots that inherit from the Piece class"""

    def __init__(self, *args):
        """Our class constructor"""
        super().__init__(*args)
        self._name = CHARIOT
        self.character =  "\u265C"

        # valid spots that the chariot can move within
        self._spaces = self.get_owner().get_board()

        # our chariot's valid moves
        self._moves = [(x, 0) for x in range(-9, 9, 1)] + \
            [(0, y) for y in range(-10, 9, 1)]


class Cannon(Piece):
    """A class for Cannons that inherit from the Piece class"""

    def __init__(self, *args):
        """Our class constructor"""
        super().__init__(*args)
        self._name = CANNON
        self.character =  "\u25CE"
        

        # our cannon's valid moves
        self._moves = [(x, 0) for x in range(-9, 9, 1)] + \
            [(0, y) for y in range(-10, 9, 1)]


class Soldier(Piece):
    """A class for Soldiers that inherit from the Piece class"""

    def __init__(self, *args):
        """Our class constructor"""
        super().__init__(*args)
        self._name = SOLDIER
        self.character =  "\u265F"

        # ensure that the soldiers are moving in the correct direction
        if self.get_owner().get_name() == RED:
            self._moves = [(0, 1)]
        else:
            self._moves = [(0, -1)]

    def promote(self):
        """A function for promoting soldier pieces for greater movement"""

        # ensure that the soldiers are moving in the correct direction
        if self.get_owner().get_name() == RED:
            self._moves = [(0, 1), (1, 0), (-1, 0)]
        else:
            self._moves = [(0, -1), (1, 0), (-1, 0)]

    def set_position(self, value):
        """An overriding set_position function for pawns that allows promotion"""
        self._position = value
        if self._position not in self.get_owner().get_side():
            self.promote()


if __name__ == '__main__':
    game = XiangqiGame()
    move_result = game.make_move('a1', 'a2')
    print(game)
