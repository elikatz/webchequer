
/**
 * Function to keep the top bar at the top of the visible screen
 */
function placeIt() {
  document.getElementById("top_bar").style.top = window.pageYOffset +"px"; // For Mozilla etc.
  window.setTimeout("placeIt()", 100);
}