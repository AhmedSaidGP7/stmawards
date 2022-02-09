document.querySelector('#homepage3').style.display = 'none';
document.querySelector('.homepage2').style.display = 'none';
document.querySelector('#home-q2').style.display = 'none';
document.querySelector('#home-q3').style.display = 'none';
document.querySelector('#home-q4').style.display = 'none';
document.querySelector('#thenextbutton').style.display = 'none';



var theCounter = 3;
function pageLoaded() {
   const loadedpage =  document.querySelector('.stmawardslandingpage');
   loadedpage.style.display = 'none';
   const homebody = document.querySelector('body');
   homebody.style.overflow = 'auto';
} 

function myCounter(){
    theCounter--;
    document.getElementById("numberOfTrials").innerHTML = theCounter;
}


function q2()
{
    const q1 = document.querySelector('#home-q1');
    const q2 = document.querySelector('#home-q2');
    q2.style.display = 'block';
    q1.style.display = 'none';
}

function q3()
{
    const q2 = document.querySelector('#home-q2');
    const q3 = document.querySelector('#home-q3');
    q2.style.display = 'none';
    q3.style.display = 'block';

}

function q4()
{
    const q3 = document.querySelector('#home-q3');
    const q4 = document.querySelector('#home-q4');
    q3.style.display = 'none';
    q4.style.display = 'block';

}

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
    page3.style.display = 'block';

}