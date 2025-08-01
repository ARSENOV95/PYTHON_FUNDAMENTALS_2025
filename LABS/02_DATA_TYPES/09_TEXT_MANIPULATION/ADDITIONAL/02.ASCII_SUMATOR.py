start_intr,end_intr = input(),input()

loopup_string = input()

#converting the start and end intervals into ascii character code
start_index = ord(start_intr)
end_index = ord(end_intr)

charactes = [ord(char) for char in loopup_string if ord(char)> start_index and  ord(char) < end_index]

print(sum(charactes))

