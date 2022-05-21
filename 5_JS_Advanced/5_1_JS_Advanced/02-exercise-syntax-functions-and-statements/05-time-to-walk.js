function timeToWalk(stepsCnt, footprintLengthInMeters, speedInKmH) {
    let distance = (stepsCnt * footprintLengthInMeters) / 1000; // In kilometers
    let bonusTime = Math.floor(distance / 0.5) * 60; // In seconds
    let totalHours = distance / speedInKmH;
    let totalSeconds = totalHours * 3600 + bonusTime;

    let hours = Math.floor(totalSeconds / 3600);
    let minutes = Math.floor(totalSeconds / 60);
    let seconds = Math.round(totalSeconds - hours * 3600 - minutes * 60);

    hours = hours < 10 ? `0${hours}` : hours;
    minutes = minutes < 10 ? `0${minutes}` : minutes;
    seconds = seconds < 10 ? `0${seconds}` : seconds;

    console.log(hours + ':' + minutes + ':' + seconds);
}

timeToWalk(4000, 0.6, 5);
timeToWalk(2564, 0.7, 5.5);
