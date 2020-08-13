function menuHovered(myId) {
  let target = document.getElementById(myId);

  target.style.backgroundColor = "yellow";
  target.style.color = "black";
}

function menuUnHovered(myId) {
  let target = document.getElementById(myId);

  if (myId === "blogField") {
    target.style.backgroundColor = "white";
    target.style.color = "black";
  } else {
    target.style.backgroundColor = "black";
    target.style.color = "white";
  }
}

//functions deals with tags

function loadGeneral() {
  let target = document.getElementById("general");

  target.style.backgroundColor = "#cc0000";
  target.style.color = "white";
}

function loadTag(tagId) {
  let target = document.getElementById(tagId);

  target.style.backgroundColor = "#cc0000";
  target.style.color = "white";
}

function tagHovered(myId) {
  let target = document.getElementById(myId);

  target.style.backgroundColor = "#cc0000";
  target.style.color = "white";
}

function tagUnHovered(myId, tagId) {
  let target = document.getElementById(myId);

  if (myId === tagId || (tagId === "" && myId === "general")) {
    target.style.backgroundColor = "#cc0000";
    target.style.color = "white";
  } else {
    target.style.backgroundColor = "white";
    target.style.color = "black";
  }
}

// end here

function titleHovered(myId) {
  let target = document.getElementById(myId);

  target.style.color = "blue";
}

function titleUnHovered(myId) {
  let target = document.getElementById(myId);

  target.style.color = "black";
}
