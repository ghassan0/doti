"""
Print [un]stow[-root] results.
"""


def print_results(counter):
    """Print results."""
    if counter[0] > 0:
        print("Total stowd to '~': " + str(counter[0]))
    if counter[1] > 0:
        print("Total unstowd from '~': " + str(counter[1]))
    if counter[2] > 0:
        print("Total stowd to '/': " + str(counter[2]))
    if counter[3] > 0:
        print("Total unstowd from '/': " + str(counter[3]))
    if counter[4] > 0:
        print("Total ingnored: " + str(counter[4]))
    if sum(counter) == 0:
        print("Nothing done")
