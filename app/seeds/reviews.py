from app.models import db, Review, environment, SCHEMA
from sqlalchemy.sql import text


def seed_reviews():
    reviews = [
        Review(
            user_id = 1,
            business_id = 1,
            review_body = "Great food, excellent service, coming from San Francisco I wanted to try a local Italian joint and everything was great and I couldn't fault a thing. The restaurant was busy and had great family and young people vibes. The servers were all super friendly from my phone call to the staff.",
            rating = 5
        )
          Review(
            user_id = 2,
            business_id = 1,
            review_body = "The Food is good and the atmosphere is solid. Authentic italian food. The service is solid and waiters are on top of it.",
            rating = 4
        )
          Review(
            user_id = 3,
            business_id = 1,
            review_body = "Food and ambiance were wonderful. In particular, the burrata, shrimp with voka, and apple bread pudding were all great.",
            rating = 4
        )
          Review(
            user_id = 4,
            business_id = 2,
            review_body = "I have food allergies, and they didn't pay attention to the food they gave me and I got sick",
            rating = 1
        )
          Review(
            user_id = 5
            business_id = 2
            review_body = "Wow, what a gem!  Delicious sandwiches and very nice services. Prices are reasonable, too.",
            rating = 5
        )
          Review(
            user_id = 6,
            business_id = 2,
            review_body = "One of my favorite Italian restaurants in the city. The chicken parm is killer",
            rating = 5
        )
          Review(
            user_id = 7,
            business_id = 3
            review_body = "Real authentic Italian food ! Owners are Italians and speak the language which they know the real recipes.",
            rating = 5
        )
          Review(
            user_id = 8,
            business_id = 3,
            review_body = "Fresh and flavorful pastas in the area. Hidden Gem in the area. Ambiance is perfect. ",
            rating = 4
        )
          Review(
            user_id = 9,
            business_id = 3,
            review_body = "Went on Mothers Day. The service was very good even though it was very busy. The food was spectacular!",
            rating = 5
        )
          Review(
            user_id = 10,
            business_id = 4,
            review_body = "excellent food !! we got take out and it was delicious. they have amazing eggplant parmigiana and caprese",
            rating = 5
        )
          Review(
            user_id = 11,
            business_id = 4,
            review_body = "Very good Italian food. Large portions, fair prices, waitstaff is attentive and it's not too loud.",
            rating = 4
        )
          Review(
            user_id = 12,
            business_id = 4,
            review_body = "Wonderful food, service and ambiance Frute De Mare, Lobster Ravioli.",
            rating = 5
        )
          Review(
            user_id = 13,
            business_id = 4,
            review_body = "One of my favorite Italian food spots.",
            rating = 4
        )
          Review(
            user_id = 14,
            business_id = 5,
            review_body = "The food was outstanding and so delicious if your hungry and want something super delicious you should definitely go and try paradise pizza!",
            rating = 5
        )
          Review(
            user_id = 15,
            business_id = 5,
            review_body = "One of my favorite Italian food spots.",
            rating = 5
        )
          Review(
            user_id = 16,
            business_id = 5,
            review_body = "I have food allergies, and they didn't pay attention to the food they gave me and I got sick",
            rating = 1
        )
          Review(
            user_id = 17,
            business_id = 6,
            review_body = "Regular stop when we want a treat. Staff always awesome. Sometimes a wait but what do you expect. It's a destination!",
            rating = 5
        )
          Review(
            user_id = 18,
            business_id = 6,
            review_body = "Good stuff, though at times spotty.  Had great meals there and others were just meh.!",
            rating = 3
        )
          Review(
            user_id = 19,
            business_id = 6,
            review_body = "Wonderful pizzas",
            rating = 5
        )
          Review(
            user_id = 1,
            business_id = 7,
            review_body = "Delish! Food and drinks were fantastic guacamole was ok but everything else was way beyond!",
            rating = 4
        )
          Review(
            user_id = 2,
            business_id = 7,
            review_body = "Second time we had take out recently. Both times were excellent. We are fans of the pork.",
            rating = 5
        )
          Review(
            user_id = 3,
            business_id = 7,
            review_body = "Wonderful place",
            rating = 5
        )
          Review(
            user_id = 4,
            business_id = 8,
            review_body = "The only thing better than their large burritos is the taste",
            rating = 5
        )
          Review(
            user_id = 5,
            business_id = 8,
            review_body = "Love love love this place! Authentic Mx food to the core",
            rating = 4
        )
          Review(
            user_id = 6,
            business_id = 8,
            review_body = "Very good place. Got sopes appetizer and tacos. Wife got chili rejeno.",
            rating = 4
        )
          Review(
            user_id = 7,
            business_id = 9,
            review_body = "OMG! Finally great Mexican food! I can't even tell you what NOT to order because 5 of us had a variety, and all of it was sooo good!",
            rating = 5
        )
          Review(
            user_id = 8,
            business_id = 9,
            review_body = "Everything was fresh and delicious, will be back again and again!!",
            rating = 4
        )
          Review(
            user_id = 9,
            business_id = 9,
            review_body = "Wow, what a place. Will be coming back",
            rating = 5
        )
          Review(
            user_id = 10,
            business_id = 10,
            review_body = "Really excellent food - very enjoyable! Also, lots of corn tortilla dishes, so no worries if you are gluten sensitive.",
            rating = 4
        )
          Review(
            user_id = 11,
            business_id = 10,
            review_body = "It was okay. I definetely have had better",
            rating = 3
        )
          Review(
            user_id = 12,
            business_id = 10,
            review_body = "Great place!  Food was delicious also, my son is in a wheelchair, and, even though it was pretty crowded, they made it work. ",
            rating = 5
        )
          Review(
            user_id = 13,
            business_id = 11,
            review_body = "Best Mexican restaurant in New England! Everything is absolutely delicious and the service is fantastic.",
            rating = 4
        )
          Review(
            user_id = 14,
            business_id = 11,
            review_body = "Amazing Rice & equal or better than anything I have eaten in the Southwest or Mexico!! Had the Enchiladas Verde & they were MAGNIFICENT!!",
            rating = 5
        )
          Review(
            user_id = 15,
            business_id = 11,
            review_body = "Good food, service wasnt very good",
            rating = 3
        )
          Review(
            user_id = 16,
            business_id = 12,
            review_body = "Yummy food and amazing drinks , ambiance is quite nice too .definitely recommend this",
            rating = 4
        )
          Review(
            user_id = 17,
            business_id = 12,
            review_body = "Not a huge fan unfortunately.",
            rating = 3
        )
          Review(
            user_id = 18,
            business_id = 12,
            review_body = "Cool looking place on the inside. The margaritas aren't amazing but not bad. My bad experience was drinking soap in my margarita. It honestly taste like bleach. Maybe the cup wasn't rinsed or something. Also salsa tastes weird",
            rating = 3
        )
          Review(
            user_id = 1,
            business_id = 13,
            review_body = "Devoured my food before remembering to take a picture."
            rating = 5
        )
          Review(
            user_id = 2,
            business_id = 13,
            review_body = "Fantastic food! Everything was delicious. 5+ STARS!!! Had a veggie plate which came with an abundance of salad, hummus, rice, stuffed grape leave, eggplant and more. Healthy portion of tasty delicious food. I left a very happy customer.",
            rating = 5
        )
          Review(
            user_id = 3,
            business_id = 13,
            review_body = "Excellent fresh food & great customer service .  Easy & fast takeout . Definitely one of my favorite spots for lunch",
            rating = 4
        )
          Review(
            user_id = 4,
            business_id = 14,
            review_body = "Best Lebanese food I have ever had. Charlie the owner, is one of the nicest people I have ever met. Great food, great atmosphere.",
            rating = 5
        )
          Review(
            user_id = 5,
            business_id = 14,
            review_body = "Got the Beef Shawarma wrap and I would get it again. Not too messy for eating on the go. Online ordering was very easy and the order was ready sooner than the estimated pickup time. Friendly staff.",
            rating = 4
        )
          Review(
            user_id = 6,
            business_id = 14,
            review_body = "The owners are amazing, super gracious and lovely. The hummus was good, garlic sauce is still amazing, as is the tahini. The shawarma sandwich was great.",
            rating = 4
        )
          Review(
            user_id = 7,
            business_id = 15,
            review_body = "Clean good price for what you get deff will go again cashier was super friendly and engaging",
            rating = 4
        )
          Review(
            user_id = 8,
            business_id = 15,
            review_body = "Delicious chicken and beef shawarma and very nice people.. great baba ghanoush too!!!",
            rating = 4
        )
          Review(
            user_id = 9,
            business_id = 16,
            review_body = "Fresh food, great service, and a super friendly owner who is proud of his the business he's built, a winning combination. Spacious seating, lots of choices. This is the spot for us next time we're back in town.",
            rating = 3
        )
          Review(
            user_id = 10,
            business_id = 17,
            review_body = "High priced and skimpy food. Owner yells at employees in front of customers, very unprofessional. Much better food and nicer owners at other places.",
            rating = 4
        )
          Review(
            user_id = 11,
            business_id = 17,
            review_body = "dirty place   Food isn't palatable.  Go to McDonald's. You'll be better off than going here",
            rating = 1
        )
          Review(
            user_id = 12,
            business_id = 17,
            review_body = "Amazing food and staff! I highly recommend their plates  are super filling and delicious!",
            rating = 5
        )
          Review(
            user_id = 13,
            business_id = 18,
            review_body = "So so tasty and the people who work here are very nice and fast paced. I order here almost every other day for lunch",
            rating = 5
        )
          Review(
            user_id = 14,
            business_id = 18,
            review_body = "Best shwarma around.  I would give it 5 stars but the ordering can be a bit hap hazard.  Sometimes its part of its charm sometimes its annoying.  Either way the shwarma and baklava are always worth it.  If you love garlic get the combo shwarma.",
            rating = 4
        )
          Review(
            user_id = 15,
            business_id = 18,
            review_body = "The beef shawarma sandwich is great. Chicken not so much. The service is great. They let me in after hours to get my pickup order.",
            rating = 4
        )
          Review(
            user_id = 16,
            business_id = 19,
            review_body = "AWESOME FOOD!  AWESOME PEOPLE!  I have been going here since they were on Pleasant St",
            rating = 5
        )
          Review(
            user_id = 17,
            business_id = 19,
            review_body = "This place is amazing. My first sharma spot I've tried. Didn't know what to expect. Now I've been coming here once a week for the sharma wrap. Damn that thing is good.",
            rating = 4
        )
          Review(
            user_id = 18,
            business_id = 19,
            review_body = "Always great food and friendly service. The new location is expanded allowing for a nice dining in experience.",
            rating = 4
        )
          Review(
            user_id = 1,
            business_id = 20,
            review_body = "Amazing sushi, amazing service good pricing",
            rating = 4
        )
          Review(
            user_id = 2,
            business_id = 20,
            review_body = "I just love this place. The sushi is incredible and the restaurant has this authentic feel.",
            rating = 5
        )
          Review(
            user_id = 3,
            business_id = 20,
            review_body = "Best sushi in Worcester for sure. A little pricey but very good quality. The place is very small so gotta like it cozy. Service is good... not real fast.",
            rating = 5
        )
          Review(
            user_id = 4,
            business_id = 21,
            review_body = "The sushi chef obviously felt most comfortable making his creations by "hand". He would sometimes handle the raw fish with a plastic glove, but most of the time he was using his bare hands. The part where I almost walked out was when he sneezed. He had turned from the food and went towards the back wall to sneeze openly, then sneezed again into his hands. He started walking back, looked at me and then went over to the sink to wash his hands. He then put on the plastic glove to his right hand while his left hand was used for positioning the food on the plate (no glove).",
            rating = 3
        )
          Review(
            user_id = 5,
            business_id = 21,
            review_body = "Chef Nori's sushi is the best around here. It is authentic Japanese food! I highly recommend it!",
            rating = 5
        )
          Review(
            user_id = 6,
            business_id = 21,
            review_body = "One of our favorite sushi places in Worcester! BYOB. VERY small dining area, call ahead for reservations (pre-Covid). Great take out spot. Quality sushi. The owner is the best!",
            rating = 4
        )
          Review(
            user_id = 7,
            business_id = 22,
            review_body = "The sashimi tastes so fresh! Sushi dinner was great too! Also love their miso soup! Sometimes food can come super slow. So before you come to taste the amazing seafood, maybe consider eating something first  last time I went, it was not slow at all.",
            rating = 4
        )
          Review(
            user_id = 8,
            business_id = 22,
            review_body = " it was just okay, nothing special",
            rating = 3
        )
          Review(
            user_id = 9,
            business_id = 22,
            review_body = "Unfortunately, nowadays with the amount of patrons that file in for dinner, they can't keep up and the food suffers. Service is always friendly, but the food isn't the same. It seems to be slapped together with whatever leftover pieces of fish they have. On busy nights expect to have to wait, and to spend 1-2 hours there for a dinner.",
            rating = 3
        )
          Review(
            user_id = 10,
            business_id = 23,
            review_body = "Definitely worth a 5 star. It is one of the top Japanese restaurants in Massachusetts. All the sushi are very authentic, especially the Dragon roll and Volcano roll (Highly recommended). OMAKASE is another dish recommended. The mixture of different food source is great and shining the wisdom of the Japanese cooking culture. Sushi Miyazawa will provide different delicious deserts, once I tried one green tea ice cream which is also great.",
            rating = 5
        )
          Review(
            user_id = 11,
            business_id = 24,
            review_body = "The food is great but the atmosphere is lacking. Baby octopus and lobster rolls were fantastic.",
            rating = 4
        )
          Review(
            user_id = 12,
            business_id = 24,
            review_body = "The best best best sushi in the area. Super small space but well worth the wait. Once they reopen! We ordered pick up yesterday and it did NOT disappoint. Super nice staff and chefs are amazing. I honestly haven't had one thing I didn't love.",
            rating = 5
        )
          Review(
            user_id = 13,
            business_id = 24,
            review_body = "my boyfriend and I are new to the area and were looking for a fun place to go on a date night. loving sushi, and with the positive reviews, we felt good about Miyazawa being our first sushi place in the area. We don't regret a thing, and it will honestly be difficult for another restaurant to top our experience here! incredibly fresh sushi and such wonderful staff.  coming back and taking our friends!!",
            rating = 4
        )
          Review(
            user_id =  14,
            business_id = 25,
            review_body = "This was the freshest sushi I've had in Worcester. It felt like I was in Boston or LA. I love the intimate atmosphere and of course the fact that it's BYOB. Amazing addition to the city!",
            rating = 5
        )
          Review(
            user_id = 15,
            business_id = 25,
            review_body = "Great experience, delicious and fresh food. We ordered three rolls. Must order (for people who like sauce) volcano roll & eel roll. Raw, the spicy tuna/salmon is good. The besssssst one is Chazuke!! Amazing taste. My first time.",
            rating = 4
        )
          Review(
            user_id = 16,
            business_id = 25,
            review_body = "Freshest seafood made masterfully by authentic sushi chef. Will be ordering from here more often. The prices quality and price for sushi is great!",
            rating = 3
        )
          Review(
            user_id = 17,
            business_id = 26,
            review_body = "Made my second trip tonight, and the food and service were both excellent. The sushi is incredible, especially for the price, and the staff was very helpful and friendly. I officially love this place, especially since it's around the corner!",
            rating = 4
        )
          Review(
            user_id = 18,
            business_id = 26,
            review_body = "i had an omakase. Too much sugar in the all dishes (Takako sushi, chawan mushi, Anago-source.....). Miso soup with shrimp heads, tasted like cheap ramen noodle soup. Not happy with the Omakase course....",
            rating = 1
        )
          Review(
            user_id = 19,
            business_id = 26,
            review_body = "This is the best sushi in Worcester, end of story. They say they aren't a kid place but we came here the first time because my kid is a sushi fanatic and we wanted him to have an authentic experience. We keep going back at least a couple of times a year. This is a BYOB, small and does not take reservations. That being said we have never had to wait long for a table. We usually order off the specials menu and have never been disappointed. Service is prompt and friendly",
            rating = 5
        )
          Review(
            user_id = 1,
            business_id = 27,
            review_body = "This restaurant is on point. We had fried pickles for an appetizer. The tugboat sandwich is also fantastic. The seared Boynton Tuna sashimi, which is pictured here was fantastic. Highly recommend it and this restaurant.",
            rating = 5
        )
          Review(
            user_id = 2,
            business_id = 28,
            review_body = "Always dependable. Service was wonderful (thank you, Meg!).  Steak fries are wonderful-- crispy, real potatoes. Burgers cooked perfectly. Margarita pizza, tasty but soggy.",
            rating = 4
        )
          Review(
            user_id = 3,
            business_id = 28,
            review_body = "Please note that I've only had takeout orders from here, but both times the food has not been great. First time ordering I got the Cesar salad pizza. When I brought home my food and opened the box, it was a plain pizza crust with all of the toppings having fallen off and into the box. There wasn't any sauce or dressing I could use to "rebuild" it, so I eventually just ate a salad and bread. My second time I ordered a burger, because, if a restaurant can mess up a burger, what can they make? It was so bad. No flavor, the meat wasn't seasoned. I could only take two bites. Fries were the highlight of the meal, that's saying something.",
            rating = 2
        )
          Review(
            user_id = 4,
            business_id = 28,
            review_body = "Great prompt friendly service with Dee. Had a nice big comfy-cushiony booth. Food was 'perfectous' delight. See the photos to get some insight. This place may be our new 'to-go",
            rating = 4
        )
          Review(
            user_id = 5,
            business_id = 29,
            review_body = "They are now adding a 4 charge to use a credit card. This is illegal by the way. And NOT a good way to treat customers. Food wasn't great to begin with. This seals their fate for me. I won't be back.",
            rating = 1
        )
          Review(
            user_id = 6,
            business_id = 29,
            review_body = " Can and should be better for the price",
            rating = 3
        )
           Review(
            user_id = 7,
            business_id = 29,
            review_body = "Great service and ambiance Blooming OnionBuffalo WingsLobster Roll Lobster Rangoons Gluten Free Pizza and Meatballs",
            rating = 4
        )
           Review(
            user_id = 8,
            business_id = 30,
            review_body = "I've heard a lot about the place so I was excited to try it but honestly we were a little let down. I got pasta and my boyfriend got steak tips. My pasta was relatively good but the sauce was very soupy. One of my boyfriend's steak tips was completely raw. More positively, I will say the bacon wrapped scallops were pretty good and our server was great :)",
            rating = 3
        )
           Review(
            user_id = 9,
            business_id = 30,
            review_body = "Iconic spot in Worcester. Expect a bar / grille atmosphere, bar / grille menu options and bar / grille experience! You will get decent service, pay average prices, and get in some good people watching. There is outdoor seating in the summer, and luckily a parking lot in the back. It's not going to be the best meal you've ever had, but you will likely have an enjoyable time with your people in the relaxed atmosphere.",
            rating = 3
        )
           Review(
            user_id = 10,
            business_id = 31,
            review_body = "Food is great service is a little slow ambiance very loud hard to talk to someone across the table all and all good place",
            rating = 4
        )
           Review(
            user_id = 11,
            business_id = 31,
            review_body = "Always good food and great service. I had the Mediterranean bowl and my mother and kids had pepperoni pizza. All excellent! Anytime we're in the Worcester area this is where we stop!",
            rating = 5
        )
           Review(
            user_id = 12,
            business_id = 31,
            review_body = "The pesto, peach and hot honey burrata pizza was amazing! Other things seemed just fine, but this pizza was fantastic.",
            rating = 4
        )
           Review(
            user_id = 13,
            business_id = 32,
            review_body = "We have been going to the Boynton for more years than I'd like to admit! We just arrived from Washington DC and we are heading to the Boynton for lunch! I don't think I need to say more, but let me just say the food, drinks and service are all great!!",
            rating = 5
        )
           Review(
            user_id = 14,
            business_id = 32,
            review_body = "Covid ruined this one for me. I don't know what exactly changed during or after, but something feels different about this spot. The prices did skyrocket so maybe it is just the value changed?!",
            rating = 3
        )
           Review(
            user_id = 15,
            business_id = 32,
            review_body = "We just went a few weeks wand it was pretty good! I started with raw oysters which were fresh and delicious. We got the Poutine for the table. It was ok. Everyone enjoyed their meals, except my husband. He ordered the Caesar Salad Flat Bread which wasn't flat at all. It was a bulky pizza with a ton of romaine and little else. Oh well, he won't order that again. Drinks were good. Waitress was excellent. ( Sorry dark haired girl, very pretty). We'll come back.",
            rating = 4
        )
           Review(
            user_id = 16,
            business_id = 32,
            review_body = "We had our first visit here for lunch today, party of five. The service was good and the food was fine, however the smell of cleaning chemicals was strong. It was so strong it was difficult to enjoy the food and I ended up with a headache for the afternoon. Maybe it's because we arrived right when they opened, but they should tone down the smell, and/or air the place out for a few hours before serving, that was bad.",
            rating = 4
        )
    ]

    db.session.add_all(reviews)
    db.session.commit()

def undo_reviews():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reviews"))

    db.session.commit()
