window.onload = function(){
    var Words = document.getElementById("message");
    var TalkWords = document.getElementById("talkwords");
    var TalkSub = document.getElementById("talksub");

    TalkSub.onclick = function(){
        var str = "";
        if(TalkWords.value == ""){
            alert("can not send empty message");
            return;
        }
        str = '<div class="usertalk"><span>' + TalkWords.value +'</span></div>' ;
        Words.innerHTML = Words.innerHTML + str;
    }
}
