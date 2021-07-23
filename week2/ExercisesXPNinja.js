
//Exercise 1 : Find Nemo
let nemo = prompt("Please give us a sentence containing the word Nemo");
let findNemo = nemo.indexOf("Nemo");
let findNemo1 = nemo.indexOf("nemo");


if(findNemo !== -1 && findNemo1 ===-1){
	
	findNemo++;
	console.log("I found Nemo at the position " + findNemo);
}

if(findNemo === -1 && findNemo1 !==-1){
	findNemo1++;
	console.log("I found Nemo at the position " + findNemo1);

}
else {
	console.log("“I can’t find Nemo”");
}

//Exercise 1 : Evaluation
	5 >= 1//true
    0 === 1//false
    4 <= 1//false
    1 != 1//false
    "A" > "B"//false
    "B" < "C"//true
    "a" > "A"//true
    "b" < "A"//false
    true === false//false
    true != true//false

//Exercise 2 : Evaluation(2)
    let c; //c has no value - undifined
    let a = 34; 
    let b = 21;
    a = 2; //a=2
    console.log(a + b); //2+21=23 

    console.log(3 + 4 + '5'); //output 75


//Exercise 4 : BOOM//didn't finish yet
let number = prompt("Please choose a random number");

if(number > 2){
	let repeat = "o".repeat(number-2);													
	if(number%5===0 && number%2===0){
		repeat = repeat.toUpperCase();
		console.log("BO"+ repeat +"OM!")
	}
	else if (number%5===0){
		repeat = repeat.toUpperCase();
		console.log("BO"+ repeat +"OM");
	}
	else if (number%2===0){
		console.log("bo"+ repeat +"om!");
	}
}

else {
	console.log("boom");
}


