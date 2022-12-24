const fs = require('fs')

const data = fs.readFileSync('./input.txt', {encoding: 'utf8'})
const map = data.slice(0, data.indexOf("move"))
const instructionData = data.slice(data.indexOf("move"))
const instructions = instructionData.replace(/(move )|(from )|(to )/g, "").replace(/\n/g, " ").split(" ")
const crates = /\w/g

const generateMap = (map) => {
    const mapArray = [...map.matchAll(crates)]
    const numOfStacks = parseInt(mapArray[mapArray.length - 1])
    const numOfCrates = mapArray.length - numOfStacks
    
    const startingMap = {}

    for (let i = 0; i < numOfCrates; i++){
            let crate = mapArray[i][0]
            let stackNumber = Math.floor(mapArray[i].index / 4) % mapArray[mapArray.length - 1] + 1
            if(startingMap.hasOwnProperty(stackNumber)){
                startingMap[stackNumber].push(crate)
            }
            else {
                startingMap[stackNumber] = [crate]
            }
    }
    return startingMap
}

const moveCrates = (map, instructions) => {
    const crateMap = generateMap(map)
    console.log(crateMap)

    for(let i = 0; i < instructions.length; i += 3){
        let quantity = parseInt(instructions[i])
        let target = instructions[i + 1]
        let destination = instructions[i + 2]
        let liftedCrates = crateMap[target].splice(0, quantity)

        for(const crate of liftedCrates){
            crateMap[destination].unshift(crate)
        }
    }
    
    //Definately a more efficient way to achieve this... Need refactor
    let answer = ""
    for (const pile of Object.keys(crateMap)){
        answer += crateMap[pile][0]
    }

    return answer
}

moveCrates(map, instructions)