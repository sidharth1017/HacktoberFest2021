
var randomNumber1=Math.floor(Math.random() * 6)+1;


var randomDiceImage="dice"+ randomNumber1 + ".png";

var randomImageSource="images/"+ randomDiceImage;

var image1=document.querySelectorAll("img")[0];
image1.setAttribute("src",randomImageSource);

var randomNumber2;
randomNumber2=Math.floor(Math.random() * 6) +1;


var randomImageSource2="images/dice"+ randomNumber2 + ".png";
document.querySelectorAll("img")[1].setAttribute("src",randomImageSource2);

if (randomNumber1 > randomNumber2){
  document.querySelector("h1").innerHTML="Player 1 Wins!✨";
}
else if (randomNumber1 == randomNumber2) {
  document.querySelector("h1").innerHTML="Draw!👀";

}
else{
  document.querySelector("h1").innerHTML="Player 2 Wins!✨";
}
