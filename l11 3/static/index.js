const b = document.querySelector(".burger-button");
const k = document.querySelector(".krest");


b.addEventListener("click", (e) => {
    e.preventDefault();
    e.stopPropagation();
    document.querySelector(".burger-menu").classList.toggle("activate");
});

k.addEventListener("click", (e) => {
    e.preventDefault();
    e.stopPropagation();
    document.querySelector(".burger-menu").classList.toggle("activate");
});