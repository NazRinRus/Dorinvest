async function getSixExhibitions(){
	try{
		const response = await fetch("http://127.0.0.1:8000/api/exhibition/previous/")
		const data = await response.json()
		//console.log(data)
		return data[0]

	}catch{

	}
}

//const SixExhibition = await getSixExhibitions()

export {getSixExhibitions}