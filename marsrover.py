class Rover:
    def __init__(self, roverx, rovery, direction):
        directionmodularlist = ["N", "W", "S", "E"]
        self.roverx = roverx
        self.rovery = rovery
        self.direction = directionmodularlist.index(direction)
    
    def change_direction(self, direction):
        if direction == "L":
            self.direction += 1
        elif direction == "R":
            self.direction -= 1
    
    def move(self):
        #We use modular arithmetic to change our direction without having a massive for loop
        #that accounts for every switch, instead, turning left ticks up a number, and turning right
        #ticks down said number
        if self.direction % 4== 0:
            self.rovery += 1
        elif self.direction % 4 == 1:
            self.roverx -= 1
        elif self.direction % 4 == 2:
            self.rovery -= 1
        elif self.direction % 4 == 3:
            self.roverx += 1

        if self.rovery > mapy:
            self.rovery -= 1
        if self.rovery < 0:
            self.rovery += 1
        if self.roverx > mapx:
            self.roverx -= 1
        if self.roverx < 0:
            self.roverx += 1

    def __repr__(self):
        directionmodularlist = ["North", "West", "South", "East"]
        return "This rover is current at position (%s, %s) facing %s." %(self.roverx, self.rovery, directionmodularlist[self.direction])

rover1 = Rover(0, 0, "N")
rover2 = Rover(0, 0, "N")

mapsize = "5,9"

for i, character in enumerate(mapsize):
    if i == 0:
        mapx = int(character)
    if i == 2:
        mapy = int(character)

nasainput = "LRLRMMMMLRLRMMLRMRM"
for character in nasainput:
    if character == "M":
        rover1.move()
    else:
        rover1.change_direction(character)
print(rover1)



