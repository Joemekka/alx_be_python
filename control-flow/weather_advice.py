inputUser = input("What's the weather like today? (sunny/rainy/cold):")

if inputUser == 'sunny':
        print('Wear a t-shirt and sunglasses.')
elif inputUser == 'rainy':
        print("Don't forget your umbrella and a raincoat.")
elif inputUser == 'cold':
        print("Make sure to wear a warm coat and a scarf.")
else:
        print("Sorry, I don't have recommendations for this weather.")