class Player:
    X = 0
    Y = 0
    F = "NORTH"

player = Player()

# def start():
#     while True:
#         try:
#             command = input('enter command: ')
#             place, string = command.split(" ")
#             actual = string.split(",")
#             player.X = int(actual[0])
#             player.Y = int(actual[1])
#             player.F = actual[2]
#             if player.X < 0 or player.X > 4 or player.Y < 0 or player.Y > 4:
#                 raise ValueError #this will send it to the print message and back to the input option
#             break
#         except ValueError:
#             print("Invalid input")

def pacman():
    while True:
        try:
            command = input('enter command: ')
            place, string = command.split(" ")
            actual = string.split(",")
            player.X = int(actual[0])
            player.Y = int(actual[1])
            player.F = actual[2]
            if player.X < 0 or player.X > 4 or player.Y < 0 or player.Y > 4:
                raise ValueError #this will send it to the print message and back to the input option
            break
        except ValueError:
            print("Invalid input")
    flag = True
    while flag:
        if "PLACE" in command:
            place, string = command.split(" ")
            actual = string.split(",")
            checkx = int(actual[0])
            checky = int(actual[1])
            if 0 <= checkx <= 4 and 0 <= checky <= 4:
                player.X = int(actual[0])
                player.Y = int(actual[1])
                player.F = actual[2]
            else:
                player.X = player.X
                player.Y = player.Y
                player.F = player.F
            command = input('enter command: ')
        elif command == "MOVE":
            if player.F == "NORTH":
                player.Y = player.Y + 1
                command = input('enter command: ')
            elif player.F == "SOUTH":
                player.Y = player.Y - 1
                command = input('enter command: ')
            elif player.F == "EAST":
                player.X = player.X + 1
                command = input('enter command: ')
            elif player.F == "WEST":
                player.X = player.X - 1
                command = input('enter command: ')
            else:
                print('invalid command')
                flag = False
        elif command == "REPORT":
            print("Output:",player.X,",",player.Y,",",player.F)
            command = input('enter command: ')
        elif command == "RIGHT":
            if player.F == "NORTH":
                player.F = "EAST"
                command = input('enter command: ')
            elif player.F == "SOUTH":
                player.F = "WEST"
                command = input('enter command: ')
            elif player.F == "EAST":
                player.F = "SOUTH"
                command = input('enter command: ')
            elif player.F == "WEST":
                player.F = "NORTH"
                command = input('enter command: ')
            else:
                print('invalid command')
                flag = False
        elif command == "LEFT":
            if player.F == "NORTH":
                player.F = "WEST"
                command = input('enter command: ')
            elif player.F == "SOUTH":
                player.F = "EAST"
                command = input('enter command: ')
            elif player.F == "EAST":
                player.F = "NORTH"
                command = input('enter command: ')
            elif player.F == "WEST":
                player.F = "SOUTH"
                command = input('enter command: ')
            else:
                print('invalid command')
                flag = False
        elif command == "END":
            break
        else:
            continue


pacman()
