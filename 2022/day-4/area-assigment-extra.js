const fs = require('fs')

const data = fs.readFileSync('./input.txt', {encoding: 'utf8'})
const input = data.split(/[^0-9]/g)

const areaAssignment = (input) => {
    let overlaps = 0
    for (let i = 0; i < input.length; i += 5){
        let elf1Start = parseInt(input[i])
        let elf1End = parseInt(input[i + 1])
        let elf2Start = parseInt(input[i + 2])
        let elf2End = parseInt(input[i + 3])

        if (!(elf1End < elf2Start) && !(elf2End < elf1Start)) overlaps++
    }
    return overlaps
}

console.log(areaAssignment(input))