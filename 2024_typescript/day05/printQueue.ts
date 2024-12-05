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
    let successfulPatternSum: number = 0
    for (const updatePattern of updateList){
        let isSuccessful = true;
        for (const i in updatePattern){
            if (i != '0'){
                if (updatePattern[i] in ruleList && !isUpdatePatternCorrect(updatePattern.slice(0, i), ruleList[updatePattern[i]])){
                    isSuccessful = false;
                    break;
                }
            }
        }

        if (isSuccessful){
            const pagePosition = Math.ceil((updatePattern.length/2) - 1)
            successfulPatternSum += parseInt(updatePattern[pagePosition])
        }

    }
    return successfulPatternSum
}

function isUpdatePatternCorrect (updatePagesLeft: string[], ruleList: string[]): boolean {
    for (const updatePage of updatePagesLeft){
        for (const rule of ruleList){
            if (rule == updatePage){
                return false;
            }
        }
    }
    return true;
}

const [ruleList, updateList] = processData(rawData)
const answer = getSumFromCorrectUpdateLists(ruleList, updateList)
console.log(answer)