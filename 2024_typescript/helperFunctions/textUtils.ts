import * as fs from 'fs';
import * as path from 'path';
import { fileURLToPath, Url } from 'url';

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

/**
 * Gets current directory when import.meta.url is inserted into the prompt.
 * @param url - import.meta.url
 * @param test - whether or not it should retrieve test file or not
 * @returns directory and filename
 */
export function getDir(url: URL|string, test: boolean = false): string {
    const __filename = fileURLToPath(url);
    const __dirname = path.dirname(__filename);
    const directory = path.basename(__dirname);
    const filename = test ? "test-input.txt" : "input.txt"
    return directory + "/" + filename
}