##############################################################################
#
# File:         driver.py
# Date:         Tue 11 Sep 2018  11:33
# Author:       Ken Basye
# Description:  Driver for testing bloxorz algorithms
#
##############################################################################

"""
Driver for testing bloxorz algorithms

"""

from bloxorz_problem import BloxorzProblem
from bloxorz import Board
import searchGeneric
from searchGeneric import AStarMultiPruneSearcher, AStarSearcher
import searchBFS
from searchBFS import BFSMultiPruneSearcher
import os
import glob
import pandas as pd

def searchTest(algo, board):
    bp0 = BloxorzProblem(board)
    if algo=="BFSMPP":
        searcher=BFSMultiPruneSearcher(bp0)
        result=searcher.search()
    elif algo=="A*":
        searcher=AStarSearcher(bp0)
        result = searcher.search(True)
    elif algo=="A*MPP":
        searcher=AStarMultiPruneSearcher(bp0)
        result = searcher.search(True)
    else:
        raise ValueError("invalid search algo")
    expansion=searcher.num_expanded
    return (result,expansion)

# def genStat(board, algo):


if __name__ == "__main__":
    board_names = glob.glob("boards/*.blx")
    # board_names = glob.glob("boards/cat.blx")
    exclude = ["ben","cat","mike","navid","rayyan","skyler","yu","zongyao"]
    exclude_names = ["boards\\"+i+".blx" for i in exclude]
    algo = ["BFSMPP", "A*", "A*MPP"]
    dftemp=[]
    for board_name in sorted(board_names):
        print("Loading board file %s" % (board_name,))
        with open(board_name) as file:
            board = Board.read_board(file)
        for alg in algo:
            res_len=""
            res_exp=""
            if board_name in exclude_names:
                print("For board %s, %s found no solution!" % (board_name,alg))
                res_len=-1
                res_exp=-1
                continue
            tup=searchTest(alg, board)
            res=tup[0]
            if res is None:
                print("For board %s, found no solution!" % (board_name,))
                res_len = -1
                res_exp = -1
                continue

            sequence = [arc.action for arc in res.arcs()]
            print("For board %s, %s found solution with length %d using %d expansions" % (board_name,alg, len(sequence),tup[1] ))
            if res_len!=-1:
                res_len=len(sequence)
            if res_exp!=-1:
                res_exp=tup[1]
            dftemp.append((board_name, alg, res_len, res_exp))
    # print(); print()
    pd.set_option('mode.chained_assignment', None)
    df=pd.DataFrame(dftemp, columns=['Name', 'Algo', 'Sln len', 'Sln expansion'])
    print(df)
    avg_exp = df.loc[df['Sln expansion'] != -1]
    for alg in algo:
        avg_exp_temp = df.loc[(df['Algo']==alg) & (df['Sln expansion']!=-1) & (df['Sln len']!=-1)]
        avg_exp[alg+" expansion/soln move"]=avg_exp_temp["Sln expansion"]/avg_exp_temp["Sln len"]
        print(avg_exp[alg+" expansion/soln move"].mean())
    print(avg_exp.to_html(index=False))






