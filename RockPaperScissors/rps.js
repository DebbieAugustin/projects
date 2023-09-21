document.addEventListener("DOMContentLoaded", function() {
    const playerChoiceSelect = document.getElementById("player-choice");
    const difficultySelect = document.getElementById("difficulty");
    const playButton = document.getElementById("play-button");
    const resultSection = document.getElementById("result-section");
    const roundResult = document.getElementById("round-result");
    const score = document.getElementById("score");

    let player_score = 0;
    let computer_score = 0;

    playButton.addEventListener("click", function() {
        const playerChoice = playerChoiceSelect.value;
        const difficulty = difficultySelect.value;
        const computerChoice = getComputerChoice(difficulty);
        const roundResultText = determineRoundResult(playerChoice, computerChoice);
        
        roundResult.textContent = roundResultText;
        score.textContent = `Score => You: ${player_score}, Computer: ${computer_score}`;
        resultSection.classList.remove("hidden");
    });

    function getComputerChoice(difficulty) {
        if (difficulty === "easy") {
            return choices[Math.floor(Math.random() * choices.length)];
        } else if (difficulty === "medium") {
            // Medium difficulty: Computer's choice is somewhat random
            if (playerChoice === "rock") {
                return choices[Math.floor(Math.random() * 3)];
            } else if (playerChoice === "paper") {
                return choices[Math.floor(Math.random() * 3)];
            } else {
                return choices[Math.floor(Math.random() * 3)];
            }
        } else {
            // Hard difficulty: Computer's choice is based on trying to win or tie
            // Implement the hard difficulty logic here
        }
    }

    function determineRoundResult(playerChoice, computerChoice) {
        if (playerChoice === computerChoice) {
            return "It's a tie";
        } else if (
            (playerChoice === "rock" && computerChoice === "scissors") ||
            (playerChoice === "paper" && computerChoice === "rock") ||
            (playerChoice === "scissors" && computerChoice === "paper")
        ) {
            player_score++;
            return "You win";
        } else {
            computer_score++;
            return "Computer wins";
        }
    }
});
