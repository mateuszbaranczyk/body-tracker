import requests

url = "https://frog01-20364.wykr.es/upload"

mail = ""
password = ""

print("Enter data:")

weight = float(input("Weight: "))
percentFat = input("Percent fat: ")
percentHydration = input("Percent hydration: ")
boneMass = input("Bone mass: ")
muscleMass = input("Muscle mass: ")
visceralFatRating = input("Visceral fat rating: ")
physiqueRating = input("Physique rating: ")
metabolicAge = input("Metabolic age: ")
bodyMassIndex = weight / 172**2

print(
    """
Sending...
    """
)

query = {
    "timeStamp": -1,
    "weight": str(weight),
    "percentFat": percentFat,
    "percentHydration": percentHydration,
    "boneMass": boneMass,
    "muscleMass": muscleMass,
    "visceralFatRating": visceralFatRating,
    "physiqueRating": physiqueRating,
    "metabolicAge": metabolicAge,
    "bodyMassIndex": str(round(bodyMassIndex * 10000, 1)),
    "email": mail,
    "password": password,
    "mfaCode": "",
    "clientId": "",
}

response = requests.post(url, json=query)

if response.status_code == 201:
    print("Data sent.")
else:
    print(response.content)
    print(response.status_code)