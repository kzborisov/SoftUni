function attachGradientEvents() {
    const box = document.getElementById("gradient");
    box.addEventListener("mousemove", onMouseMove);

    function onMouseMove(e) {
        const currentPos = Math.floor((e.offsetX / e.target.clientWidth) * 100);
        document.getElementById("result").textContent = `${currentPos}%`;
    }
}
