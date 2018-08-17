from copy import deepcopy


class TowerOfHanoi:
    def __init__(self, n: int) -> None:
        """Initiate a tower of Hanoi game with n disks.

        :param n: the number of disks.
        """
        # Store disks on each peg by their sizes from top to bottom
        self.pegs = [list(range(1, n + 1)), [], []]
        self.history = []
        self.move_cnt = 0
        self.num_disks = n

    def __repr__(self) -> str:
        pegs_repr = []
        max_disk_width = 2 * self.num_disks - 1
        for peg in self.pegs:
            peg_repr = []
            for disk_size in [0] * (self.num_disks - len(peg)) + peg:
                disk_width = 2 * disk_size - 1 if disk_size != 0 else 0
                void_width = (max_disk_width - disk_width) // 2
                void = " " * void_width
                disk_repr = void + "-" * disk_width + void
                disk_repr += " " * (max_disk_width - len(disk_repr))
                peg_repr.append(disk_repr)
            pegs_repr.append(peg_repr)
        return "\n".join(map(lambda s: " | ".join(s), zip(*pegs_repr)))

    def is_legal(self) -> bool:
        """Verify if the current configuration is legal.

        :return: True if on all pegs smaller disks are on top of larger disks,
                 False otherwise.
        """
        for peg in self.pegs:
            prev_disk_size = -1
            for disk_size in peg:
                if disk_size <= prev_disk_size:
                    return False
                prev_disk_size = disk_size
        return True

    def is_finished(self) -> bool:
        """Verify if the game is finished.

        :return: True if all n disks are on the right-most peg,
                 top to bottom from smallest to biggest,
                 False otherwise.
        """
        # Verify that there are no disks on the 2 first pegs
        if any(self.pegs[:-1]):
            return False
        return self.is_legal()

    def move(self, from_: int, to: int) -> bool:
        """Move the disk at the top of the first peg to the top of the second peg.

        :param from_: the index of the peg of the disk to be moved;
                      must be between 0 and 2, inclusive.
        :param to: the index of the peg that the disk is to be moved to;
                   must be between 0 and 2, inclusive.
        :return: True if move was successful else False.
        """
        # Coordinates out of bound
        if not (0 <= from_ <= 2 and 0 <= to <= 2) or abs(from_ - to) >= 2:
            return False
        # No disk on peg to be moved
        if not self.pegs[from_]:
            return False
        # Copy self.pegs to avoid history being modified by reference.
        self.history.append(deepcopy(self.pegs))
        self.pegs[to].insert(0, self.pegs[from_].pop(0))
        if not self.is_legal():
            self.undo()
            return False
        self.move_cnt += 1
        return True

    def undo(self) -> bool:
        """Undo the last move and restore the previous configuration.

        :return: True if action was successful else False.
        """
        if not self.history:
            return False
        self.pegs = self.history.pop()
        self.move_cnt -= 1
        return True


def launch_terminal_game():
    intro_text = "===Tower of Hanoi"
    print(intro_text)

    game = TowerOfHanoi(int(input("Number of disks: ")))

    instruction_text = "===Available actions:\n" \
                       "* 'UNDO' to restore previous configuration;\n" \
                       "* 'a b' with a and b two integers between 1\n" \
                       "   and 3 (inclusive) to move disk from a to b"
    print(instruction_text)

    while not game.is_finished():
        print(game)
        action = input("\n> ")
        if action == "UNDO":
            if not game.undo():
                print("Cannot undo: history is empty.")
        else:
            try:
                a, b = map(int, action.split(' '))
                if not game.move(from_=a - 1, to=b - 1):
                    print(f"Cannot move from {a} to {b}: illegal.")
            except ValueError:
                print(f"Cannot read integers a and b from '{action}'")
    else:
        print(game)
        print(f"===You finished in {game.move_cnt} moves.")


if __name__ == '__main__':
    launch_terminal_game()
