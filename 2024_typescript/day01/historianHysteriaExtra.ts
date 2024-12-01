import * as txt from '../helperFunctions/textUtils'

const filePath = txt.getDir(import.meta.url, false);
const rawData = txt.getData(filePath)

function processList(rawData: string): [number[], number[]] {
    const rawDataArray = rawData.split("\r\n")
    const leftList: number[] = []
    const rightList: number[] = []
    for (const data of rawDataArray){
        const splitDataList = data.split("   ");
        leftList.push(parseInt(splitDataList[0]))
        rightList.push(parseInt(splitDataList[1]))
    }
    return [leftList.sort(), rightList.sort()]
}

function findOccurancesBetweenLists(lists: [number[], number[]]): number {
    const occuranceMemory: { [key: number]: number } = {}
    const [numsToCheck, listToCheck] = lists;
    let sumSimilarityScore = 0;
    let pointerPos = 0;

    for (const numToCheck of numsToCheck){
        let occurances = 0;
        if (!occuranceMemory[numToCheck]){
            while (pointerPos !== listToCheck.length - 1){
                const num = listToCheck[pointerPos]
                if (numToCheck === num){
                    occurances++
                } else if (numToCheck < num){
                    break;
                }
                pointerPos++
            }
            occuranceMemory[numToCheck] = occurances * numToCheck;
        }
        sumSimilarityScore += occuranceMemory[numToCheck]
    }

    return sumSimilarityScore;
}

const processedLists = processList(rawData)
const answer = findOccurancesBetweenLists(processedLists);

console.log(answer)