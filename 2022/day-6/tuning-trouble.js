const fs = require('fs')

const detunedString = fs.readFileSync('./input.txt', {encoding: 'utf8'})
const findDuplicates = /(.).*\1/i
const getPacketStart = (detunedString) => {
    for (let i = 0; i < detunedString.length; i++){
        if(!findDuplicates.test(detunedString.slice(i, i + 4))){
            return i + 4;
        }

    }
}

console.log(getPacketStart(detunedString))