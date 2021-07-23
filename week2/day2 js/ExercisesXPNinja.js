//Exercise 1 : Age Difference
let yearY = 1991;
let yearO = 1970;
let age1 = 2021 - yearY;
let age2 = 2021 - yearO;
let halfAge = age2/2;


halfAge = halfAge.toFixed(0);
halfAge = parseInt(halfAge);
console.log("The date when the younger one is exactly half the age of the older one is " + (yearY+ halfAge));

//Exercise 2 : Zip Codes- Not Succeded
let zipCode = prompt("What is your zip code?");
let length = zipCode.length;
let space = zipCode.indexOf(" ");
let number = typeof(zipCode);

if(length === 5 && space === flase && number === number){


}
else{
	console.log("success");
}


//Exercise 2 : Zip Codes- Not Succeded

let zip = prompt("What is your zip code?");
let patt = /[A-Za-z]/;
let isExisting = zip.match(patt);
console.log(isExisting);