import jinja2
import os
import xsrfutil

PROJECT_ID = 'our-bikes'

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
JINJA_ENVIRONMENT.globals['xsrf_token'] = xsrfutil.xsrf_token

PAGES = {
  '/': 'index.html',
  '/supporters': 'supporters.html',
  '/countdown': 'countdown.html',
  '/actionalert': 'alert.html',
}

REDIRECTS = {
  '/newsletter': 'https://us19.campaign-archive.com/?u=a1b97c965afa1a1543759ba94&id=939d61e88e',
  '/stories': 'https://docs.google.com/forms/d/e/1FAIpQLSfMz5RxGoqetMsFF6B31RCfGsC3_6bO3EtqQ2PU2FZ36ANcFQ/viewform',
  '/why': 'https://medium.com/@ourbikes/why-bike-share-stations-are-good-for-our-neighborhood-in-san-francisco-1f3931c87519',
  '/map': '/stories',
  '/nick': 'https://www.nickjosefowitz.com/events/volunteer-canvass-social-with-ourbikes-sf',
  '/parking': 'https://www.sfmta.com/getting-around/bike/bike-parking/request-bike-rack',
  '/bikeracks': 'https://www.sfmta.com/getting-around/bike/bike-parking/request-bike-rack',
  '/countdown': '/',
}

RECIPIENTS = "Aaron.Peskin@sfgov.org, hello@ourbikes.org"

EMAIL_SUBJECTS = [
  "Please support bike share in District 3.",
  "My support for more bike share in D3.",
  "I support Ford GoBike and JUMP",
  "I bike in D3. Help me by supporting more bike share.",
  "A note of support for bike share (JUMP/Ford GoBike)",
  "Bike share in D3",
]

EMAIL_OPEN = [
  "Hello Supervisor Aaron Peskin,",
  "Supervisor Peskin:",
  "Dear Supervisor Aaron Peskin,",
  "Supervisor Aaron Peskin,",
]

EMAIL_CLOSE = [
  "Thanks.",
  "I look forward to using these new biking options and reducing traffic in our neighborhoods. Thank you.",
  "Thank you.",
  "I hope you will support new Ford GoBike bike share stations and help expand the JUMP system.\n\nThanks!",
  "I appreciate your work in supporting bike share.\n\nThanks!",
]

EMAIL_BODYS = [
"""I am writing in support of bike share in District 3. As a resident of D3, I believe we need more transportation options and bike share is a smart way to get people out of cars.

I wanted to take a quick moment to let you know that I use bike share - both Ford GoBike and JUMP. I fully support expanding these systems and hope you will do the same.""",

"""Bike share is a sustainable and healthy way to get around the city. Sadly, D3 doesn't have the bike share coverage of other areas of the city. It has made living in our part of the city more difficult and often forces me to take an Uber or Lyft.

As our D3 Supervisor, I hope you will encourage both Ford GoBike and JUMP to grow their networks in our district. This will really help me get around and I think it will help improve quality of life for all residents.""",

"""I am excited to hear a few new Ford GoBike stations may be installed soon in District 3 and that JUMP will increase to 500 bikes citywide (which might allow them to extend coverage to our neighborhood).

As my supervisor, I hope you'll support the rollout of these new transportation options. It's the right choice for our city, community, and planet.""",

"""Bike share has revolutionized how many of my friends get around the city. Unfortunately, living in District 3, there isn't a solid bike share network for me to use.

Supervisor, please support more bike share (JUMP and Ford GoBike) in North Beach, Russian Hill, and Nob Hill.""",

]

NEIGHBORHOODS = [
  {
    "name": "Alamo Square",
    "primary_district": "5"
  },
  {
    "name": "Anza Vista",
    "primary_district": "2"
  },
  {
    "name": "Ashbury Heights",
    "primary_district": "5"
  },
  {
    "name": "Balboa Park",
    "primary_district": "11"
  },
  {
    "name": "Balboa Terrace",
    "primary_district": "7"
  },
  {
    "name": "Bayview",
    "primary_district": "10"
  },
  {
    "name": "Bernal Heights",
    "primary_district": "9"
  },
  {
    "name": "Buena Vista",
    "primary_district": "8"
  },
  {
    "name": "Castro",
    "primary_district": "8"
  },
  {
    "name": "Cathedral Hill",
    "primary_district": "5"
  },
  {
    "name": "China Basin",
    "primary_district": "6"
  },
  {
    "name": "Chinatown",
    "primary_district": "3"
  },
  {
    "name": "Civic Center",
    "primary_district": "3"
  },
  {
    "name": "Cole Valley",
    "primary_district": "5"
  },
  {
    "name": "Corona Heights",
    "primary_district": "8"
  },
  {
    "name": "Cow Hollow",
    "primary_district": "2"
  },
  {
    "name": "Crocker-Amazon",
    "primary_district": "11"
  },
  {
    "name": "Design District",
    "primary_district": "6"
  },
  {
    "name": "Diamond Heights",
    "primary_district": "8"
  },
  {
    "name": "Dogpatch",
    "primary_district": "10"
  },
  {
    "name": "Dolores Heights",
    "primary_district": "8"
  },
  {
    "name": "Duboce Triangle",
    "primary_district": "8"
  },
  {
    "name": "Embarcadero",
    "primary_district": "6"
  },
  {
    "name": "Eureka Valley",
    "primary_district": "8"
  },
  {
    "name": "Excelsior",
    "primary_district": "11"
  },
  {
    "name": "Fillmore",
    "primary_district": "5"
  },
  {
    "name": "Financial District",  
    "primary_district": "3"
  },
  {
    "name": "Fisherman's Wharf",
    "primary_district": "3"
  },
  {
    "name": "Glen Park",
    "primary_district": "8"
  },
  {
    "name": "Golden Gate Heights", 
    "primary_district": "7"
  },
  {
    "name": "Haight-Ashbury",
    "primary_district": "5"
  },
  {
    "name": "Hayes Valley",
    "primary_district": "5"
  },
  {
    "name": "Hunters Point",
    "primary_district": "10"
  },
  {
    "name": "India Basin",
    "primary_district": "10"
  },
  {
    "name": "Ingleside",
    "primary_district": "11"
  },
  {
    "name": "Ingleside Terraces",  
    "primary_district": "11"
  },
  {
    "name": "Inner Sunset",
    "primary_district": "7"
  },
  {
    "name": "Jackson Square",
    "primary_district": "3"
  },
  {
    "name": "Japantown",
    "primary_district": "5"
  },
  {
    "name": "Jordan Park",
    "primary_district": "2"
  },
  {
    "name": "Laguna Honda",
    "primary_district": "7"
  },
  {
    "name": "Lake Street",
    "primary_district": "2"
  },
  {
    "name": "Lakeside",
    "primary_district": "7"
  },
  {
    "name": "Lakeshore",
    "primary_district": "7"
  },
  {
    "name": "Laurel Heights",
    "primary_district": "2"
  },
  {
    "name": "Little Russia",
    "primary_district": "2"
  },
  {
    "name": "Little Saigon",
    "primary_district": "3"
  },
  {
    "name": "Lone Mountain",
    "primary_district": "1"
  },
  {
    "name": "Lower Haight",
    "primary_district": "5"
  },
  {
    "name": "Lower Pacific Heights", 
    "primary_district": "2"
  },
  {
    "name": "Lower Nob Hill",
    "primary_district": "3"
  },
  {
    "name": "Marina District",
    "primary_district": "2"
  },
  {
    "name": "Merced Heights",
    "primary_district": "7"
  },
  {
    "name": "Midtown Terrace",
    "primary_district": "7"
  },
  {
    "name": "Mid-Market",
    "primary_district": "6"
  },
  {
    "name": "Miraloma Park",
    "primary_district": "7"
  },
  {
    "name": "Mission Bay",
    "primary_district": "6"
  },
  {
    "name": "Mission District",
    "primary_district": "9"
  },
  {
    "name": "Mission Dolores",
    "primary_district": "8"
  },
  {
    "name": "Mission Terrace",
    "primary_district": "8"
  },
  {
    "name": "Nob Hill",
    "primary_district": "3"
  },
  {
    "name": "Noe Valley",
    "primary_district": "8"
  },
  {
    "name": "North Beach",
    "primary_district": "3"
  },
  {
    "name": "North of Panhandle",  
    "primary_district": "5"
  },
  {
    "name": "Oceanview",
    "primary_district": "11"
  },
  {
    "name": "Outer Mission",
    "primary_district": "11"
  },
  {
    "name": "Outer Sunset",
    "primary_district": "4"
  },
  {
    "name": "Pacific Heights",
    "primary_district": "2"
  },
  {
    "name": "Parkmerced",
    "primary_district": "7"
  },
  {
    "name": "Parkside",
    "primary_district": "4"
  },
  {
    "name": "Polk Gulch",
    "primary_district": "2"
  },
  {
    "name": "Portola",
    "primary_district": "9"
  },
  {
    "name": "Portola Place",
    "primary_district": "9"
  },
  {
    "name": "Potrero Hill",
    "primary_district": "10"
  },
  {
    "name": "Presidio",
    "primary_district": "2"
  },
  {
    "name": "Presidio Heights",
    "primary_district": "2"
  },
  {
    "name": "Richmond District",
    "primary_district": "1"
  },
  {
    "name": "Rincon Hill",
    "primary_district": "6"
  },
  {
    "name": "Russian Hill",
    "primary_district": "2"
  },
  {
    "name": "Saint Francis Wood",  
    "primary_district": "7"
  },
  {
    "name": "Sea Cliff",
    "primary_district": "2"
  },
  {
    "name": "Sherwood Forest",
    "primary_district": "7"
  },
  {
    "name": "Silver Terrace",
    "primary_district": "10"
  },
  {
    "name": "South Beach",
    "primary_district": "6"
  },
  {
    "name": "South of Market",
    "primary_district": "6"
  },
  {
    "name": "South Park",
    "primary_district": "6"
  },
  {
    "name": "Sunnydale",
    "primary_district": "10"
  },
  {
    "name": "Sunnyside",
    "primary_district": "7"
  },
  {
    "name": "Sunset District",
    "primary_district": "4"
  },
  {
    "name": "Telegraph Hill",
    "primary_district": "3"
  },
  {
    "name": "Tenderloin",
    "primary_district": "6"
  },
  {
    "name": "Treasure Island",
    "primary_district": "6"
  },
  {
    "name": "Twin Peaks",
    "primary_district": "8"
  },
  {
    "name": "Union Square",
    "primary_district": "3"
  },
  {
    "name": "Upper Market",
    "primary_district": "8"
  },
  {
    "name": "Visitacion Valley",
    "primary_district": "10"
  },
  {
    "name": "Vista del Mar",
    "primary_district": "1"
  },
  {
    "name": "West Portal",
    "primary_district": "7"
  },
  {
    "name": "Western Addition",
    "primary_district": "5"
  },
  {
    "name": "Yerba Buena",
    "primary_district": "6"
  },
  {
    "name": "Other / Outside San Francisco"
  }
]