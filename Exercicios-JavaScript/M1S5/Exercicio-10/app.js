const getBtn = document.getElementById('btn');
const getImg = document.getElementById('imgGato');
const getUrl = 'https://api.thecatapi.com/v1/images/search'

getBtn.addEventListener('click', async () =>{
    try{
        const response = await fetch(getUrl)
        const responseJson = await response.json()
        getImg.src = responseJson[0].url;
    }
    catch(error){
        console.log(error)
    }
})