//Exercise 1 : The World Translator
let name = prompt ("Which language do you speak? ");
name= name.toLowerCase();

if(name === "french"){ 
	console.log("Bonjour");
}

else if(name === "english"){
	console.log("Hello");

}
else if(name === "hebrew"){
	console.log("Shalom");
}
else{
	console.log("01110011 01101111 01110010 01110010 01111001");
}

//Exercise 2 : The Grade Assigner
let grade = prompt ("What is your grade?");
if(grade > 90){
	console.log("A");
}
else if(grade > 80 && grade <=90){
	console.log("B");
}
else if(grade >= 70 && grade <= 80){
	console.log("C");
}
else{
	console.log("D");
}

//Exercise 3 : Verbing
let verb = prompt ("Please pick a word - It must be a verb.");
let ing = verb.includes("ing");
let count = verb.length;
if (count > 3 && ing === true){
	console.log(verb +"ly");
}
else if (count > 3 && ing === false){
		let e = verb.substring (count-1);
	if (e === e){
		verb = verb.slice(0, -1);
		console.log(verb +"ing");
	}
	else {
		console.log(verb +"ing");
	}
}
else{
	console.log(verb);
}
