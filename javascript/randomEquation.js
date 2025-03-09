let randomEquation = () => {
    let num1, num2;
    do {
        num1 = Math.floor(Math.random() * 10);
        num2 = Math.floor(Math.random() * 10);
    } while (num1 < num2);

    let answer;
    let operator = ['+', '-', '*', '/'][Math.floor(Math.random() * 4)];
    switch (operator) {
        case '+':
            answer = num1 + num2;
            break;
        case '-':
            answer = num1 - num2;
            break;
        case '*':
            answer = num1 * num2;
            break;
        case '/':
            if (num2 !== 0) {
                answer = (num1 / num2).toFixed(2);
                answer = parseFloat(answer);
            } else {
                answer = NaN;
            }
            break;
        default:
            answer = NaN;
            break;
    }

    let playerAnswer = prompt(`What is ${num1} ${operator} ${num2}? (in case of a division, round to 2 decimal places)`);
    if (parseFloat(playerAnswer) === answer) {
        console.log('Correct!');
        randomEquation();
    } else {
        console.log('Incorrect!');
        randomEquation();
    }
}

randomEquation();