let timer;
let timeLeft = 25 * 60;
let isRunning = false;

function startPomodoro() {
    if (isRunning) return;
    isRunning = true;

    timer = setInterval(() => {
        if (timeLeft > 0) {
            timeLeft--;
            updateTimerDisplay();
        } else {
            clearInterval(timer);
            alert("Time's up! Take a break!");
            resetTimer();
        }
    }, 1000);
}

function resetTimer() {
    clearInterval(timer);
    timeLeft = 25 * 60;
    isRunning = false;
    updateTimerDisplay();
}

function updateTimerDisplay() {
    const minutes = Math.floor(timeLeft / 60);
    const seconds = timeLeft % 60;
    document.getElementById("timer").innerText = `${minutes}:${seconds < 10 ? "0" : ""}${seconds}`;
}
