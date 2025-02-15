"""
import random

class Minesweeper:
    def __init__(self, height=8, width=8, mines=8):
        self.height = height
        self.width = width
        self.mines = set()
        self.board = [[False for _ in range(width)] for _ in range(height)]
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True
        self.mines_found = set()

    def print(self):
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                print("|X" if self.board[i][j] else "| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        count = 0
        for i in range(cell[0]-1, cell[0]+2):
            for j in range(cell[1]-1, cell[1]+2):
                if (i, j) == cell:
                    continue
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1
        return count

    def won(self):
        return self.mines_found == self.mines

class Sentence:
    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        return set(self.cells) if len(self.cells) == self.count else set()

    def known_safes(self):
        return set(self.cells) if self.count == 0 else set()

    def mark_mine(self, cell):
        if cell in self.cells:
            self.cells.remove(cell)
            self.count -= 1

    def mark_safe(self, cell):
        if cell in self.cells:
            self.cells.remove(cell)

class MinesweeperAI:
    def __init__(self, height=8, width=8):
        self.height = height
        self.width = width
        self.moves_made = set()
        self.mines = set()
        self.safes = set()
        self.knowledge = []

    def mark_mine(self, cell):
        if cell not in self.mines:
            self.mines.add(cell)
            for sentence in self.knowledge:
                sentence.mark_mine(cell)

    def mark_safe(self, cell):
        if cell not in self.safes:
            self.safes.add(cell)
            for sentence in self.knowledge:
                sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        self.moves_made.add(cell)
        self.mark_safe(cell)

        neighbors = set()
        known_mines = 0
        for i in range(cell[0]-1, cell[0]+2):
            for j in range(cell[1]-1, cell[1]+2):
                if (i, j) == cell:
                    continue
                if 0 <= i < self.height and 0 <= j < self.width:
                    if (i, j) in self.safes:
                        continue
                    if (i, j) in self.mines:
                        known_mines += 1
                    else:
                        neighbors.add((i, j))

        new_count = count - known_mines
        if neighbors:
            new_sentence = Sentence(neighbors, new_count)
            if new_sentence not in self.knowledge:
                self.knowledge.append(new_sentence)

        changed = True
        while changed:
            changed = False
            safe_copy = self.safes.copy()
            mine_copy = self.mines.copy()

            for sentence in self.knowledge.copy():
                if not sentence.cells:
                    self.knowledge.remove(sentence)
                    continue

                safes = sentence.known_safes().copy()
                for safe in safes:
                    if safe not in safe_copy:
                        self.mark_safe(safe)
                        changed = True

                mines = sentence.known_mines().copy()
                for mine in mines:
                    if mine not in mine_copy:
                        self.mark_mine(mine)
                        changed = True

            for sentence1 in self.knowledge.copy():
                for sentence2 in self.knowledge.copy():
                    if sentence1 == sentence2:
                        continue
                    if sentence1.cells.issubset(sentence2.cells):
                        new_cells = sentence2.cells - sentence1.cells
                        new_count = sentence2.count - sentence1.count
                        if new_count >= 0 and new_cells:
                            new_sentence = Sentence(new_cells, new_count)
                            if new_sentence not in self.knowledge:
                                self.knowledge.append(new_sentence)
                                changed = True

    def make_safe_move(self):
        for safe in self.safes:
            if safe not in self.moves_made and safe not in self.mines:
                return safe
        return None

    def make_random_move(self):
        possible_moves = []
        for i in range(self.height):
            for j in range(self.width):
                move = (i, j)
                if move not in self.moves_made and move not in self.mines:
                    possible_moves.append(move)
        return random.choice(possible_moves) if possible_moves else None
    """

changed = True
while changed:
    changed = False
    new_mines = set()
    new_safes = set()
    for sentence in self.knowledge:
        known_mines = sentence.known_mines()
        known_safes = sentence.known_safes()
        if known_mines:
            new_mines.update(known_mines)
        if known_safes:
            new_safes.update(known_safes)
        for mine in new_mines:
            if mine not in self.mines:  ###
                self.mark_mine(mine)
                changed = True
        for safe in known_safes:
            if safe not in self.safes:  ###
                self.mark_safe(safe)
                changed = True
    new_knowledge = []
    for sentence in self.knowledge:
        if sentence.cells:  # Assuming 'edits' is a condition/attribute
            new_knowledge.append(sentence)
    self.knowledge = new_knowledge



    for sentence1 in self.knowledge:
        for sentence2 in self.knowledge:
            if sentence1 != sentence2 and sentence1.cells.issubset(sentence2.cells) and sentence2.cells:
                new_set_cells = sentence2.cells - sentence1.cells
                new_sentence_count = sentence2.count - sentence1.count
                if new_sentence_count >= 0:  ###
                    new_concluded_sentence = Sentence(new_set_cells, new_sentence_count)
                    if new_concluded_sentence not in self.knowledge:  ###
                        self.knowledge.append(new_concluded_sentence)