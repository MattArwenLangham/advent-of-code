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

function findSumOfDifferenceOfTwoSortedLists(lists: [number[], number[]]): number {
    let sum: number = 0;
    for (let i in lists[0]){
        sum += Math.abs(lists[0][i] - lists[1][i]);
    }
    return sum
}

const processedLists = processList(rawData)
const answer = findSumOfDifferenceOfTwoSortedLists(processedLists);

console.log(answer)