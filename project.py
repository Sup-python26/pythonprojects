import requests
while True:
 name=input("Which pokemon do you want to find?")
 name=name.lower()
 url=f"https://pokeapi.co/api/v2/pokemon/{name}"
 req=requests.get(url)
 print(req.status_code)
 if req.status_code==200:
    jdict=req.json()
    print(f"Name is {jdict['name']}")
    print("Abilities:")
    for ability in jdict['abilities']:
      print(ability['ability']['name'])
 else:
   print("Pokemon not found")
