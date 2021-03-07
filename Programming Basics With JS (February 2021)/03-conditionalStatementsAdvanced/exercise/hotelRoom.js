// Task 8 - On Time For Exam

function onTimeForExam(input) {
    // Read Input Data
    let examHour = Number(input[0]);
    let examMinute = Number(input[1]);
    let arivalHour = Number(input[2]);
    let arrivalMinute = Number(input[3]);
   
    // Logic
    let examTotalTime = (examHour * 60) + examMinute;
    let arivalTotalTime = (arivalHour * 60) + arrivalMinute;

    let status = "";
    let result = "";

    if (examTotalTime < arivalTotalTime) {
        status = "Late";
    } else if (examTotalTime === arivalTotalTime || examTotalTime <= arivalTotalTime + 30) {
        status = "On time";
    } else if (examTotalTime > arivalTotalTime) {
        status = "Early";
    }



    if (!(examTotalTime === arivalTotalTime)) {
        let hour = Math.floor(Math.abs((examTotalTime - arivalTotalTime) / 60));
        let minutes = Math.abs((examTotalTime - arivalTotalTime) % 60);

        if (hour >= 1 && minutes < 10) {
            minutes = `0${minutes}`;
        }

        if (status === "Late" && hour >= 1) {
            result = `${hour}:${minutes} hours after the start`;
        } else if(status === "Late") {
            result = `${minutes} minutes after the start`;
        } else if (status === "Early" && hour >= 1) {
            result = `${hour}:${minutes} hours before the start`;
        } else if (status === "Early" || status === "On time") {
            result = `${minutes} minutes before the start`;
        }
    }

    // Print Result
    console.log(status);
    console.log(result);
}

onTimeForExam(["14",
"00",
"13",
"55"]);