//아래와 같이 
// 매개변수가 없으면 -999를 리턴
// 매개변수가 1개 이상이면 누적합을 리턴
// 하는 가변인자 함수 sumAll()을 작성한 스크립트sumAll.js 파일을 이용하시오

function sumAll(){
    result=0;
    if(arguments.length>=1){
        // for(let idx=0; idx<arguments.length; idx++){
        //     result+=arguments[idx];
        //     }

        // for(let i in arguments){
        //     result+= arguments[i];
        // }
        for(let data of arguments){
            result += data;
        }
        

    }else{
        result=-999;
    }
    return result;
}
console.log(sumAll());
console.log(sumAll(1,2,3));