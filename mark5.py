# from mark5_functions import get_todos, write_todos
from mytodoapp import mark5_functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_input = input("Add,Show,Edit,Complete or Exit: ")
    user_input = user_input.strip()

    if user_input.startswith('add'):
        todo = user_input[4:]

        todos = mark5_functions.get_todos()

        todos.append(todo + '\n')

        mark5_functions.write_todos(todos)

    elif user_input.startswith('show'):

        todos = mark5_functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            row = f"{index + 1}-{item.capitalize()}"
            print(row)

    elif user_input.startswith('edit'):
        try:
            number = int(user_input[5:])
            print(number)

            number = number - 1

            todos = mark5_functions.get_todos()

            new_item = input("Enter the new todo:")
            todos[number] = new_item + '\n'

            mark5_functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_input.startswith('complete'):
        try:
            number = int(user_input[9:])

            todos = mark5_functions.get_todos()

            number = number - 1
            todo_to_remove = todos[number].strip('\n')
            todos.pop(number)

            mark5_functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_input.startswith('exit'):
        break
    else:
        print("Command not valid")

print("bye")
