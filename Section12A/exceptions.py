import requests

# number = input("Enter a number: ")

#try:
#    print(int(number) * 2)
#except ValueError:
#    print("You did not enter a base 10 number! Try again.")
#except LookupError:
#    print("Lookup error? This should never happen...")

#print("Hello")

r = requests.post("http://text-processing.com/api/sentiment", data={'text': 'hello world'})

try:
    label = r.json()['label']
    print(label)
except JSONDecodeError:
    print("We could not decode the JSON reponse")
except KeyError:
    print("Key Error")
