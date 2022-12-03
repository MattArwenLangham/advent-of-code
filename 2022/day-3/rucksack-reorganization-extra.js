const fs = require('fs')

const data = fs.readFileSync('./input.txt', {encoding: 'utf8'})
input = data.replaceAll("\n", "").split("\r")

const compartmentCheck = (compartment1, compartment2, compartment3) => {
    for (const item of compartment1){
        if(compartment2.includes(item) && compartment3.includes(item)){
            return item
        }
    }
}

const itemToPriority = (commonItem) => {
    let commonItemValue = commonItem.charCodeAt()
    if(commonItemValue <= 90) commonItemValue -= 38
    else commonItemValue -= 96

    return commonItemValue
}

const rucksackSum = (input) => {
    let itemSum = 0
    for (let i = 0; i < input.length; i += 3){
        let commonItem = compartmentCheck(input[i], input[i + 1], input[i + 2])
        itemSum += itemToPriority(commonItem)
    }
    return itemSum
}

console.log(rucksackSum(input))