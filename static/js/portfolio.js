import "/static/js/hystmodal.min.js"
import {currentExhibition} from "./getCurrentExhibition";


if(window.location.href.includes("portfolio")){
	const myModal = new HystModal({
		linkAttributeName: "data-hystmodal",
	});
	
	showPortfolio()
	autoFillModal()
} 

function showPortfolio(){
	const portfolios = new Map()
	currentExhibition.participants.forEach((item)=>{
		portfolios.set(item.id, item)
	})

	const id = new URLSearchParams(window.location.search).get('id');
	const portfolio = portfolios.get(+id);
	const swiper = document.querySelector(".portfolio-swiper-wrapper")

	let avatar
	let photo2
	let photo3

	if(!portfolio.avatar_id) {
		avatar = `<p class="portfolio-avatar-plug">${portfolio.name} не даёт себя сфотографировать, но мы не оставляем попыток!</p>`
		//document.querySelector(".portfolio-swiper-button-next").style.display = "none"
	}
	else avatar = `<img src="${portfolio.avatar_id}" alt="">`

	if(portfolio.participant_foto && portfolio.participant_foto.length > 2){
		document.querySelector(".portfolio-swiper-button-next").style.display = "block"
	}


/* 	if(!portfolio.participant_foto[0]) photo2 = ``
	else photo2 = `<img src="${portfolio.participant_foto[0].foto}" alt="">`

	if(!portfolio.participant_foto[1]) photo3 = ``
	else photo3 = `<img src="${portfolio.participant_foto[1].foto}" alt="">` */

	document.querySelector(".photo-1").innerHTML = avatar
/* 	document.querySelector(".photo-2").innerHTML = photo2
	document.querySelector(".photo-3").innerHTML = photo3 */


	portfolio.participant_foto.forEach((item, index)=>{
		
		const slide = document.createElement("div")
		slide.classList.add("swiper-slide")
		slide.innerHTML = `
		<div class="photo photo-${index+2}">
			<img src="${item.foto}" alt="">
		</div>`

		swiper.appendChild(slide)
	})





	document.querySelector(".portfolio__name").innerHTML = `${portfolio.name}`
	document.querySelector(".portfolio__description__breed").innerHTML = `${portfolio.breed.name}`

	if(portfolio.color !== null){
		document.querySelector(".portfolio__description__color").innerHTML = `${portfolio.color}`
	} else document.querySelector(".description__color").style.display = "none"

	document.querySelector(".portfolio__description__age").innerHTML = `${portfolio.age}`

	if(portfolio.gender === "boy"){
		document.querySelector(".portfolio__description__sex").innerHTML = `Мальчик`
	} else if(portfolio.gender === "girl"){
		document.querySelector(".portfolio__description__sex").innerHTML = `Девочка`
	}else document.querySelector(".description__sex").style.display = "none"

	if(portfolio.other !== null){
		document.querySelector(".portfolio__description__other").innerHTML = `${portfolio.other}`
	} else document.querySelector(".description__other").style.display = "none"

}

	function autoFillModal(){
		const input = document.querySelector("#participant")
		input.value = document.querySelector(".portfolio__name").innerHTML + " " + window.location.href
	}