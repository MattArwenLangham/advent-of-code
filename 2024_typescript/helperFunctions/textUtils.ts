import * as fs from 'fs';

/**
 * Reads a file and splits its content into an array of strings.
 * @param filePath - Path to the file to read.
 * @param separator - Separator for splitting the file content (default: "\r?\n").
 * @returns An array of strings containing the split file content.
 */
export function toArray(filePath: string, seperator: string = "\r"): string[] {
    try {
        const data: string = fs.readFileSync(filePath.toString(), 'utf8');
        return data.split(seperator);
    } catch (error) {
        console.error(`Error reading file at ${error}: `, error);
        return [];
    }
}

