function Cell(i,j){
    this.i = i; // row number
    this.j = j; // column number
    this.visited = false;
    this.walls = {top: true, right: true, bottom: true, left: true};
    this.isCurrentCell = false;
}
Cell.prototype.drawCell = function(){   // render the cell
    let x_pix = this.j * cellSize;
    let y_pix = this.i * cellSize;
    // draw walls
    stroke('#6e6a62');
    (this.walls.top) ? line(x_pix, y_pix, x_pix+cellSize, y_pix) : {};                       // top wall
    (this.walls.right) ? line(x_pix+cellSize, y_pix, x_pix+cellSize, y_pix+cellSize) : {};   // right wall
    (this.walls.bottom) ? line(x_pix, y_pix+cellSize, x_pix+cellSize, y_pix+cellSize) : {};  // bottom wall
    (this.walls.left) ? line(x_pix, y_pix, x_pix, y_pix+cellSize) : {};                      // left wall
    // fill with color if visited
    if(this.visited){
        noStroke();
        //fill('#9e9788');
	fill('#8a8478');
        rect(x_pix,y_pix,cellSize,cellSize);
    }
    if(this.isCurrentCell){
        noStroke();
        //fill('#8a8478');
	fill('#9e9788');
        rect(x_pix,y_pix,cellSize,cellSize);
    }
}
Cell.prototype.getUnvisitedNeighbors = function(){   // get valid next steps
    let neighbors = [(this.i-1 < 0) ? undefined : grid[this.i-1][this.j],		// top
                     (this.j+1 > ncols-1) ? undefined : grid[this.i][this.j+1],	// right
                     (this.i+1 > nrows-1) ? undefined : grid[this.i+1][this.j],	// bottom
                     (this.j-1 < 0) ? undefined : grid[this.i][this.j-1]];		// left
    let unvisitedNeighbors = [];
    for(let n = 0; n < neighbors.length; n++)
        if(neighbors[n] && !neighbors[n].visited)
            unvisitedNeighbors.push(neighbors[n]);
    return unvisitedNeighbors;
}
Cell.prototype.getNextStep = function(){    // decide where to go next
    let stepChoices = this.getUnvisitedNeighbors();
    if(stepChoices.length > 0){
        let r = floor(random(0, stepChoices.length))
        return stepChoices[r];
    } else return undefined;
}
Cell.prototype.removeWall = function(nextCell){     // remove the appropriate wall between 2 cells
    let deltaCoords = [this.i - nextCell.i, this.j - nextCell.j];
    if(deltaCoords[0]===1 && deltaCoords[1]===0){     // remove top-current and bottom-next
        this.walls.top = false;
        nextCell.walls.bottom = false;
    } else if(deltaCoords[0]===0 && deltaCoords[1]===1){     // remove left-current and right-next
        this.walls.left = false;
        nextCell.walls.right = false;
    } else if(deltaCoords[0]===-1 && deltaCoords[1]===0){    // remove bottom-current and top-next
        this.walls.bottom = false;
        nextCell.walls.top = false;
    } else if(deltaCoords[0]===0 && deltaCoords[1]===-1){    // remove right-current and left-next
        this.walls.right = false;
        nextCell.walls.left = false;
    }
}
