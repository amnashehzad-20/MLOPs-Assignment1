let timer;
let timeLeft = 25 * 60;
let isRunning = false;
let isBreak = false;
const workTime = 25 * 60;
const breakTime = 5 * 60;

function startPomodoro() {
    if (isRunning) return;
    isRunning = true;

    timer = setInterval(() => {
        if (timeLeft > 0) {
            timeLeft--;
            updateTimerDisplay();
        } else {
            clearInterval(timer);
            if (!isBreak) {
                alert("Time's up! Take a break!");
                startBreak();
            } else {
                alert("Break's over! Back to work!");
                resetTimer();
            }
        }
    }, 1000);
}

function startBreak() {
    isBreak = true;
    timeLeft = breakTime;
    isRunning = false;
    updateTimerDisplay();
    updateTimerLabel();
}

function resetTimer() {
    clearInterval(timer);
    isBreak = false;
    timeLeft = workTime;
    isRunning = false;
    updateTimerDisplay();
    updateTimerLabel();
}

function updateTimerDisplay() {
    const minutes = Math.floor(timeLeft / 60);
    const seconds = timeLeft % 60;
    document.getElementById("timer").innerText = `${minutes}:${seconds < 10 ? "0" : ""}${seconds}`;
}

function updateTimerLabel() {
    document.getElementById("timer-label").innerText = isBreak ? "Break Time" : "Work Time";
}
