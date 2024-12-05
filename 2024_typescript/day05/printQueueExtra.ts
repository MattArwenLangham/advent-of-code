import * as txt from '../helperFunctions/textUtils'

const filePath = txt.getDir(import.meta.url, false);
const rawData = txt.getData(filePath)

function processData(rawData: string): [{}, string[][]] {
    const rawLines = rawData.split("\n")
    const ruleList: {} = {}
    const updateList: string[][] = []
    let isUpdates = false
    for (const line of rawLines) {
        if (line === "") {
            isUpdates = true;
        } else if (isUpdates) {
            updateList.push(line.split(","))
        } else {
            const [before, after] = line.split("|")
            if (before in ruleList){
                ruleList[before].push(after);
            } else {
                ruleList[before] = [after];
            }
        }
    }
    return [ruleList, updateList]
}

function getSumFromCorrectUpdateLists (ruleList: {}, updateList): number {
    let fixedPatternSum: number = 0
    for (const updatePattern of updateList){
        let wasFixed = false;
        for (let i = 0; i < updatePattern.length; i++){
            if (i != 0){
                if (updatePattern[i] in ruleList){
                    let indexToChange: number = fixPatternIfBroken(updatePattern.slice(0, i), ruleList[updatePattern[i]])
                    if (indexToChange >= 0) {
                        const updateToMove = updatePattern.splice(i, 1)[0]
                        updatePattern.splice(indexToChange, 0, updateToMove)
                        i = indexToChange
                        wasFixed = true;
                    }
                }
            }
        }

        if (wasFixed){
            const pagePosition = Math.ceil((updatePattern.length/2) - 1)
            fixedPatternSum += parseInt(updatePattern[pagePosition])
        }

    }
    return fixedPatternSum
}

function fixPatternIfBroken (updatePagesLeft: string[], ruleList: string[]): number {
    for (const i in updatePagesLeft){
        for (const rule of ruleList){
            if (rule == updatePagesLeft[i]){
                return parseInt(i);
            }
        }
    }
    return -1;
}

const [ruleList, updateList] = processData(rawData)
const answer = getSumFromCorrectUpdateLists(ruleList, updateList)
console.log(answer)