document.querySelector('#homepage3').style.display = 'none';
document.querySelector('.homepage2').style.display = 'none';

function page2() {
    const page1 = document.querySelector('.homepage1');
    const page2 = document.querySelector('.homepage2');
    const page3 = document.querySelector('#homepage3');
    page1.style.display = 'none';
    page2.style.display = 'block';

}


function page3() {
    const page1 = document.querySelector('.homepage1');
    const page2 = document.querySelector('.homepage2');
    const page3 = document.querySelector('#homepage3');
    const modaaal = document.querySelector("#exampleModal");
    page1.style.display = 'none';
    page2.style.display = 'none';
    modaaal.style.display = 'none';
    page3.style.display = 'block';

}