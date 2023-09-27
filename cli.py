#importing function from functions.py
import functions
import time

now = time.strftime("%D, %Y %H:%M:%S")
print(now)
while True:
    # Get user input and strip space characters from it.
    user_action = input("Type add,show,edit,complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo=user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos( )

        for index,item in enumerate(todos):
            item = item.strip('\n')
            row=f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            todos = functions.get_todos()

            new_todo = input("Enter the new_todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos((todos))

        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos( )
            todos.pop(number-1)

            functions.write_todos(todos)

        except IndexError:
            print("There is no item with that number!")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Command is not valid.")
print("Bye!")
