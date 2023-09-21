document.addEventListener("DOMContentLoaded", function() {
    const wordInput = document.getElementById("wordInput");
    const saltSpan = document.getElementById("salt");
    const hashedWordSpan = document.getElementById("hashedWord");
    const hashButton = document.getElementById("hashButton");

    hashButton.addEventListener("click", function() {
        const inputWord = wordInput.value;
        const salt = Math.floor(Math.random() * 10000) + 1;
        const hashedWord = hashWord(inputWord, salt.toString());

        saltSpan.textContent = salt;
        hashedWordSpan.textContent = hashedWord;

        // Show the result div
        const resultDiv = document.querySelector(".result");
        resultDiv.style.display = "block";
    });

    function hashWord(word, salt) {

    }
});