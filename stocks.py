def stock_purchases():
    amazon = 3000
    apple = 100
    fb = 250
    google = 1400
    msft = 200

    # Given the prices above and a client's investment budget, how much stock can they buy?
    # 1.1 TODO: Ask the client's name (use the string: "What is your name? ") and save it into a variable
    user_input_dic = {
        'client_name': input("What is your name? "),
        'investment': int(input("How much would you like to invest? $")),
        'stock': input(
            "\nWhich stock are you interested in? Enter the corresponding number:\n1. Amazon\n2. Apple\n3. Facebook\n4. Google\n5. Microsoft\nNumber: "
        )
    }
    # YOU KNOW I WAS EXTREMELY SKEPTICAL THIS WAS GOING TO WORK AS EXPECTED BUT IT DOES SO HURRAY ME!!

    # client_name = input("What is your name? ")
    # # 1.2 TODO: Ask the client how many dollars they would like to invest (use the string: "How much would you like to invest? $")
    # # and save it into a variable
    # invtmnt = int(input("How much would you like to invest? $"))
    # # NOTE: When you use the `input` function to get user input, what do numbers get saved as? strings
    # # ANSWER: strings
    # # 1.3 TODO: Uncomment the line below to ask the client which stock they're interested in.
    # # NOTE: Take a look at how this input string prints out
    # stock = input(
    #     "\nWhich stock are you interested in? Enter the corresponding number:\n1. Amazon\n2. Apple\n3. Facebook\n4. Google\n5. Microsoft\nNumber: "
    # )
    affordable = 0
    service = ""
    currentPrice = ""

    if user_input_dic['stock'] == "1":
        service = "Amazon"
        currentPrice = f"${amazon}"
        affordable = int(user_input_dic['investment'] / amazon)
    elif user_input_dic['stock'] == "2":
        service = "Apple"
        currentPrice = f"${apple}"
        affordable = int(user_input_dic['investment'] / apple)
    elif user_input_dic['stock'] == "3":
        service = "Facebook"
        currentPrice = f"${fb}"
        affordable = int(user_input_dic['investment'] / fb)
    elif user_input_dic['stock'] == "4":
        service = "Google"
        currentPrice = f"${google}"
        affordable = int(user_input_dic['investment'] / google)
    elif user_input_dic['stock'] == "5":
        service = "Microsoft"
        currentPrice = f"${msft}"
        affordable = int(user_input_dic['investment'] / msft)

        print(service)
        print(affordable)
        print(currentPrice)
    else:
        service = ""
        currentPrice = ""
        affordable = 0

    print(
        f"{user_input_dic['client_name']} has ${user_input_dic['investment']} to invest and can buy {affordable} shares of {service} at the current price of {currentPrice}."
    )


# stock_purchases()
