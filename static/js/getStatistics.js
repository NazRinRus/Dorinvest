async function getFullStatistics(){
	try{
		const response = await fetch("http://127.0.0.1:8000/api/statistics_all/")
		const data = await response.json()

		const fullStatistics = formatingKeys(data)
		return fullStatistics

	}catch{

	}
}

const fullStatistics = await getFullStatistics()

async function getStatistics(exhibitionID){
	try{
		const response = await fetch(`http://127.0.0.1:8000/api/statistics/${exhibitionID}`)
		const data = await response.json()

		const statistics = formatingKeys(data)
		return statistics

	}catch{

	}
}

function formatingKeys(data) {
	const allKeys = []
	const newStatistics = {}

	for (let key in data){
		if(key.toLowerCase().includes("кош")) newStatistics.кошка = data[key]
		if(key.toLowerCase().includes("соб")) newStatistics.собака = data[key]
		allKeys.push(key.toLowerCase())
	}	
	return newStatistics
}


export {fullStatistics, getStatistics}