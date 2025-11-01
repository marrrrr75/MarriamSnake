class Snake:
    def __init__(self, start_pos):
        self.body = [start_pos]
        self.direction = 0
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.alive = True

    def move(self, ms_size):
        if not self.alive:
            return
        new_pos = (self.body[0][0] + self.directions[self.direction][0],
                   self.body[0][1] + self.directions[self.direction][1])
        if not (0 <= new_pos[0] < ms_size[0] and 0 <= new_pos[1] < ms_size[1]) \
           or new_pos in self.body:
            self.alive = False
        else:
            self.body.insert(0, new_pos)
            self.body.pop(-1)

    def grow(self):
        self.body.append(self.body[-1])
