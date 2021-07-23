// 1 Create a variable called sentence. The value of the variable should be a string that 
// contains the words “not” and “bad”. For example, “The movie is not that bad, I like it”.
// 2 Create a variable called wordNot where it’s value is the first appearance of the substring “not” 
// (from the sentence variable).
// 3 Create a variable called wordBad where it’s value is the first appearance of the substring “bad” 
// (from the sentence variable).
// 4 If the word “bad” comes after the word “not”, you should replace the whole “not…bad” 
// substring with “good”, then console.log the result.
// 5 For example, the result here should be : “The movie is good, I like it”
// If the word “bad” does not come after “not” or the words are not in the sentence, 
// console.log the original sentence.

let sentence = prompt ("What is your sentence?");
let re = /not/;
let not = sentence.includes ("not");
let bad = sentence.includes ("bad");
let wordNot = sentence.indexOf("not");
let wordBad = sentence.indexOf("bad");

if (not === true && bad === true && not < bad){

	
 console.log();

}
else {
	console.log(sentence);
}

// var str = "I dont like not to to bad ";
// alert(str.split("not").pop());//to to bad
// var str2 = "another ont and not bad"; //no output nothing
// alert(str2.split("not bad").pop());



// Your string is : 'This dinner is not that bad ! You cook well', 
//   --> the result is : 'This dinner is good ! You cook well'

//   Your string is : 'This movie is not so bad!' 
//   --> the result is : 'This movie is good!'

//   Your string is : 'This dinner is bad!' 
//   --> the result is : 'This dinner is bad!'