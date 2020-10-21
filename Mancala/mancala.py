import math
from utils import Struct
from games import Game


class MancalaGame(Game):
    MAX = "MAX"
    MIN = "MIN"
    VAL = {"MAX": 1, "MIN": -1}
    OPPOSITE = {"MAX": "MIN", "MIN": "MAX"}
    SLOT_PER_PLAYER = 6
    NUM_STONE = 4
    NUM_SLOT = (SLOT_PER_PLAYER * 2) + 2
    MAX_MANCALA = SLOT_PER_PLAYER
    MIN_MANCALA = NUM_SLOT - 1
    MAX_START = 0
    MIN_START = SLOT_PER_PLAYER + 1

    def __init__(self):
        self.board = [self.NUM_STONE] * self.NUM_SLOT
        self.board[self.MAX_MANCALA] = 0
        self.board[self.MIN_MANCALA] = 0
        self.moves = [i for i in range(0, self.NUM_SLOT)]
        self.initial = Struct(to_move=self.MAX, utility=0, board=self.board, moves=self.moves)

    def legal_moves(self, state):
        return state.moves

    def utility(self, state, player):
        """
        :return: the utitlity, which is the difference between the player's mancala and their opponent
        """
        if not self.terminal_test(state):
            return 0
        return self.utility_helper(state.board, player)


    def utility_helper(self, board, player):
        max_stones = board[self.MAX_MANCALA]
        min_stones = board[self.MIN_MANCALA]
        if player == self.MAX:
            return max_stones - min_stones
        else:
            assert (player == self.MIN)
            return min_stones - max_stones

    def to_move_utils(self, to_move):
        """
        helper fn to determine start and mancala given who to_move is
        """
        if to_move == self.MAX:
            start = self.MAX_START
            mancala = self.MAX_MANCALA
        else:
            assert (to_move == self.MIN)
            start = self.MIN_START
            mancala = self.MIN_MANCALA
        return start, mancala

    def make_move(self, move, state):
        """
        :param move: move 0-5 inclusive
        :param state: current state
        :return: new state after move is made
        """
        if move not in state.moves:
            return
        # print(state.to_move)

        board = state.board.copy()
        to_move = state.to_move
        start, mancala = self.to_move_utils(to_move)

        # 0-5 choice
        move_to = start + move
        stone_count = board[move_to]

        # picked up the stone and go counterclockwise
        board[move_to] = 0
        cycle = self.NUM_SLOT
        curr_pos = move_to + 1

        while stone_count > 0:
            # print(curr_pos)
            if (to_move == self.MAX and curr_pos == self.MIN_MANCALA) | \
                    (to_move == self.MIN and curr_pos == self.MAX_MANCALA):
                curr_pos += 1
            if curr_pos >= cycle:
                curr_pos = curr_pos - cycle
            board[curr_pos] += 1
            stone_count -= 1
            curr_pos += 1

        curr_pos -= 1

        # if board[curr_pos]==1 and not mancalas, meaning we just landed on empty slot
        if curr_pos != self.MIN_MANCALA and curr_pos != self.MAX_MANCALA and board[curr_pos] == 1:
            # determine which side this position is on based on game consts
            pos_side = self.MAX if math.ceil(curr_pos / self.SLOT_PER_PLAYER) == 1 else self.MIN
            opposite_index = self.SLOT_PER_PLAYER * 2 - curr_pos
            if pos_side == to_move and board[opposite_index] != 0:
                captures = board[curr_pos] + board[opposite_index]
                # print(f" cap {captures}")
                # print(f" curr pos {curr_pos}")
                # print(f" board cur {board[curr_pos]}")
                # print(f" opp i {opposite_index}")
                # print(f" curr manc {board[mancala]}")
                # print(f" board opp {board[opposite_index]}")
                board[mancala] += captures
                # print(" board",board[mancala])
                board[curr_pos] = 0
                board[opposite_index] = 0

        # if land on your mancala, go again
        if (to_move == self.MAX and curr_pos == self.MAX_MANCALA) | \
                (to_move == self.MIN and curr_pos == self.MIN_MANCALA):
            to_move = to_move
        else:
            to_move = self.OPPOSITE[to_move]

        # check to move
        start, mancala = self.to_move_utils(to_move)

        # next state
        moves = [i - start for i in range(start, mancala) if board[i] != 0]

        # check if terminal state, if so add all the remaining stones to the corresponding mancala
        maxs = self.sum_stones(board, self.MAX)
        mins = self.sum_stones(board, self.MIN)
        if maxs == 0 and mins != 0:
            board[self.MIN_MANCALA] += mins - maxs
            for i in range(self.MIN_START, self.MIN_MANCALA):
                board[i] = 0
        if mins == 0 and maxs != 0:
            board[self.MAX_MANCALA] += maxs - mins
            for i in range(self.MAX_START, self.MAX_MANCALA):
                board[i] = 0

        utility = self.utility_helper(board, to_move)
        new_state = Struct(to_move=to_move, utility=utility, board=board, moves=moves)
        return new_state

    def terminal_test(self, state):
        board = state.board
        return self.sum_stones(board, self.MAX)==0 or self.sum_stones(board, self.MAX)==0

    def to_move(self, state):
        return state.to_move

    def max_to_move(self, state):
        return state.to_move == self.MAX

    #sum of stones that are not in mancala
    def sum_stones(self, board, to_move):
        if to_move==self.MAX:
            return sum(board[self.MAX_START:self.MAX_MANCALA])
        else:
            assert(to_move==self.MIN)
            return sum(board[self.MIN_START:self.MIN_MANCALA])

    def display(self, state):
        board = state.board

        min_list = [board[i] for i in range(self.MIN_MANCALA - 1, self.MIN_START - 1, -1)]
        print(f"    {min_list}")
        print(f"{board[self.MIN_MANCALA]}                         {board[self.MAX_MANCALA]}")
        max_list = [board[i] for i in range(self.MAX_START, self.MAX_MANCALA)]
        print(f"    {max_list}")


def eval(game, state):
    to_move = state.to_move
    start, mancala = game.to_move_utils(to_move)
    board = state.board
    manc = board[mancala]
    stone = game.sum_stones(board,to_move)
    CONST_MANCALA = .85
    CONST_STONE = 1-CONST_MANCALA

    return ((CONST_MANCALA*manc) + (CONST_STONE*stone)) * game.VAL[to_move]

#
# test = Mancala()
# # test.display(test.initial)
# print(test.terminal_test(test.initial))
# # test.display(test.make_move(3, test.initial))
# one = test.make_move(3, test.initial)
# two = test.make_move(2, one)
# test.display(two)
# print(test.utility(two, -1))
