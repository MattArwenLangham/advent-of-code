const fs = require('fs')

const data = fs.readFileSync('./input.txt', {encoding: 'utf8'})
input = data.replaceAll("\n", "").split("\r")


const moveScores = {
    A: {X: 3, Y: 1 + 3, Z: 2 + 6},
    B: {X: 1, Y: 2 + 3, Z: 3 + 6},
    C: {X: 2, Y: 3 + 3, Z: 1 + 6}
}

const calculateTourneyScore = (input) => {
    let score = 0;
    for (const round of input){
        score += moveScores[round[0]][round[2]]
    }
    return score
}

console.log(calculateTourneyScore(input))