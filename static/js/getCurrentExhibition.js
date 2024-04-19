async function getCurrentExhibition(){
	try{
		const response = await fetch("http://127.0.0.1:8000/api/exhibition/now/")
		const data = await response.json()
		console.log(data)

	}catch{

	}
}

const currentExhibition = await getCurrentExhibition()

export {currentExhibition}