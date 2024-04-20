function createPhotoCard(photos, container){
	const photoCard = document.createElement("div")
	photoCard.classList.add("photo")

	photoCard.innerHTML = `<img src="${photos}" alt="">`
	container.appendChild(photoCard)
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
function addActiveClass(linkContainerClassName){
	if(document.querySelector(".navigation__list__item_active")){
		document.querySelector(".navigation__list__item_active").classList.remove("navigation__list__item_active")
	}
	document.querySelector(linkContainerClassName).classList.add("navigation__list__item_active")
}

export {createPhotoCard, formatDays, formatMonth, addActiveClass}