import json

# File containing the board JSON
json_file = "tower-move-board.json"

# Number of boards
max_index = 9  # Adjust as needed

# Load data from the file
with open(json_file, "r") as f:
    data = json.load(f)


# Color mapping
color_map = {
    "bl": "blue-square.svg",
    "rd": "red-square.svg",
    "yl": "yellow-square.svg",
    "gy": "grey-square.svg",
    "blc": "blue-square-circle.svg",
    "rdc": "red-square-circle.svg",
    "ylc": "yellow-square-circle.svg",
    "gyc": "grey-square-circle.svg",
    "blch": "blue-square-circle-highlighted.svg",
    "rdch": "red-square-circle-highlighted.svg",
    "ylch": "yellow-square.svg",
}
# --------------------------------------------
# ✅ Remove full rows/columns of "?" across all boards
# --------------------------------------------

# Assuming all boards are the same shape
original_board = data["0"]["board"]
orig_rows = len(original_board)
orig_cols = len(original_board[0])

# Track which rows/cols are entirely "?" in all boards
valid_rows = [False] * orig_rows
valid_cols = [False] * orig_cols

# Mark any row/col that has at least one non-"?" cell in any board
for board_index in range(max_index):
    board = data[str(board_index)]["board"]
    for r in range(orig_rows):
        for c in range(orig_cols):
            if board[r][c] != "?":
                valid_rows[r] = True
                valid_cols[c] = True

# Indices to keep
kept_row_indices = [i for i, keep in enumerate(valid_rows) if keep]
kept_col_indices = [i for i, keep in enumerate(valid_cols) if keep]

# Now filter each board's rows and columns
for board_index in range(max_index):
    board = data[str(board_index)]["board"]
    # Filter rows
    filtered_board = []
    for r in kept_row_indices:
        row = [board[r][c] for c in kept_col_indices]
        filtered_board.append(row)
    # Replace with filtered board
    data[str(board_index)]["board"] = filtered_board

# --------------------------------------------
# 🔽 Continue as normal from line 21 onwards
# --------------------------------------------

# Use board 0 to determine shape
sample_board = data["0"]["board"]
rows = len(sample_board)
cols = len(sample_board[0])

# Create 2D grid to collect square entries per cell
cell_squares = [[[] for _ in range(cols)] for _ in range(rows)]

# Track previous values per cell to detect changes
previous_values = [[None for _ in range(cols)] for _ in range(rows)]

# Process each board
for board_index in range(max_index):
    board = data[str(board_index)]["board"]
    for row_idx in range(rows):
        for col_idx in range(cols):
            cell = board[row_idx][col_idx]
            prev_cell = previous_values[row_idx][col_idx]

            # Only add if the value is different and it's a known color
            if cell != prev_cell and cell in color_map:
                svg = color_map[cell]
                square_entry = f'{{"sq":"{svg}", "ind":"{board_index}"}}'
                cell_squares[row_idx][col_idx].append(square_entry)

            # Update previous value
            previous_values[row_idx][col_idx] = cell

# Now convert cell_squares into a 2D grid of AniSquare `squares` strings
vue_grid = []

for row in cell_squares:
    vue_row = []
    for cell_entries in row:
        if cell_entries:
            # Join entries into a single squares string
            squares_attr = ";".join(cell_entries)
            vue_row.append(squares_attr)
        else:
            vue_row.append("")
    vue_grid.append(vue_row)

# Output the result as a string that can be used in Vue
vue_grid_str = json.dumps(vue_grid, indent=2)
print(vue_grid_str)