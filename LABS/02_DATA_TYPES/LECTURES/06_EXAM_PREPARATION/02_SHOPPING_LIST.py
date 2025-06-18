def urgent_function(data, item):
    if item not in data:
        data.insert(0, item)


def process_command(data,command):
    command_parts = command.split()
    action = command_parts[0]

    if action == "Urgent":
        urgent_function(data, command_parts[1])

    elif action == "Unnecessary":
        if command_parts[1] in data:
            data.remove(command_parts[1])





def main():
    data = input().split()

    while True:
        command - input()

        if command == "Go Shopping!":
            break

        process_command(data,command)