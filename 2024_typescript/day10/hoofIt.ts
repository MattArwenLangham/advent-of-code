import { toNamespacedPath } from 'path';
import * as txt from '../helperFunctions/textUtils'

const filePath = txt.getDir(import.meta.url, false);
const rawData = txt.getData(filePath)

function processData(rawData: string): number[][] {
    const rawLines = rawData.split("\r\n")
    const topographicMap: number[][] = []
    for (const rawLine of rawLines){
        topographicMap.push(rawLine.split("").map(num => parseInt(num, 10)));
    }
    return topographicMap;
}

let indexSet: Set<string>;

function findTrailhead(topographicMap: number[][]): number {
    let trailheadScore = 0;
    for (const row in topographicMap){
        for (const num in topographicMap[row]){
            if (topographicMap[row][num] == 0){
                indexSet = new Set();
                trailheadScore += findTrailHeadScore(topographicMap, parseInt(row), parseInt(num))
            }
        }
    }
    return trailheadScore;
}

function findTrailHeadScore(topographicMap: number[][], row: number, num: number): number {
    const directionArray: [number, number][] = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    const nextStep = topographicMap[row][num] + 1;
    for (const direction of directionArray){
        const [nextRow, nextNum] = direction;
        if (isInBounds(row + nextRow, num + nextNum, topographicMap.length, topographicMap[0].length)){
            const nextMove = topographicMap[nextRow + row][nextNum + num];
            if (nextStep === 9 && nextMove === 9){
                const indicesString = (nextRow + row).toString() + "," + (nextNum + num).toString()
                if (!indexSet.has(indicesString)){
                    indexSet.add(indicesString)
                }
            } else if (nextMove === nextStep) {
                findTrailHeadScore(topographicMap, row + nextRow, num + nextNum)
            }
        }
    }
    return indexSet.size;
}

function isInBounds(nextRow: number, nextNum: number, rowMax: number, numMax: number): boolean {
    if (nextRow >= 0 && nextRow < rowMax){
        if (nextNum >= 0 && nextNum < numMax){
            return true;
        }
    }
    return false;
}

const topographicMap: number[][] = processData(rawData);
const totalTrailheadScore = findTrailhead(topographicMap)
console.log(totalTrailheadScore)