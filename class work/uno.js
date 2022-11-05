//1 2 3 4 5 6 7 8 9 wild, skip, reverse,
let playerTurn = true;
let start = false;
let placeCard = {"type" : 2, "color": 4};
//Create a throw away list and make it add used cards until there are no more cards to be used
//use -1 in the object to find the last one.
let playerCards = {};
let botCards = {};
let playable = false;

let gameRules = {
	pluckAndPlay: false,
	stacking: false,
	drawTilPlay: false,
}

const colorNum = [1, 2, 3, 4];
//1=blue, 2=green, 3=yellow, 4=red
// all numbers are the same numbers as they are and 10 is skips, 11, reverses, 12, is wild card, 13 is plus 4
const typeNum = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 13];
const typeCOmp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

let i = 0;
let x = 0;
//x is = to the starting number of cards. to begin with assigned later on

//actually does the dealing mechanic
function intialDeal(playerCards, botCards, colorNum, typeNum, x) {
	for (let i = 0; i < x; i++) {
		//gives the player its cards.
		playerCards[i] = {};
		playerCards[i]["type"] = typeNum[Math.floor(Math.random() * typeNum.length)];
		playerCards[i]["color"] = colorNum[Math.floor(Math.random() * colorNum.length)];
		//Gives the bots its card.
		botCards[i] = {};
		botCards[i]["type"] = typeNum[Math.floor(Math.random() * typeNum.length)];
		botCards[i]["color"] = colorNum[Math.floor(Math.random() * colorNum.length)];
		//add dupe checker HERE
	}
	return playerCards, botCards, start = true;
}


function dealing(playerCards, botCards, colorNum, typeNum, x, start) {
	//does all of the dealing logic.
	intialDeal(playerCards, botCards, colorNum, typeNum, x);
	//put a if instatement into here for pluck and play.
}


// Stratagies for uno series
function combined(botCards, args) {
	let totalType = [];
	for (let i = 0; i < Object.keys(botCards).length; i++) {
		if (botCards[i]["type"] == args) {
			possible = true;
			console.log("hello");
			if (possible == true) {
				totalType.push(botCards[i]);
			}
		} else {
			return false;
		}
	}
	return totalType;
}


function bot(playerCards, botCards, colorNum, typeNum, x, start, playerTurn, placeCard) {
	let args;
	for (let i = 0; i < Object.keys(botCards); i++) {
		botCards[i]["type"]
	} 
	let series =	combined(botCards, args);
	let possibles = checkerBots(botCards, colorNum, typeNum, x, placeCard, combined);
	console.log(series);
	console.log(possibles);
	// add a loop to check for cards with the same number but different colors or same colors and then make sure that they stay together.
	// This loop will check back and pass the info onto the checker and it will find all other ones and if there isnt any other the just use from the series. 
}


function checkerBots(botCards, colorNum, typeNum, x, placeCard, combined) {
	//checks for card aviablility
	//Adds number of keys from the object to the list for checking
	// array used to store possible working 
	let possibleNums = [];
  for (let i = 0; i < Object.keys(botCards).length; i++) { 
    if (botCards[i]["type"] == placeCard["type"] || botCards[i]["color"] == placeCard["color"]) {
			possible = true; 
			//checks if its possible to prevent error
			if (possible == true) {
				possibleNums.push(botCards[i]);
			}
		} else {
			return false;
		}	
	}
	return possibleNums;
}


function checkerPlayers (playerCards, colorNum, typeNum, x) {
	//checks
}


function repeatChecker(playerCards,colorNum, botCards, typeNum, x, start) {
	// need to add in checks to see if there are too many dupes of a card.
}

function placer(playerCards, colorNum, botCards, typeNum, x, start) {
	//TODO: have it remove the players or the bot cards from the deck. 
}

function game(playerCards, botCards, colorNum, typeNum, x, start, playerTurn, placeCard, combined) {
	//Add placing cards
	//stacking logic needs to be added
	if (start == false) {
		x = 7;
		dealing(playerCards, botCards, colorNum, typeNum, x, start);
	}
	bot(playerCards, botCards, colorNum, typeNum, x, start, playerTurn, placeCard);
}

game(playerCards, botCards, colorNum, typeNum, x, start, playerTurn, placeCard, combined);

console.log(botCards);
//Refefrence repl.it