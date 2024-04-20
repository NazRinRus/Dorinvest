async function getQuestions(){
	try{
		const response = await fetch("http://127.0.0.1:8000/api/faq/")
		const data = await response.json()
		//console.log(data)
		return data
		
	}catch{

	}
}

const faq = await getQuestions()

export {faq}