import json

# File containing the board JSON
json_file = "boards.json"

# Number of boards in the file
max_index = 3  # Adjust as needed (e.g., if you have "0", "1", "2")

# Load data from the file
with open(json_file, "r") as f:
    data = json.load(f)

# Color mapping
color_map = {
    "bl": "blue-square.svg",
    "rd": "red-square.svg",
    "yl": "yellow-square.svg",
    "gy": "grey-square.svg"
}

# Get one board to determine shape
sample_board = data["0"]["board"]
rows = len(sample_board)
cols = len(sample_board[0])

# Build squares per cell (row x col) with all boards
# We create a 2D grid: each cell is a list of {"sq": ..., "ind": ...}
cell_squares = [[[] for _ in range(cols)] for _ in range(rows)]

for board_index in range(max_index):
    board = data[str(board_index)]["board"]
    for row_idx in range(rows):
        for col_idx in range(cols):
            cell = board[row_idx][col_idx]
            if cell in color_map:
                svg = color_map[cell]
                square_entry = f'{{"sq":"{svg}", "ind":"{board_index}"}}'
                cell_squares[row_idx][col_idx].append(square_entry)

# Transpose to column-major order for column-based layout
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
    html += '    <div>\n'
    for item in column:
        if item:
            html += f'      {item}\n'
        # else:
            # html += '      <!-- empty -->\n'
    html += '    </div>\n'

html += '  </div>\n'
html += '</div>'

# Output result
print(html)
