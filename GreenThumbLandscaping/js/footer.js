const footerSpan = document.querySelector(".footer-span");

footerSpan.innerHTML = `${(new Date().getFullYear())}`;


let open = document.getElementById('hamburger');
let changeIcon = true;
let about = document.getElementsByClassName('about');
let container2 = document.getElementsByClassName('container2');
let services = document.getElementsByClassName('we-offer-area');
let tablewrap = document.getElementsByClassName('table-wrap');

open.addEventListener("click", function () {

    let overlay = document.querySelector('.overlay');
    let nav = document.querySelector('nav');
    let icon = document.querySelector('.menu-toggle i');

    overlay.classList.toggle("menu-open");
    nav.classList.toggle("menu-open");

    if (changeIcon) {
        icon.classList.remove("fa-bars");
        icon.classList.add("fa-times");

        changeIcon = false;

        // hide class element
        testimonials.style.display = "none";
        // hide class element
        for (let i = 0; i < about.length; i++)
            about[i].style.display = "none";
        // hide class element
        for (let j = 0; j < container2.length; j++)
            container2[j].style.display = "none";
        // hide class element
        for (let k = 0; k < services.length; k++)
            services[k].style.display = "none";
        // hide class element
        for (let l = 0; l < tablewrap.length; l++)
            tablewrap[l].style.display = "none";
    }
    else {
        icon.classList.remove("fa-times");
        icon.classList.add("fa-bars");
        changeIcon = true;
        // show class element
        testimonials.style.display = "block";
        // show class element
        for (let i = 0; i < about.length; i++)
            about[i].style.display = "block";
        // show class element
        for (let j = 0; j < container2.length; j++)
            container2[j].style.display = "block";
        // show class element
        for (let k = 0; k < services.length; k++)
            services[k].style.display = "block";
        // show class element
        for (let l = 0; l < tablewrap.length; l++)
            tablewrap[l].style.display = "block";
    }
});