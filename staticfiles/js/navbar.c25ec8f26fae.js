// JS FOR removing Preload anfter loading
// LISTENING TO MENU BUTTON CLICKS TO OPEN NAVBAR
// LISTENING TO OVERLAY CLICKS TO CLOSE NAVBAR

window.addEventListener("load", () => {
  document.body.classList.remove("preload");
})
document.addEventListener("DOMContentLoaded", () => {
  const nav = document.querySelector(".nav");

  document.querySelector("#btnNav").addEventListener("click", () =>{
      nav.classList.add("nav--open");
  });
  document.querySelector(".nav__overlay").addEventListener("click", () =>{
      nav.classList.remove("nav--open");
  });
});
