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

function checkIfValid(num1: number, num2: number, isIncreasing:boolean): boolean {
    const diff = num1 - num2
    if (!isIncreasing && diff > 0 && diff <= 3){
        return true;
    } else if (isIncreasing && diff < 0 && diff >= -3){
        return true;
    } else return false
}

//71, 69, 70, 71, 72, 75
function determineIsIncreasing(lineToTest: number[]): [boolean, boolean] {
    let errors = 0;
    let isIncreasing;
    let line = lineToTest.slice(0, 4)

    for (let i = 0; i < 3; i++){
        const diff = line[i] - line[i + 1];

        if (i === 0) {      
            if (diff < 0) {
                isIncreasing = true
            } else if (diff > 0) {
                isIncreasing = false
            } else {
                errors++
            }
        } else if (i === 1 && errors === 1){
            //If dupes
            if (diff < 0) {
                isIncreasing = true
            } else if (diff > 0) {
                isIncreasing = false
            } else {
                return [false, false]
            }
        } else if (!checkIfValid(line[i], line[i + 1], isIncreasing)){
            errors++
        }
    }

    if (errors < 2){
        return [isIncreasing, false]
    } else {
        return [!isIncreasing, true]
    }
}

function getNumOfSafeLines(lines: number[][]): number {
    let safeFloors = 0;
    for (const line of lines){
        let lastLvl = 0;
        let errors = 0
        let [isIncreasing, shouldIgnoreFirst] = determineIsIncreasing(line)

        for (const i in line){
            if (i === "0"){
                if (shouldIgnoreFirst){
                    errors++;
                } else {
                    lastLvl = line[i];
                }
            } else {
                if (shouldIgnoreFirst) {
                    lastLvl = line[i];
                    shouldIgnoreFirst = false;
                } else if (checkIfValid(lastLvl, line[i], isIncreasing)){
                    console.log("Success")
                    lastLvl = line[i]
                } else {
                    if (errors > 0){
                        break;
                    }
                    errors++
                };
                
                if (parseInt(i) == line.length - 1){
                    safeFloors++
                    break;
                }
            }
        }
    }
    return safeFloors;
}

const processedLines = processData(rawData)
const answer = getNumOfSafeLines(processedLines)

console.log(answer)