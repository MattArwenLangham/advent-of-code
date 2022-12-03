const fs = require('fs')

const data = fs.readFileSync('./input.txt', {encoding: 'utf8'})
input = data.replaceAll("\n", "").split("\r")

const compartmentCheck = (compartment1, compartment2) => {
    for (const item of compartment1){
        if(compartment2.includes(item)) return item
    }
}

const rucksackSum = (input) => {
    let itemSum = 0
    for (const rucksack of input){
        let split = Math.ceil(rucksack.length / 2)
        let compartment1 = rucksack.slice(0, split)
        let compartment2 = rucksack.slice(split, rucksack.length)
        
        let commonItem = compartmentCheck(compartment1, compartment2)
        let commonItemValue = commonItem.charCodeAt()
        if(commonItemValue <= 90){
            commonItemValue -= 38
        } else {
            commonItemValue -= 96
        }
        itemSum += commonItemValue
    }
    return itemSum
}

console.log(rucksackSum(input))