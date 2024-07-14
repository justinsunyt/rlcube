import numpy as np


class Cube:
    def __init__(self, side_length: int, scramble: bool = False):
        # 0: White, 1: Yellow, 2: Red, 3: Orange, 4: Green, 5: Blue
        # Top, Bottom, Front, Back, Left, Right
        self.faces = np.array(
            [[[i] * side_length for _ in range(side_length)] for i in range(6)]
        )
        if scramble:
            self.scramble()

    def __str__(self):
        return str(self.faces)

    def rotate_face(self, face_index: int, clockwise: bool = True):
        if face_index == 0:
            # Rotate top
            self.faces[0] = np.rot90(self.faces[0], 1 if clockwise else 3)
            # Store left
            # Move front to left
            # Move right to front
            # Move back to right
            # Move left to back
        elif face_index == 1:
            # Rotate bottom
            self.faces[1] = np.rot90(self.faces[1], 1 if clockwise else 3)
            # Store left
            # Move back to left
            # Move right to back
            # Move front to right
            # Move left to front
            pass
        elif face_index == 2:
            pass
        elif face_index == 3:
            pass
        elif face_index == 4:
            pass
        elif face_index == 5:
            pass

    def scramble(self):
        pass
