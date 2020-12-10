# learnDT.py - Learning a binary decision tree
# AIFCA Python3 code Version 0.7.6 Documentation at http://aipython.org

# Artificial Intelligence: Foundations of Computational Agents
# http://artint.info
# Copyright David L Poole and Alan K Mackworth 2017.
# This work is licensed under a Creative Commons
# Attribution-NonCommercial-ShareAlike 4.0 International License.
# See: http://creativecommons.org/licenses/by-nc-sa/4.0/deed.en

from learnDT import DT_learner
from learnProblem import Data_set, Data_from_file


def test(data):
    """Prints errors and the trees for various evaluation criteria and ways to select leaves.
    """
    for crit in Data_set.evaluation_criteria:
        for leaf in ("mean", "median"):
            tree = DT_learner(data, to_optimize=crit, leaf_selection=leaf).learn()
            print("For", crit, "using", leaf, "at leaves, tree built is:", tree.__doc__)
            if data.test:
                for ecrit in Data_set.evaluation_criteria:
                    test_error = data.evaluate_dataset(data.test, tree, ecrit)
                    print("    Average error for", ecrit, "using", leaf, "at leaves is", test_error)


if __name__ == "__main__":
    test(data=Data_from_file('pima.txt', target_index=8))