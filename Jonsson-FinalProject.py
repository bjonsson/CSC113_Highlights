# Brenda Jonsson 11/19/2022
# Final Project

# "Boredom Beater for the Artsy-Craftsy"
#
# I would like to make a program that gives the user a quiz to see what type of craft they might like to do next.
# Then, it returns the most popular current Etsy item or items in that category.
#
# One of the features I could add is the option to skip the quiz and just select a craft from a list of options.
#
# The quiz will be a series of nested “if” statements, much like the car assignment was.
# This decision tree will lead to the most befitting type of craft.
# There will also be an explanation of why the results fit the person’s answers, and a brief guide to how to do the
# craft–either as a very general summary done by me, or as recommended links to websites and videos that will guide
# the user. I will pick the crafts first, and then I will work backwards to create the questions.
# There will be 10-20 different crafts to score.
#
# I could make classes out of various categories of each craft. In each craft, there will be repeatable characteristics
# among the others. I can use classes to print repetitive information for crafts that have similarities. I anticipate
# having to use a dictionary to store unique information.
#
# The program keeps a list of how many times a person who takes the quiz scores a certain craft–for research purposes.
# This will be written to a file. A “1” will be added in the column for the craft. I will create a function to return the
# percentage of test takers who score a particular craft. I will also list how many people have taken the test so far.
#
# I will connect to Etsy’s API in order to find out what the most popular kits are for that craft and then point to
# that URL. I have never connected to Etsy’s API before, so I’m just crossing my fingers and hoping that it will work
# and I can figure it out.
#
# The only way I can think of to truly test the beginning of this program is to go through and score every craft at
# least once. Probably I can double check the API’s accuracy by doing a manual search on Etsy’s site and seeing what
# items come up first under the same search terms I will use for the API.
#
# At the moment, I’m not anticipating having to use any libraries, but I am not sure if the API will require them.
# (We haven’t gotten to that chapter yet and won’t until after this paper is due.)

# Connecting to API
# Imports
import requests
import json

# The URL is customized to get just 1 of the active listings with the "amigurumi" tag as an example.
#req = requests.get("https://openapi.etsy.com/v2/listings/active?tags=amigurumi&limit=1&api_key=dkuzdt3r4l4jycbgdojnczgy")

# This lets you see whether or not the API has connected. 200 is good, the 400s are a no go.
#print(req.status_code)

# This lets you see the results in a way that makes it easy to call the nested list/dictionary
#print(json.dumps(parsed, indent =4))

# This is what the meat and potatoes of the code looks like.
#parsed = json.loads(req.text)
#results = parsed['results']
#print(results[0]['title'])
#print(results[0]['url'])


# Writing to a file with a function
def write(craft):

    filename = 'EtsyQuizResults.txt'

    with open(filename, 'a') as file_object:
        file_object.write(str(craft)+"\n")

# Greeting
print("Welcome to the Boredom Beater for the Artsy-Craftsy! Take a quiz, and we'll let you know what craft you might "
      "want to start next. We are not affiliated with Etsy, but will recommend the most popular kit in each category "
      "in real time on the popular arts and crafts website.")

# Reading statistics about test takers

def stats(craft):

    filename = 'EtsyQuizResults.txt'

    with open(filename, 'r') as file_object:
        count = 0
        num_tests = 0
        for line in file_object:
            num_tests += 1
            if (line.rstrip() == craft):
                count = count + 1

    num_tests = len(filename)
    percentage = (count/num_tests) * 100

    print(f"This craft has been scored {percentage}% of the time.")

# Dictionaries
# Includes the description, class, title, and URL of each craft kit.
# First a custom URL is created, then parsed, then put into the dictionary.

req = requests.get("https://openapi.etsy.com/v2/listings/active?tags=air+dry+clay&limit=1&api_key=dkuzdt3r4l4jycbgdojnczgy")
parsed = json.loads(req.text)
results = parsed['results']

air_dry_clay = {'description': 'Air dry clay! Air dry clay hardens at room temperature without any additional '
                               'treatment. '
                               'It can be used to make jewelry, pots, or embellishments for cards, and it can be '
                               'painted with acrylics or varnished. The clay itself can be made out of a variety of '
                               'synthetic and natural materials.',
                'time spent': 'days', 'class': [], 'title': results[0]['title'], 'url': results[0]['url']}

req = requests.get("https://openapi.etsy.com/v2/listings/active?tags=amigurumi+kit&limit=1&api_key=dkuzdt3r4l4jycbgdojnczgy")
parsed = json.loads(req.text)
results = parsed['results']

amigurumi = {'description': 'Amigurumi! Amigurumi are a type of round, miniature, kawaii dolls made with crochet. '
                            'With a pattern to guide you, a little bit of yarn, and perhaps some beads for the eyes, '
                            'you can make characters ranging from triceratops to Lieutenant Commander Data from Star '
                            'Trek.',
             'time spent': 'days', 'class': ["portable"], 'title': results[0]['title'], 'url': results[0]['url']}

req = requests.get("https://openapi.etsy.com/v2/listings/active?tags=basket+weaving+kit&limit=1&api_key=dkuzdt3r4l4jycbgdojnczgy")
parsed = json.loads(req.text)
results = parsed['results']

basket_weaving = {'description': 'Basket weaving! Humanity has a long, rich history of weaving baskets. Although'
                                 'we can appreciate them as artistic artifacts, they also have pragmatic uses'
                                 'as containers. They are traditionally made with natural materials, like pine'
                                 'needles and waxed thread.',
                  'time spent': 'weeks', 'class': [], 'title': results[0]['title'], 'url': results[0]['url']}

req = requests.get("https://openapi.etsy.com/v2/listings/active?tags=book+binding+kit&limit=1&api_key=dkuzdt3r4l4jycbgdojnczgy")
parsed = json.loads(req.text)
results = parsed['results']

book_binding = {'description': 'Book binding! Sew the pages of a journal together into a very personal book that is also a '
                               'work of art.',
                'time spent': 'days', 'class': [], 'title': results[0]['title'], 'url': results[0]['url']}

req = requests.get("https://openapi.etsy.com/v2/listings/active?tags=bracelet+kit&limit=1&api_key=dkuzdt3r4l4jycbgdojnczgy")
parsed = json.loads(req.text)
results = parsed['results']

bracelet = {'description': 'Bracelet making! DIY bracelets make for unforgettable handmade presents. They can use elastic'
                           'string, leather, hemp or other materials to string the beads.',
            'time spent': 'days', 'class': ["portable"], 'title': results[0]['title'], 'url': results[0]['url']}

req = requests.get("https://openapi.etsy.com/v2/listings/active?tags=candle+making+kit&limit=1&api_key=dkuzdt3r4l4jycbgdojnczgy")
parsed = json.loads(req.text)
results = parsed['results']

candle_making = {'description': 'Candle making! Candles smell amazing, and they glow. It is surprising how simple '
                                'it is to make your own candles, and they make wonderful gifts, home decor and air '
                                'fresheners.',
                 'time spent': 'days', 'class': ["kitchen"], 'title': results[0]['title'], 'url': results[0]['url']}

req = requests.get("https://openapi.etsy.com/v2/listings/active?tags=wood+carving+kit&limit=1&api_key=dkuzdt3r4l4jycbgdojnczgy")
parsed = json.loads(req.text)
results = parsed['results']

carving = {'description': 'Wood carving! Wood carving, or whittling might be something you can picture yourself doing '
                          'while sitting on your porch, carving away bit by bit of wood with a knife to reveal an '
                          'interesting figure.',
           'time spent': 'days', 'class': ["portable"], 'title': results[0]['title'], 'url': results[0]['url']}

req = requests.get("https://openapi.etsy.com/v2/listings/active?tags=chocolate+kit&limit=1&api_key=dkuzdt3r4l4jycbgdojnczgy")
parsed = json.loads(req.text)
results = parsed['results']

chocolate = {'description': 'Chocolate making! Make your own chocolate! These kits usually require access to a kitchen in order to'
                            'heat the ingredients.',
             'time spent': 'days', 'class': ["kitchen"], 'title': results[0]['title'], 'url': results[0]['url']}

req = requests.get("https://openapi.etsy.com/v2/listings/active?tags=dream+catcher+kit&limit=1&api_key=dkuzdt3r4l4jycbgdojnczgy")
parsed = json.loads(req.text)
results = parsed['results']

dream_catcher = {'description': 'Dream catcher! Dream catchers originate from Native American cultures and are said to protect '
                                'one from nightmares.',
                 'time spent': 'days', 'class': [], 'title': results[0]['title'], 'url': results[0]['url']}

req = requests.get("https://openapi.etsy.com/v2/listings/active?tags=embroidery+kit&limit=1&api_key=dkuzdt3r4l4jycbgdojnczgy")
parsed = json.loads(req.text)
results = parsed['results']

embroidery = {'description': 'Embroidery! Embroidery is the use of thread in special cloth to create decorative effects.'
                             'One of the simpler forms of embroidery is cross stitch, which stretches perforated '
                             'cloth across a hoop and draws the needle in and out in the shape of an "x."',
              'time spent': 'weeks', 'class': ["portable"], 'title': results[0]['title'], 'url': results[0]['url']}

req = requests.get("https://openapi.etsy.com/v2/listings/active?tags=flower+press&limit=1&api_key=dkuzdt3r4l4jycbgdojnczgy")
parsed = json.loads(req.text)
results = parsed['results']

flower_press = {'description': 'Flower pressing! You can go outside and collect some flowers and other vegetation to '
                               'press and dry for use in cards, papermaking, resin, or other projects.',
                'time spent': 'weeks', 'class': [], 'title': results[0]['title'], 'url': results[0]['url']}

req = requests.get("https://openapi.etsy.com/v2/listings/active?tags=garland+kit&limit=1&api_key=dkuzdt3r4l4jycbgdojnczgy")
parsed = json.loads(req.text)
results = parsed['results']

garland = {'description': 'Garland making! Do you feel festive? There are many different kinds of garlands one ',
           'can make in order to decorate the house. Some are paper, some are balloons, and some are even felt.'
           'time spent': 'days', 'class': [], 'title': results[0]['title'], 'url': results[0]['url']}

req = requests.get("https://openapi.etsy.com/v2/listings/active?tags=kintsugi+kit&limit=1&api_key=dkuzdt3r4l4jycbgdojnczgy")
parsed = json.loads(req.text)
results = parsed['results']

kintsugi = {'description': 'Kintsugi! Kintsugi is the art of putting broken pieces of pottery back together again, '
                           'celebrating the cracks with a gold filling/adhesive.',
            'time spent': 'days', 'class': [], 'title': results[0]['title'], 'url': results[0]['url']}

req = requests.get("https://openapi.etsy.com/v2/listings/active?tags=scarf+knitting+kit&limit=1&api_key=dkuzdt3r4l4jycbgdojnczgy")
parsed = json.loads(req.text)
results = parsed['results']

knitting = {'description': 'Knitting a shawl or scarf! Knitting is a skill that give you decades of enjoyment. '
                           'Take two large knitting needles and loop the yarn around them in such a fashion '
                           'that the yarn takes on a fabric-like dimension.',
            'time spent': 'weeks', 'class': ["portable"], 'title': results[0]['title'], 'url': results[0]['url']}

req = requests.get("https://openapi.etsy.com/v2/listings/active?tags=loom+weaving+kit&limit=1&api_key=dkuzdt3r4l4jycbgdojnczgy")
parsed = json.loads(req.text)
results = parsed['results']

loom_weaving = {'description': 'Loom weaving! Loom weaving involves using thread-like strands to create a'
                               ' carpet-like sheet. It is almost like a cross between basket weaving and embroidery. '
                               'It involves the use of a frame to assist in the weaving.',
                'time spent': 'weeks', 'class': [], 'title': results[0]['title'], 'url': results[0]['url']}

req = requests.get("https://openapi.etsy.com/v2/listings/active?tags=macaron+kit&limit=1&api_key=dkuzdt3r4l4jycbgdojnczgy")
parsed = json.loads(req.text)
results = parsed['results']

macaron = {'description': 'Baking marcarons! Macarons are French cookies with a delicate buttercream icing sandwiched '
                          'between cookies that are crisp on the outside and soft and chewy on the inside. These can '
                          'be a challenge for the amateur baker, but maybe you like a challenge.',
           'time spent': 'days', 'class': ["kitchen"], 'title': results[0]['title'], 'url': results[0]['url']}

req = requests.get("https://openapi.etsy.com/v2/listings/active?tags=macrame+kit&limit=1&api_key=dkuzdt3r4l4jycbgdojnczgy")
parsed = json.loads(req.text)
results = parsed['results']

macrame = {'description': 'Macrame! Macrame was all the rage in the 1970s. Macrame involves tying thin ropes into knots.'
                          ' Today, these kits often involve hanging things, like plant pots.',
           'time spent': 'days', 'class': [], 'title': results[0]['title'], 'url': results[0]['url']}

req = requests.get("https://openapi.etsy.com/v2/listings/active?tags=moss+wall+kit&limit=1&api_key=dkuzdt3r4l4jycbgdojnczgy")
parsed = json.loads(req.text)
results = parsed['results']

moss_art = {'description': 'Moss art! Create art with living, natural, real materials from nature! Moss kits generally '
                           'involve making either terrariums or wall art.',
            'time spent': 'days', 'class': [], 'title': results[0]['title'], 'url': results[0]['url']}

req = requests.get("https://openapi.etsy.com/v2/listings/active?tags=needle+felting+kit&limit=1&api_key=dkuzdt3r4l4jycbgdojnczgy")
parsed = json.loads(req.text)
results = parsed['results']

needle_felting = {'description': 'Needle felting! Needle felting involves jabbing a needle into loose wool until'
                                 ' it becomes somewhat solid. Lots of people make dolls and other figurines with'
                                 'needle felting techniques.',
                  'time spent': 'days', 'class': ["portable"], 'title': results[0]['title'], 'url': results[0]['url']}

req = requests.get("https://openapi.etsy.com/v2/listings/active?tags=paint+numbers+kit&limit=1&api_key=dkuzdt3r4l4jycbgdojnczgy")
parsed = json.loads(req.text)
results = parsed['results']

painting = {'description': 'Paint by numbers! Use a brush to paint acrylics over specially-marked areas for a '
                           'given color. You will end up with a beautiful picture. The paints come in tiny plastic '
                           'containers, so this is a relatively portable craft if you can get a small cup of water.',
            'time spent': 'weeks', 'class': ["portable"], 'title': results[0]['title'], 'url': results[0]['url']}

req = requests.get("https://openapi.etsy.com/v2/listings/active?tags=plush+kit&limit=1&api_key=dkuzdt3r4l4jycbgdojnczgy")
parsed = json.loads(req.text)
results = parsed['results']

plush = {'description': 'Sewing a plush! Making your own stuffed animals can be very satisfying, and it is a skill'
                        ' that can come in especially handy if children are in your life.',
         'time spent': 'weeks', 'class': [], 'title': results[0]['title'], 'url': results[0]['url']}

req = requests.get("https://openapi.etsy.com/v2/listings/active?tags=polymer+clay+kit&limit=1&api_key=dkuzdt3r4l4jycbgdojnczgy")
parsed = json.loads(req.text)
results = parsed['results']

polymer_clay = {'description': 'Polymer clay! Polymer clay comes in a variety of colors from jet black to hot pink.'
                               ' Polymer clay can be used to sculpt figurines or make jewelry, But it has to be baked'
                               ' in order to set.',
                'time spent': 'days', 'class': ["kitchen"], 'title': results[0]['title'], 'url': results[0]['url']}

req = requests.get("https://openapi.etsy.com/v2/listings/active?tags=quilting+kit&limit=1&api_key=dkuzdt3r4l4jycbgdojnczgy")
parsed = json.loads(req.text)
results = parsed['results']

quilting = {'description': 'Quilting! Sewing a quilt takes time, patience, and dedication, but it is a time-honored '
                           'form of expression through fabric art, and a way to really dress up a blanket. You might'
                           ' enjoy the history and tradition behind quilt patterns.',
            'time spent': 'days', 'class': [], 'title': results[0]['title'], 'url': results[0]['url']}

req = requests.get("https://openapi.etsy.com/v2/listings/active?tags=scandinavian+baking+kit&limit=1&api_key=dkuzdt3r4l4jycbgdojnczgy")
parsed = json.loads(req.text)
results = parsed['results']

scandinavian_baking = {'description': 'Scandinavian baking! This is a very Christmasy craft. Most kits for '
                                      'Scandinavian baking are for cinnamon or cardamom pastries.',
                       'time spent': 'days', 'class': ["kitchen"], 'title': results[0]['title'], 'url': results[0]['url']}

req = requests.get("https://openapi.etsy.com/v2/listings/active?tags=soap+making+kit&limit=1&api_key=dkuzdt3r4l4jycbgdojnczgy")
parsed = json.loads(req.text)
results = parsed['results']

soap_making = {'description': 'Soap making! There are different types of soap making. Cold pressed soap making '
                              'involves some dangerous chemicals, so do be cautious if you have pets or children. '
                              'But customizing your own soap means you can put your own fragrances and exfoliants and '
                              'other ingredients in it, and can even top it off with a bit of crushed rose petals. '
                              'And it is practical because everyone needs soap.',
               'time spent': 'days', 'class': ["kitchen"], 'title': results[0]['title'], 'url': results[0]['url']}

req = requests.get("https://openapi.etsy.com/v2/listings/active?tags=solar+printing+kit&limit=1&api_key=dkuzdt3r4l4jycbgdojnczgy")
parsed = json.loads(req.text)
results = parsed['results']

solar_printing = {'description': 'Solar printing! This involves placing an object like a leaf over a page of '
                                 'specially-treated paper to create a shadow image of that object. It takes about '
                                 'a day to process, and it makes a beautiful picture.',
                  'time spent': 'days', 'class': [], 'title': results[0]['title'], 'url': results[0]['url']}

req = requests.get("https://openapi.etsy.com/v2/listings/active?tags=tie+dye+kit&limit=1&api_key=dkuzdt3r4l4jycbgdojnczgy")
parsed = json.loads(req.text)
results = parsed['results']

tie_dye = {'description': 'Tie dye! Twist and tie up a plain shirt and squirt different colored dyes over the fabric.'
                          ' You will be surprised at the designs that come out of it! This is a wearable craft!',
           'time spent': 'days', 'class': [], 'title': results[0]['title'], 'url': results[0]['url']}

req = requests.get("https://openapi.etsy.com/v2/listings/active?tags=wax+seal+kit&limit=1&api_key=dkuzdt3r4l4jycbgdojnczgy")
parsed = json.loads(req.text)
results = parsed['results']

wax_seal = {'description': 'Wax seals! Once used by the emperors of Rome and other dignitaries, wax seals are still an '
                           'elegant way to seal the envelopes of your handwritten correspondence.',
            'time spent': 'days', 'class': [], 'title': results[0]['title'], 'url': results[0]['url']}

req = requests.get("https://openapi.etsy.com/v2/listings/active?tags=wire+wrap+kit&limit=1&api_key=dkuzdt3r4l4jycbgdojnczgy")
parsed = json.loads(req.text)
results = parsed['results']

wire_wrap = {'description': 'Wire wrapped necklaces! Wire wrapping involves taking a thread-like piece of metal and '
                            'twisting and looping it in order to create beautiful settings for cabochons '
                            'and beads. This is a great skill to have during Christmas!',
             'time spent': 'days', 'class': ["portable"], 'title': results[0]['title'], 'url': results[0]['url']}

req = requests.get("https://openapi.etsy.com/v2/listings/active?tags=witchcraft+kit&limit=1&api_key=dkuzdt3r4l4jycbgdojnczgy")
parsed = json.loads(req.text)
results = parsed['results']

witchcraft = {'description': 'Witchcraft kit! This is a unique craft. It is for your own personal and spiritual needs. '
                             'It will not produce something you can give as a material gift. But with a witchcraft '
                             'kit, you should be able to cast spells, perform rituals, observe the cycles of the moon, '
                             'and basically wish well for the people and things in your life that matter.',
              'time spent': 'months', 'class': [], 'title': results[0]['title'], 'url': results[0]['url']}

# List of all 30 crafts in alphabetical order
all_crafts = [air_dry_clay, amigurumi, basket_weaving, book_binding, bracelet, candle_making, carving, chocolate,
              dream_catcher, embroidery, flower_press, garland, kintsugi, knitting, loom_weaving, macaron,
              macrame, moss_art, needle_felting, painting, plush, polymer_clay, quilting, scandinavian_baking,
              soap_making, solar_printing, tie_dye, wax_seal, wire_wrap, witchcraft]

# Classes
# Prints extra descriptions based on whether or not a class exists

class HasClass():
    """In case the class value is not empty"""
    def __init__(self):
        """Initialize car attributes."""
    def kitchen(self):
        """Prints statement about needing a kitchen."""
        print("This is a craft which requires access to a kitchen. "
              "It may need utensils, baking sheets, or other items that are traditionally found in a kitchen as well.")
    def portable(self):
        """Prints statement about being portable"""
        print("This craft is portable! You can probably work on it during a visit to your local cafe.")


# Quiz

quizTop = input("How long do you want this new project to take? Enter a menu number. "
                "\n1: HOURS OR DAYS, 2: WEEKS, 3: MONTHS, 4: DON'T CARE\n")

if quizTop == "1":
# Hours/Days projects.

# Options narrow to air_dry_clay, amigurumi, book_binding, bracelet, candle_making, carving, chocolate,
# dream_catcher, garland, kintsugi, macaron, moss_art, needle_felting, polymer_clay,
# scandinavian_baking, soap_making, solar_printing, tie_dye, wax_seal, wire_wrap

     q1portable = input("Do you want something portable?\n1: YES, 2: DON’T CARE\n")
     if q1portable == "1":
     # Hours/Days projects that are portable.
     # Options narrow to amigurumi, bracelet, carving, needle_felting, wire_wrap
         q1portable1 = input("Do you want to make a figurine or jewelry?\n1: FIGURINE, 2: JEWELRY\n")
         if q1portable1 == "1":
             q1portable1_1 = input("Are you okay with working with sharp tools?\n1: YES, 2: NO\n")
             if q1portable1_1 == "1":
                 q1portable1_1_1 = input("Knife or large, jabby needle?\n1: KNIFE, 2: NEEDLE\n")
                 if q1portable1_1_1 == "1":
                     write("carving")
                     print()
                     print(carving["description"])
                     print()
                     print(carving['url'])
                     print(carving['title'])
                     if carving['class']:
                         for theclass, thearguments in carving.items():
                             for argument in thearguments:
                                 if argument == "kitchen":
                                     HasClass().kitchen()
                                 elif argument == "portable":
                                     HasClass().portable()
                     stats("carving")
                     exit()

                 elif q1portable1_1_1 == "2":
                     write("needle_felting")
                     print()
                     print(needle_felting["description"])
                     print()
                     print(needle_felting['url'])
                     print(needle_felting['title'])
                     if needle_felting['class']:
                         for theclass, thearguments in needle_felting.items():
                             for argument in thearguments:
                                 if argument == "kitchen":
                                     HasClass().kitchen()
                                 elif argument == "portable":
                                     HasClass().portable()
                     stats("needle_felting")
                     exit()

             elif q1portable1_1 == "2":
                 write("amigurumi")
                 print()
                 print(amigurumi["description"])
                 print()
                 print(amigurumi['url'])
                 print(amigurumi['title'])
                 if amigurumi['class']:
                     for theclass, thearguments in amigurumi.items():
                         for argument in thearguments:
                             if argument == "kitchen":
                                 HasClass().kitchen()
                             elif argument == "portable":
                                 HasClass().portable()
                 stats("amigurumi")
                 exit()

         elif q1portable1 == "2":
         # Hours/Days projects that are jewelry.
             q1portable1_2 = input("Do you want to make a necklace or a bracelet?\n1: NECKLACE, 2: BRACELET\n")
             if q1portable1_2 == "1":
                 write("wire_wrap")
                 print()
                 print(wire_wrap["description"])
                 print()
                 print(wire_wrap['url'])
                 print(wire_wrap['title'])
                 if wire_wrap['class']:
                     for theclass, thearguments in wire_wrap.items():
                         for argument in thearguments:
                             if argument == "kitchen":
                                 HasClass().kitchen()
                             elif argument == "portable":
                                 HasClass().portable()
                 stats("wire_wrap")
                 exit()
             elif q1portable1_2 == "2":
                 write("bracelet")
                 print()
                 print(bracelet["description"])
                 print()
                 print(bracelet['url'])
                 print(bracelet['title'])
                 if bracelet['class']:
                     for theclass, thearguments in bracelet.items():
                         for argument in thearguments:
                             if argument == "kitchen":
                                 HasClass().kitchen()
                             elif argument == "portable":
                                 HasClass().portable()
                 stats("bracelet")
                 exit()


     elif q1portable == "2":
     # Hours/Days projects that aren't necessarily portable.

     # Options remain air_dry_clay, amigurumi, book_binding, bracelet, candle_making, carving, chocolate,
     # dream_catcher, garland, kintsugi, macaron, moss_art, needle_felting, polymer_clay,
     # scandinavian_baking, soap_making, solar_printing, tie_dye, wax_seal, wire_wrap

        q1portable2 = input("Do you want to work with clay or pottery?\n1: YES, 2: DON'T CARE\n")

        if q1portable2 == "1":
            q1portable2_1 = input("Would you like to try kintsugi?\n1: YES, 2: NO\n")
            if q1portable2_1 == "1":
                write("kintsugi")
                print()
                print(kintsugi["description"])
                print()
                print(kintsugi['url'])
                print(kintsugi['title'])
                if kintsugi['class']:
                    for theclass, thearguments in kintsugi.items():
                        for argument in thearguments:
                            if argument == "kitchen":
                                HasClass().kitchen()
                            elif argument == "portable":
                                HasClass().portable()
                stats("kintsugi")
                exit()
            elif q1portable2_1 == "2":
                q1portable2_1_2 = input("Do you have access to an oven?\n1: YES, 2: NO\n")
                if q1portable2_1_2 == "1":
                    q1portable2_1_2_1 = input("Do you want to work with colorful clay, or do you want to paint the clay?\n1:COLORFUL CLAY, 2: PLAIN CLAY\n")
                    if q1portable2_1_2_1 == "1":
                        write("polymer_clay")
                        print()
                        print(polymer_clay["description"])
                        print()
                        print(polymer_clay['url'])
                        print(polymer_clay['title'])
                        if polymer_clay['class']:
                            for theclass, thearguments in polymer_clay.items():
                                for argument in thearguments:
                                    if argument == "kitchen":
                                        HasClass().kitchen()
                                    elif argument == "portable":
                                        HasClass().portable()
                        stats("polymer_clay")
                        exit()
                    elif q1portable2_1_2_1 =="2":
                        write("air_dry_clay")
                        print()
                        print(air_dry_clay["description"])
                        print()
                        print(air_dry_clay['url'])
                        print(air_dry_clay['title'])
                        if air_dry_clay['class']:
                            for theclass, thearguments in air_dry_clay.items():
                                for argument in thearguments:
                                    if argument == "kitchen":
                                        HasClass().kitchen()
                                    elif argument == "portable":
                                        HasClass().portable()
                        stats("air_dry_clay")
                        exit()
                elif q1portable2_1_2 == "2":
                    write("air_dry_clay")
                    print()
                    print(air_dry_clay["description"])
                    print()
                    print(air_dry_clay['url'])
                    print(air_dry_clay['title'])
                    if air_dry_clay['class']:
                        for theclass, thearguments in air_dry_clay.items():
                            for argument in thearguments:
                                if argument == "kitchen":
                                    HasClass().kitchen()
                                elif argument == "portable":
                                    HasClass().portable()
                    stats("air_dry_clay")
                    exit()



        q1portable2_2 = input("Do you want to make fabric art?\n1: YES, 2: NO\n")

        if q1portable2_2 == "1":
            q1portable2_2_1 = input("Do you want to make something wearable?\n1: YES, 2: NO\n")
            if q1portable2_2_1 == "1":
                write("tie_dye")
                print()
                print(tie_dye["description"])
                print()
                print(tie_dye['url'])
                print(tie_dye['title'])
                if tie_dye['class']:
                    for theclass, thearguments in tie_dye.items():
                        for argument in thearguments:
                            if argument == "kitchen":
                                HasClass().kitchen()
                            elif argument == "portable":
                                HasClass().portable()
                stats("tie_dye")
                exit()
            elif q1portable2_2_1 == "2":
                q1portable2_2_2_2 = input ("Do you want to make a figurine?\n1: YES, 2: NO\n")
                if q1portable2_2_2_2 == "1":
                    q1portable2_2_2_2_1 = input("Do you want to crochet or use a needle to jab things?\n1: CROCHET, 2: NEEDLE FELTING\n")
                    if q1portable2_2_2_2_1 == "1":
                        write("amigurumi")
                        print()
                        print(amigurumi["description"])
                        print()
                        print(amigurumi['url'])
                        print(amigurumi['title'])
                        if amigurumi['class']:
                            for theclass, thearguments in amigurumi.items():
                                for argument in thearguments:
                                    if argument == "kitchen":
                                        HasClass().kitchen()
                                    elif argument == "portable":
                                        HasClass().portable()
                        stats("amigurumi")
                        exit()
                    elif q1portable2_2_2_2_1 == "2":
                        write("needle_felting")
                        print()
                        print(needle_felting["description"])
                        print()
                        print(needle_felting['url'])
                        print(needle_felting['title'])
                        if needle_felting['class']:
                            for theclass, thearguments in needle_felting.items():
                                for argument in thearguments:
                                    if argument == "kitchen":
                                        HasClass().kitchen()
                                    elif argument == "portable":
                                        HasClass().portable()
                        stats("needle_felting")
                        exit()


        elif q1portable2_2 == "2":
            q1portable2_2_2 = input("Do you want to do some writing by hand?\n1: YES, 2: NO\n")
            if q1portable2_2_2 == "1":
                q1portable2_2_2_1 = input("Do you want to write a letter?\n1: YES, 2: NO\n")
                if q1portable2_2_2_1 == "1":
                    write("wax_seal")
                    print()
                    print(wax_seal["description"])
                    print()
                    print(wax_seal['url'])
                    print(wax_seal['title'])
                    if wax_seal['class']:
                        for theclass, thearguments in wax_seal.items():
                            for argument in thearguments:
                                if argument == "kitchen":
                                    HasClass().kitchen()
                                elif argument == "portable":
                                    HasClass().portable()
                    stats("wax_seal")
                    exit()

            elif q1portable2_2_2 == "2":
                q1portable2_2_2_2 = input("Are you interested in making a journal or making something to send?\n1: JOURNAL, 2: SOMETHING TO SEND\n")
                if q1portable2_2_2_2 == "1":
                    write("book_binding")
                    print()
                    print(book_binding["description"])
                    print()
                    print(book_binding['url'])
                    print(book_binding['title'])
                    if book_binding['class']:
                        for theclass, thearguments in book_binding.items():
                            for argument in thearguments:
                                if argument == "kitchen":
                                    HasClass().kitchen()
                                elif argument == "portable":
                                    HasClass().portable()
                    stats("book_binding")
                    exit()
                elif q1portable2_2_2_2 == "2":
                    write("solar_printing")
                    print()
                    print(solar_printing["description"])
                    print()
                    print(solar_printing['url'])
                    print(solar_printing['title'])
                    if solar_printing['class']:
                        for theclass, thearguments in solar_printing.items():
                            for argument in thearguments:
                                if argument == "kitchen":
                                    HasClass().kitchen()
                                elif argument == "portable":
                                    HasClass().portable()
                    stats("solar_printing")
                    exit()




            q1p2_2_2_2_jewelry = input("Do you want to make jewelry?\n1: YES, 2: NO\n")
            if q1p2_2_2_2_jewelry == "1":
                q1p2_2_2_2_jewelry_1 = input("Do you want to work with metal and a cabochon or beads?\n1: METAL, 2: BEADS\n")
                if q1p2_2_2_2_jewelry_1 == "1":
                    write("wire_wrap")
                    print()
                    print(wire_wrap["description"])
                    print()
                    print(wire_wrap['url'])
                    print(wire_wrap['title'])
                    if wire_wrap['class']:
                        for theclass, thearguments in wire_wrap.items():
                            for argument in thearguments:
                                if argument == "kitchen":
                                    HasClass().kitchen()
                                elif argument == "portable":
                                    HasClass().portable()
                    stats("wire_wrap")
                    exit()
                elif q1p2_2_2_2_jewelry_1 == "2":
                    write("bracelet")
                    print()
                    print(bracelet["description"])
                    print()
                    print(bracelet['url'])
                    print(bracelet['title'])
                    if bracelet['class']:
                        for theclass, thearguments in bracelet.items():
                            for argument in thearguments:
                                if argument == "kitchen":
                                    HasClass().kitchen()
                                elif argument == "portable":
                                    HasClass().portable()
                    stats("bracelet")
                    exit()



            q1p2_2_2_2_2_practical = input("Do you want to make something practical?\n1: YES, 2: NO\n")
            if q1p2_2_2_2_2_practical == "1":
                q1p2_2_2_2_2_practical_1 = input("Do you want to make something edible?\n1: YES, 2: NO\n")
                if q1p2_2_2_2_2_practical_1 == "1":
                    q1p2_2_2_2_2_practical_1_1= input("Is this for the holidays?\n1: YES, 2: NO\n")
                    if q1p2_2_2_2_2_practical_1_1 == "1":
                        write("scandinavian_caking")
                        print()
                        print(scandinavian_baking["description"])
                        print()
                        print(scandinavian_baking['url'])
                        print(scandinavian_baking['title'])
                        if scandinavian_baking['class']:
                            for theclass, thearguments in scandinavian_baking.items():
                                for argument in thearguments:
                                    if argument == "kitchen":
                                        HasClass().kitchen()
                                    elif argument == "portable":
                                        HasClass().portable()
                        stats("scandinavian_baking")
                        exit()
                    elif q1p2_2_2_2_2_practical_1_1 == "2":
                        q1p2_2_2_2_2_practical_1_1 = input("Chocolate or cookies?\n1: CHOCOLATE, 2: COOKIES\n")
                        if q1p2_2_2_2_2_practical_1_1 == "1":
                            write("chocolate")
                            print()
                            print(chocolate["description"])
                            print()
                            print(chocolate['url'])
                            print(chocolate['title'])
                            if chocolate['class']:
                                for theclass, thearguments in chocolate.items():
                                    for argument in thearguments:
                                        if argument == "kitchen":
                                            HasClass().kitchen()
                                        elif argument == "portable":
                                            HasClass().portable()
                            stats("chocolate")
                            exit()
                        elif q1p2_2_2_2_2_practical_1_1 == "2":
                            write("macaron")
                            print()
                            print(macaron["description"])
                            print()
                            print(macaron['url'])
                            print(macaron['title'])
                            if macaron['class']:
                                for theclass, thearguments in macaron.items():
                                    for argument in thearguments:
                                        if argument == "kitchen":
                                            HasClass().kitchen()
                                        elif argument == "portable":
                                            HasClass().portable()
                            stats('macaron')
                            exit()



            if q1p2_2_2_2_2_practical == "2":
                q1p2_2_2_2_2_practical_2 == input("Soap or candles?\n1: SOAP, 2: CANDLES\n")
                if q1p2_2_2_2_2_practical_2 == "1":
                    write("soap_making")
                    print()
                    print(soap_making["description"])
                    print()
                    print(soap_making['url'])
                    print(soap_making['title'])
                    if soap_making['class']:
                        for theclass, thearguments in soap_making.items():
                            for argument in thearguments:
                                if argument == "kitchen":
                                    HasClass().kitchen()
                                elif argument == "portable":
                                    HasClass().portable()
                    stats('soap_making')
                    exit()
                elif q1p2_2_2_2_2_practical_2 == "2":
                    write("candle_making")
                    print()
                    print(candle_making["description"])
                    print()
                    print(candle_making['url'])
                    print(candle_making['title'])
                    if candle_making['class']:
                        for theclass, thearguments in candle_making.items():
                            for argument in thearguments:
                                if argument == "kitchen":
                                    HasClass().kitchen()
                                elif argument == "portable":
                                    HasClass().portable()
                    stats('candle_making')
                    exit()


            q1p2_2_2_2_2_knife = input("Are you okay with working with a knife?\n1: YES, 2: NO\n")
            if q1p2_2_2_2_2_knife == "1":
                write("carving")
                print()
                print(carving["description"])
                print()
                print(carving['url'])
                print(carving['title'])
                if carving['class']:
                    for theclass, thearguments in carving.items():
                        for argument in thearguments:
                            if argument == "kitchen":
                                HasClass().kitchen()
                            elif argument == "portable":
                                HasClass().portable()
                stats('carving')
                exit()


            q1p2_2_2_2_2_hang = input("Do you want something you can hang up?\n1:YES, 2:NO\n")
            if q1p2_2_2_2_2_hang == "1":
                q1p2_2_2_2_2_hang_1 = input("Are you going to celebrate an event soon?\n1: YES, 2: NO\n")
                if q1p2_2_2_2_2_hang_1 == "1":
                    write("garland")
                    print()
                    print(garland["description"])
                    print()
                    print(garland['url'])
                    print(garland['title'])
                    if garland['class']:
                        for theclass, thearguments in garland.items():
                            for argument in thearguments:
                                if argument == "kitchen":
                                    HasClass().kitchen()
                                elif argument == "portable":
                                    HasClass().portable()
                    stats('garland')
                    exit()

            elif q1p2_2_2_2_2_hang == "2":
                q1p2_2_2_2_2_hang_2 = input("Do you want to work with living plants?\n1: YES, 2: NO\n")
                if q1p2_2_2_2_2_hang_2 == "1":
                    write("moss_art")
                    print()
                    print(moss_art["description"])
                    print()
                    print(moss_art['url'])
                    print(moss_art['title'])
                    if moss_art['class']:
                        for theclass, thearguments in moss_art.items():
                            for argument in thearguments:
                                if argument == "kitchen":
                                    HasClass().kitchen()
                                elif argument == "portable":
                                    HasClass().portable()
                    stats('moss_art')
                    exit()


                q1p2_2_2_2_2_hang_2point1 = input("Do you want a new age craft?\n1: YES, 2: NO\n")
                if q1p2_2_2_2_2_hang_2point1 == "1":
                    write("dream_catcher")
                    print()
                    print(dream_catcher["description"])
                    print()
                    print(dream_catcher['url'])
                    print(dream_catcher['title'])
                    if dream_catcher['class']:
                        for theclass, thearguments in dream_catcher.items():
                            for argument in thearguments:
                                if argument == "kitchen":
                                    HasClass().kitchen()
                                elif argument == "portable":
                                    HasClass().portable()
                    stats('dream_catcher')
                    exit()
                elif q1p2_2_2_2_2_hang_2point1 == "2":
                    print("Sorry, I don't think we have a craft idea for you!")

            else:
                print("Sorry, I don't think we have a craft idea for you!")



elif quizTop == "2":
    # Weeks-long projects.
    # Options narrow to basket_weaving, embroidery, flower_press, knitting, loom_weaving, macrame, painting, plush, quilting
    q2portable = input("Do you want something portable?\n1: YES, 2: DON’T CARE\n")
    if q2portable == "1":
    # Weeks-long projects that are portable.
    # Options narrow to embroidery, knitting, painting
        q2portable_1 = input("Do you want to sew, knit, or paint?\n1: SEW, 2: KNIT, 3: PAINT\n")
        if q2portable_1 == "1":
            write("embroidery")
            print()
            print(embroidery["description"])
            print()
            print(embroidery['url'])
            print(embroidery['title'])
            if embroidery['class']:
                for theclass, thearguments in embroidery.items():
                    for argument in thearguments:
                        if argument == "kitchen":
                            HasClass().kitchen()
                        elif argument == "portable":
                            HasClass().portable()
            stats('embroidery')
            exit()
        elif q2portable_1 == "2":
            write("knitting")
            print()
            print(knitting["description"])
            print()
            print(knitting['url'])
            print(knitting['title'])
            if knitting['class']:
                for theclass, thearguments in knitting.items():
                    for argument in thearguments:
                        if argument == "kitchen":
                            HasClass().kitchen()
                        elif argument == "portable":
                            HasClass().portable()
            stats('knitting')
            exit()
        elif q2portable_1 == "3":
            write("painting")
            print()
            print(painting["description"])
            print()
            print(painting['url'])
            print(painting['title'])
            if painting['class']:
                for theclass, thearguments in painting.items():
                    for argument in thearguments:
                        if argument == "kitchen":
                            HasClass().kitchen()
                        elif argument == "portable":
                            HasClass().portable()
            stats('painting')
            exit()
        else:
            print("Sorry, I don't think we have a craft idea for you!")

    elif q2portable == "2":
    # Weeks-long projects that are not necessarily portable.
    # Options remain basket_weaving, embroidery, flower_press, knitting, loom_weaving, macrame, painting, plush, quilting
        q2portable_2 = input("Do you want to tie knots?\n1: YES, 2: NO\n")
        if q2portable_2 == "1":
            write("macrame")
            print()
            print(macrame["description"])
            print()
            print(macrame['url'])
            print(macrame['title'])
            if macrame['class']:
                for theclass, thearguments in macrame.items():
                    for argument in thearguments:
                        if argument == "kitchen":
                            HasClass().kitchen()
                        elif argument == "portable":
                            HasClass().portable()
            stats('macrame')
            exit()
        elif q2portable_2 == "2":
            q2portable_2_2 = input("Do you want to knit?\n1: YES, 2: NO\n")
            if q2portable_2_2 == "1":
                write("knitting")
                print()
                print(knitting["description"])
                print()
                print(knitting['url'])
                print(knitting['title'])
                if knitting['class']:
                    for theclass, thearguments in knitting.items():
                        for argument in thearguments:
                            if argument == "kitchen":
                                HasClass().kitchen()
                            elif argument == "portable":
                                HasClass().portable()
                stats('knitting')
                exit()
            elif q2portable_2_2 == "2":
                q2portable_2_2_2 = input("Do you want to weave a basket or a cloth?\n1: BASKET, 2: CLOTH, 3: NO\n")
                if q2portable_2_2_2 == "1":
                    write("basket_weaving")
                    print()
                    print(basket_weaving["description"])
                    print()
                    print(basket_weaving['url'])
                    print(basket_weaving['title'])
                    if basket_weaving['class']:
                        for theclass, thearguments in basket_weaving.items():
                            for argument in thearguments:
                                if argument == "kitchen":
                                    HasClass().kitchen()
                                elif argument == "portable":
                                    HasClass().portable()
                    stats('basket_weaving')
                    exit()
                elif q2portable_2_2_2 == "2":
                    write("loom_weaving")
                    print()
                    print(loom_weaving["description"])
                    print()
                    print(loom_weaving['url'])
                    print(loom_weaving['title'])
                    if loom_weaving['class']:
                        for theclass, thearguments in loom_weaving.items():
                            for argument in thearguments:
                                if argument == "kitchen":
                                    HasClass().kitchen()
                                elif argument == "portable":
                                    HasClass().portable()
                    stats('loom_weaving')
                    exit()
                elif q2portable_2_2_2 == "3":
                    q2portable_2_2_2_3 = input("Do you want to sew?\n1: YES, 2: NO\n")
                    if q2portable_2_2_2_3 == "1":
                        q2portable_2_2_2_3_1 = input("Quilting or embroidery?\n1: QUILTING, 2: EMBROIDERY, 3: NEITHER\n")
                        if q2portable_2_2_2_3_1 == "1":
                            write("quilting")
                            print()
                            print(quilting["description"])
                            print()
                            print(quilting['url'])
                            print(quilting['title'])
                            if quilting['class']:
                                for theclass, thearguments in quilting.items():
                                    for argument in thearguments:
                                        if argument == "kitchen":
                                            HasClass().kitchen()
                                        elif argument == "portable":
                                            HasClass().portable()
                            stats('quilting')
                            exit()
                        elif q2portable_2_2_2_3_1 == "2":
                            write("embroidery")
                            print()
                            print(embroidery["description"])
                            print()
                            print(embroidery['url'])
                            print(embroidery['title'])
                            if embroidery['class']:
                                for theclass, thearguments in embroidery.items():
                                    for argument in thearguments:
                                        if argument == "kitchen":
                                            HasClass().kitchen()
                                        elif argument == "portable":
                                            HasClass().portable()
                            stats('embroidery')
                            exit()


                        elif q2portable_2_2_2_3 == "2":
                             q2portable_2_2_2_3_2 = input("Picking flowers or painting?\n1: FLOWERS, 2: PAINTING, 3: NEITHER\n")
                             if q2portable_2_2_2_3_2 == "1":
                                 write("flower_press")
                                 print()
                                 print(flower_press["description"])
                                 print()
                                 print(flower_press['url'])
                                 print(flower_press['title'])
                                 if flower_press['class']:
                                     for theclass, thearguments in flower_press.items():
                                         for argument in thearguments:
                                             if argument == "kitchen":
                                                 HasClass().kitchen()
                                             elif argument == "portable":
                                                 HasClass().portable()
                                 stats('flower_press')
                                 exit()
                             elif q2portable_2_2_2_3_2 == "2":
                                 write("painting")
                                 print()
                                 print(painting["description"])
                                 print()
                                 print(painting['url'])
                                 print(painting['title'])
                                 if painting['class']:
                                     for theclass, thearguments in painting.items():
                                         for argument in thearguments:
                                             if argument == "kitchen":
                                                 HasClass().kitchen()
                                             elif argument == "portable":
                                                 HasClass().portable()
                                 stats('painting')
                                 exit()
                             elif q2portable_2_2_2_3_2 == "3":
                                 print("Sorry, I don't think we have any craft ideas for you!")



elif quizTop == "3":
# Months long projects.
    write("witchcraft")
    print()
    print(witchcraft["description"])
    print()
    print(witchcraft['url'])
    print(witchcraft['title'])
    if witchcraft['class']:
        for theclass, thearguments in witchcraft.items():
            for argument in thearguments:
                if argument == "kitchen":
                    HasClass().kitchen()
                elif argument == "portable":
                    HasClass().portable()
    stats('witchcraft')
    exit()

elif quizTop == "4":
    # All options available
    q4portable = input("Do you want something portable?\n1: YES, 2: DON’T CARE\n")
    if q4portable == "1":
    # All portable projects.
    # Options narrow to amigurumi, bracelet, carving, embroidery, knitting, needle_felting, painting, wire_wrap
        q4portable_1 = input("Do you want to work with textile art?\n1:YES, 2: NO\n")
        if q4portable_1 == "1":
            q4portable_1_1 = input("Do you want to knit, or do you want to use a sharp needle?\n1: KNIT, 2: NEEDLE\n")
            if q4portable_1_1 == "1":
                q4portable_1_1_1 = "Do you want to embroider or jab wool?\n1: EMBROIDER, 2: WOOL"
                if q4portable_1_1_1 == "1":
                    write("embroidery")
                    print()
                    print(embroidery["description"])
                    print()
                    print(embroidery['url'])
                    print(embroidery['title'])
                    if embroidery['class']:
                        for theclass, thearguments in embroidery.items():
                            for argument in thearguments:
                                if argument == "kitchen":
                                    HasClass().kitchen()
                                elif argument == "portable":
                                    HasClass().portable()
                    stats('embroidery')
                    exit()
                elif q4portable_1_1_1 == "2":
                    write("needle_felting")
                    print()
                    print(needle_felting["description"])
                    print()
                    print(needle_felting['url'])
                    print(needle_felting['title'])
                    if needle_felting['class']:
                        for theclass, thearguments in needle_felting.items():
                            for argument in thearguments:
                                if argument == "kitchen":
                                    HasClass().kitchen()
                                elif argument == "portable":
                                    HasClass().portable()
                    stats('needle_felting')
                    exit()
            elif q4portable_1_1 == "2":
                q4portable_1_1_2 = input("Do you want to make a figure or something to wear?\n1: YES, 2: NO\n")
                if q4portable_1_1_2 == "1":
                    write("knitting")
                    print()
                    print(knitting["description"])
                    print()
                    print(knitting['url'])
                    print(knitting['title'])
                    if knitting['class']:
                        for theclass, thearguments in knitting.items():
                            for argument in thearguments:
                                if argument == "kitchen":
                                    HasClass().kitchen()
                                elif argument == "portable":
                                    HasClass().portable()
                    stats('knitting')
                    exit()
                elif q4portable_1_1_2 == "2":
                    write("amigurumi")
                    print()
                    print(amigurumi["description"])
                    print()
                    print(amigurumi['url'])
                    print(amigurumi['title'])
                    if amigurumi['class']:
                        for theclass, thearguments in amigurumi.items():
                            for argument in thearguments:
                                if argument == "kitchen":
                                    HasClass().kitchen()
                                elif argument == "portable":
                                    HasClass().portable()
                    stats('amigurumi')
                    exit()


        q4portable_1_jewelry = input("Do you want to make jewelry?\n1: YES, 2: NO\n")
        if q4portable_1_jewelry == "1":
            q4portable_1_jewelry_1 = input("Do you want to work with metal and a cabochon or beads?\n1: CABOCHON, 2: BEADS\n")
            if q4portable_1_jewelry_1 == "1":
                write("wire_wrap")
                print()
                print(wire_wrap["description"])
                print()
                print(wire_wrap['url'])
                print(wire_wrap['title'])
                if wire_wrap['class']:
                    for theclass, thearguments in wire_wrap.items():
                        for argument in thearguments:
                            if argument == "kitchen":
                                HasClass().kitchen()
                            elif argument == "portable":
                                HasClass().portable()
                stats('wire_wrap')
                exit()
            elif q4portable_1_jewelry_1 == "2":
                write("bracelet")
                print()
                print(bracelet["description"])
                print()
                print(bracelet['url'])
                print(bracelet['title'])
                if bracelet['class']:
                    for theclass, thearguments in bracelet.items():
                        for argument in thearguments:
                            if argument == "kitchen":
                                HasClass().kitchen()
                            elif argument == "portable":
                                HasClass().portable()
                stats('bracelet')
                exit()


        q4portable_1_leftover = input("Would you rather work with a knife or a brush?\n1: KNIFE, 2: BRUSH\n")
        if q4portable_1_leftover == "1":
            write("carving")
            print()
            print(carving["description"])
            print()
            print(carving['url'])
            print(carving['title'])
            if carving['class']:
                for theclass, thearguments in carving.items():
                    for argument in thearguments:
                        if argument == "kitchen":
                            HasClass().kitchen()
                        elif argument == "portable":
                            HasClass().portable()
            stats('carving')
            exit()
        elif q4portable_1_leftover == "2":
            write("painting")
            print()
            print(painting["description"])
            print()
            print(painting['url'])
            print(painting['title'])
            if painting['class']:
                for theclass, thearguments in painting.items():
                    for argument in thearguments:
                        if argument == "kitchen":
                            HasClass().kitchen()
                        elif argument == "portable":
                            HasClass().portable()
            stats('painting')
            exit()


    elif q4portable == "2":
    # All options available: air_dry_clay, amigurumi, basket_weaving, book_binding, bracelet, candle_making, carving, chocolate,
    # dream_catcher, embroidery, flower_press, garland, kintsugi, knitting, loom_weaving, macaron,
    # macrame, moss_art, needle_felting, painting, plush, polymer_clay, quilting, scandinavian_baking,
    # soap_making, solar_printing, tie_dye, wax_seal, wire_wrap, witchcraft
        q4portable_2 = input("Do you want to work with clay or pottery?\n1: YES, 2: NO\n")
        if q4portable_2 == "1":
            q4portable_2_1 = input("Do you want to try kintsugi?\n1:YES, 2: NO\n")
            if q4portable_2_1 == "1":
                write("kintsugi")
                print()
                print(kintsugi["description"])
                print()
                print(kintsugi['url'])
                print(kintsugi['title'])
                if kintsugi['class']:
                    for theclass, thearguments in kintsugi.items():
                        for argument in thearguments:
                            if argument == "kitchen":
                                HasClass().kitchen()
                            elif argument == "portable":
                                HasClass().portable()
                stats('kintsugi')
                exit()

            q4portable_2_1_plain = input("Do you want to work with colorful clay or do you want to paint plain clay?\n1: COLORFUL, 2: PLAIN\n")
            if q4portable_2_1_plain == "1":
                q4portable_2_1_plain_1 = input("Do you have access to an oven?\n1: YES, 2: NO\n")
                if q4portable_2_1_plain_1 == "1":
                    write("polymer_clay")
                    print()
                    print(polymer_clay["description"])
                    print()
                    print(polymer_clay['url'])
                    print(polymer_clay['title'])
                    if polymer_clay['class']:
                        for theclass, thearguments in polymer_clay.items():
                            for argument in thearguments:
                                if argument == "kitchen":
                                    HasClass().kitchen()
                                elif argument == "portable":
                                    HasClass().portable()
                    stats('polymer_clay')
                    exit()
                elif q4portable_2_1_plain_1 == "2":
                    print("You need to bake the colorful clay. Here is the alternative.")
                    write("air_dry_clay")
                    print()
                    print(air_dry_clay["description"])
                    print()
                    print(air_dry_clay['url'])
                    print(air_dry_clay['title'])
                    if air_dry_clay['class']:
                        for theclass, thearguments in air_dry_clay.items():
                            for argument in thearguments:
                                if argument == "kitchen":
                                    HasClass().kitchen()
                                elif argument == "portable":
                                    HasClass().portable()
                    stats('air_dry_clay')
                    exit()
            elif q4portable_2_1_plain == "2":
                write("air_dry_clay")
                print()
                print(air_dry_clay["description"])
                print()
                print(air_dry_clay['url'])
                print(air_dry_clay['title'])
                if air_dry_clay['class']:
                    for theclass, thearguments in air_dry_clay.items():
                        for argument in thearguments:
                            if argument == "kitchen":
                                HasClass().kitchen()
                            elif argument == "portable":
                                HasClass().portable()
                stats('air_dry_clay')
                exit()


        q4portable_2_text = input("Do you want to make textile art?\n1: YES, 2: NO\n")
        if q4portable_2_text == "1":
            q4portable_2_text_1 = input("Do you want to knit or crochet?\n1: YES, 2: NO\n")
            if q4portable_2_text_1 == "1":
                q4portable_2_text_1_1 = input("Enter 1 to knit, 2 to crochet.\n")
                if q4portable_2_text_1_1 == "1":
                    write("knitting")
                    print()
                    print(knitting["description"])
                    print()
                    print(knitting['url'])
                    print(knitting['title'])
                    if knitting['class']:
                        for theclass, thearguments in knitting.items():
                            for argument in thearguments:
                                if argument == "kitchen":
                                    HasClass().kitchen()
                                elif argument == "portable":
                                    HasClass().portable()
                    stats('knitting')
                    exit()
                elif q4portable_2_text_1_1 == "2":
                    write("amigurumi")
                    print()
                    print(amigurumi["description"])
                    print()
                    print(amigurumi['url'])
                    print(amigurumi['title'])
                    if amigurumi['class']:
                        for theclass, thearguments in amigurumi.items():
                            for argument in thearguments:
                                if argument == "kitchen":
                                    HasClass().kitchen()
                                elif argument == "portable":
                                    HasClass().portable()
                    stats('amigurumi')
                    exit()
            elif q4portable_2_text_1 == "2":
                q4portable_2_text_1_2 = input("Do you want to make something wearable?\n1: YES, 2: NO\n")
                if q4portable_2_text_1_2 == "1":
                    write("tie_dye")
                    print()
                    print(tie_dye["description"])
                    print()
                    print(tie_dye['url'])
                    print(tie_dye['title'])
                    if tie_dye['class']:
                        for theclass, thearguments in tie_dye.items():
                            for argument in thearguments:
                                if argument == "kitchen":
                                    HasClass().kitchen()
                                elif argument == "portable":
                                    HasClass().portable()
                    stats('tie_dye')
                    exit()
                elif q4portable_2_text_1_2 == "2":
                    q4portable_2_text_1_2_2 = input("Do you want to make a figurine?\n1: YES, 2: NO\n")
                    if q4portable_2_text_1_2_2 == "1":
                        q4portable_2_text_1_2_2_1 = input("Do you want to sew or jab wool with a needle?\n1: SEW, 2: JAB\n")
                        if q4portable_2_text_1_2_2_1 == "1":
                            write("plush")
                            print()
                            print(plush["description"])
                            print()
                            print(plush['url'])
                            print(plush['title'])
                            if plush['class']:
                                for theclass, thearguments in plush.items():
                                    for argument in thearguments:
                                        if argument == "kitchen":
                                            HasClass().kitchen()
                                        elif argument == "portable":
                                            HasClass().portable()
                            stats('plush')
                            exit()
                        elif q4portable_2_text_1_2_2_1 == "2":
                            write("needle_felting")
                            print()
                            print(needle_felting["description"])
                            print()
                            print(needle_felting['url'])
                            print(needle_felting['title'])
                            if needle_felting['class']:
                                for theclass, thearguments in needle_felting.items():
                                    for argument in thearguments:
                                        if argument == "kitchen":
                                            HasClass().kitchen()
                                        elif argument == "portable":
                                            HasClass().portable()
                            stats("needle_felting")
                            exit()
                    elif q4portable_2_text_1_2_2 == "2":
                        write("quilting")
                        print()
                        print(quilting["description"])
                        print()
                        print(quilting['url'])
                        print(quilting['title'])
                        if quilting['class']:
                            for theclass, thearguments in quilting.items():
                                for argument in thearguments:
                                    if argument == "kitchen":
                                        HasClass().kitchen()
                                    elif argument == "portable":
                                        HasClass().portable()
                        stats("quilting")
                        exit()




        q4portable_2_macrame = input("Do you want to tie knots or use a loom?\n1: KNOTS, 2: LOOM, 3: NEITHER\n")
        if q4portable_2_macrame == "1":
            write("macrame")
            print()
            print(macrame["description"])
            print()
            print(macrame['url'])
            print(macrame['title'])
            if macrame['class']:
                for theclass, thearguments in macrame.items():
                    for argument in thearguments:
                        if argument == "kitchen":
                            HasClass().kitchen()
                        elif argument == "portable":
                            HasClass().portable()
            stats("macrame")
            exit()
        elif q4portable_2_macrame =="2":
            write("loom_weaving")
            print()
            print(loom_weaving["description"])
            print()
            print(loom_weaving['url'])
            print(loom_weaving['title'])
            if loom_weaving['class']:
                for theclass, thearguments in loom_weaving.items():
                    for argument in thearguments:
                        if argument == "kitchen":
                            HasClass().kitchen()
                        elif argument == "portable":
                            HasClass().portable()
            stats("loom_weaving")
            exit()



        q4portable_2_natural = input("Do you want to work with natural materials?\n1: YES, 2: NO\n")
        if q4portable_2_natural == "1":
            q4portable_2_natural_1 = input("Do you want to work with live plants?\n1: YES, 2: NO\n")
            if q4portable_2_natural_1 == "1":
                q4portable_2_natural_1_1 = input("Enter 1 for flower picking or 2 for arranging moss.\n")
                if q4portable_2_natural_1_1 == "1":
                    write("flower_press")
                    print()
                    print(flower_press["description"])
                    print()
                    print(flower_press['url'])
                    print(flower_press['title'])
                    if flower_press['class']:
                        for theclass, thearguments in flower_press.items():
                            for argument in thearguments:
                                if argument == "kitchen":
                                    HasClass().kitchen()
                                elif argument == "portable":
                                    HasClass().portable()
                    stats("flower_press")
                    exit()
                elif q4portable_2_natural_1_1 == "2":
                    write("moss_art")
                    print()
                    print(moss_art["description"])
                    print()
                    print(moss_art['url'])
                    print(moss_art['title'])
                    if moss_art['class']:
                        for theclass, thearguments in moss_art.items():
                            for argument in thearguments:
                                if argument == "kitchen":
                                    HasClass().kitchen()
                                elif argument == "portable":
                                    HasClass().portable()
                    stats("moss_art")
                    exit()
        elif q4portable_2_natural == "2":
            q4portable_2_natural_2 = input("Do you want to make something practical?\n1: YES, 2: NO\n")
            if q4portable_2_natural_2 == "1":
                write("basket_weaving")
                print()
                print(basket_weaving["description"])
                print()
                print(basket_weaving['url'])
                print(basket_weaving['title'])
                if basket_weaving['class']:
                    for theclass, thearguments in basket_weaving.items():
                        for argument in thearguments:
                            if argument == "kitchen":
                                HasClass().kitchen()
                            elif argument == "portable":
                                HasClass().portable()
                stats("basket_weaving")
                exit()
            elif q4portable_2_natural_2 == "2":
                q4portable_2_natural_2_1 = input("Have you considered whittling?\n1: YES, 2: NO\n")
                if q4portable_2_natural_2_1 == "1":
                    write("carving")
                    print()
                    print(carving["description"])
                    print()
                    print(carving['url'])
                    print(carving['title'])
                    if needle_felting['class']:
                        for theclass, thearguments in carving.items():
                            for argument in thearguments:
                                if argument == "kitchen":
                                    HasClass().kitchen()
                                elif argument == "portable":
                                    HasClass().portable()
                    stats("carving")
                    exit()
                elif q4portable_2_natural_2_1 == "2":
                    q4portable_2_natural_2_1_2 = input("Are you open to the New Age movement?\n1: YES, 2: NO\n")
                    if q4portable_2_natural_2_1_2 == "1":
                        write("witchcraft")
                        print()
                        print(witchcraft["description"])
                        print()
                        print(witchcraft['url'])
                        print(witchcraft['title'])
                        if witchcraft['class']:
                            for theclass, thearguments in witchcraft.items():
                                for argument in thearguments:
                                    if argument == "kitchen":
                                        HasClass().kitchen()
                                    elif argument == "portable":
                                        HasClass().portable()
                        stats("witchcraft")
                        exit()




        q4portable_2_hand = input("Do you want to write something by hand?\n1: YES, 2: NO\n")
        if q4portable_2_hand == "1":
            q4portable_2_hand_1 = input("Do you want to journal?\n1:YES, 2: NO\n")
            if q4portable_2_hand_1 == "1":
                write("book_binding")
                print()
                print(book_binding["description"])
                print()
                print(book_binding['url'])
                print(book_binding['title'])
                if book_binding['class']:
                    for theclass, thearguments in book_binding.items():
                        for argument in thearguments:
                            if argument == "kitchen":
                                HasClass().kitchen()
                            elif argument == "portable":
                                HasClass().portable()
                stats("book_binding")
                exit()
            elif q4portable_2_hand_1 == "2":
                 q4portable_2_hand_1_2 = input("Do you want to write a letter?\n1: YES, 2: NO\n")
                 if q4portable_2_hand_1_2 == "1":
                     q4portable_2_hand_1_2_1 = input("Do you want to make something you can send, or focus on wax seals?\n1: SEND, 2: WAX SEALS\n")
                     if q4portable_2_hand_1_2_1 == "1":
                         q4portable_2_hand_1_2_1_1 = input("Enter 1 for solar printing, 2 for botanical pressing.\n")
                         if q4portable_2_hand_1_2_1_1 == "1":
                             write("solar_printing")
                             print()
                             print(solar_printing["description"])
                             print()
                             print(solar_printing['url'])
                             print(solar_printing['title'])
                             if solar_printing['class']:
                                 for theclass, thearguments in solar_printing.items():
                                     for argument in thearguments:
                                         if argument == "kitchen":
                                             HasClass().kitchen()
                                         elif argument == "portable":
                                             HasClass().portable()
                             stats("solar_printing")
                             exit()
                         elif q4portable_2_hand_1_2_1_1 == "2":
                             write("flower_press")
                             print()
                             print(flower_press["description"])
                             print()
                             print(flower_press['url'])
                             print(flower_press['title'])
                             if flower_press['class']:
                                 for theclass, thearguments in flower_press.items():
                                     for argument in thearguments:
                                         if argument == "kitchen":
                                             HasClass().kitchen()
                                         elif argument == "portable":
                                             HasClass().portable()
                             stats("flower_press")
                             exit()
                     elif q4portable_2_hand_1_2_1 == "2":
                         write("wax_seal")
                         print()
                         print(wax_seal["description"])
                         print()
                         print(wax_seal['url'])
                         print(wax_seal['title'])
                         if wax_seal['class']:
                             for theclass, thearguments in wax_seal.items():
                                 for argument in thearguments:
                                     if argument == "kitchen":
                                         HasClass().kitchen()
                                     elif argument == "portable":
                                         HasClass().portable()
                         stats("wax_seal")
                         exit()




        q4portable_2_garland = input("Do you want to make something to decorate a room?\n1: YES, 2: NO\n")
        if q4portable_2_garland == "1":
            write("garland")
            print()
            print(garland["description"])
            print()
            print(garland['url'])
            print(garland['title'])
            if garland['class']:
                for theclass, thearguments in garland.items():
                    for argument in thearguments:
                        if argument == "kitchen":
                            HasClass().kitchen()
                        elif argument == "portable":
                            HasClass().portable()
            stats("garland")
            exit()


        q4portable_2_jewelry = input("Do you want to make jewelry?\n1: YES, 2: NO\n")
        if q4portable_2_jewelry == "1":
            q4portable_2_jewelry_1 = input("Do you want to work with metal and a cabochon or beads?\n1: CABOCHON, 2: BEADS\n")
            if q4portable_2_jewelry_1 == "1":
                write("wire_wrap")
                print()
                print(wire_wrap["description"])
                print()
                print(wire_wrap['url'])
                print(wire_wrap['title'])
                if wire_wrap['class']:
                    for theclass, thearguments in wire_wrap.items():
                        for argument in thearguments:
                            if argument == "kitchen":
                                HasClass().kitchen()
                            elif argument == "portable":
                                HasClass().portable()
                stats("wire_wrap")
                exit()
            elif q4portable_2_jewelry_1 == "2":
                write("bracelet")
                print()
                print(bracelet["description"])
                print()
                print(bracelet['url'])
                print(bracelet['title'])
                if bracelet['class']:
                    for theclass, thearguments in bracelet.items():
                        for argument in thearguments:
                            if argument == "kitchen":
                                HasClass().kitchen()
                            elif argument == "portable":
                                HasClass().portable()
                stats("bracelet")
                exit()



        q4portable_2_practical = input("Do you want to make something practical?\n1: YES, 2: NO\n")
        if q4portable_2_practical == "1":
            q4portable_2_practical_1 = input("Do you need a basket, candles, or soap?\n1: BASKET, 2: CANDLES, 3: SOAP\n")
            if q4portable_2_practical_1 == "1":
                write("basket_weaving")
                print()
                print(basket_weaving["description"])
                print()
                print(basket_weaving['url'])
                print(basket_weaving['title'])
                if basket_weaving['class']:
                    for theclass, thearguments in basket_weaving.items():
                        for argument in thearguments:
                            if argument == "kitchen":
                                HasClass().kitchen()
                            elif argument == "portable":
                                HasClass().portable()
                stats("basket_weaving")
                exit()
            elif q4portable_2_practical_1 == "2":
                write("candle_making")
                print()
                print(candle_making["description"])
                print()
                print(candle_making['url'])
                print(candle_making['title'])
                if candle_making['class']:
                    for theclass, thearguments in candle_making.items():
                        for argument in thearguments:
                            if argument == "kitchen":
                                HasClass().kitchen()
                            elif argument == "portable":
                                HasClass().portable()
                stats("candle_making")
                exit()
            elif q4portable_2_practical_1 == "3":
                write("soap_making")
                print()
                print(soap_making["description"])
                print()
                print(soap_making['url'])
                print(soap_making['title'])
                if soap_making['class']:
                    for theclass, thearguments in soap_making.items():
                        for argument in thearguments:
                            if argument == "kitchen":
                                HasClass().kitchen()
                            elif argument == "portable":
                                HasClass().portable()
                stats("soap_making")
                exit()



        q4portable_2_edible = input("Do you want to make something edible?\n1: YES, 2: NO\n")
        if q4portable_2_edible == "1":
            q4portable_2_edible_1 = input("Is this for the holidays?\n1: YES, 2: NO\n")
            if q4portable_2_edible_1 == "1":
                write("scandinavian_baking")
                print()
                print(scandinavian_baking["description"])
                print()
                print(scandinavian_baking['url'])
                print(scandinavian_baking['title'])
                if scandinavian_baking['class']:
                    for theclass, thearguments in scandinavian_baking.items():
                        for argument in thearguments:
                            if argument == "kitchen":
                                HasClass().kitchen()
                            elif argument == "portable":
                                HasClass().portable()
                stats("scandinavian_baking")
                exit()
            elif q4portable_2_edible_1 == "2":
                q4portable_2_edible_1_2 = input("Chocolate or cookies?\n1: CHOCOLATE, 2: COOKIES\n")
                if q4portable_2_edible_1_2 == "1":
                    write("chocolate")
                    print()
                    print(chocolate["description"])
                    print()
                    print(chocolate['url'])
                    print(chocolate['title'])
                    if chocolate['class']:
                        for theclass, thearguments in chocolate.items():
                            for argument in thearguments:
                                if argument == "kitchen":
                                    HasClass().kitchen()
                                elif argument == "portable":
                                    HasClass().portable()
                    stats("chocolate")
                    exit()
                elif q4portable_2_edible_1_2 == "2":
                    write("macaron")
                    print()
                    print(macaron["description"])
                    print()
                    print(macaron['url'])
                    print(macaron['title'])
                    if macaron['class']:
                        for theclass, thearguments in macaron.items():
                            for argument in thearguments:
                                if argument == "kitchen":
                                    HasClass().kitchen()
                                elif argument == "portable":
                                    HasClass().portable()
                    stats("macaron")
                    exit()


        q4portable_2_new = input("Do you want something New Age?\n1: YES, 2: NO\n")
        if q4portable_2_new == "1":
            q4portable_2_new_1 = input("Enter 1 for dream catcher, 2 for witchcraft.\n")
            write("dream_catcher")
            if q4portable_2_new_1 == "1":
                print()
                print(dream_catcher["description"])
                print()
                print(dream_catcher['url'])
                print(dream_catcher['title'])
                if dream_catcher['class']:
                    for theclass, thearguments in dream_catcher.items():
                        for argument in thearguments:
                            if argument == "kitchen":
                                HasClass().kitchen()
                            elif argument == "portable":
                                HasClass().portable()
                stats("dream_catcher")
                exit()
            elif q4portable_2_new_1 == "2":
                write("witchcraft")
                print()
                print(witchcraft["description"])
                print()
                print(witchcraft['url'])
                print(witchcraft['title'])
                if witchcraft['class']:
                    for theclass, thearguments in witchcraft.items():
                        for argument in thearguments:
                            if argument == "kitchen":
                                HasClass().kitchen()
                            elif argument == "portable":
                                HasClass().portable()
                stats("witchcraft")
                exit()


        q4portable_2_painting = input("What about painting?\n1: YES, 2: NO\n")
        if q4portable_2_painting == "1":
            write("painting")
            print()
            print(painting["description"])
            print()
            print(painting['url'])
            print(painting['title'])
            if painting['class']:
                for theclass, thearguments in painting.items():
                    for argument in thearguments:
                        if argument == "kitchen":
                            HasClass().kitchen()
                        elif argument == "portable":
                            HasClass().portable()
            stats("painting")
            exit()
        else:
            print("Sorry, we don't have any other craft ideas for you!")
            exit()