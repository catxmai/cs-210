# Mancala Project
#### Project layout: MancalaGame(Game):

All functions required by Game interface are implemented. 
- State is represented by Struct in utils class.  
- Board is an n array, where `n = (SLOT_PER_PLAYER)*2 + 2.` In this report, `SLOT_PER_PLAYER = 6.`
- `utility` is the difference between the current player's mancala and their opponent.
- `eval` is ``((CONST_MANCALA*manc) + (CONST_STONE*stone)) * val`` where `manc` is number of stones in mancala, and `stone` is sum of stones not counting mancala, and `val=-1` if player is `MIN` and `val=1` if player is `MAX`. In this report, `CONST_MANCALA = .85` and `CONST_STONE = .15`

I set the `display` default of random player to `False` and commented out the `board.display` in the body of `play_game2`.

#### Win rate and average difference
Using `alpha_beta_player2` with `d` depth cutoff, and `n` number of matches, where `avg_diff` is average difference between mancala stones by the end of game, and `wr` is average winrate.

 * d=4, n=100, wr= 0.93, avg_diff= 18.56
 * d=5, n=100, wr= 0.96, avg_diff= 21.84
 * d=6, n=100, wr= 1.00, avg_diff= 24.1
 * d=7, n=50,  wr= 1.00, avg_diff= 23.68

Reaching d=7, each game takes about 17s so I only ran 50 games. 