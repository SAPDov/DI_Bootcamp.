//Exercise 1 : Your Favorite Colors
let people = ["Greg", "Mary", "Devon", "James"];
people.splice(0, 1);
console.log(people);
people.splice (2, 1, "Jason");
console.log(people);
people.push("Sapir");
console.log(people);

// Using a loop, iterate through the people array and console.log each person.
for ( let i=0; i< people.length; i++){
console.log (people[i]);
}

// Using a loop, iterate through the people array and after you console.log “Jason” exit the loop.
let people = ["Greg", "Mary", "Devon", "James", "Sapir", "Guy"];
let nameJames = people.indexOf ("James");
for( let i=0; i<=nameJames; i++ ){
console.log(people[i]);
}
// Write code to make a copy of the people array using slice.
 // The copy should NOT include “Mary” or your name.
let people = ["Greg", "Mary", "Devon", "James", "Sapir", "Guy"];
let nameJames = people.indexOf ("James");
people.splice(nameJames, 1);
let myName = people.indexOf ("Sapir");
people.splice(myName, 1);
console.log(people);

// Write code that console.logs Mary’s index. take a look at indexOf on google.
let people = ["Greg", "Mary", "Devon", "James", "Sapir", "Guy"];
console.log (people.indexOf("Mary"));

// Write code that gives the indexOf “Foo” (this should return -1). Why does it return -1
console.log (people.indexOf("Foo")); //when an element can not be found in the array it returns -1 - like Foo

// Create a variable called last which value is the last element of the array.
let people = ["Greg", "Mary", "Devon", "James", "Sapir", "Guy"];
// let last = people.pop();
// console.log(last);
console.log(people.indexOf("Guy"));
console.log(people);
console.log(people.length);

// Hint: What is the relationship between the index of the last element in the array and the length of the array? // 
// (-1) length starts from 0 and indexOf search for location which starts from 0

// Exercise 3 : Repeat The Question

// Instructions


let number = prompt("Pick a number");
let number =0;
let i =0;
do {
let i = prompt("Pick a number");
i++;
} while (i < 10); 

for(let i=0; i=0; i++){
let number = prompt("Pick a number");

	if(number>10){
		i++
	}
	else{
	let number = prompt("Pick a number");

}
}



// Prompt the user for a number, while the number is smaller than 10 continue asking the user for a new number.
// Tip : Which while loop is more relevant for this situation?
// Hint : Check the data type you receive from the prompt (ie. typeof method)