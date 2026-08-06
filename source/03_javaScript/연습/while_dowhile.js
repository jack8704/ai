var cnt=0;
var startTime=new Date().getTime();

do{cnt++;
}while(new Date().getTime()<=startTime+10);
console.log('1초동안 do while문 수행회수:'+cnt);