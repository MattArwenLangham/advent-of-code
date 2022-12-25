class Folder {
    constructor(name, parent = null, children){
        this.name = name
        this.parent = parent
        this.children = []
    }
}

const root = new Folder("root")

const fs = require('fs')

const instructions = fs.readFileSync('./test-input.txt', {encoding: 'utf8'}).split("\n")

const fileSystem = {
        "/": root
}

const createFileSystem = (instructions) => {
    let currDir = "/"
    for(let instruction of instructions){
        const commands = instruction.split(" ")

        if(commands[0] === "$"){
            let command = commands[1]
            if(command === "cd"){
                const path = commands[2]
                switch(path){
                    case "..":
                        currDir = fileSystem[currDir].parent
                    break
                    default:
                        currDir = path
                    break
                }
            }
        } else if (commands[0] === "dir"){
            const folderName = commands[1]
            fileSystem[folderName] = new Folder(folderName, currDir)
            fileSystem[currDir].children.push(fileSystem[folderName])

        } else if (parseInt(commands[0]) !== NaN) {
            const fileName = commands[1]
            const fileSize = parseInt(commands[0])
            fileSystem[currDir][fileName] = parseInt(fileSize)
        }
    }
    console.log(fileSystem["/"])
}

createFileSystem(instructions)