function colorize() {
    const rows = document.querySelectorAll('tr:nth-child(2n)');
    for (let i = 0; i < rows.length; i++) {
        rows[i].style.background = 'teal';
    }
}
