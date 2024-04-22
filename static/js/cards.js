import { allExhibitions } from "./getAllExhibitions"
import { currentExhibition } from "./getCurrentExhibition"
import {formatDays, formatMonth, addActiveClass} from "./functions"

const participants = currentExhibition.participants

if(window.location.href.includes("participants")){
	showParticipants()
	addActiveClass(".link__participants")
} else if(window.location.href.includes("exhibitions")) {
	showExhibitions()
}	

function showParticipants(){
	const participantsContainer = document.querySelector(".cards__container")
	const participantCards = participants

	participantCards.forEach((item, index)=>{
		showParticipantCard(item, index)
	})
	
	function showParticipantCard(card, index){

		const cardContainer = document.createElement("a")
		let avatar;
		if(card.avatar_id === null) avatar = card.participant_foto[0].foto
		else avatar = card.avatar_id
		cardContainer.classList.add("card")
		cardContainer.href = `/portfolio/?id=${card.id}`

		cardContainer.innerHTML = `
		<div class="card__description">
			<h2 class="description__title title">${card.name}</h2>
		</div>
		<div class="card__image">
			<img src="${avatar}" alt="">
		</div>`
		participantsContainer.appendChild(cardContainer)
	}
}


function showExhibitions(){
	const exhibitionsContainer = document.querySelector(".cards__container")
	const exhibitionCards = allExhibitions
	const currentDate = new Date()
	
	exhibitionCards.forEach((item, index)=>{
		showExhibitionCard(item, index)
	})
	
	function showExhibitionCard(card, index){
		if(new Date(card.date_begin) > currentDate) return
		const cardContainer = document.createElement("a")
		let photo
		if(card.exhibition_foto[0] === undefined) photo = "/static/images/reserve/reserve-exhibition-photo.jpg"
		else photo = card.exhibition_foto[0].foto
		
		cardContainer.classList.add("card")
		cardContainer.href = `/past/?id=${card.id}`
	
		cardContainer.innerHTML = `
		<div class="card__description">
			<h2 class="description__title description__date title">${formatDays(card)} ${formatMonth(card.date_begin)}</h2>
			<p class="description__text">${card.venue}</p>
		</div>
		<div class="card__image">
			<img src="${photo}" alt="">
		</div>`
		exhibitionsContainer.appendChild(cardContainer)
	}

}
