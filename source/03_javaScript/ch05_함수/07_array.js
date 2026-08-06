/*array함수 : 가변인자함수(함수표현식으로만 가능 화살표함수는 안됨)*/
// 선언적 함수로
//매개변수가 0개: length가 0인 배열을return
//매개변수가 1개: length가 매개변수만큼인 크기의 배열을 return 
//매개변수가 2개이상: 매개변수로 배열을 생성 return

// 매개변수 한개일때는 빈배열을 
// 매개변수가 한개일때는 그수만큼 빈배열을
// 매개변수가 두개이상일때는 배열값
function array(){ //arguments : 매개변수 내용이 들어옴
    //console.log(arguments,arguments.length);
    let result =[];
    if(arguments.length==1){
        //result를 arguments[0] 만큼 크기의 빈배열
        for(let cnt=1; cnt<=arguments[0]; cnt++){
            result.push(undefined);
        }
    }else if(arguments.length>=2){
       //result를 arguments의 내용으로 만들기
        // for(let idx=0 ; idx<arguments.length;idx++){
        //     result.push(arguments[idx]);
        // } //for
        for (var data of arguments){
            result.push(data);
        }
    } //if
    return result;
} // array


var arr2=array(1,2,'삼'); // 매개변수가 2개이상
var arr4=array(3); // 매개변수가 1개일때는 입력값만큼 빈배열 
var arr6=array(); //매개변수가 0개
console.log(arr2);
console.log(arr4);
console.log(arr6);