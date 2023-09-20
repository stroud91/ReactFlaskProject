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
        about="""Specialties
                 Rita's Italian Ice & Frozen Custard is the largest Italian Ice concept in the nation,
                 currently operating in 31 states with over 600 shops.
                 Our popular chain offers a variety of frozen treats including its famous Italian Ice,
                 made fresh daily, Frozen Custard, Milkshakes, Sundaes, CustardCookie Sandwiches,
                 layered Gelati, as well as signature Misto and Blendini creations.

                History
                 Established in 2016.

                 Rita's Italian Ice of Colorado Springs opened in August of 2016.""",
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
        about="""Specialties
                 The most delicious bagel in Colorado! Bella's Bagels - baked for boosting happiness.
                 Family-owned, Bella's Bagels is a genuine NY-style bagel shop born in Colorado Springs and
                 inspired by NJ roots. Our bagels are formed with natural ingredients, sourced from devoted providers,
                 crafted with careful nuance, baked for boosting happiness! And, our home made sandwiches are
                 the perfect comfort food for the upcoming holiday season. Consider a Bella's Bagel your warm dough hug.

                History
                 Established in 2023.

                 Jason and Michelle are two crazy technologists who have a deep love for bagels.
                 Jason is a serial entrepreneur, originally from NJ where bagel snobs are grown and
                 deployed into the world. Michelle runs cybersecurity programs that protect assets in space
                 (yes, Space.) Jason still remembers the smell of freshly baked bagels wafting
                 through the streets of his childhood home. Michelle is a home baking superstar whose been
                 whipping up amazing bagels for the family for years. Her food truly makes people happy.
                 During the pandemic, they decided to share their passion for bagels with the Springs and
                 started selling at local farmers markets. The response was overwhelming - selling out almost
                 every time and getting a fast following! Fast forward...they decided in the Summer of 2022 to
                 take a huge leap of faith and build their very own traditional, NY Style bagel shop.
                 These bagels are truly baked for boosting happiness. Come visit us and taste the love that
                 goes into each bagel we bake!""",
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
        about=""" Specialties
                   Classic San Francisco Pizzeria. Full Italian menu. Dine in, Take out & Delivery. Have your next family meal at Gaspare's Pizza.

                  History
                   Established in 1985.

                   First opened as a Pizzeria and Italian Dinner house in 1985.""",
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
        about="""Specialties
                  The two hope to bring reasonably-priced Italian meals--with an authentic Italian vibe--to the area.
                  And true to the family-friendly spirit of Italian eateries, the restaurant was created with both parents and their children in mind.

                History
                 Established in 2017.

                 Roma Antica was born in the heart of the Marina District. The product of a rich cultural heritage that passed along for generations,
                 the art of Roman Cuisine, revisited in a modern style. We aim through our cuisine to share our family tradition,
                 surrounding you with a simple meal in great company. The menu offers a selection of authentic recipes from Rome as well
                 as additional specialties from the magic of sitting around a table, sipping good wine and enjoy all the regions of Italy.
                 All of this, wrapped in a true Italian accent, will make you feel as if you were living a typical day in Rome,
                 where "the sun kisses you, the wind caresses you and the city protects you! The partners are Dogukan Solmaz and Roberto Sbaraglia,
                 a Roman whose father has owned a restaurant in Rome, Antica, for the past 30 years The two met at hospitality school
                 in Rome in 2005 and have been looking for a place in San Francisco for the past three years.""",
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
        about="""OUR STORY
                In 2015, Brandon approached Boris with an idea: a delicious, quality, wood-fired pizza shop with fresh ingredients was needed in
                the Richmond District of San Francisco. As an SF native who grew up a few blocks from Fiorella, Boris was excited by this concept.
                The Richmond District had not been a place for fine dining when he was a kid. This idea presented an opportunity to bring soulful,
                classic Italian cooking with a modern and fresh approach to Clement Street.
                After careful research, lots of work, and a whole lot of love, FIORELLA: Neighborhood Italian was born.""",
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
        about="""Specialties
                  Sunset Cantina was established in September 2019. Our mission is to offer the freshest classic Mexican street food faves.
                  We look forward to serving our friends, neighbors, and community. Bienvenidos ...

                History
                 Established in 2019.

                 Sunset Cantina was created by three like minded friends looking to serve authentic Mexico City street
                 food paired with delicious cocktails, Tequila, and Mezcal !""",
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
        about="""The husband and wife team that brought Son's Addition to the Mission corridor is excited to unveil Otra to the Lower Haight neighborhood.
        Focused on fresh masa, bold flavors, and traditional Mexcian cooking techniques, Otra brings you dishes reflective of Chef Nick's
        childhood experiences. He first gained interest in cooking from watching his mother Linda and Aunt Virginia,
        who always had a simmering pot on the stove to feed the entire family. Majoring in political science and philosophy at the University of Texas,
        Nick worked in kitchens to support himself, learning everything from dishwashing to prep cooking.
        After graduating from UT, he decided to follow his parents' advice and enroll in culinary school in San Francisco.
        Later he worked with the acclaimed chef Traci Des Jardins in San Francisco, and then moved to Luna Park San Francisco as Executive Chef.
        In 2009, he moved to Los Angeles to open two restaurants for Luna Park owner AJ Gilbert, and served as the Executive Chef at The Farm of
        Beverly Hills, where he created a fine dining experience with classic American cuisine.
        Chef Cobarruvias returned to San Francisco in 2016 as the Chef de Cuisine at Marlowe under acclaimed chef Jennifer Puccio.""",
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
        about="""Specialties
                  Our margaritas are made with 100% blue agave tequilas. We hope our homemade infusions make for a unique experience.
                  Our passion is all agave spirits. We have curated a list that will cure all your worries.
                  Traditional Michoacán carnitas, Pulpo al Pastor, and Tinga Flautas are just a few of the dishes you can expect from our menu.

                History
                 Established in 2021.

                 The story begins in a small village outside of San Felipe, Guanajuato, located in the heart of Mexico, called El Varal,
                 where I was raised by my grandparents, Mama Emilia and Papa Reyes.
                 I wanted to honor my childhood in El Varal with the perfect unity of Mama Emilia's healing through plants and prayer and
                 Papa Reyes' gift in captivating the true essence of the agave, something tequila, mezcal, or sotol will never do.
                 Here at Santería, we have started our quest in reverse, into the beginning of this incredible story of maguey by adding
                 an intentional element of healing and tradition into every dish and cocktail.""",
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
        about="""Specialties
                 Blink and you might miss it, but this little spot in the Inner Richmond is serving up some of the freshest, most flavorful
                 Mexican food in the city. Certain recipes on the menu were highly perfected over generations.
                 However, Chef Raul Garcia Antolin's flair for studying under his sought out masters means a host of influences.
                 Here you can enjoy sticky, smokey tamarind ribs; "cheesy crusted" burritos, and munch on warm tortilla chips as
                 the staff prepares your meal with love. Come on in and see for yourself why locals rave about the service,
                 the food, and the uncompromising quality - despite the laid back, casual location.""",
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
        about="""Specialties
                Mazra is a family-owned Mediterranean restaurant located in San Bruno, just minutes from San Francisco Airport.
                Rooted in tradition, we serve a wide variety of wood-fired meats, rotisserie chicken, wraps, seasonal mezzas and sides, and
                artisan desserts. Freshness, quality, and affordability are our favorite ingredients.
                We are constantly innovating to push culinary limits to bring bold and inspiring flavors into your life! Whether
                you're looking for traditional Mediterranean dishes or find yourself feeling adventurous, you'll feel right at home with us.""",
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
        about="""Specialties
                  Authentic Arabic comfort food with fresh ingredients sourced from local farms, made and served with love.

                History
                 Established in 2019.

                 Since opening in 2019, Beit Rima has been voted Best New Restaurant by San Franciscans via SF Weekly and Top 100 Restaurant from
                 the SF Chronicle and with rave reviews from food critics. In 2020, Beit Rima was recognized on a national level when
                 we were listed as a semi finalist for Best New Restaurant via the prestigious James Beard Awards.
                 Follow us on Instagram @beitrima to stay updated on seasonal specials! We look forward to having you!""",
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
        about="""Hummus With Beef & Lamb Shawarma
                 The shawarma is tender yet crispy, and well-seasoned throughout. Combined with the hummus, its a consistent hit and
                 our favorite item on the menu. Order this.

                Chicken Shawarma Wrap
                 The huge shawarma wraps are loaded with hummus and tahini and filled with everything from falafel to beef and lamb.
                 But we especially like it with the chicken shawarma. Make sure to add some of their housemade hot sauce to every bite.

                Stuffed Falafel
                 If falafel are still missing from whatever you order, get some on the side (preferably stuffed with mozzarella or caramelized onions,
                 sumac, and pine nuts). Theyre perfectly-fried and should be on your table.""",
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
        about="""History
                 Established in 2019.

                 Since opening in 2019, Beit Rima has been voted Best New Restaurant by San Franciscans via SF Weekly and Top 100 Restaurant
                 from the SF Chronicle along with rave reviews from food critics. In 2020, Beit Rima was recognized on a national level when
                 we were listed as a semi finalist for Best New Restaurant via the prestigious James Beard Awards.
                 Follow us on Instagram @beitrima to stay updated on seasonal specials! We look forward to having you!""",
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
        about="""Specialties
                 Reem's offers the warmth of Arab hospitality through the discovery of the flavors, aromas, and techniques of Arab street corner bakeries.
                 Our breads and dishes are inspired by classic street foods enjoyed daily throughout the Arab world, and made with California love.
                 Our feature product is the man'oushe, a fresh baked to order flatbread with organic local ingredients.

                History
                 Established in 2014.

                 Reem's was launched in 2014 through a series of pop-ups in Oakland and Berkeley and was incubated at La Cocina SF.
                 We opened our first brick & mortar - a bakery/cafe - in the Fruitvale Oakland neighborhood on Tuesday, May 16th, 2017!
                 We launched our second brick & mortar location in the Mission District of San Francisco on March 11, 2020!
                 In addition to our brick and mortars, we also currently provide wholesale and catering for functions and special events
                 throughout the Bay Area.""",
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
        about="""Specialties
                 We offer a traditional spread of middle eastern and Mediterranean delights ranging from kababs to vegetarian dishes.
                 We are also known for our famous desert Kunafa made in-house on a gigantic cast iron griddle straight from the Holy Land.

                History
                 Established in 2005.

                 Old Jerusalem is a small family-owned business that has been operating for 16 years in the heart of Mission.
                 The original owner Ahmad Nasser from the West Bank, opened the restaurant in 2005.
                 He wanted to bring a piece of the Holy Land to our beloved San Francisco.
                 Over the years, he has successfully created a neighborhood restaurant.
                 He later brings on one of his dearest friends Hajem Almukdad from Syria, as a business partner.
                 Together, they have brought an iconic restaurant to the Mission full of culture and family traditions.""",
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
        about="""Specialties
                 Only the tastiest and freshest Japanese food is served here.""",
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
        about="""Specialties
                 Kappo kaiseki style restaurant""",
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
        about="""Specialties
                 Have you tried the real Sushi with a Brazilian flavor?

                History
                 Established in 2020.

                 Born out of a passion for flavor and tradition, Japa Team Sushi is a journey of success that blossomed
                 in the corners of a modest apartment in California's Bay Area. In the magical year of 2020, under the welcoming roof
                 of a space measuring just six square meters, we, a family united by cooking and love, started our dream.
                 Fate traced a new chapter, and our small house could no longer contain the grandeur of our dreams.
                 From tears of gratitude to smiles of achievement, we lifted our anchors and ventured into an industrial kitchen.
                 But the universe smiled once more, opening doors that seemed to exist only in our dreams. Today, we are here, in a space that
                 transcends our initial imagination: the Japa Team Sushi restaurant, where cultures merge in every bite.
                 Here, the chairs embrace the guests, and the sushi comes to life in a rotation of emotions. Come live this moment with us!""",
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
        about="""Bento Peak, Japanese Cuisine offers high quality, great value and fast sushi or Japanese restaurant dining experiences.
        Our restaurant serves innovative arrays that include dishes form Western cuisines, which the combination of fresh ingredients and the
        scorching technique draw out the umani of the meat.""",
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
        about="""Specialties
                 First of all, Nara offers Happy hours between 5-7pm, During Happy hours, fresh miyagi oysters $2.50EA ,
                 spicy tuna, spicy salmon handroll $5 EA, $11 Mr. Taco ball! $2 off draft beer (Sappro, Asahi),
                 and $2 off Hot Sake, Happy hours is great time for sake bomb.""",
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
        about="""History
                 Established in 2019.

                 Grand opening will be 9/4/2019""",
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
        about="""Specialties
                  Hard Rock Cafe on Pier #39 is here to make your trip rock! The Cafe is located next to the Bay's waterfront, is full of rock-n-roll
                  memorabilia and features a savory menu as the cherry on top. We are conveniently located at the entrance to Pier 39, directly across
                  from the F-Line trolley, Uber/Lyft/Taxi zone, bus loading zone and Pier 39 parking garage. Let us welcome you to Pier 39 by stopping
                  for a quick bite before or after your adventures. Hard Rock is so much more than just a cafe! You can explore our Rock Shop® for some
                  great gifts and souvenirs or check out all of our rock-n-roll memorabilia. You are sure to leave with an unforgettable memory. Rock on
                  Hard Rock family, we'll see you soon!

                History
                 Established in 1984.

                 Two Shaggy-haired guys just wanted to find a good American Burger while living in London, in 1971 they opened their own American Style
                 diner in an old Rolls Royce Dealership. They called it Hard Rock Cafe founded by Isaac Tigrett and Peter Morton. The Seminole Tribe of
                 Florida purchased Hard Rock in 2007 which now has venues in more than 76 countries around the world.""",
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
        about="""Specialties
                Your choice of family-style restaurant in South San Francisco, Our unique family-style dining, also known as casual style dining, offers
                very affordable entrées from menus featuring a mix of classic cuisines, with our touch of signature sauces, dips, or other toppings
                cuisine. Through the years, we developed our own unique definition of the expression "family style cuisine". We excel in serving our
                clients with the taste of homemade sauce and dishes that will bring you memories of that good place.. Kitchen Open Till 9 PM

                History
                 Established in 1954.

                 The Garden Club Story The Garden Club was originally opened in 1964 by Michael Casentini, an avid duck hunter, as a duck hunting bar.
                 Years later, Michael met Alicia, they fell in love, got married, and together opened an adjoining restaurant. Michael and Alicia ran
                 The Garden Club for over 50 years, maintained a wonderful reputation of great quality Italian-American cuisine, old school charm, stiff
                 drink pours, and of course....a whole lot of ducks. The Garden Club Family is committed to keeping this restaurant a welcoming,
                 family-friendly establishment. Our goal is to have you leave with happy faces, full bellies and always wanting to come back for more.
                 We appreciate all feedback so we can always ensure an enjoyable atmosphere with every visit. Thank you for your patronage and support.
                 With Love, The Garden Club""",
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
        about="""Specialties
                  Unique cocktails, local beer, small-producer wines, and modern Californian comfort food -- all served up in a warm and
                  comfortable environment.

                History
                 Established in 2017.

                 Four friends look to share their passion for great food, strong drinks, and the best beer and wine California has to offer.""",
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
        about="""Specialties
                 We have an unique space in front of the fireplace for private parties that seats up to 16. It is perfect for special occasions,
                 birthdays, work gatherings, etc. We can also accommodate 16+ people in the dining room and/or bar seating. Call for more information!
                 Our 18 seat bar has 3 TVs and will be playing sporting events on any given day. Come stop by for a drink and a bite to eat at our bar!

                History
                 Established in 2017.

                 Heritage Restaurant and Bar took over the space of Clement Street Bar and Grill. The space has been completely renovated, while still
                 keeping the same charm of the room. The brick fireplace in the main dining room creates a comfortable atmosphere for dinner. There is
                 a separate space for private parties, and a inviting bar area with lots of seating as you walk in.""",
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
        about="""Specialties
                 Breakfast, Brunch, Bloody Marys, Millionaire's Bacon

                History
                 Established in 2012.

                 Kitchen Story is a Family restaurant with homestyle cooking located on the corner of 16th & Sanchez in the mission.
                 We are a California Cuisine restaurant with influences of Asian Fusion.""",
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
        about="""Specialties
                 Open during SF Shelter in place for Outdoor Seating Dine-In, Take-outs, Curb-Side, and Deliveries including Beer, Wine & Cocktails.
                 A family friendly full service restaurant with a wide variety of food options combining traditional and modern American Diner offering
                 all day breakfast, salads, classic sandwiches, burgers, appetizers, and entrees. In addition we serve organic Peruvian coffee,
                 full Espresso bar, Numi Organic Teas, Pomegranate Quince iced tea, old fashion milkshakes, and a fresh squeezed juice bar. Your food
                 will be served by very highly experienced servers who served in the Russian Hill neighborhood for many years. We support local farmers
                 and producers. Simply visit us to get best quality tasty foods with superior service. Owned by the community to serve the community.

                History
                 Established in 2017.

                 End of march 2017, it was announced that Polkers Gourmet was sold and new owners will make that location a Greek Restaurant.
                 That was sad time to the neighbors to loose a 23 years old favorite destination, and emotional to the family of coworkers
                 who worked together for many years. The hunt for a new place started by my Finace Nazeira who was a server at Polkers and myself Sam.
                 Things went so smooth when we found a location on the corner of Polk and Union, and within days the deal was closed, and the renovation
                 started. May 27 memorial weekend we opened doors providing some similar items as Polkers while adding many new modern and some
                 traditional American Diner choices using local organic and natural ingredients. We also added organic coffee, organic teas,
                 Espresso bar, and fresh Juice bar. Of course what motivated us the most to get the restaurant opened so quickly was the family of
                 coworkers of Polkers whom most of them joined our team. And the adventure started.""",
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
       db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
       db.session.execute(text("DELETE FROM users"))

    db.session.commit()
