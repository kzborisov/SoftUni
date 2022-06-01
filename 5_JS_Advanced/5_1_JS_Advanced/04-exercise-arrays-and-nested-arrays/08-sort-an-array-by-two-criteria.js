function sortByTwoCriteria(input) {
    return input
        .sort((a, b) => {
            if (a.length === b.length) {
                return a.localeCompare(b);
            }
            return a.length - b.length;
        })
        .join('\n');
}

console.log(sortByTwoCriteria(['alpha', 'beta', 'gamma']));
