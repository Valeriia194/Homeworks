// TASK 1 -----------------------------------------------

// let a = prompt("How old are you?")
// if (a>0&&a<=12){
//     alert("U are children")
// }
// else if(a>12&&a<=18){
//     alert("U are teenager")
// }
// else if(a>18&&a<=60){
//     alert("U are adult")
// }
// else if(a>60){
//     alert("U are pensioner")
// }
// else {
//     alert("No way")
// }

// TASK 2 -----------------------------------------------

// let a = prompt("Enter the number from 0 to 9: ")
// switch (a){
//     case '0': 
//     alert(")");
//     break;

//     case '1': 
//     alert("!");
//     break;
  
//     case '2': 
//     alert("@");
//     break;

//     case '3': 
//     alert("#");
//     break;

//     case '4': 
//     alert("$");
//     break;

//     case '5': 
//     alert("%");
//     break;

//     case '6': 
//     alert("^");
//     break;

//     case '7': 
//     alert("&");
//     break;

//     case '8': 
//     alert("*");
//     break;

//     case '9': 
//     alert("(");
//     break;

//     default:
//     alert("Wrong number!");
// }


// TASK 3 -----------------------------------------------

// let a = prompt("Enter the number: ")
// let one = (a/100)-((a%100)/100)
// let three = a%10
// let two = Math.trunc((a/10)%10)
// if (one==two || one==three || two==three) {
//     alert("Here is similiar numbers!")
// }
// else {
//     alert("No similiar numbers!")
// }

// TASK 4 -----------------------------------------------

// let a = prompt("Enter the year(2000-2132): ")
// if (a%4==0 || a%4000==0){
//    alert("Its leap year!") 
// }
// else {
//     alert("Not leap year!")
// }

// TASK 5 -----------------------------------------------

// let a = prompt("Enter the number:")
// let one = (a/100)-((a%100)/100)
// let three = a%10
// let two = Math.trunc((a/10)%10)
// let result = (three*100)+(two*10)+one
// alert(`Palindrom is: ${result}!`)

// TASK 6 -----------------------------------------------

// let a = prompt("Enter the quantity of dollars: ")
// let b = prompt("Enter the currency(EUR, UAR, AZN): ")
// switch (b) {
//     case "EUR":
//         alert(`U will get ${a*0.95}`)
//         break;
//     case "UAR":
//         alert(`U will get ${a*36.93}`)
//         break;
//     case "AZN":
//         alert(`U will get ${a*1.7}`)
//         break;
// }

// TASK 7 -----------------------------------------------

// let a = prompt("Enter the sum of the purchase: ")
// if (a>=200&&a<=300) {
//     alert(`Your sum with discount ${a - (a*0.03)}`)
// }
// else if (a>300&&a<=500){
//     alert(`Your sum with discount ${a - (a*0.05)}`)
// }
// else if (a>500){
//     alert(`Your sum with discount ${a - (a*0.07)}`)
// }
// else {
//     alert("No discount!")
// }

// TASK 8 -----------------------------------------------

// let a = prompt("Enter the length of circle: ")
// let b = prompt("Enter the perimetre of quadrate: ")
// if (b/(2/Math.sqrt(2)) >= a) {
//     alert("Circle can be in quadrate")
// }  
// else {
//     alert("Circle cant be in quadrate") 
// }

// TASK 9 -----------------------------------------------

// let a = prompt("Cat is an animal? (Yes, No, Partly)");
// let b = prompt("How much questions u need to answer? (3, 1, 15)");
// let c = prompt("The color of sky? (blue, red, green)");
// let rightAnswers = 0;
// switch (a){
//     case 'Yes':
//         rightAnswers = rightAnswers+1;
        
// }
// switch (b){
//     case '3':
//         rightAnswers = rightAnswers+1;
        
// }
// switch (c){
//     case 'blue':
//         rightAnswers = rightAnswers+1;
        
// }
// alert(`U ask right on ${rightAnswers} questions!`)

// TASK 10 -----------------------------------------------

// let day = prompt("Enter the day: ");
// let mon = prompt("Enter the month: ");
// let year = prompt("Enter the year: ");
// let choice = prompt("Show next day, month or year?(d, m, y)")

// if (choice == 'd'){
//     alert(`The date is ${day+=1} ${mon} ${year}`)
// }
// else if (choice == 'm'){
//     alert(`The date is ${day} ${mon+=1} ${year}`)
// }
// else if (choice == 'y'){
//     alert(`The date is ${day} ${mon} ${year+=1}`)
// }