function formatDays(exhibition){
	const start = +(exhibition.date_begin[8]+exhibition.date_begin[9])
	const end = +(exhibition.date_end[8]+exhibition.date_end[9])

	const result = `${start}–${end}`
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
function createPagination(allQuantity, needQuantity){
	const pagesQuantity = Math.ceil(allQuantity / needQuantity)
	if(pagesQuantity === 1) return

	const pagination = document.querySelector(".pagination")

	//pagination.innerHTML = ``
	//parentNode.addChild(pagination)

	
	for(let i = 0; i < pagesQuantity; i++){
		console.log(i)
		const paginationItem = document.createElement("button")
		paginationItem.classList.add("pagination__item")
		paginationItem.innerHTML = `${i+1}`
		
		pagination.appendChild(paginationItem)
	}
}

export {formatDays, formatMonth, addActiveClass, createPagination}