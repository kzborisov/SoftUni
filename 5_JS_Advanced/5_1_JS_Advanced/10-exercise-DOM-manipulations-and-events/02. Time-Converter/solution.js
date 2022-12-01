function attachEventsListeners() {
    const days = document.getElementById("days");
    const hours = document.getElementById("hours");
    const minutes = document.getElementById("minutes");
    const seconds = document.getElementById("seconds");

    document.getElementById("daysBtn").addEventListener("click", () => {
        const currDays = Number(days.value);

        hours.value = currDays * 24;
        minutes.value = currDays * 24 * 60;
        seconds.value = currDays * 24 * 60 * 60;
    });

    document.getElementById("hoursBtn").addEventListener("click", () => {
        const currHour = Number(hours.value);

        days.value = currHour / 24;
        minutes.value = currHour * 60;
        seconds.value = currHour * 60 * 60;
    });
    document.getElementById("minutesBtn").addEventListener("click", () => {
        const mins = Number(minutes.value);

        days.value = mins / (60 * 24);
        hours.value = mins / 60;
        seconds.value = mins * 60;
    });

    document.getElementById("secondsBtn").addEventListener("click", () => {
        const secs = Number(seconds.value);

        days.value = secs / (60 * 60 * 24);
        hours.value = secs / (60 * 60);
        minutes.value = secs / 60;
    });
}
