function openTab(evt, tabName) {
  var i, tabContent, tabLinks;

  tabContent = document.getElementsByClassName("tab-content");
  for (i = 0; i < tabContent.length; i++) {
    tabContent[i].style.display = "none";
  }

  tabLinks = document.getElementsByTagName("button");
  for (i = 0; i < tabLinks.length; i++) {
    tabLinks[i].classList.remove("bg-gray-300");
    tabLinks[i].classList.remove("active:bg-gray-300");
  }

  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.classList.add("bg-gray-300");
  evt.currentTarget.classList.add("active:bg-gray-300");
}

// Functioning of the scroll up button

let calcScrollValue = () => {
  let scrollProgress = document.getElementById("scroll");
  let pos = document.documentElement.scrollTop;
  let calcHeight =
      document.documentElement.scrollHeight -
      document.documentElement.clientHeight;
  let scrollValue = Math.round((pos * 100) / calcHeight);
  if (pos > 100) {
      scrollProgress.style.display = "grid";
  } else {
      scrollProgress.style.display = "none";
  }
  scrollProgress.addEventListener("click", () => {
      document.documentElement.scrollTop = 0;
  });
  scrollProgress.style.background = `conic-gradient(#0366d6 ${scrollValue}%, #d7d7d7 ${scrollValue}%)`;
};

window.onscroll = calcScrollValue;
window.onload = calcScrollValue;
