# pacman-simulator
# IE Code Challenge 1 - Pacman Simulator
# Test data (example input and output)

# TestData1 ------
# PLACE 0,0,NORTH
# MOVE
# REPORT
# Output: 0,1,NORTH

# TestData2 ------
# PLACE 0,0,NORTH
# LEFT
# REPORT
# Output: 0,0,WEST

# TestData3 ------
# PLACE 1,2,EAST
# MOVE
# MOVE
# LEFT
# MOVE
# REPORT
# Output: 3,3,NORTH

# TestData4 (test that first valid command is PLACE command) ------
# REPORT
# Output: Invalid input

# TestData5 (test out of bounds coordinates) ------
# PLACE 1,2,NORTH
# PLACE 6,6,NORTH
# REPORT
# Output: 1,2,NORTH

# TestData6 (test out of bounds coordinates) ------
# PLACE 1,2,NORTH
# PLACE -1,-1,NORTH
# REPORT
# Output: 1,2,NORTH

# TestData7 ------
# PLACE 1,2,NORTH
# LEFT
# MOVE
# RIGHT
# MOVE
# MOVE
# LEFT
# REPORT
# Output: 0,4,WEST
