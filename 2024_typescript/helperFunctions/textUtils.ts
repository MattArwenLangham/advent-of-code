import * as fs from 'fs';


/**
 * Reads and returns a file as a string.
 * @param filePath - Path to the file to read.
 * @returns File data as string
 */
export function getData(filePath: string): string {
    try {
        return fs.readFileSync(filePath, 'utf8');
    } catch (error) {
        console.error(`Error reading file at ${error}: `, error);
        return "";
    }
}
