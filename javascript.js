function swapStyleSheet(sheet) {
    document.getElementById("pagestyle").setAttribute("href", sheet);
}

function initiate() {

    var style1 = document.getElementById("light");
    var style2 = document.getElementById("dark");

    style1.onclick = function () { swapStyleSheet("/static/stylesheet.css") };
    style2.onclick = function () { swapStyleSheet("/static/darkstylesheet.css"); };
}

window.onload = initiate;


