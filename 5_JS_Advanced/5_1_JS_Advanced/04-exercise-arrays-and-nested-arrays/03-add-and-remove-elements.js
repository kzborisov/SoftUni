function addAndRemoveElements(input) {
    let newArr = [];
    let num = 0;

    for (let i = 0; i < input.length; i++) {
        num++;
        let cmd = input[i];

        if (cmd === 'add') {
            newArr.push(num);
        } else if (cmd === 'remove') {
            newArr.pop();
        }
    }

    if (newArr.length === 0) {
        console.log('Empty');
    } else {
        console.log(newArr.join('\n'));
    }
}

addAndRemoveElements(['add', 'add', 'remove', 'add', 'add']);
