import { allExhibitions } from "./getAllExhibitions"
import {formatDays, formatMonth, addActiveClass} from "./functions"
import { getStatistics } from "./getStatistics";

if(window.location.href.includes("past")){
	addActiveClass(".link__photoreport")
	const exhibitions = new Map()
	allExhibitions.forEach((item)=>{
		exhibitions.set(item.id, item)
	})	

	const id = new URLSearchParams(window.location.search).get('id');	

	

	showPhotos(exhibitions.get(+id))	
	showPlug(exhibitions.get(+id))
	showRepot(exhibitions.get(+id))
} 

function showPhotos(exhibition){
	if(exhibition.exhibition_foto[0] === undefined) return
	const photos = []
	exhibition.exhibition_foto.forEach(item => photos.push(item.foto))

	document.querySelector(".photos__date").innerHTML = `${formatDays(exhibition)} ${formatMonth(exhibition.date_begin)}`
	document.querySelector(".photos__place").innerHTML = `${exhibition.venue}`
	const photosContainer = document.querySelector(".photos__container")
	photos.forEach(item => createPhotoCard(item, photosContainer))

	showStatistics(exhibition.id)

}

function createPhotoCard(photos, container){
	const photoCard = document.createElement("div")
	photoCard.classList.add("photo")

	photoCard.innerHTML = `<img src="${photos}" alt="">`
	container.appendChild(photoCard)
}

async function showStatistics(exhibitionID){
	const numbersOfPets = await getStatistics(exhibitionID)

	if(numbersOfPets.кошка || numbersOfPets.собака){
		
		document.querySelector(".exhibition-statistics").innerHTML = 
		`			
		<div class="exhibition-statistics__container">
			<img class="exhibition-statistics__decor" src="/static/images/past-decor-cat.png" alt="">
			<div class="statistics__description">
				<h2 class="statistics__description__title">Благодаря вашему участию<br>новый дом нашли</h2>
				<div class="statistics__description__numbers"></div>
			</div>
		</div>`
		} else {
			document.querySelector(".exhibition-statistics").style.display = "none"
			document.querySelector(".exhibition-statistics").style.display = "none"
			return}

	
	if(numbersOfPets.кошка){
		const cats = document.createElement("div")
		cats.innerHTML =
		`
		<div class="statistics__cats">
			<span class="cats__title">кошки:</span>
			<span class="cats__number">${numbersOfPets.кошка}</span>
		</div>
		`
		document.querySelector(".statistics__description__numbers").appendChild(cats)
	}

	if(numbersOfPets.собака){
		const dogs = document.createElement("div")
		dogs.innerHTML = 
		`
		<div class="statistics__dogs">
			<span class="dogs__title">собаки:</span>
			<span class="dogs__number">${numbersOfPets.собака}</span>
		</div>
		`
		document.querySelector(".statistics__description__numbers").appendChild(dogs)
	}

}

function showPlug(exhibition){
	if(exhibition.exhibition_foto[0]) return
	document.querySelector(".exhibition-statistics").innerHTML = 
		`			
		<div class="exhibition-statistics__container">
			<img class="exhibition-statistics__decor" src="/static/images/past-decor-cat.png" alt="">
			<div class="statistics__description">
			<h2 class="statistics__description__title">Фотографии скоро появятся!<br>Загляните сюда позже.</h2>
		</div>
		</div>`
}

function showRepot(exhibition){
	if(!exhibition.results) return
	const reportArea = document.createElement("section")
	reportArea.classList.add("exhibition__report")

	const accordeon = document.createElement("div")
	accordeon.classList.add("accordion__container")
	accordeon.innerHTML = `
	<label for="chk-1" class="accordion__label">				
	<input id="chk-1" type="checkbox"/>
	 <div class="accordion__title__container">
			 <h3 class="accordion__title title">Результаты</h3>
	 </div>
		<div class="accordion__content">
			<p class="accordion__text">${exhibition.results}</p>
		</div>
	</label>`	
	document.querySelector(".main").appendChild(reportArea)	
	reportArea.appendChild(accordeon)	
}