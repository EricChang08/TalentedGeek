function menuHovered(myId) {
  let target = document.getElementById(myId);

  target.style.backgroundColor = "yellow";
  target.style.color = "black";
}

function menuUnHovered(myId) {
  let target = document.getElementById(myId);

  console.log("use");
  if (myId === "cvField") {
    target.style.backgroundColor = "white";
    target.style.color = "black";
  } else {
    target.style.backgroundColor = "black";
    target.style.color = "white";
  }
}
