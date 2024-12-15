import { toNamespacedPath } from 'path';
import * as txt from '../helperFunctions/textUtils'

const filePath = txt.getDir(import.meta.url, true);
const rawData = txt.getData(filePath)

function processData(rawData: string): string[] {
    return rawData.split(" ");
}

function blinkMultiple(numOfTimes, stoneArray){
    for (let i = 0; i < numOfTimes; i++){
        blink(stoneArray);
    }
}

function blink(stoneArray){
    for (let i = 0; i < stoneArray.length; i++){
        let stone = stoneArray[i];
        if (stone == "0"){
            stoneArray[i] = "1";
        } else if (stone.length % 2 === 0){
            const midPoint = (stone.length / 2);
            const splitStones: string[] = [];
            splitStones.push(stone.substring(0, midPoint))
            let newStone = stone.substring(midPoint);
            while (newStone.length > 1 && newStone[0] === "0"){
                newStone = newStone.substring(1)
            }
            splitStones.push(newStone);
            stoneArray.splice(i, 1, ...splitStones);
            i++
        } else {
            const newStone = parseInt(stone, 10) * 2024
            stoneArray.splice(i, 1, newStone.toString())
        }
    }
    return stoneArray;
}

const stoneArray = processData(rawData);
blinkMultiple(25, stoneArray);
console.log(stoneArray.length);