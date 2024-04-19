async function getFullStatistics(){
	try{
		const response = await fetch("http://127.0.0.1:8000/api/statistics_all/")
		const data = await response.json()
		console.log(data)

	}catch{

	}
}

const fullStatistics = await getFullStatistics()

async function getStatistics(exhibitionID){
	try{
		const response = await fetch(`http://127.0.0.1:8000/api/statistics/${exhibitionID}`)
		const data = await response.json()
		console.log(data)

	}catch{

	}
}

export {fullStatistics, getStatistics}