import games
import mancala
import time

def player_fn(game, state):
   return games.alphabeta_player2(game, state, mancala.eval, display=False)

def test1():
    game = mancala.MancalaGame()
    named_players = (("MAX", games.query_player_py_exp), ("MIN", games.query_player_py_exp))
    result = games.play_game2(game, named_players)
    print(result)
    return result

def test2():
    game = mancala.MancalaGame()
    named_players = (("MAX", games.query_player_py_exp), ("MIN", games.alphabeta_player))
    result = games.play_game2(game, named_players)
    print(result)
    return result

def test3():
    game = mancala.MancalaGame()
    named_players = (("MAX", player_fn), ("MIN", games.query_player_py_exp))
    result = games.play_game2(game, named_players)
    # print(result)
    return result

def test4():
    game = mancala.MancalaGame()
    named_players = (("MAX", player_fn), ("MIN", player_fn))
    result = games.play_game2(game, named_players)
    print(result)
    return result

if __name__ == '__main__':
    NUM_MATCH = 10
    win_count = 0
    delta = 0
    for i in range(0, NUM_MATCH):
        start = time.time()
        print(i)
        result = test3()
        if result["MAX"]>result["MIN"]:
            win_count+=1
            delta+=result["MAX"]
        stop = time.time()
        print(start-stop)

    print(f"winrate: {win_count/NUM_MATCH}")
    print(f"avf digg: {delta/NUM_MATCH}")
