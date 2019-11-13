function check(flag, score) {
    var user_flag = document.getElementById(flag).value;

    if(user_flag == flag ){
        alert("correct"+" 글쓰니: "+ user_flag+" 정답: "+ flag + " 점수는 " + score);
        document.getElementById('answer').value = "";
    }else{
        alert("fail"+" 글쓰니: "+ user_flag+" 정답: "+ flag);
        document.getElementById('answer').value = "";
    }  
}