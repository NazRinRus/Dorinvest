import { allExhibitions } from "./getAllExhibitions"
import { currentExhibition } from "./getCurrentExhibition"
import { faq } from "./getQuestions"
import { fullStatistics } from "./getStatistics";

import Accordion from '/static/js/accordion.min.js';
import '/static/css/accordion.min.css';

if(window.location.href === "http://127.0.0.1:8000/"){
	const nowExhibition = currentExhibition

	//console.log(currentExhibition)
	
// HERO

document.querySelector(".hero__info__title").innerHTML = nowExhibition.name
document.querySelector(".hero__info__description").innerHTML = nowExhibition.description
document.querySelector(".hero__date__days").innerHTML = formatDays(nowExhibition)
document.querySelector(".hero__date__month").innerHTML =  formatMonth(nowExhibition.date_begin)
document.querySelector(".hero__date__time").innerHTML = nowExhibition.time_event
document.querySelector(".hero__place").innerHTML = nowExhibition.location
document.querySelector(".about__description__text").innerHTML = nowExhibition.about

//console.log(nowExhibition.exhibition_foto)

// PARTICIPANTS

const participantsGallery = document.querySelector(".participants__gallery")
const participantsphotos = nowExhibition.exhibition_foto

participantsphotos.forEach((item, index)=>{
	//console.log(item.foto)
	showParticipantsPhoto(item, index)
})

//ФОТО НЕ ГРУЗИТ

function showParticipantsPhoto(photo, index){
	const photoContainer = document.createElement("div")
	photoContainer.classList.add("participants__gallery__item")
	photoContainer.classList.add(`participants__gallery__item-${index + 1}`)
	photoContainer.innerHTML = `<img src="${photo.foto}">`
	participantsGallery.appendChild(photoContainer)
}


// PAST

const exhibitions = allExhibitions
const exhibitionsGallery = document.querySelector(".past__gallery")


exhibitions.forEach((item, index)=>{
	if(index > 6) return
	showPastExgibitions(item, index)
})

if (exhibitions.length < 6){
	for(let i = exhibitions.length; i < 6; i++){
		const exhibitionContainer = document.createElement("div")
		exhibitionContainer.classList.add("past__gallery__item")
		exhibitionContainer.classList.add(`past__gallery__item-${i + 1}`)

		exhibitionContainer.innerHTML = `<img src="/static/images/reserve/reserve-photo-${i}.jpg" alt="" loading="lazy">`
		exhibitionsGallery.appendChild(exhibitionContainer) 
	}
}

function showPastExgibitions(exhibition, index){
	const exhibitionContainer = document.createElement("a")
	exhibitionContainer.classList.add("past__gallery__item")
	exhibitionContainer.classList.add(`past__gallery__item-${index + 1}`)
	exhibitionContainer.href = "#"

	if(index === 0) {
		exhibitionContainer.innerHTML = 
		`<div class="item__description item__description_main">
			<div class="item__description__background"></div>
			<div class="item__description__container">
				<p class="item__description__date item__description__date_main">${formatDays(exhibition)} ${formatMonth(exhibition.date_begin)}</p>
			</div>
		</div>
		<img src="${exhibition.exhibition_foto[0].foto}" alt="" loading="lazy">`
	}
	else if(index > 0){
	exhibitionContainer.innerHTML = 
	`<div class="item__description">
		<div class="item__description__background"></div>
		<div class="item__description__container">
			<p class="item__description__date">${formatDays(exhibition)} ${formatMonth(exhibition.date_begin)}</p>
		</div>
	</div>
	<img src="${exhibition.exhibition_foto[0].foto}" alt="" loading="lazy">`}
	exhibitionsGallery.appendChild(exhibitionContainer) 
}


// STATISTICS

document.querySelector(".cats__number").innerHTML = fullStatistics.Кошка
document.querySelector(".dogs__number").innerHTML = fullStatistics.Собака


// QUESTIONS

const questionsContainer = document.querySelector(".accordion-container")
const questions = faq



questions.forEach((item, index)=>{
	showQuestions(item, index)
})

function showQuestions(question, index){

	const questionContainer = document.createElement("div")
	questionContainer.classList.add("ac")
		
	questionContainer.innerHTML = 
	`<h2 class="ac-header">
		<button type="button" class="ac-trigger">${question.question}</button>
	</h2>
	<div class="ac-panel">
		<p class="ac-text">${question.answer}</p>
	</div>`
	questionsContainer.appendChild(questionContainer) 


}
	let ac = document.querySelector(".accordion-container")

	if(ac !== null){
		new Accordion('.accordion-container', {
			duration: 400,
			showMultiple: true,
		});
	}

// PARTNERS

	const partners = nowExhibition.partners
	const partnersContainer = document.querySelector(".partners__swiper-wrapper")

	partners.forEach((item, index)=>{
		showPartners(item)
	})

	if((document.documentElement.clientWidth > 1060 && partners.length < 3)|| (partners.length < 2)){
		partnersContainer.style.justifyContent = "center"
	}

	function showPartners(partner){

		const partnerContainer = document.createElement("div")
		partnerContainer.classList.add("swiper-slide")
		partnerContainer.classList.add("partners__swiper-slide")
			
		partnerContainer.innerHTML = 
		`<a href="${partner.website}">
			<div class="slide__content partners__slide__content ">
				<img src="${partner.logo}" alt="" loading="lazy">
			</div>
		</a>`
		partnersContainer.appendChild(partnerContainer) 
	}


	function formatDays(exhibition){
		const start = +(exhibition.date_begin[8]+exhibition.date_begin[9])
		const end = +(exhibition.date_end[8]+exhibition.date_end[9])

		const result = `${start}-${end}`
		return result
	}

	function formatMonth(dateBegin){
		const months = {
			1: "января",
			2: "февраля",
			3: "марта",
			4: "апреля",
			5: "мая",
			6: "июня",
			7: "июля",
			8: "августа",
			9: "сентября",
			10: "октября",
			11: "ноября",
			12: "декабря",
		}

		const month = +(dateBegin[5]+dateBegin[6])

		return months[month]
	}
} else {
	console.log(1)
}





