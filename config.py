import jinja2
import os
import xsrfutil

PROJECT_ID = 'our-bikes'

GLOBAL_STRINGS = {
  'name': 'Our Bikes'
}

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
JINJA_ENVIRONMENT.globals['xsrf_token'] = xsrfutil.xsrf_token

# Site config

PAGES = {
  '/': 'index.html',
  '/supporters': 'supporters.html',
  '/countdown': 'countdown.html',
  '/actionalert': 'alert.html',
}

REDIRECTS = {
  '/bikeracks': 'https://www.sfmta.com/getting-around/bike/bike-parking/request-bike-rack',
  '/countdown': '/',
  '/map': '/stories',
  '/newsletter': 'https://us19.campaign-archive.com/?u=a1b97c965afa1a1543759ba94&id=939d61e88e',
  '/nick': 'https://www.nickjosefowitz.com/events/volunteer-canvass-social-with-ourbikes-sf',
  '/parking': 'https://www.sfmta.com/getting-around/bike/bike-parking/request-bike-rack',
  '/stories': 'https://docs.google.com/forms/d/e/1FAIpQLSfMz5RxGoqetMsFF6B31RCfGsC3_6bO3EtqQ2PU2FZ36ANcFQ/viewform',
  '/why': 'https://medium.com/@ourbikes/why-bike-share-stations-are-good-for-our-neighborhood-in-san-francisco-1f3931c87519',
}


# Letter campaign config

LETTER_CAMPAIGN_ACTIVE = True

EMAIL_TO = "bevan.dufty@bart.gov"
EMAIL_BCC = "hello@ourbikes.org"

EMAIL_SUBJECTS = [
  "Delay on bike share at 24th St Mission BART?",
  "Help me get to BART easier with bike share!",
  "Bike share at the Mission BART stations",
  "Ford GoBike at Mission BART stations",
  "Support for Ford GoBike at 24th Street Mission BART",
  "Support for Ford GoBike at Mission BART stations.",
  "Help us get bike share at 24th St BART",
  "Please help us get bike share at 24th Street BART",
  "Unblock 24th Street BART bike share.",
  "Bike share at BART isn't controversial.",
  "Bevan, help us bike share to BART!",
  "Bike share on the 24th BART Plaza",
  "I use bike share and BART.",
  "Ford GoBike at BART in the Mission",
  "GoBike at BART's 24th Street Mission station",
  "Ford GoBike station at 24th Street BART",
  "Bike share at 24th Street BART",
  "24th St Mission BART Bike Share Station?"
]

EMAIL_OPEN = [
  "Hello Director Bevan Dufty,",
  "BART Director Dufty,",
  "Dear BART Director Bevan Dufty,",
  "Hi Director Dufty,",
  "Bevan,",
  "Director Dufty,",
  "BART Director Bevan Dufty -"
]

EMAIL_CLOSE = [
  "Best regards,",
  "Thank you,",
  "Sincerely,",
  "Thanks,",
  "Regards,",
  "Best,",
  "",
]

EMAIL_BODYS = [

# Email 1 - Bayview
"""I want to encourage you to **support BART staff and** approve Ford GoBike at 24th Street Mission BART.

**I understand there is a small group that is resisting this station. That is often the case, but you must look at the bigger picture. Hundreds of low income users rely on bike share. Those folks deserve an easier way to get to BART.**

**Ford** GoBike recently expanded to the Bayview. It takes less than 20 minutes to get to the 24th Street Mission BART station.

Do not deny our neighbors to BART via bike share. I ask you to support this bike share station.""",


# Email 2 - 16th Street success
"""The **Ford** GoBike station at 16th St Mission BART has been a **huge** success. The station is **both cleaner and** easier to get to than ever.

It's time to bring that success to the station at 24th Street. **Please do not block this progress.**

**I hear **BART staff has a plan to install bike share on the BART plaza at 24th Street in an unused space and that they have worked hard over the past 2 years to plan for bike share at this station.

**This new bike share station will increase usage of BART and decrease our city's carbon footprint.**

I hope you will support the BART staff **and our community** and get this station installed** now**.""",


# Email 3 - Personal
"""**I am an avid bike share user and so **I would benefit greatly from having bike share at 24th Street Mission BART.

This will increase my personal usage of BART **to get around the Bay Area** as it will allow me easier access to this station.

**As a Director, **I urge you to not block BART's work to approve this bike share station.""",


# Email 4 - Friendly for bikers
"""**I love BART and bike share, so wanted to raise an important issue.**

**As you know, **24th Street is BART's most walkable station in terms of the mode that riders arrive. We must build on this success and make this station also a friendly station for bikers.

I ask you to install a **Ford** GoBike station directly at 24th **Street** Mission BART as soon as possible.

**This station has been in the works since November 2016.** I am concerned that you have acted to delay the installation further.

This hurts **thousands of** bike share users like myself who rely on bike share to get around.""",


# Email 5 - More outreach
"""**Wanted to take a moment to ask for your help.**

We need bike share at 24th Street Mission BART** as soon as possible**. We do not need more outreach.

**Ford** GoBike conducted a survey **of residents** and the **vast** majority of the 500+ respondants supported bringing bike share to this station. **With this data, now is the time to install the station.**

**This station has been in the works since November 2016. It is time to install bike share on the BART plaza.**

Low-income Ford GoBike riders are disproportionately more likely to bike to BART stations than other bike share users. Time for you to be their voice and act accordingly.""",


# Email 6 - Equity
"""**Respectfully,** I **firmly** believe you should direct BART **staff** to install bike share at 24th **Street** Mission BART.

**This is a matter of transportation equity.** **Ford** GoBike has the most successful docked bike share equity program in US. 20 percent of **all** members are part of the bike share for all program. **These low income users have taken more than 80,000 riders since launch.**

Do not hurt our low income bike community by restricting access to BART at 24th Street Mission.""",

# Email 7 - 2 million
"""**I am writing regarding bike share at BART.**

**Ford** GoBike just passed the 2 million ride mark. **However, **I am concerned that you **still** do not take this transportation mode seriously.

We need a bike station at the 24th St **Mission** BART. Many **other** BART stations have bike share. I am curious to know why this BART station can't have bike share? **The space is not being used.**

I urge you to support bike share at all BART stations, particularly at 24th St. **Mission.**""",

# Email 8 - I use it
"""I use bike share **to get around San Francisco** frequently. I am not alone as the **Ford GoBike** system has over 2 million rides. Over 80,000 of those rides were to low income users.

Please approve bike share at 24th Street Mission BART. It should be directly on the plaza to encourage more usage.

**This will allow me and my fellow bike share users to connect to BART more easily.** This should be an easy decision given the success at other BART stations. **I welcome your support!**""",

"""Please help us get bike share at 24th Street Mission BART!

**20% of all Ford GoBike members are low income.** Bike share is making it cheaper and healthier for a diverse set of people in our city to get around.

**Being able to use bike share to get to BART makes the Bay Area's overall transit system work better and reduces our reliance on cars.**

As an elected BART director, I hope you'll take action to get this important bike share station installed."""

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