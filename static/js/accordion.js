import Accordion from 'accordion-js';
import 'accordion-js/dist/accordion.min.css';

let ac = document.querySelector(".accordion-container")


if(ac !== null){
  new Accordion('.accordion-container', {
    duration: 400,
    showMultiple: true,
  });
}

