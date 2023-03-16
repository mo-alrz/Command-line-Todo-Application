import sys


def show_list_of_todos():
    """ function to see the list of todos """
    with open('todo.txt', 'r') as list_of_todos:
        lines = list_of_todos.readlines()
        for line in lines:
            print(str(lines.index(line) + 1) + ' - ' + line, end='')
        if len(lines) == 0:  # if it's empty it will print a message
            print("No todos for today! ")


def adding_a_task():
    """ function to add a task """
    with open('todo.txt', 'a') as add:
        add.write(str(' '.join(sys.argv[2:])) + "\n")


def removing_a_task(number_of_removing_task):
    """ function to remove a task """
    with open('todo.txt', 'r') as file_read:
        lines = file_read.readlines()
        ptr = 1
        with open('todo.txt', 'w') as file_write:
            for line in lines:
                if ptr != int(number_of_removing_task):
                    file_write.write(line)
                ptr += 1
    if number_of_removing_task > len(lines):
        print("Unable to remove: index is out of bound")


def completing_a_task(number_of_completed_task):
    """
    function to complete a task and show the list of
    all tasks and differentiate the completed ones
    """
    with open('todo.txt', 'r') as file:
        lines = file.readlines()
        if '[X]' not in lines[number_of_completed_task]:
            lines[number_of_completed_task] = "[X] - " + lines[number_of_completed_task]
    with open('todo.txt', 'w') as file:
        file.writelines(lines)
    show_list_of_todos()


if len(sys.argv) < 2:  # logic to see options when you run python todo.py
    print("\n$ todo"
          "\nCommand Line Todo application"
          "\n============================="
          "\n\nCommand line arguments:"
          "\n    -l   Lists all the tasks"
          "\n    -a   Adds a new task"
          "\n    -r   Removes a task,please write the task number"
          "\n    -c   Completes a task,please write the task number\n")

    exit()

if sys.argv[1] == '-l' and len(sys.argv) > 2:  # the need to be used only as -l
    print("Unable to see list, enter the -l without any other arguments")
    exit()

if sys.argv[1] == '-l':
    show_list_of_todos()

try:
    if sys.argv[1] == '-a' and sys.argv[2]:
        adding_a_task()
except IndexError:
    print("Unable to add: no task provided")

try:
    if sys.argv[1] == '-r' and sys.argv[2]:
        remove_task_number = int(sys.argv[2])
        removing_a_task(remove_task_number)
except IndexError:
    print("Unable to remove: no index provided")
except ValueError:
    print("Unable to remove: index is not a number")

try:
    if sys.argv[1] == '-c' and sys.argv[2]:
        complete_task_num = int(sys.argv[2]) - 1
        completing_a_task(complete_task_num)
except IndexError:
    print("Unable to remove: no index inside the range provided")
except ValueError:
    print("Unable to remove: index is not a number")
