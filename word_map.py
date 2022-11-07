class WordMap:
    def __init__(self, lines):
        self.map = lines
        self.find_start()
        self.num_rows = len(self.map)
        m = 0
        for line in self.map:
            m = max(m, len(line))
        self.num_cols = m
        for i in range(len(self.map)):
            d = self.num_cols - len(self.map[i])
            self.map[i] += " "*d
        self.directions = {(-1,0):'up', (1,0):'down', (0,-1):'left', (0,1):'right'}
        self.directions_keys = {'up':(-1,0), 'down':(1,0), 'left':(0,-1), 'right':(0,1)}

    def find_start(self):
        for i in range(len(self.map)):
            if self.map[i].find('@') >= 0:
                self.start = (i, self.map[i].find('@'))

    def neighbours(self, x, y, d=None):
        q = []
        priority = 1
        if y < self.num_cols-1:
            if d == 'right':
                q.append((1, (x, y+1)))
            else:
                priority+=1
                q.append((priority, (x, y+1)))
        if y > 0:
            if d == 'left':
                q.append((1, (x, y-1)))
            else:
                priority += 1
                q.append((priority, (x, y-1)))
        if x < self.num_rows-1:
            if d == 'down':
                q.append((1, (x+1, y)))
            else:
                priority += 1
                q.append((priority, (x+1, y)))
        if x > 0:
            if d == 'up':
                q.append((1, (x-1, y)))
            else:
                priority += 1
                q.append((priority, (x-1, y)))
        q.sort()
        return q

    def find_starting_direction(self):
        x, y = self.start
        n = self.neighbours(x, y)
        num_poss_dir = 0
        for el in n:
            i, j = el[1]
            if self.map[i][j] != " ":
                nx,ny = i-x,j-y
                num_poss_dir += 1
        if num_poss_dir == 0:
            return None
        elif num_poss_dir == 1:
            return self.directions[(nx,ny)]
        else:
            raise Exception("Can't find start")


    def get_direction(self, x1,y1,x2,y2):
        return self.directions[(x1-x2,y1-y2)]

    def traverse(self):
        path = '@'
        letters = ""
        visited = [self.start]
        current_x, current_y = self.start
        direction = self.find_starting_direction()
        possible_pos = self.neighbours(current_x, current_y, direction)
        while self.map[current_x][current_y] != "x":
            can_move = True
            if possible_pos[0][0] == 1:
                x,y = possible_pos[0][1]
                if possible_pos[0][1] not in visited and self.map[x][y] != " ":
                    path += self.map[x][y]
                    visited.append((x, y))
                    direction = self.get_direction(x,y,current_x, current_y)
                    current_x = x
                    current_y = y
                    can_move = False
            if can_move:
                for p in possible_pos:
                    x, y = p[1]
                    if p[1] not in visited and self.map[x][y] != " ":
                        path += self.map[x][y]
                        visited.append((x, y))
                        direction = self.get_direction(x,y,current_x, current_y)
                        current_x = x
                        current_y = y
            if can_move and possible_pos[0][1] in visited:
                current_x += self.directions_keys[direction][0]
                current_y += self.directions_keys[direction][1]
                path += self.map[current_x][current_y]
            possible_pos = self.neighbours(current_x, current_y, direction)
        for l in path:
            if l.isalpha() and l != 'x':
                letters += l
        return letters, path