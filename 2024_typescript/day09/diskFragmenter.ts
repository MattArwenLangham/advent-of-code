import * as txt from '../helperFunctions/textUtils'

const filePath = txt.getDir(import.meta.url, false);
const rawData = txt.getData(filePath)

function processData(rawData: string): string {
    return rawData;
}

function fragmentDisk(diskMapArray: string){
    let pt1 = 0;
    let pt2 = diskMapArray.length - 1;
    let pt2FilesizeLeft = 0;
    const finalFragmentedDiskArray: number[] = []

    while (pt2 - pt1 - 1 > 0){
        const file = diskMapArray[pt1]
        //last iteration
        if (pt2 - pt1 === 2){
            for (let i = 0; i < parseInt(diskMapArray[pt1]); i++){
                finalFragmentedDiskArray.push(pt1 / 2)
            }
            pt1++
            for (let i = 0; i < pt2FilesizeLeft; i++){
                finalFragmentedDiskArray.push(pt2 / 2)
            }
            break;
        }

        if (pt1 % 2 == 0){
            for (let i = 0; i < parseInt(diskMapArray[pt1]); i++){
                finalFragmentedDiskArray.push(pt1 / 2)
            }
        } else {
            let fileSize = pt2FilesizeLeft ? pt2FilesizeLeft : parseInt(diskMapArray[pt2])
            for (let i = 0; i < parseInt(diskMapArray[pt1]); i++){
                finalFragmentedDiskArray.push(pt2 / 2)
                fileSize--
                if (fileSize == 0 && pt2 - 2 > pt1){
                    pt2 -= 2;
                    fileSize = parseInt(diskMapArray[pt2])
                }
            }
            pt2FilesizeLeft = fileSize
        }
        pt1++
    }
    return finalFragmentedDiskArray
}

function generateDiskArrayCheckSum(diskArray: number[]){
    let checkSum = 0;
    for (const num in diskArray){
        checkSum += parseInt(num) * diskArray[num];
    }
    return checkSum
}

const diskMap = processData(rawData)
const finalFragmentedDiskArray = fragmentDisk(diskMap);
console.log(finalFragmentedDiskArray);
const checkSum = generateDiskArrayCheckSum(finalFragmentedDiskArray);

console.log(checkSum)