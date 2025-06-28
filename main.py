from graph import graph
from langchain_core.messages import HumanMessage




def main():
    while(True):
        user_input = input("Enter: ")
        if(user_input == "quit"):
            break
        result = graph.invoke({"messages":HumanMessage(content=user_input)})
        

        conversation_history = result["messages"]
        for m in result['messages']:
            print(m.pretty_print())



if __name__ == "__main__":
    main()
