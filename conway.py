class Conway(object):
    grid = [
        (0, 0, False), (0, 1, False), (0, 2, False),
        (1, 0, True), (1, 1, True), (1, 2, True),
        (2, 0, False), (2, 1, False), (2, 2, False)
    ]

    def get_list_of_neighbors(self, coordinate):
        the_list = []

        for cell in self.grid:
            last_column = max([x[1] for x in self.grid])
            right_column = 1
            if cell[1] > last_column:
                right_column = 0

            left_column = -1
            if cell[1] < 0:
                left_column = 0

            last_row = max([x[0] for x in self.grid])
            bottom_row = 1
            if cell[0] > last_row:
                bottom_row = 0
            top_row = -1
            if cell[0] < 0:
                top_row = 0

            # right
            if cell[0] == coordinate[0] and cell[1] == coordinate[1] + right_column:
                the_list.append(cell)
            # bottom right
            elif cell[0] == coordinate[0] + bottom_row and cell[1] == coordinate[1] + right_column:
                the_list.append(cell)
            # bottom
            elif cell[0] == coordinate[0] + bottom_row and cell[1] == coordinate[1]:
                the_list.append(cell)
            # bottom-left
            elif cell[0] == coordinate[0] + bottom_row and cell[1] == coordinate[1] + left_column:
                the_list.append(cell)
            # left
            elif cell[0] == coordinate[0] and cell[1] == coordinate[1] + left_column:
                the_list.append(cell)
            # top- left
            elif cell[0] == coordinate[0] + top_row and cell[1] == coordinate[1] + left_column:
                the_list.append(cell)
            # top
            elif cell[0] == coordinate[0] + top_row and cell[1] == coordinate[1]:
                the_list.append(cell)
            # top-right
            elif cell[0] == coordinate[0] + top_row and cell[1] == coordinate[1] + right_column:
                the_list.append(cell)
        return the_list

    def get_live_neighbor_count(self, coordinate):
        neighbors = self.get_list_of_neighbors(coordinate)
        return len([n for n in neighbors if n[2] == True])

    def get_cell(self, coordinate):
        for cell in self.grid:
            if cell[0] == coordinate[0] and cell[1] == coordinate[1]:
                return cell

    def determine_cell_life(self, coordinate):
        cell = self.get_cell(coordinate)
        lives = None
        if cell[2]:
            if self.get_live_neighbor_count(cell) < 2:
                lives = False
            elif self.get_live_neighbor_count(cell) <= 3:
                lives = True
            elif self.get_live_neighbor_count(cell) > 3:
                lives = False
        elif not cell[2] and self.get_live_neighbor_count(cell) == 3:
            lives = True

        # only return true or false if different from current status
        if lives != cell[2]:
            return lives

    def iterate(self):
        change_list = []
        for cell in self.grid:
            new_status = self.determine_cell_life(cell)
            if new_status is not None:
                change_list.append((cell[0], cell[1], new_status))

        for cell in enumerate(self.grid):
            for change_cell in change_list:
                if change_cell[0] == cell[1][0] and change_cell[1] == cell[1][1]:
                    self.grid[cell[0]] = change_cell

    def get_grid(self):
        output = ''
        for cell in sorted(self.grid, key=lambda c: str(c[0]) + str(c[1])):
            if cell[2] == True:
                output += 'x'
            else:
                output += str(' ')
            if cell[1] == max([x[1] for x in self.grid]):
                output += '\n'
        output = output[:-1]
        return output

