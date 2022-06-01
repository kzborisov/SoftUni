function listOfNames(names) {
    return names
        .sort((a, b) => a.localeCompare(b))
        .map((x, i) => `${i + 1}.${x}`)
        .join('\n');
}

console.log(listOfNames(['John', 'Bob', 'Christina', 'Ema']));
