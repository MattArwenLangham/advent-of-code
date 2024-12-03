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

function getNumOfSafeLines(lines: number[][]): number {
    let safeFloors = 0;
    for (const line of lines){
        let lastLvl = 0;
        let isIncreasing = true;

        for (const i in line){
            if (i === "0"){
              lastLvl = line[0]
              let levelToCheck = line[0] - line[1]
              if (levelToCheck > 0){
                isIncreasing = false;
              } else if (levelToCheck < 0){
                isIncreasing = true;
              } else break;
            } else {
                let levelToCheck = line[i] - lastLvl

                if (isIncreasing && levelToCheck > 0 && levelToCheck <= 3){
                    lastLvl = line[i]
                } else if (!isIncreasing && levelToCheck < 0 && levelToCheck >= -3){
                    lastLvl = line[i]
                } else {
                    break;
                }

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

// console.log(answer)

function isSafe(report: number[]): boolean {
    // Check if the report is strictly increasing or decreasing with valid differences
    const increasing = report.every((_, i) =>
        i === 0 || (report[i] - report[i - 1] >= 1 && report[i] - report[i - 1] <= 3)
    );
    const decreasing = report.every((_, i) =>
        i === 0 || (report[i - 1] - report[i] >= 1 && report[i - 1] - report[i] <= 3)
    );
    return increasing || decreasing;
}

function canBeSafe(report: number[]): boolean {
    // Check if removing one level makes the report safe
    for (let i = 0; i < report.length; i++) {
        const modifiedReport = report.slice(0, i).concat(report.slice(i + 1));
        if (isSafe(modifiedReport)) {
            return true;
        }
    }
    return false;
}

function countSafeReports(reports: number[][]): number {
    let safeCount = 0;

    for (const report of reports) {
        if (isSafe(report) || canBeSafe(report)) {
            safeCount++;
        }
    }

    return safeCount;
}

const processedLines2 = processData(rawData)
const answer2 = countSafeReports(processedLines2)

console.log(answer2)