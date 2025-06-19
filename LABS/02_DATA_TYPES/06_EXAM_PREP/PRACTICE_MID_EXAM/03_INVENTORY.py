item_journal = input().split(", ") #intial input for items journal

while (command := input()) != "Craft!": #do a while loop until the entered command = Craft!
    action,items = command.split(" - ") #the command is split int otwo pars body and items 
    if ":" in items:  #if the command is Combine we need to addtinally split  the items strig int old and new 
        old_item,new_item  = items.split(":")

    if action == 'Collect':
        if items not in item_journal:
            item_journal.append(items)

    elif action == 'Drop':
        if items in item_journal:
            item_journal.remove(items)

    elif action == 'Combine Items':
        if old_item in item_journal: 
            item_position = item_journal.index(old_item)  #if combine we find the position of the item and iser the new item next to it
            item_journal.insert(item_position + 1,new_item)

    elif action == 'Renew':
        if items in item_journal:  #if we need to renew an item we find its inex dax,pop it and add it to the back
            item_position = item_journal.index(items)
            item_for_rewal = item_journal.pop(item_position)
            item_journal.append(item_for_rewal)

print(", ".join(item_journal))