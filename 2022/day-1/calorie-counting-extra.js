const fs = require('fs')

const data = fs.readFileSync('./input.txt', {encoding: 'utf8'})
input = data.split("\r")
input.push("\n")
const topThree = [0, 0, 0]

const highestThreeCalories = (input) => {
    let currentCalorieCount = 0
    let calorieThreashold = topThree[0, 0, 0]

    for (calories of input){
        calories = parseInt(calories)
    
        if(!calories){
            if (currentCalorieCount > calorieThreashold){
                topThree[0] = currentCalorieCount
                topThree.sort((a,b) => a-b)
            }
            currentCalorieCount = 0
            
        } else {
            currentCalorieCount += calories
        }
    }
    return topThree.reduce((prev, curr) => prev + curr)
}

console.log(highestThreeCalories(input))