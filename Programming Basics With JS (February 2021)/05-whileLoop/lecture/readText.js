// Task 1 - Read Text

function readText(input) {
    while (true) {
        let text = input.shift();
        if (text === "Stop"){
            break;
        }
        console.log(text);
    }
}

readText(["Nakov",
"SoftUni",
"Sofia",
"Bulgaria",
"SomeText",
"Stop",
"AfterStop",
"Europe",
"HelloWorld"]);