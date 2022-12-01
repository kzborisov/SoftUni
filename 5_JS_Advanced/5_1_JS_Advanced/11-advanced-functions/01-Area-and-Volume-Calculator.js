function solve(area, vol, input) {
    return JSON.parse(input).map((fig) => ({
        area: area.call(fig),
        volume: vol.call(fig),
    }));
}

function area() {
    console.log(this);
    return Math.abs(this.x * this.y);
}

function vol() {
    return Math.abs(this.x * this.y * this.z);
}

console.log(
    solve(
        area,
        vol,
        `
[
{"x":"1","y":"2","z":"10"},
{"x":"7","y":"7","z":"10"},
{"x":"5","y":"2","z":"10"} 
]`
    )
);
