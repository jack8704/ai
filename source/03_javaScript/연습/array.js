function array(){
    let result =[];
    if(arguments.length==1){
        //result를 arguments[0] 만큼 크기의 빈배열
        for(let cnt=1; cnt<=arguments[0]; cnt++){
            result.push(undefined);
        }
    }
    return result;    
    }
console.log(array(4))
