//Exercise 1: Simple If/Else Statement
let x = 5;
let y = 2;
if (x > y){
	console.log( x + " is a bigger number");
}
else{
	console.log( y + " is a bigger number");
}

//Exercise 2: Chihuahua
	let newDog = "Chihuahua";
	let count = newDog.length;
	console.log(count);
	console.log(newDog.toUpperCase());
	console.log(newDog.toLowerCase());

if(newDog === "Chihuahua"){
	console.log("I love Chihuahuas, it’s my favorite dog breed");
}
else{
	console.log("I dont care, I prefer cats");
}

//Exercise 3: Even Or Odd
let number = prompt("please choose a random number");
if(number%2===0){
	console.log(number + " is an even number");
}
else{
	console.log(number + " is an odd number");
}

//Exercise 4: Group Chat
let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
let count = users.length;
console.log(count);

if(count===0){
	console.log ("no one is online.");
}
else if (count===1){
	console.log(users[0] + " is online");
}
else if (count===2){
	console.log(users[0] + " and " + users[1] + " are online");
}

else{
	count = count - 2;
	console.log(users[0] + ", " + users[1] + " and " + count + " more are online");
}
