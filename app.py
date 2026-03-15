from flask import Flask, render_template, request

app = Flask(__name__)

india_travel = {
    "Maharashtra": {
        "Mumbai": [
            {"name": "Gateway of India", "img": "https://upload.wikipedia.org/wikipedia/commons/4/4f/Gateway_of_India.jpg"},
            {"name": "Marine Drive", "img": "https://upload.wikipedia.org/wikipedia/commons/b/b0/Marine_Drive.jpg"},
            {"name": "Elephanta Caves", "img": "https://upload.wikipedia.org/wikipedia/commons/3/3f/Elephanta_Caves.jpg"}
        ],
     "Nashik": [
            {"name": "Trimbakeshwar Temple", "img": "https://upload.wikipedia.org/wikipedia/commons/8/88/Trimbakeshwar.jpg"},
            {"name": "Sula Vineyards", "img": "https://upload.wikipedia.org/wikipedia/commons/4/49/Sula_Vineyards.jpg"},
            {"name": "Pandavleni Caves", "img": "https://upload.wikipedia.org/wikipedia/commons/a/a3/Pandavleni.jpg"}
        ]
    },

    "Chhattisgarh": {
        "Raipur": [
            {"name": "Nandan Van Zoo", "img": "https://upload.wikipedia.org/wikipedia/commons/e/e2/Nandan_Van_Zoo.jpg"},
            {"name": "Vivekananda Sarovar", "img": "https://upload.wikipedia.org/wikipedia/commons/0/0f/Budha_Talab_Raipur.jpg"},
            {"name": "Mahant Ghasidas Museum", "img": "https://upload.wikipedia.org/wikipedia/commons/f/f7/Mahant_Ghasidas_Museum.jpg"}
           ]
},
    "Rajasthan": {
     "Jaipur": [
           {"name": "Hawa Mahal", "img": "https://upload.wikimedia.org/wikipedia/commons/4/4c/Hawa_Mahal.jpg"},
           {"name": "Amber Fort", "img": "https://upload.wikimedia.org/wikipedia/commons/d/d1/Amber_Fort.jpg"}
    ],
    "Udaipur": [
        {"name": "Lake Pichola", "img": "https://upload.wikimedia.org/wikipedia/commons/6/6e/Lake_Pichola.jpg"},
        {"name": "City Palace Udaipur", "img": "https://upload.wikimedia.org/wikipedia/commons/9/94/City_Palace_Udaipur.jpg"}
    ]
},

  "Uttar Pradesh": {
           "Agra": [
             {"name": "Taj Mahal", "img": "https://upload.wikimedia.org/wikipedia/commons/d/da/Taj-Mahal.jpg"},
             {"name": "Agra Fort", "img": "https://upload.wikimedia.org/wikipedia/commons/9/99/Agra_Fort.jpg"}
    ],
         "Varanasi": [
                {"name": "Kashi Vishwanath Temple", "img": "https://upload.wikipedia.org/wikipedia/commons/4/4d/Kashi_Vishwanath.jpg"},
                {"name": "Dashashwamedh Ghat", "img": "https://upload.wikipedia.org/wikipedia/commons/2/28/Dashashwamedh_Ghat.jpg"}
    ]
},

     "Delhi": {
    "Delhi": [
        {"name": "India Gate", "img": "https://upload.wikimedia.org/wikipedia/commons/9/99/India_Gate.jpg"},
        {"name": "Red Fort", "img": "https://upload.wikimedia.org/wikipedia/commons/0/0c/Red_Fort.jpg"}
    ]
},

"Goa": {
    "Panaji": [
        {"name": "Baga Beach", "img": "https://images.unsplash.com/photo-1501785888041-af3ef285b470"},
        {"name": "Fort Aguada", "img": "https://upload.wikimedia.org/wikipedia/commons/7/7c/Fort_Aguada.jpg"}
    ]
},

"Kerala": {
    "Munnar": [
        {"name": "Tea Gardens Munnar", "img": "https://images.unsplash.com/photo-1501785888041-af3ef285b470"},
        {"name": "Eravikulam National Park", "img": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee"
        }
    ]
},

"Tamil Nadu": {
    "Chennai": [
        {"name": "Marina Beach", "img": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Marina_Beach.jpg"},
        {"name": "Kapaleeshwarar Temple", "img": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Kapaleeshwarar.jpg"}
    ]
}

}
        
@app.route("/")
def home():
    states = list(india_travel.keys())
    return render_template("index.html", states=states)

@app.route("/plan", methods=["POST"])
def plan():

    state = request.form.get("state")
    city = request.form.get("city")
    days = int(request.form.get("days"))

    if state in india_travel and city in india_travel[state]:
       places = india_travel[state][city]
       itinerary = places[:days]

       return render_template("result.html", itinerary=itinerary, city=city)
    else:
       return "sorry we don't have this city data"
if __name__ == "__main__":
    app.run(debug=True)
