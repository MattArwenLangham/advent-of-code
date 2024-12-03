import * as txt from '../helperFunctions/textUtils'

const filePath = txt.getDir(import.meta.url, false);
const rawData = txt.getData(filePath)

const REGEXQUERY = /mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)/g

function processData(rawData: string): string[]|null {
    return rawData.toString().match(REGEXQUERY);
}

function executeArrayOfInstructions(instructions: string[]): number {
    let totalSum = 0;
    let executeSum = true;
    for (const instruction of instructions) {
        if (instruction === "do()"){
            executeSum = true
        } else if (instruction === "don't()"){
            executeSum = false
        } else {
            if (executeSum){
                const [str1, str2] = instruction.split(",");
                const int1 = parseInt(str1.replace("mul(", ""))
                const int2 = parseInt(str2.replace(")", ""))
                totalSum += int1 * int2
            }
        }
    }
    return totalSum
}

const instructions = processData(rawData)
if (instructions != null){
    const answer = executeArrayOfInstructions(instructions)
    console.log(answer);
}