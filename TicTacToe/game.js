//gave myself 45 minutes

var board = []

function createBoard(n){
    board = [];
    for(let i = 0; i < n; i++){
        let row = []
        for(let j = 0; j < n; j++){
            row.push("")
        }
        board.push(row);
    }
}

function checkWin(){
    let n = board.length;
    //rows
    for(let i = 0; i < n; i++){
        let row = board[i];
        let win = true;
        for(let j = 1; j < n; j++){
            if(row[j] != row[j-1] || row[j] == ""){
                win = false;
                break;
            }
        }
        if(win == true){
            return true;
        }
    }
    //cols
    for(let i = 0; i < n; i++){
        let win = true;
        for(let j = 1; j < n; j++){
            if(board[j][i] != board[j-1][i] || board[j][i] == ""){
                win = false;
                break;
            }
        }
        if(win == true){
            return true;
        }
    }

    //diagonal
    let win = true;
    for(let i = 1; i < n; i++){
        if(board[i][i] != board[i-1][i-1] || board[i][i] == ""){
            win = false;
            break;
        }
    }
    if(win == true){
        return true;
    }

    win = true;
    for(let i = n-1; i > 0; i--){
        if(board[i][i] != board[i-1][i-1] || board[i][i] == ""){
            win = false;
            break;
        }
    }

    return win;

}

function getMoves(){
    let n = board.length;

    let indicies = Array.from(Array(n).keys());
    let positions = [];

    for(let i = 0; i < n; i++){
        let first = indicies[i];
        for(let j = 0; j < n; j++){
            positions.push( [first, indicies[j]] );    
        }
    }

    return positions;
}

function makeMove(moves, mark){
    let m = moves.length;
    let indx = Math.floor(m*Math.random());

    let move = moves.splice(indx,1);

    board[move[0][0]][move[0][1]] = mark;

    return moves;
}

function gameLoop(n){

    createBoard(n);

    let moves = getMoves();

    let p1 = "x";
    let p2 = "o";
    let mark = "";
    for(let i = 0; i < n*n; i++){
        if(i % 2 == 0){
            mark = p1;
        }
        else{
            mark = p2;
        }

        makeMove(moves, mark);

        if(checkWin()){
            if(mark == p1){
                console.log("Player 1 wins!");
            }
            else{
                console.log("Player 2 wins!");
            }
            console.log(board);
            return;
        }
    }
    console.log("Its a tie!");
    console.log(board);

}

function play(){
    let n = parseInt(document.getElementById("n").value);
    gameLoop(n);
}