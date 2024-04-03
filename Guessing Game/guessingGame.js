var numGuesses = 10

function compare(){
    var secretNumber = parseInt(Math.random() * 101);  //  0 to 100
    let guess = document.getElementById("guess1").value;
    document.getElementById("Guesses").innerHTML = "Guesses Left: " + (numGuesses - 1);
    if (numGuesses != 1){
        if (guess == secretNumber){
            alert("This is correct. YOU WON!!!!!");
        }
        else if (guess > secretNumber){
            numGuesses = numGuesses - 1;
            alert("Guess lower");
        }
        else if (guess < secretNumber){
            numGuesses = numGuesses - 1;
            alert("Guess higher");
        }
    }
    else{
        if (guess == secretNumber){
            alert("This is correct. YOU WON!!!!!!");
        }
        else{
            numGuesses = numGuesses - 1;
            alert("You have lost the game. Click on the replay button to play again");
            document.getElementById("guessButton").disabled = true;
        }
    }
    document.getElementById("guess1").value = "";
}

function play_again(){
    numGuesses = 10;
    var secretNumber = (Math.random() * 101);  //  0 to 100
    document.getElementById("guessButton").disabled = false;
    document.getElementById("Guesses").innerHTML = "Guesses Left: " + numGuesses;
} 

function disappear(){
    document.getElementById("uguess").hidden = true;
    document.getElementById("Submit").hidden = true;
}

function compare2(){
    let secretNumber = document.getElementById("uguess").value;
    let guess = document.getElementById("guess1").value;
    document.getElementById("Guesses").innerHTML = "Guesses Left: " + (numGuesses - 1);
    if (numGuesses != 1){
        if (guess == secretNumber){
            alert("This is correct. YOU WON!!!!!");
        }
        else if (guess > secretNumber){
            numGuesses = numGuesses - 1;
            alert("Guess lower");
        }
        else if (guess < secretNumber){
            numGuesses = numGuesses - 1;
            alert("Guess higher");
        }
    }
    else{
        if (guess == secretNumber){
            alert("This is correct. YOU WON!!!!!!");
        }
        else{
            numGuesses = numGuesses - 1;
            alert("You have lost the game. Click on the replay button to play again");
            document.getElementById("guessButton").disabled = true;
            document.getElementById("guess1").disabled = true;
        }
    }
    document.getElementById("guess1").value = "";
}
function play_again2(){
    numGuesses = 10;
    document.getElementById("guessButton").disabled = false;
    document.getElementById("guess1").disabled = false;
    document.getElementById("uguess").hidden = false;
    document.getElementById("Submit").hidden = false;
    document.getElementById("Guesses").innerHTML = "Guesses Left: " + numGuesses;
} 
