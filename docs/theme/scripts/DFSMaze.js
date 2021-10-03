//var mazeWidth = 500;
var cellSize = 10;
var mazeWidth = Math.floor((document.getElementById("topBox").offsetWidth * 0.60) / cellSize) * cellSize;
//var mazeHeight = Math.floor((mazeWidth/5) / cellSize) * cellSize;
var mazeHeight = 10 * cellSize;
//var mazeHeight = document.getElementsByClassName("siteTitle").offsetHeight;
var nrows = mazeHeight / cellSize;
var ncols = mazeWidth / cellSize;
var grid = [];
var stack = [];
var initialCell;
var currentCell;

function setup(){
    //frameRate(30);
    var canvas = createCanvas(mazeWidth, mazeHeight);
    canvas.parent("canvasContainer");
    // make the canvas clickable -- so that it takes you to the blog post about the maze
    document.getElementById("canvasDiv").onmousedown = function(){
        location.replace('/maze-animation.html');
        return true;
    };
    // create the grid
    for(let i = 0; i < nrows; i++){
        let gridRow = [];
        for(let j = 0; j < ncols; j++){
            let cell = new Cell(i,j);
            gridRow.push(cell);
        }
        grid.push(gridRow);
    }
    currentCell = grid[0][0];
}

function draw(){
    currentCell.visited = true;
    currentCell.isCurrentCell = true;
    // draw the grid
    for(let i = 0; i < nrows; i++)
        for(let j = 0; j < ncols; j++)
            grid[i][j].drawCell();
    // get next step, change current cell
    var nextCell = currentCell.getNextStep();
    if(nextCell){
        nextCell.visited = true;
        stack.push(currentCell);
        currentCell.removeWall(nextCell);
        currentCell.isCurrentCell = false;
        currentCell = nextCell;
    } else if(stack.length > 0){
        currentCell = stack.pop();
    }
}
