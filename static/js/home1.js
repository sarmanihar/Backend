const API_KEY = `d1def1caf39bde54c9449e6730f209cf`

const form = document.querySelector("form")
const search = document.querySelector("#search")
const search1 = document.querySelector("#song_name")
const search2 = document.querySelector("#artist_name")
const switch1 = document.querySelector('#btn')
const weather = document.querySelector("#weather")
const getlyrics = async(city1, city2) => {
    weather.innerHTML = `<h2> Loading... <h2>`
    const api_url = `https://cors-anywhere.herokuapp.com/https://api.musixmatch.com/ws/1.1/matcher.lyrics.get?q_track=${city1}&q_artist=${city2}&apikey=${API_KEY}`
    const response = await fetch(api_url)
    const data = await response.json()
}

const showlyrics = (data) => {
    if (data.cod == "404") {
        weather.innerHTML = `<h2> City Not Found <h2>`
        return;
    }
    console.log(data.message.body.lyrics.lyrics_body)
    weather.innerHTML = `

        <div>
            <p>${data.message.body.lyrics.lyrics_body} </p>

        </div>

    `
}
switch1.addEventListener('click', (e) => {

        getlyrics(search1.value.replace(/\s/g, '%20'), search2.value)
        console.log(search1.value.replace(/\s/g, '%20'))
        console.log(search2.value)

    })
    /*{% if abcd == 1 %}
        
           <a href="http://127.0.0.1:8000/signup1/">
            <h1>signup</h1>
           </a>
           <a href="http://127.0.0.1:8000/login/">
            <h1>login</h1>
           </a>
              
    {% else %}
        
          <p>welcome {{abcd}}</p>
          {% if fgh == 1 %}   
             <a href="http://127.0.0.1:8000/showseller1/">make your objects</a>
             <a href="http://127.0.0.1:8000/showseller2/">write their amounts,price etc..</a>
             <a href="http://127.0.0.1:8000/showseller3/">chek your orders</a>
           {% else %}
              <a href="http://127.0.0.1:8000/showbuyer1/">order</a>
            {% endif %}
                         
    {% endif %}

    */