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

def good(mov):
    if mov["imdb"]>5.5:
        return True
    else:
        return False
    
def lgood(mov):
    lst = []
    for i in range(0, len(movies)):
        if mov[i]["imdb"]>5.5:
            lst.append(mov[i]["name"])
    return lst
def category(s):
    lst =[]
    for i in range(0, len(movies)):
        if movies[i]["category"] == s:
            lst.append(movies[i]["name"])
    return lst
def average(mov):
    cnt = 0
    for i in range(0, len(mov)):
        cnt += mov[i]["imdb"]
    return cnt/len(mov)
def avr(cat):
    cnt = 0
    kolvo = 0
    for i in range(0, len(movies)):
        if movies[i]["category"]==cat:
            cnt += movies[i]["imdb"]
            kolvo += 1
    return cnt/kolvo
        
    
print(good(movies[3]))
print(lgood(movies))
print(category("Romance"))
print(average(movies))
print(avr("Romance"))