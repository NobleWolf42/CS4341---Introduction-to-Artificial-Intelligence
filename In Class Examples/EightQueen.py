from search import *

def main():
    N = 8
    EightQueensProblem = NQueensProblem(N)
    initial_state = EightQueensProblem.initial
    print("Initial State: ", initial_state)
    print("Does it reach the goal state? ", EightQueensProblem.goal_test(initial_state))
    print("What action can be taken in the Column 1?", EightQueensProblem.actions(initial_state))
    print()

    new_state = EightQueensProblem.result(initial_state, 0)
    print("New State: ", new_state)
    print("Does it reach the goal state? ", EightQueensProblem.goal_test(new_state))
    print("What action can be taken in the Column 2?", EightQueensProblem.actions(new_state))
    print()

    new_state = EightQueensProblem.result(new_state, 6)
    print("Does it reach the goal state? ", EightQueensProblem.goal_test(new_state))
    print("What action can be taken in the Column 3?", EightQueensProblem.actions(new_state))
    print()

    new_state = EightQueensProblem.result(new_state, 4)
    print("Does it reach the goal state? ", EightQueensProblem.goal_test(new_state))
    print("What action can be taken in the Column 4?", EightQueensProblem.actions(new_state))
    print()

    new_state = EightQueensProblem.result(new_state, 7)
    print("Does it reach the goal state? ", EightQueensProblem.goal_test(new_state))
    print("What action can be taken in the Column 5?", EightQueensProblem.actions(new_state))
    print()

    new_state = EightQueensProblem.result(new_state, 1)
    print("Does it reach the goal state? ", EightQueensProblem.goal_test(new_state))
    print("What action can be taken in the Column 6?", EightQueensProblem.actions(new_state))
    print()

    new_state = EightQueensProblem.result(new_state, 3)
    print("Does it reach the goal state? ", EightQueensProblem.goal_test(new_state))
    print("What action can be taken in the Column 7?", EightQueensProblem.actions(new_state))
    print()

    new_state = EightQueensProblem.result(new_state, 5)
    print("Does it reach the goal state? ", EightQueensProblem.goal_test(new_state))
    print("What action can be taken in the Column 8?", EightQueensProblem.actions(new_state))
    print()

    new_state = EightQueensProblem.result(new_state, 2)
    print("Does it reach the goal state? ", EightQueensProblem.goal_test(new_state))
    print(EightQueensProblem.actions(new_state))

if __name__ == "__main__":
    main()