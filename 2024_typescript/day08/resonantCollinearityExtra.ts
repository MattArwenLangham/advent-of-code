import * as txt from '../helperFunctions/textUtils'

const filePath = txt.getDir(import.meta.url, false);
const rawData = txt.getData(filePath)

function processData(rawData: string) {
    const rawLines = rawData.split("\r\n")
    const frequencyMap: string[][] = []
    for (const rawLine of rawLines){
        frequencyMap.push(rawLine.split(""))
    }
    return frequencyMap;
}

function findAntinodesInFrequencyMap (frequencyMap: string[][]) {
    const frequencyObj = getFrequencyObject(frequencyMap)
    const antinodeSet: Set<string> = new Set<string>
    for(const key in frequencyObj){
        const frequency = frequencyObj[key];
        for (let i = 0; i < frequency.length - 1; i++){
            for(let j = i + 1; j < frequency.length; j++){
                const freq1 = frequency[i]
                const freq2 = frequency[j]
                const modifier = [freq1[0] - (freq2[0]), freq1[1] - freq2[1]]
                let antinode1 = [freq1[0] + modifier[0], freq1[1] + modifier[1]];
                let antinode2 = [freq2[0] - modifier[0], freq2[1] - modifier[1]];
                
                while(isOnMap(frequencyMap, antinode1)){
                    antinodeSet.add(antinode1.toString())
                    antinode1[0] += modifier[0]
                    antinode1[1] += modifier[1]
                }

                while(isOnMap(frequencyMap, antinode2)){
                    antinodeSet.add(antinode2.toString())
                    antinode2[0] -= modifier[0]
                    antinode2[1] -= modifier[1]
                }
            }
        }

        for (const frequency of frequencyObj[key]){
            antinodeSet.add(frequency.toString())
        }
    }
    
    frequencyObj['#'] = antinodeSet
    for (const coordinates of frequencyObj['#']){
        const array = coordinates.split(",");
        frequencyMap[parseInt(array[0])][parseInt(array[1])] = '#'
    }
    txt.renderMap(frequencyMap)
    return frequencyObj['#'].size
}

function isOnMap(frequencyMap: string[][], antinode: number[]): boolean {
    const maxLine = frequencyMap.length;
    const maxCol = frequencyMap[0].length;

    if (antinode[0] < 0 || antinode[0] >= maxLine){
        return false
    } else if(antinode[1] < 0 || antinode[1] >= maxCol){
        return false
    }
    return true;
}

function getFrequencyObject(frequencyMap: string[][]): object{ 
    const frequencyObj = {}
    for (const line in frequencyMap){
        for (const col in frequencyMap[line]){
            const frequency = frequencyMap[line][col]
            if (frequency != "."){
                if (!(frequency in frequencyObj)){
                    frequencyObj[frequency] = []
                }
                frequencyObj[frequency].push([parseInt(line), parseInt(col)])
            }
        }
    }
    return frequencyObj;
}

const frequencyMap = processData(rawData);
const answer = findAntinodesInFrequencyMap(frequencyMap)
console.log(answer)