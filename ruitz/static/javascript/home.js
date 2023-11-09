const logoContainer = document.getElementById('logoContainer');
const Header = document.getElementById('Header');
window.setInterval(cambio_fondo_header, 20000);

var screenW = window.innerWidth;
var navbar = document.getElementById('navDown');

window.addEventListener('scroll', function() {   
    console.log('scroll');
    if (screenW > 600) {
        console.log("scroll >600");
        if (window.pageYOffset > window.innerHeight) {
            console.log("down >600");
            navbar.classList.add('navbarDown');
        } else {
            navbar.classList.remove('navbarDown');
            console.log('up <600');
        }
    } else {            
        if (window.pageYOffset > window.innerHeight) {
            navbar.classList.add('navbarDown');
        } else {
            navbar.classList.remove('navbarDown');
        }
    }
});


logoContainer.addEventListener('mousemove', (e) => {
    const containerWidth = logoContainer.offsetWidth;
    const containerHeight = logoContainer.offsetHeight;
    const mouseX = e.pageX - logoContainer.offsetLeft;
    const mouseY = e.pageY - logoContainer.offsetTop;

    const rotateY = (mouseX / containerWidth - 0.5) * 100; // Ajusta el valor para controlar la rotación en el eje Y
    const rotateX = (0.5 - mouseY / containerHeight) * 100; // Ajusta el valor para controlar la rotación en el eje X

    logoContainer.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
});

logoContainer.addEventListener('mouseleave', () => {
    logoContainer.style.transform = 'perspective(1000px) rotateX(0) rotateY(0)';
});    

function cambio_fondo_header(){
    console.log("cambio fondo");
    for (let i = 1; i < 7; i++) {
        Header.classList.remove("Fondo_"+i);
    }
    let numero = Math.floor(Math.random() * 6) + 1;
    switch (numero) {
        case 1:
            Header.classList.add("Fondo_1")
            break;
        case 2:
            Header.classList.add("Fondo_2")
            break;
        case 3:
            Header.classList.add("Fondo_3")
            break;
        case 4:
            Header.classList.add("Fondo_4")
            break;
        case 5:
            Header.classList.add("Fondo_5")
            break;
        case 6:
            Header.classList.add("Fondo_6")
            break;
        default:
            Header.style.backgroundImage = "url('url(../img/Fondo_3.png);')";
    };
}   