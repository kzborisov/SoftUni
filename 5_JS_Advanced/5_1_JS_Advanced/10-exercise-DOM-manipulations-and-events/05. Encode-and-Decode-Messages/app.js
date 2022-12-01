function encodeAndDecodeMessages() {
    const [encodeBtn, decodeBtn] = [...document.querySelectorAll("button")];
    const [input, output] = [...document.querySelectorAll("textarea")];

    encodeBtn.addEventListener("click", encodeAndSent);
    decodeBtn.addEventListener("click", decodeAndRead);

    function encodeAndSent() {
        let encodedStr = "";
        [...input.value].forEach((c) => {
            encodedStr += processChar("encode", c);
        });
        output.value = encodedStr;
        input.value = "";
    }

    function decodeAndRead(e) {
        let decodedStr = "";
        [...output.value].forEach((c) => {
            decodedStr += processChar("decode", c);
        });
        output.value = decodedStr;
    }

    function processChar(type, c) {
        return type == "encode"
            ? String.fromCharCode(c.charCodeAt() + 1)
            : String.fromCharCode(c.charCodeAt() - 1);
    }
}
