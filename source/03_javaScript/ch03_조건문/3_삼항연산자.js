let num1 = 60;
let num2 = 40;
// let difference;
// if(num1>num2){
//     difference = num1-num2;
// }else{
//     difference = num2-num1;

// }
let difference =(num1>num2) ? num1-num2 : num2-num1;
let msg = (num1>num2)? `첫번째 수가 ${difference}만큼 더크다` : 
                (num2>num1)? `두번째 수가 ${difference}만큼 더크다` : '두 수는 같다';
console.log(msg);
