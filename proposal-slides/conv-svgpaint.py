import json

# Input JSON
data = {
    "0": {
        "parent": None,
        "board": [
            ["?","?","?","?","?","?","?","?","?","?","?"],
            ["?","gy","rd","rd","rd","rd","rd","rd","rd","rd","?"],
            ["?","bl","gy","rd","rd","rd","rd","rd","rd","rd","?"],
            ["?","bl","bl","gy","rd","rd","rd","rd","rd","rd","?"],
            ["?","bl","bl","yl","gy","rd","rd","rd","rd","rd","?"],
            ["?","bl","bl","yl","yl","gy","rd","rd","rd","rd","?"],
            ["?","bl","bl","bl","yl","yl","gy","rd","rd","rd","?"],
            ["?","bl","bl","bl","yl","yl","yl","gy","rd","rd","?"],
            ["?","bl","bl","bl","bl","bl","bl","bl","gy","rd","?"],
            ["?","bl","bl","bl","bl","bl","bl","bl","bl","gy","?"],
            ["?","?","?","?","?","?","?","?","?","?","?"]
        ],
        "x": 0,
        "y": 0
    }
}

# Color mapping
color_map = {
    "bl": "blue-square.svg",
    "rd": "red-square.svg",
    "yl": "yellow-square.svg",
    "Gy": "grey-square.svg"
}

# Extract the board
board = data["0"]["board"]
rows = len(board)
cols = len(board[0])

# Transpose the board to process column-wise
columns_data = [[] for _ in range(cols)]

for row in board:
    for col_idx, cell in enumerate(row):
        if(cell == "Gy"):
            print(cell)
            print(cell in color_map)
            
        if cell in color_map:
            svg = color_map[cell]
            squares_attr = f'{{"sq":"{svg}", "ind":"0"}}'
            ani_square_html = f'''<AniSquare squares='{squares_attr}'/>'''
            columns_data[col_idx].append(ani_square_html)
        else:
            columns_data[col_idx].append(None)  # Preserve position with None

# Build the HTML
html = '<div class="flex flex-col items-center">\n'
html += f'  <div class="grid grid-cols-{cols} gap-1em">\n'

for column in columns_data:
    html += '    <div>\n'
    for item in column:
        if item:
            html += f'      {item}\n'
        else:
            html += '      <!-- empty -->\n'
    html += '    </div>\n'

html += '  </div>\n'
html += '</div>'

# Output result
print(html)

