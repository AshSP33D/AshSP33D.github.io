var bar = document.getElementById("barDiv");
var barContent = document.getElementById("barInner");
var waitingTime = 0.05;

var colorPicker = document.getElementById("colorPicker");
var hexArea = document.getElementById("hexArea");
var channelName = document.getElementById("channelName");
var previewText = document.getElementById("previewText");
var barWatchingText = document.getElementById("barWatchingText");
var waitDuration = document.getElementById("waitDuration");

var finalURL = document.getElementById("finalURL");
var timesRun = 0;

var args = new URLSearchParams(window.location.search);

if (args.get("name") != null) {
    barWatchingText.innerHTML = "You're watching " + args.get("name") + "!";
    channelName.value = args.get("name");
}

else {
    channelName.value = "[Name]";
}

if (args.get("color") != null) {
    if (args.get("color") == "rainbow") {
        barWatchingText.style.animation = "rainbow 1s ease";
        barWatchingText.style.animationIterationCount = "infinite";
    }
    else {
        hexArea.value = args.get("color");
        colorPicker.value = "#" + args.get("color");
        barWatchingText.style.color = "#" + args.get("color");
    }
}

if (args.get("time") != null) {
    waitingTime = parseFloat(args.get("time"));
    waitDuration.value = args.get("time");
}

updatePreview();

barContent.style.animation = "barContent 20s ease";

bar.addEventListener("animationend", function () {
    bar.style.animation = "none";
    barContent.style.animation = "none";
    bar.style.transform = "translateY(30px)";
    timesRun += 1;
    setTimeout(function () {

        if (timesRun == (Math.round(60 / waitingTime)))         //At the minute this should be set to refresh almost every hour.
        {
            location.reload(true);      //Auto refresh (just in case I decide to push any updates while someone's stream is running. Shouldn't pose too much of an issue.)
        }

        bar.style.animation = "";
        barContent.style.animation = "";
        bar.style.transform = "";
    }, waitingTime * 60000);
}, false);

function updatePreview() {
    previewText.innerHTML = "You're watching " + channelName.value + "!";
    previewText.style.color = "#" + hexArea.value;
}

function createURL() {
    finalURL.innerHTML = window.location.href.replace(window.location.search, "") + "?name=" + channelName.value + "&color=" + hexArea.value + "&time=" + waitingTime.toString();
}