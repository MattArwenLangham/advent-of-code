import * as txt from '../helperFunctions/textUtils'

const filePath = txt.getDir(import.meta.url, false);
const rawData = txt.getData(filePath)

function processData(rawData: string) {
    const rawLines = rawData.split("\r\n")
    const mapArray: string[][] = []
    for (const line of rawLines){
        mapArray.push(line.split(""));
    }
    return mapArray
}

function traceGuardOnMap(mapArray: string[][]) {
    const startingPos = findStartPosition(mapArray)
    traceGuard(mapArray, startingPos)
    return mapArray;
}

function findStartPosition(mapArray: string[][]) {
    for (const row in mapArray){
        let column = mapArray[row].indexOf("^")
        if (column >= 0){
            return [parseInt(row), column]
        }
    }

    return []
}
function traceGuard(mapArray: string[][], startingPos: number[]) {
    let [row, column] = startingPos
    let directionInd = 0;
    let patrolHasFinished = false;
    let directionOfTravelArray = ["N", "E", "S", "W"]
    const directionObj = {
        "N": [-1, 0],
        "E": [0, 1],
        "S": [1, 0],
        "W": [0, -1]
    }

    while (!patrolHasFinished){
        let nextMove = directionObj[directionOfTravelArray[directionInd]] 
        mapArray[row][column] = 'X';
        let [nextMoveSafe, hasGuardLeftArea] = isNextMoveSafe(mapArray, row + nextMove[0], column + nextMove[1])
        if (nextMoveSafe){
            column += nextMove[1]
            row += nextMove[0]
        } else {
            if (directionInd < 3){
                directionInd++
            } else {
                directionInd = 0;
            }
        }
        patrolHasFinished = hasGuardLeftArea
    }
}

function isNextMoveSafe(mapArray, row, column): boolean[] {
    if(row >= mapArray.length || row < 0){
        return [false, true];
    } else if (column >= mapArray.length || column < 0){
        return [false, true];
    } else if (mapArray[row][column] == '#' ){
        return [false, false];
    }
    return [true, false];
}

function renderMap(mapArray: string[][]) {
    for (const line of mapArray){
        console.log(line.toString().replace(",", ""));
    }
    console.log()
}

function countUniquePositionsOnMap(finishedMapArray: string[][]){
    let sum = 0
    for (const row of finishedMapArray){
        sum += row.filter(item => item === "X").length
    }
    return sum;
}

const mapArray = processData(rawData)
const finishedMapArray = traceGuardOnMap(mapArray)
const answer = countUniquePositionsOnMap(finishedMapArray)
console.log(answer)