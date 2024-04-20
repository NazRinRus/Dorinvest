import "/static/js/hystmodal.min.js"
import {currentExhibition} from "./getCurrentExhibition";


if(window.location.href.includes("portfolio")){
	const myModal = new HystModal({
		linkAttributeName: "data-hystmodal",
	});
	
	showPortfolio()
} 

function showPortfolio(){
	const portfolios = new Map()
	currentExhibition.participants.forEach((item)=>{
		portfolios.set(item.id, item)
	})

	const id = new URLSearchParams(window.location.search).get('id');
	const portfolio = portfolios.get(+id);

	document.querySelector(".photo-1").innerHTML = `<img src="${portfolio.participant_foto[0].foto}" alt="">`
	document.querySelector(".photo-2").innerHTML = `<img src="${portfolio.participant_foto[1].foto}" alt="">`
	document.querySelector(".photo-3").innerHTML = `<img src="${portfolio.participant_foto[2].foto}" alt="">`

	document.querySelector(".portfolio__name").innerHTML = `${portfolio.name}`
	document.querySelector(".portfolio__description__breed").innerHTML = `${portfolio.breed.name}`
	document.querySelector(".portfolio__description__color").innerHTML = `${portfolio.color}`
	document.querySelector(".portfolio__description__age").innerHTML = `${portfolio.breed.code}`
	document.querySelector(".portfolio__description__sex").innerHTML = `${portfolio.breed.code}`
}