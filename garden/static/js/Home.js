function menuHovered(myId) {
  let target = document.getElementById(myId);

  target.style.backgroundColor = "yellow";
  target.style.color = "black";
}

function menuUnHovered(myId) {
  let target = document.getElementById(myId);

  if (myId === "homeField") {
    target.style.backgroundColor = "white";
    target.style.color = "black";
  } else {
    target.style.backgroundColor = "black";
    target.style.color = "white";
  }
}

function jumpHovered(myId) {
  let target = document.getElementById(myId);
  target.style.backgroundColor = "#7f00ff";
}

function jumpUnHovered(myId) {
  let target = document.getElementById(myId);
  target.style.backgroundColor = "green";
}

function buttonHovered(myId) {
  let target = document.getElementById(myId);
  target.style.backgroundColor = "#cc6600";
  target.style.color = "white";
}

function buttonUnHovered(myId) {
  let target = document.getElementById(myId);
  target.style.backgroundColor = "white";
  target.style.color = "black";
}

function generalHovered(myId) {
  let target = document.getElementById(myId);
  target.style.backgroundColor = "yellow";
}

function generalUnHovered(myId) {
  let target = document.getElementById(myId);
  target.style.backgroundColor = "white";
}

function jumpContact(myId) {
  window.location.hash = myId;
  var url = window.location.href;
  var valiable = url.split("#")[0];
  window.history.pushState({}, 0, valiable);
}
