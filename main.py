from agents.router import route
from utils.logger import log

def main():
    print("Agentic AI Starter (tape 'exit' pour quitter)\n")
    
    while True:
        user_input = input(">> ")
        
        if user_input.lower() == "exit":
            break
        
        log(f"USER: {user_input}")
        
        response = route(user_input)
        
        log(f"AI: {response}")
        
        print(response)

if __name__ == "__main__":
    main()