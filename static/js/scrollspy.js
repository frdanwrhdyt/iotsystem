const makeNavLinksSmooth = () =>{
    const navLink = document.querySelectorAll("#nav");

    for(let n in navLink){
        if(navLink.hasOwnProperty(n)){
            navLink[n].addEventListener("click", e => {
                e.preventDefault();
                document.querySelector(navLink[n].hash)
                .scrollIntoView({
                    behavior : "smooth"
                });
            });
        }
    }
}

const spyScrolling = () =>{
    const sections = document.querySelectorAll('.nav-link');

    window.onscroll = () =>{
        const scrollPosition = document.documentElement.scrollTop || document.body.scrollTop;

        for (let s in sections){
            if(sections.hasOwnProperty(s) && sections[s].offsetTop <= scrollPosition){
                const id = sections[s].id;
                document.querySelector('.nav-link active').classList.remove('nav-link active');

                document.querySelector(`a[href*=${id}]`).parentNode.classList.add('nav-link active');
            }
        }
    }
}

makeNavLinksSmooth();
spyScrolling();

$(window).scroll(function(){
    var scroll = $(window).scrollTop();
    
    if(scroll >= 200){
        $("#navbar").addClass("bg-dark");
    }
    else{
        $("#navbar").removeClass("bg-dark");
    }
})