import aiml
kernel = aiml.Kernel()
kernel.learn("C:/Users/kamle/OneDrive/Desktop/aai/prac1/std-startup.xml")
kernel.learn("C:/Users/kamle/OneDrive/Desktop/aai/prac1/basic_chat.aiml")
kernel.respond("LOAD")
# Press CTRL-C to break this loop
while True:
    print( kernel.respond(input("Enter your message >> ")))
