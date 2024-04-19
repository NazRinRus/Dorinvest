import { allExhibitions } from "./getAllExhibitions"
import { currentExhibition } from "./getCurrentExhibition"
import {formatDays, formatMonth} from "./functions"

const participants = currentExhibition.participants

if(window.location.href.includes("participants")){
	showParticipants()
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
		cardContainer.classList.add("card")
		cardContainer.href = `/templates/config/pages/portfolio.html?id=${card.id}`

		cardContainer.innerHTML = `
		<div class="card__description">
			<h2 class="description__title title">${card.name}</h2>
			<p class="description__text">${card.other}</p>
		</div>
		<div class="card__image">
			<img src="${card.avatar_id}" alt="">
		</div>`
		participantsContainer.appendChild(cardContainer)
	}
}


function showExhibitions(){
	const exhibitionsContainer = document.querySelector(".cards__container")
	const exhibitionCards = allExhibitions
	
	exhibitionCards.forEach((item, index)=>{
		showExhibitionCard(item, index)
	})
	
	function showExhibitionCard(card, index){
		const cardContainer = document.createElement("a")
		cardContainer.classList.add("card")
		cardContainer.href = `/templates/config/pages/past.html?id=${card.id}`
	
		cardContainer.innerHTML = `
		<div class="card__description">
			<h2 class="description__title description__date title">${formatDays(card)} ${formatMonth(card.date_begin)}</h2>
		</div>
		<div class="card__image">
			<img src="${card.exhibition_foto[0].foto}" alt="">
		</div>`
		exhibitionsContainer.appendChild(cardContainer)
	}

}
