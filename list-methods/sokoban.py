"""
Sokoban Action History Manager

This script prompts the user to perform actions (such as moving, undoing,
or restarting) and tracks the history of actions using a Python list.
It demonstrates basic list operations such as append, pop, and clear.
"""
def main():
    history = []
    while True:
        action = input("Action: ")
        if action == "undo":
            undone = history.pop()
            print(f"undone: '{undone}'")
        elif action == "restart":
            history.clear()
        else:
            history.append(action)
        print(history)
main()