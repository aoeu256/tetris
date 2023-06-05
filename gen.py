import numpy as np

# Function to generate a random Tetris piece configuration
def generate_piece():
    piece = np.zeros((4, 4), dtype=int)
    # Randomly select four cells and mark them as filled
    filled_cells = np.random.choice(16, 4, replace=False)
    piece.ravel()[filled_cells] = 1
    return piece

# Function to rotate a Tetris piece clockwise
def rotate_piece(piece):
    return np.rot90(piece)

# Function to reflect a Tetris piece horizontally
def reflect_piece(piece):
    return np.fliplr(piece)

# Function to check if a piece is unique
def is_unique(piece, pieces):
    # Check for uniqueness among rotations and reflections
    for rotation in range(4):
        for reflection in [False, True]:
            rotated_piece = np.rot90(piece, rotation)
            if reflection:
                rotated_piece = np.fliplr(rotated_piece)
            if np.array_equal(rotated_piece, piece):
                return False
    return True

# Generate Tetris pieces
pieces = []
while len(pieces) < 7:  # Generate all 7 standard Tetris pieces
    new_piece = generate_piece()
    if is_unique(new_piece, pieces):
        pieces.append(new_piece)

# Print the generated pieces
for piece in pieces:
    print(piece)
    print()
