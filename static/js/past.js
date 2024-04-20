import { allExhibitions } from "./getAllExhibitions"
import {createPhotoCard, formatDays, formatMonth, addActiveClass} from "./functions"
import { getStatistics } from "./getStatistics";

if(window.location.href.includes("past")){
	addActiveClass(".link__photoreport")
	const exhibitions = new Map()
	allExhibitions.forEach((item)=>{
		exhibitions.set(item.id, item)
	})	

	const id = new URLSearchParams(window.location.search).get('id');	

	showPhotos(exhibitions.get(+id))
	showStatistics(+id)
} 

function showPhotos(exhibition){
	const photos = []
	exhibition.exhibition_foto.forEach(item => photos.push(item.foto))
	document.querySelector(".photos__title").innerHTML = 
	`${formatDays(exhibition)} ${formatMonth(exhibition.date_begin)}<br>${exhibition.location}`
	const photosContainer = document.querySelector(".photos__container")

	photos.forEach(item => createPhotoCard(item, photosContainer))
}

async function showStatistics(exhibitionID){
	const numbersOfPets = await getStatistics(exhibitionID)

	document.querySelector(".cats__number").innerHTML = numbersOfPets.кошка
	document.querySelector(".dogs__number").innerHTML = numbersOfPets.собака
}