var subValue = 2;
var iteration = 1;
var pi = 3;

function calculatePi() {
    while (true) {
        if (iteration % 2 != 0) {
            pi += (4 / (subValue * (subValue + 1) * (subValue + 2)));
        }

        else {
            pi -= (4 / (subValue * (subValue + 1) * (subValue + 2)));
        }

        subValue += 2;
        iteration += 1;

        console.log(pi)
    }
}

calculatePi();