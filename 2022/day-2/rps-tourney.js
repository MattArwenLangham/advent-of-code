const fs = require('fs')

const data = fs.readFileSync('./input.txt', {encoding: 'utf8'})
input = data.replaceAll("\n", "").split("\r")

const moveScores = {
    A: {X: 4, Y: 8, Z: 3},
    B: {X: 1, Y: 5, Z: 9},
    C: {X: 7, Y: 2, Z: 6}
}

const calculateTourneyScore = (input) => {
    let score = 0;
    for (const round of input){
        score += moveScores[round[0]][round[2]]
    }
    return score
}

console.log(calculateTourneyScore(input))