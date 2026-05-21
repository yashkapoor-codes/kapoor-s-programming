print ("🤖chatbot :  type Hello! to start  type 'bye' to exit ." )

while True : 
    user =input ("you :"). lower()

    if user == "hello":
        print ("🤖chatbot : hi there! ")
    elif user== " how are you ":
        print ("🤖chatbot : im good ! how about you ?")
    elif user == "your name ":
        print ("🤖chatbot : i am python  chatbot !")
    elif user == "bye":
        print ("🤖chatbot : goodbye ! have a nice day !")
        break
    else: 
        print ("🤖chatbot : sorry i didnt understand that .")