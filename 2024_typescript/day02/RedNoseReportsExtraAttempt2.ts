import * as txt from '../helperFunctions/textUtils'

const filePath = txt.getDir(import.meta.url, false);
const rawData = txt.getData(filePath)

function processData(rawData: string): number[][] {
    const rawLines = rawData.split("\r\n")
    const processedLines: number[][] = []
    for (const line of rawLines){
        const parsedLines = line.split(" ").map(
            lvl => parseInt(lvl)
        )
        processedLines.push(parsedLines);
    }
    return processedLines
}

function getNumOfSafeLines(lists: number[][]): number {
    let safeCount = 0
    for (const list of lists){
        if(isSafe(list) || couldBeSafe(list)){
            safeCount++
        }
    }

    return safeCount;
}

function couldBeSafe(list: number[]): boolean {
    for (let i = 0; i < list.length; i++) {
        const modifiedList = list.slice(0, i).concat(list.slice(i + 1));
        if (isSafe(modifiedList)) {
            return true;
        }
    }
    return false;
}

function isSafe(list: number[]): boolean {
    if (list[0] == list[1]) return false;

    const isIncreasing = getIsIncreasing(list[0], list[1]);

    for (let i = 0; i < list.length - 1; i++){
        if (!checkIfValid(list[i], list[i + 1], isIncreasing)){
            return false;
        }
    }

    return true
}

function getIsIncreasing(num1: number, num2: number): boolean {
    return num1 - num2 < 0
}

function checkIfValid(num1: number, num2: number, isIncreasing:boolean): boolean {
    const diff = num1 - num2
    if (!isIncreasing && diff > 0 && diff <= 3){
        return true;
    } else if (isIncreasing && diff < 0 && diff >= -3){
        return true;
    } else return false
}

const processedLines = processData(rawData)
const answer = getNumOfSafeLines(processedLines)

console.log(answer)