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