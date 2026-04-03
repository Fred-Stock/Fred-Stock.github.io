find . -name "*.pdf-1.png" -exec sh -c 'mv "$1" "${1%.pdf-1.png}.png"' _ {} \;

