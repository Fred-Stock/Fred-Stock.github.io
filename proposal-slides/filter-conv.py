import json

# File containing the board JSON
json_file = "recombination-board-2.json"

# Number of boards
max_index = 6  # Adjust as neeed

# Load data from the file
with open(json_file, "r") as f:
    data = json.load(f)


# Color mapping
# color_map = {
#     "bl": "blue-square.svg",
#     "rd": "red-square.svg",
#     "yl": "yellow-square.svg",
#     "Gy": "grey-square.svg"
# }

color_map = {
    "bl": "blue-square.svg",
    "rd": "red-square.svg",
    "yl": "yellow-square.svg",
    "gy": "grey-square.svg",
    "Gy": "grey-square.svg",
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
    print(data[str(board_index)]["board"])
    print("\n\n------\n\n")
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

# Transpose to column-major order
columns_data = [[] for _ in range(cols)]

for col_idx in range(cols):
    for row_idx in range(rows):
        entries = cell_squares[row_idx][col_idx]
        if entries:
            squares_attr = ";".join(entries)
            ani_square_html = f'''<AniSquare squares='{squares_attr}'/>'''
            columns_data[col_idx].append(ani_square_html)
        else:
            columns_data[col_idx].append(None)

# Build the HTML
html = '<div class="flex flex-col items-center">\n'
html += f'  <div class="grid grid-cols-{cols} gap-1em">\n'

for column in columns_data:
    for item in column:
        html += '    <div>'
        if item:
            html += f'      {item}'
        html += '    </div>\n'

html += '  </div>\n'
html += '</div>'

# Output result
print(html)
