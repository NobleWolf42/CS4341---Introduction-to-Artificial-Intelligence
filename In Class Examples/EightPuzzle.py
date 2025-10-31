from search import *

def main():
    initial_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    goal_state = (8, 7, 6, 5, 4, 3, 2, 1, 0)
    print("Initial State: ", initial_state)
    print("Goal State: ", goal_state)
    print()

    eightPuzzle = EightPuzzle(initial_state, goal_state)

    print("Index at the blank space: ", eightPuzzle.find_blank_square(initial_state))
    print("Is this state solvable? ", eightPuzzle.check_solvability(initial_state))
    print("Does it reach the goal state? ", eightPuzzle.goal_test(initial_state))
    print("Possible actions can be taken: ", eightPuzzle.actions(initial_state))
    print()

    new_state = eightPuzzle.result(initial_state, 'LEFT')
    print("New State: ", new_state)
    print("Index at the blank space: ", eightPuzzle.find_blank_square(new_state))
    print("Is this state solvable? ", eightPuzzle.check_solvability(new_state))
    print("Does it reach the goal state? ", eightPuzzle.goal_test(new_state))
    print("Possible actions can be taken: ", eightPuzzle.actions(new_state))
    print()

    new_state = eightPuzzle.result(new_state, 'UP')
    print("New State: ", new_state)
    print("Index at the blank space: ", eightPuzzle.find_blank_square(new_state))
    print("Is this state solvable? ", eightPuzzle.check_solvability(new_state))
    print("Does it reach the goal state? ", eightPuzzle.goal_test(new_state))
    print("Possible actions can be taken: ", eightPuzzle.actions(new_state))

if __name__ == "__main__":
    main()