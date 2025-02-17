def grocery(food):
    if food == 'tofu':
        print("Tofu is cheap and has few calories")
    elif food =='meat':
        print(f"Meat has the most calories")
    elif food =='salmon' or food=='white fish':
        print("Seafood is expensive but is healthy")
    else:
        print("Chicken has fewer calories than meat")
grocery("meat")
