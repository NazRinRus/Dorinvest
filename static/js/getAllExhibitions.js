async function getAllExhibitions(){
	try{
		const response = await fetch("http://127.0.0.1:8000/api/exhibition/")
		const data = await response.json()
		//console.log(data)
		return data
		
	}catch{

	}
}

const allExhibitions = await getAllExhibitions()

export {allExhibitions}