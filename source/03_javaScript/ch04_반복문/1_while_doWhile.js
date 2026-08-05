var cnt = 0;
var startTime =new Date().getTime();// 1970.1.1부터 현재까지의 밀리세컨(1/1000초)
console.log(startTime);
while(new Date().getTime()<=startTime+1000){
    cnt++;//1증가 연산자

}
console.log('1초동안 while문 수행회수:'+cnt);
cnt = 0;
startTime =new Date().getTime();
do{
    cnt++;
}while(new Date().getTime()<=startTime+1000);
console.log('1초동안 do while문 수행회수:'+cnt);