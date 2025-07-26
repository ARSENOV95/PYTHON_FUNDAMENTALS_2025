pieces = {}

number_of_peaces = int(input())

for i in range(number_of_peaces):
    curr_piece = input()

    piece,composer,key = curr_piece.split('|')

    if piece not in pieces.keys():
        pieces[piece] = {}
    pieces[piece] = {'composer': composer,'key': key}

while (command:= input()) != 'Stop':
    parts = command.split('|')
    action,piece = parts[:2]

    match action:
        case 'Add':
            composer,key = parts[2:]
            if piece not in pieces.keys():
                pieces[piece] = {'composer':composer,'key':key}
                print(f"{piece} by {composer} in {key} added to the collection!")
            else:
                print(f"{piece} is already in the collection!" )
        case 'Remove':
            if piece in pieces.keys():
                del pieces[piece]
                print(f"Successfully removed {piece}!" )
            else:
                print(f"Invalid operation! {piece} does not exist in the collection." )
        case 'ChangeKey':
            new_key = parts[2]
            if piece in pieces.keys():
                pieces[piece]['key'] = new_key
                print(f"Changed the key of {piece} to {new_key}!" )
            else:
                print(f"Invalid operation! {piece} does not exist in the collection." )

for piece,attributes in pieces.items():
    print(f"{piece} -> Composer: {attributes['composer']}, Key: {attributes['key']}")