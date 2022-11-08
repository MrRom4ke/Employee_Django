'use strict';

var togglers = document.getElementsByClassName("caret");
var i;

for (i = 0; i < togglers.length; i++) {
    togglers[i].addEventListener("click", function () {
        this.parentElement.querySelector(".nested").classList.toggle("active");
        this.classList.toggle("caret-down");
    });
}