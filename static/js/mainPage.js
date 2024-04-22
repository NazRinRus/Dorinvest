import { allExhibitions } from "./getAllExhibitions"
import { currentExhibition } from "./getCurrentExhibition"
import { faq } from "./getQuestions"
import { fullStatistics } from "./getStatistics";
import {formatDays, formatMonth, addActiveClass} from "./functions"

import Accordion from '/static/js/accordion.min.js';
import '/static/css/accordion.min.css';


Array.from(document.querySelectorAll(".link__photoreport")).forEach((item)=>{item.firstChild.href = `/past/?id=${currentExhibition.id}`})

window.onscroll = function() {scrollFunction()};
const scrollButton = document.querySelector(".scroll-to-top")

function scrollFunction() {
    if (document.body.scrollTop > 500 || document.documentElement.scrollTop > 500) {
			scrollButton.style.display = "block";
    } else {
			scrollButton.style.display = "none";
    }
}

scrollButton.addEventListener("click", ()=>{
	scrollToTop()
})

function scrollToTop() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

if(window.location.href === "http://127.0.0.1:8000/"){
	const nowExhibition = currentExhibition
	addActiveClass(".link__home")
// HERO
if(nowExhibition.bunner){
	document.querySelector(".hero__background").src = nowExhibition.bunner
	document.querySelector(".hero__background-span").remove()
} else{
	document.querySelector(".hero__background").src = "/static/images/banner.jpg"
	document.querySelector(".hero__background-span").style.display = "block"
}
document.querySelector(".hero__info__title").innerHTML = nowExhibition.name
document.querySelector(".hero__info__description").innerHTML = nowExhibition.description
document.querySelector(".hero__date__days").innerHTML = formatDays(nowExhibition)
document.querySelector(".hero__date__month").innerHTML =  formatMonth(nowExhibition.date_begin)
document.querySelector(".hero__date__time").innerHTML = nowExhibition.time_event
document.querySelector(".hero__place").innerHTML = nowExhibition.location
document.querySelector(".about__description__text").innerHTML = nowExhibition.about


// PARTICIPANTS

const participantsGallery = document.querySelector(".participants__gallery")
const participantsphotos = nowExhibition.participants

participantsphotos.forEach((item, index)=>{
	if(index > 8) return
	showParticipantsPhoto(item, index)
})

if (participantsphotos.length < 9){
	for(let i = participantsphotos.length; i < 9; i++){
		const participantsContainer = document.createElement("div")
		participantsContainer.classList.add("past__gallery__item")
		participantsContainer.classList.add(`past__gallery__item-${i + 1}`)

		participantsContainer.innerHTML = `<img src="/static/images/reserve/reserve-photo-${i}.jpg" alt="" loading="lazy">`
		participantsGallery.appendChild(participantsContainer) 
	}
}

function showParticipantsPhoto(photo, index){
	const photoContainer = document.createElement("div")
	photoContainer.classList.add("participants__gallery__item")
	photoContainer.classList.add(`participants__gallery__item-${index + 1}`)

	if(photo.avatar_id === null) photoContainer.innerHTML = `<img src="${photo.participant_foto[0].foto}">`
	else photoContainer.innerHTML = `<img src="${photo.avatar_id}">`
	
	participantsGallery.appendChild(photoContainer)
}


// PAST

const exhibitions = allExhibitions
exhibitions.shift()
const exhibitionsGallery = document.querySelector(".past__gallery")
exhibitions.forEach((item, index)=>{
	if(index > 5) return
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
	exhibitionContainer.href = `/past/?id=${exhibition.id}`
	let  exhibitionPhoto
	if(exhibition.exhibition_foto[0] === undefined) exhibitionPhoto = `static/images/reserve/reserve-photo-${index}.jpg`
	else exhibitionPhoto = exhibition.exhibition_foto[0].foto

	if(index === 0) {
		exhibitionContainer.innerHTML = 
		`<div class="item__description item__description_main">
			<div class="item__description__background"></div>
			<div class="item__description__container">
				<p class="item__description__date item__description__date_main">${formatDays(exhibition)} ${formatMonth(exhibition.date_begin)}</p>
				<p class="item__description__place item__description__place_main">${exhibition.venue}</p>
			</div>
		</div>
		<img src="${exhibitionPhoto}" alt="" loading="lazy">`
	}
	else if(index > 0){
	exhibitionContainer.innerHTML = 
	`<div class="item__description">
		<div class="item__description__background"></div>
		<div class="item__description__container">
			<p class="item__description__date">${formatDays(exhibition)} ${formatMonth(exhibition.date_begin)}</p>
			<p class="item__description__place">${exhibition.venue}</p>
		</div>
	</div>
	<img src="${exhibitionPhoto}" alt="" loading="lazy">`}
	exhibitionsGallery.appendChild(exhibitionContainer) 
}


// STATISTICS


document.querySelector(".cats__number").innerHTML = fullStatistics.кошка+192
document.querySelector(".dogs__number").innerHTML = fullStatistics.собака+133


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
		`<a href="${partner.website}" target="_blank">
			<div class="slide__content partners__slide__content ">
				<img src="${partner.logo}" alt="" loading="lazy">
			</div>
		</a>`
		partnersContainer.appendChild(partnerContainer) 
	}

// FORM

/* let formButton = document.querySelector(".form__button")
formButton.addEventListener("click",(e)=>{
	e.preventDefault()
}) */

} else {
}





