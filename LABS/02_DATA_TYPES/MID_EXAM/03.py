def message_validity(message :str,hist :list)->bool:
    return message in hist


chat_history = []

while True:
    command = input()

    args = command.split()[1:]

    if command == "end":
        print("\n".join(chat_history))
        break

    if command.startswith("Chat"):
        text = args[0]
        chat_history.append(text)

    elif command.startswith("Delete"):
        text = args[0]

        if not message_validity(text,chat_history):
            continue

        chat_history.remove(text)

    elif command.startswith("Edit"):
        text = args[0]
        edited = args[1]

        if not message_validity(text,chat_history):
            continue

        index = chat_history.index(text)
        chat_history[index] = edited

    elif command.startswith("Spam"):
        chat_history.extend(args)


    elif command.startswith("Pin"):
        text = args[0]
        if not message_validity(text, chat_history):
            continue

        index = chat_history.index(text)
        pinned = chat_history.pop(index)
        chat_history.append(pinned)




