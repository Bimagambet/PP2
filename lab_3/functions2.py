movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def over5(movie):
    return movie["imdb"] > 5.5

print(over5(movies[1]))


def allover5():
    names = []
    for i in movies:
        if i["imdb"] > 5.5:
            names.append(i["name"])
    return names

print(allover5())


def categorys(tip):
    names = []
    for i in movies:
        if i["category"] == tip:
            names.append(i["name"])
    return names

x = input("jaz")
print(categorys(x))

def avg_imdb():
    avg = 0
    for i in movies:
        avg += i["imdb"]
    return avg / len(movies)

print(avg_imdb())

def avg_category(tip):
    avg = 0
    lenght = 0
    for i in movies:
        if i["category"] == tip:
            avg += i["imdb"]
            lenght += 1
    return avg / lenght

print(avg_category(x))
            