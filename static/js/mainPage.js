async function getMain(){
	try{
		console.log(1)
		const response = await fetch("http://127.0.0.1:8000/api/exhibition/1/")
		const data = await response.json()
		console.log(data)

	}catch{

	}
}

getMain()