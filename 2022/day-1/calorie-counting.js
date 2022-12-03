const fs = require('fs')

const data = fs.readFileSync('./input.txt', {encoding: 'utf8'})
input = data.split("\r")

const topThree = []

const highestCalories = (input) => {
    let currentCalorieCount = 0
    let highestCalorieCount = topThree[0]
    for (calories of input){
        calories = parseInt(calories)
    
        if(!calories){
            if (currentCalorieCount > highestCalorieCount){
                topThree.push(currentCalorieCount)
            }
            currentCalorieCount = 0
        } else {
            currentCalorieCount += calories
        }
    }
    return highestCalorieCount
}

console.log(highestCalories(input))