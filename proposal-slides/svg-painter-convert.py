import json

# File containing the board JSON
json_file = "tower-move-board.json"

# Number of boards
max_index = 3  # Adjust as needed

# Load data from the file
with open(json_file, "r") as f:
    data = json.load(f)

# Color mapping
color_map = {
    "bl": "blue-square.svg",
    "rd": "red-square.svg",
    "yl": "yellow-square.svg",
    "Gy": "grey-square.svg"
}

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
            html += f'      {item}\n'
        # else:
        #     html += '      <!-- empty -->\n'
        html += '    </div>\n'

html += '  </div>\n'
html += '</div>'

# Output result
print(html)
