
var modalBtn = document.querySelectorAll(".modal-open");
var writeup = document.querySelectorAll(".modal-writeup")

modalBtn.forEach(function(btn) {
    btn.onclick = function() {
        var modal = btn.getAttribute("data-modal");
        document.getElementById(modal).style.display = "block"
        
    };
});

writeup.forEach(function(btn) {
    btn.onclick = function() {
        var modal = btn.getAttribute("data-modal");
        document.getElementById(modal).style.display = "block"
        
    };
});

var closeBtn = document.querySelectorAll(".modal-close");

closeBtn.forEach(function(btn){
    btn.onclick = function(){
        var modal = (btn.closest(".modal").style.display = "none");
    };
});

window.onclick = function(e){
    if(e.target.className == "modal") {
        e.target.style.display = "none";
    }
};
    