import * as txt from '../helperFunctions/textUtils'

const filePath = txt.getDir(import.meta.url, false);
const rawData = txt.getData(filePath)

function processData(rawData: string): string[][] {
    const rawLines = rawData.split("\n")
    const wordSearch: string[][] = []
    for (const rawLine of rawLines){
        wordSearch.push(rawLine.split(""))
    }
    return wordSearch
}

function findInstancesOfWordInWordsearch(wordSearch: string[][]) {
    let wordCount = 0
    for (let line = 0; line < wordSearch.length; line++){
        for (let letter = 0; letter < wordSearch[line].length; letter++) {
            if (wordSearch[line][letter] === "A"){
                wordCount += checkSurroundingLettersForWord(wordSearch, line, letter)
            }
        }
    }
    return wordCount;
}

function checkSurroundingLettersForWord(wordSearch: string[][], line: number, letter: number): number {
    let masCount = 0
    const directions = [[[-1, -1], [1, 1]], [[1, -1], [-1, 1]]]

    const lineLimit = wordSearch.length
    const lineLengthLimit = wordSearch[line].length
    let masFound = 0;

    for(const direction of directions){
        let word = wordSearch[line][letter];
        for (let i = 0; i <= 1; i++){
            if (direction[i][0] + line >= 0 && direction[i][0] + line < lineLimit && direction[i][1] + letter >= 0 && direction[i][1] + letter < lineLengthLimit){
                word += wordSearch[line + direction[i][0]][letter + direction[i][1]]
            }
        }
        
        if (word === "AMS" || word === "ASM"){
            masFound++
        }
    }

    if (masFound == 2){
        masCount++
    } 

    return masCount
}

const wordSearch = processData(rawData)
const answer = findInstancesOfWordInWordsearch(wordSearch)

console.log(answer)