const fs = require('fs')

const data = fs.readFileSync('./input.txt', {encoding: 'utf8'})
input = data.split("\r")

const highestCalories = (input) => {
    let currentCalorieCount = 0
    let highestCalorieCount = 0
    for (calories of input){
        calories = parseInt(calories)
    
        if(!calories){
            if (currentCalorieCount > highestCalorieCount){
                highestCalorieCount = currentCalorieCount
            }
            currentCalorieCount = 0
        } else {
            currentCalorieCount += calories
        }
    }
    return highestCalorieCount
}

console.log(highestCalories(input))