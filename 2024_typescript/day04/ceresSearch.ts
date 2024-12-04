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
            if (wordSearch[line][letter] === "X"){
                wordCount += checkSurroundingLettersForWord(wordSearch, line, letter)
            }
        }
    }
    return wordCount;
}

function checkSurroundingLettersForWord(wordSearch: string[][], line: number, letter: number): number {
    let wordCount = 0
    //down, up, left, right, diagonal
    const directions = [[-1, 0], [1, 0], [0, -1], [0, 1], [1, 1], [-1, -1], [-1, 1], [1, -1]]

    const lineLimit = wordSearch.length
    const lineLengthLimit = wordSearch[line].length

    for(const direction of directions){
        let word = wordSearch[line][letter];
        if (direction[0] * 3 + line >= 0 && direction[0] * 3 + line < lineLimit && direction[1] * 3 + letter >= 0 && direction[1] * 3 + letter < lineLengthLimit){
            for (let i = 1; i <= 3; i++){
                word += wordSearch[line + (direction[0] * i)][letter + (direction[1] * i)]
            }
        }

        // console.log(word);
        if (word === "XMAS"){
            wordCount++
        }
    }
    return wordCount;
}

const wordSearch = processData(rawData)
const answer = findInstancesOfWordInWordsearch(wordSearch)

console.log(answer)