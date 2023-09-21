from app.models import db, Business, environment, SCHEMA
import datetime
from sqlalchemy.sql import text

def seed_businesses():

    business1 = Business(
        name="Rita's Italian Ice & Frozen Custard",
        address="7866 N Academy Blvd Colorado",
        city="Colorado",
        state="CO",
        zip_code="12345",
        website="https://www.ritasice.com/",
        about="""Rita's Italian Ice & Frozen Custard is the largest Italian Ice concept in the nation, currently operating in 31 states with over 600 shops.""",
        phone_number="(719) 465-2867",
        type="Ice Cream & Frozen Yogurt, Desserts , Pretzels",
        category_id=1,
        owner_id=1,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )


    business2 = Business(
        name="Bella's Bagels",
        address="3582 Blue Horizon Vw Ste 148",
        city="Colorado Springs",
        state="CO",
        zip_code="80924",
        website="https://www.getbellasbagels.com/",
        about="""The most delicious bagel in Colorado! Bella's Bagels - baked for boosting happiness. Family-owned, Bella's Bagels is a genuine NY-style bagel shop born in Colorado Springs and inspired by NJ roots. """,
        phone_number="1-234-567-8902",
        type="FoodCoffee & Tea, Sandwiches, Bagels",
        category_id=1,
        owner_id=2,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    business3 = Business(
        name="Gaspare's Pizza House & Italian Restaurant",
        address="5546 Geary Blvd",
        city="San Francisco",
        state="CA",
        zip_code="94121",
        website="https://www.gasparespizzeria.com/",
        about=""" Specialties Classic San Francisco Pizzeria. Full Italian menu. Dine in, Take out & Delivery. Have your next family meal at Gaspare's Pizza.""",
        phone_number="(415) 387-5025",
        type="Pizza, Italian",
        category_id=1,
        owner_id=3,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business4 = Business(
        name="Roma Antica",
        address="3242 Scott St",
        city="San Francisco",
        state="CA",
        zip_code="94123",
        website="https://www.romasf.com/",
        about="""The two hope to bring reasonably-priced Italian meals--with an authentic Italian vibe--to the area. And true to the family-friendly spirit of Italian eateries, the restaurant was created with both parents and their children in mind.""",
        phone_number="(415) 896-4281",
        type="Pizza, Italian, Pasta Shops",
        category_id=1,
        owner_id=4,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business5 = Business(
        name="The Italian Homemade Company",
        address="1919 Union St",
        city="San Francisco",
        state="CA",
        zip_code="94123",
        website="https://italianhomemade.com/",
        about="Specialties : Fresh pasta, authentic taste!",
        phone_number="(415) 625-5965",
        type="Italian, Pasta Shops, Dessert",
        category_id=1,
        owner_id=5,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business6 = Business(
        name="Fiorella - Sunset",
        address="1240 9th Ave",
        city="San Francisco",
        state="CA",
        zip_code="94122",
        website="http://www.fiorella-sf.com/",
        about="""In 2015, Brandon approached Boris with an idea: a delicious, quality, wood-fired pizza shop with fresh ingredients was needed in the Richmond District of San Francisco. As an SF native who grew up a few blocks from Fiorella, Boris was excited by this concept.""",
        phone_number="(415) 404-6997",
        type="Italian, Pizza, Cocktail Bars",
        category_id=1,
        owner_id=6,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business7 = Business(
        name="Cielito Lindo",
        address="3450 Balboa St",
        city="San Francisco",
        state="CA",
        zip_code="94121",
        website="https://www.theinfatuation.com/san-francisco/reviews/cielito-lindo",
        about="Best Tacos in town and best place to eat",
        phone_number="(415) 742-0959",
        type="Mexican",
        category_id=2,
        owner_id=7,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business8 = Business(
        name="Sunset Cantina",
        address="3414 Judah St",
        city="San Francisco",
        state="CA",
        zip_code="94122",
        website="https://sunsetcantinasf.com/",
        about="""Specialties Sunset Cantina was established in September 2019. Our mission is to offer the freshest classic Mexican street food faves. We look forward to serving our friends, neighbors, and community. Bienvenidos ...""",
        phone_number="(415) 571-8874",
        type="Cocktails Bars, Mexican",
        category_id=2,
        owner_id=8,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business9 = Business(
        name="Otra",
        address="682 Haight St",
        city="San Francisco",
        state="CA",
        zip_code="94117",
        website="https://www.otrasf.com/",
        about="""Focused on fresh masa, bold flavors, and traditional Mexcian cooking techniques, Otra brings you dishes reflective of Chef Nick's childhood experiences.""",
        phone_number="(415) 500-2774",
        type="Cocktails Bars, Mexican",
        category_id=2,
        owner_id=9,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business10 = Business(
        name="Santeria",
        address="2251 Market St",
        city="San Francisco",
        state="CA",
        zip_code="94114",
        website="https://santeria-sf.com/",
        about="""Specialties We have curated a list that will cure all your worries. Traditional Michoacán carnitas, Pulpo al Pastor, and Tinga Flautas are just a few of the dishes you can expect from our menu.""",
        phone_number="(415) 896-4496",
        type="Mexican, Cocktails Bars, Desserts",
        category_id=2,
        owner_id=10,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business11 = Business(
        name="El Farolito",
        address="2779 Mission St",
        city="San Francisco",
        state="CA",
        zip_code="94110",
        website="https://elfarolitosf.com/",
        about="No-frills Mexican Taqueria & late-night haunt serving comfort food like tacos & burritos.",
        phone_number="(415) 824-7877",
        type="Mexican",
        category_id=2,
        owner_id=11,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business12 = Business(
        name="Caliente Bistro Kitchen",
        address="4828 Geary Blvd",
        city="San Francisco",
        state="CA",
        zip_code="94118",
        website="https://www.calientebistro.com/",
        about="""Specialties Blink and you might miss it, but this little spot in the Inner Richmond is serving up some of the freshest, most flavorful Mexican food in the city. Certain recipes on the menu were highly perfected over generations.""",
        phone_number="(415) 379-6250",
        type="Mexican, Bars",
        category_id=2,
        owner_id=12,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business13 = Business(
        name="Mazra",
        address="504 San Bruno Ave W",
        city="San Bruno",
        state="CA",
        zip_code="94066",
        website="https://www.eatmazra.com/",
        about="""Specialties Mazra is a family-owned Mediterranean restaurant located in San Bruno, just minutes from San Francisco Airport.""",
        phone_number="(650) 491-6019",
        type="Mediterranean, Barbeque, Tapas/Small Plates",
        category_id=3,
        owner_id=13,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business14 = Business(
        name="Beit Rima",
        address="138 Church St",
        city="San Francisco",
        state="CA",
        zip_code="94114",
        website="http://www.beitrimasf.com/",
        about="""Specialties Authentic Arabic comfort food with fresh ingredients sourced from local farms, made and served with love.""",
        phone_number="(415) 703-0270",
        type="Arabic ,Mediterranean ,Lebanese",
        category_id=3,
        owner_id=14,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business15 = Business(
        name="Abu Salim Middle Eastern Grill",
        address="1599 Haight St",
        city="San Francisco",
        state="CA",
        zip_code="94117",
        website="https://www.abusalimsf.com",
        about="""Hummus With Beef & Lamb Shawarma The shawarma is tender yet crispy, and well-seasoned throughout. Combined with the hummus, its a consistent hit and our favorite item on the menu. Order this.""",
        phone_number="(415) 547-0051",
        type="Halal, Falafel, Arabic",
        category_id=3,
        owner_id=15,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business16 = Business(
        name="Beit Rima",
        address="86 Carl St",
        city="San Francisco",
        state="CA",
        zip_code="94117",
        website="http://beitrimasf.com/",
        about="""Since opening in 2019, Beit Rima has been voted Best New Restaurant by San Franciscans via SF Weekly and Top 100 Restaurant from the SF Chronicle along with rave reviews from food critics. In 2020, Beit Rima was recognized on a national level""",
        phone_number="(415) 566-1274",
        type="Arabic ,Mediterranean ,Lebanese",
        category_id=3,
        owner_id=16,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business17 = Business(
        name="Reems",
        address="2901 Mission St",
        city= "San Francisco",
        state="CA",
        zip_code="94110",
        website="https://www.reemscalifornia.com/",
        about="""Specialties Reem's offers the warmth of Arab hospitality through the discovery of the flavors, aromas, and techniques of Arab street corner bakeries.""",
        phone_number="(415) 780-1953",
        type="Bakeries, Arabic, Middle Eastern",
        category_id=3,
        owner_id=17,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business18 = Business(
        name="Old Jerusalem Restaurant",
        address="2966 Mission St",
        city="San Francisco",
        state="CA",
        zip_code="94110",
        website="http://www.oldjerusalem.co/",
        about="""Specialties We offer a traditional spread of middle eastern and Mediterranean delights ranging from kababs to vegetarian dishes.""",
        phone_number="(415) 642-5958",
        type="Halal, Kebab, Mediterranean",
        category_id=3,
        owner_id=18,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business19 = Business(
        name="Shoshin Sushi",
        address="2450 Clement St",
        city="San Francisco",
        state="CA",
        zip_code="94121",
        website="https://www.shoshinsushi.com/",
        about="""Specialties Only the tastiest and freshest Japanese food is served here.""",
        phone_number="(415) 386-8008",
        type="Japanese, Sushi Bars",
        category_id=4,
        owner_id=19,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business20 = Business(
        name="Yuji",
        address="1700 post st Unit K",
        city="San Francisco",
        state="CA",
        zip_code="94115",
        website="http://kappoyuji.com/",
        about="""Specialties Kappo kaiseki style restaurant""",
        phone_number="(415) 658-7128",
        type="Japanese",
        category_id=4,
        owner_id=20,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business21 = Business(
        name="Japateam Sushi",
        address="2985 Junipero Serra Beulevard Ste 03",
        city="Daly City",
        state="CA",
        zip_code="94014",
        website="https://www.japateam.com/",
        about="""Born out of a passion for flavor and tradition, Japa Team Sushi is a journey of success that blossomed in the corners of a modest apartment in California's Bay Area.""",
        phone_number="(407) 984-0190",
        type="Japanese, Sushi Bars",
        category_id=4,
        owner_id=1,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business22 = Business(
        name="Bento Peak",
        address="4724 Geary Blvd",
        city="San Francisco",
        state="CA",
        zip_code="94118",
        website="http://www.bentopeak.com/",
        about="""Bento Peak, Japanese Cuisine offers high quality, great value and fast sushi or Japanese restaurant dining experiences.""",
        phone_number="(415) 592-8069",
        type="Japanese",
        category_id=4,
        owner_id=2,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business23 = Business(
        name="Nara Restaurant & Sake Bar",
        address="518 Haight St",
        city="San Francisco",
        state="CA",
        zip_code="94117",
        website="https://www.naraonhaight.com/",
        about="""Specialties First of all, Nara offers Happy hours between 5-7pm""",
        phone_number="(415) 417-0518",
        type= "Japanese, Sushi Bars",
        category_id=4,
        owner_id=3,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business24 = Business(
        name="Izakaya Mayumi",
        address="2221 Clement St",
        city="San Francisco",
        state="CA",
        zip_code="94121",
        website="http://izakayamayumi.com",
        about="""History Established in 2019. Grand opening will be 9/4/2019""",
        phone_number="(415) 742-4159",
        type="Izakaya",
        category_id=4,
        owner_id=4,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business25 = Business(
        name="Hard Rock Cafe",
        address="Pier 39 Space 256 Bldg Q, Level 1",
        city="San Francisco",
        state="CA",
        zip_code="94133",
        website="https://www.hardrockcafe.com/location/san-francisco/",
        about="""Specialties Hard Rock Cafe on Pier #39 is here to make your trip rock! The Cafe is located next to the Bay's waterfront, is full of rock-n-roll memorabilia and features a savory menu as the cherry on top.""",
        phone_number="(415) 358-3425",
        type="American, Burgers, Cocktail Bar",
        category_id=5,
        owner_id=5,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business26 = Business(
        name="The Garden Club",
        address="1144 Mission Rd South",
        city="San Francisco",
        state="CA",
        zip_code="94080",
        website="https://www.gardenclubrestaurant.com/",
        about="""Specialties Your choice of family-style restaurant in South San Francisco, Our unique family-style dining, also known as casual style dining.""",
        phone_number="(650) 873-4910",
        type="American, Bar, Breakfast&Brunch",
        category_id=5,
        owner_id=6,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business27 = Business(
        name="The Snug",
        address="2301 Fillmore St",
        city="San Francisco",
        state="CA",
        zip_code="94115",
        website="https://www.thesnugsf.com/",
        about="""Specialties Unique cocktails, local beer, small-producer wines, and modern Californian comfort food -- all served up in a warm and comfortable environment.""",
        phone_number="1-234-567-8902",
        type="American, Cocktail Bars",
        category_id=5,
        owner_id=7,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business28 = Business(
        name="Heritage Restaurant & Bar",
        address="708 Clement St",
        city="San Francisco",
        state="CA",
        zip_code="94118",
        website="https://www.heritagerestaurantbar.com/",
        about="""Specialties We have an unique space in front of the fireplace for private parties that seats up to 16. It is perfect for special occasions, birthdays, work gatherings, etc.""",
        phone_number="(415) 386-2200",
        type="American, Cocktail Bars",
        category_id=5,
        owner_id=8,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business29 = Business(
        name="Kitchen Story",
        address="3499 16th St",
        city="San Francisco",
        state="CA",
        zip_code="94114",
        website="https://www.kitchenstorysf.com/",
        about="""Specialties Breakfast, Brunch, Bloody Marys, Millionaire's Bacon""",
        phone_number="(415) 525-4905",
        type="American, Asian Fusion",
        category_id=5,
        owner_id=9,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
    business30 = Business(
        name="The New Spot On Polk",
        address="2401 Polk St",
        city="San Francisco",
        state="CA",
        zip_code="94109",
        website="https://thenewspotonpolk.com/",
        about="""""Specialties Open during SF Shelter in place for Outdoor Seating Dine-In, Take-outs, Curb-Side, and Deliveries including Beer, Wine & Cocktails.""",
        phone_number="(415) 913-7775",
        type="American",
        category_id=5,
        owner_id=10,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )


    db.session.add_all([
    business1, business2, business3, business4, business5,
    business6, business7, business8, business9, business10,
    business11, business12, business13, business14, business15,
    business16, business17, business18, business19, business20,
    business21, business22, business23, business24, business25,
    business26, business27, business28, business29, business30
    ])

    db.session.commit()

def undo_businesses():
    if environment == "production":
       db.session.execute(f"TRUNCATE table {SCHEMA}.businesses RESTART IDENTITY CASCADE;")
    else:
       db.session.execute(text("DELETE FROM businesses"))

    db.session.commit()
