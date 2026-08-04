//var : 변수 선언시 사용. 변수의 재선언 가능. 전역변수로 사용
//let : 변수 선언시 사용. 변수의 재선언 불가. 블록 레벨 scope 적용(지역변수)
//const : 새로운 값을 재할당 불가
v = 10;  // var는 생략가능    var v 변수 선언과 할당
v = 20;
v++;   //21
console.log('v=',v);
let l= 10;
//let l= 20;
l =20; // l변수 할당
console.log('l=',l);
const C = 10; // 수정불가
//C=20; 재할당 불가
const Carr = [1, 2, 3]; //배열 동일자료형의 집합
Carr[0] = 9;
console.log(Carr);