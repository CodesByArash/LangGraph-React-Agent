from graph import graph
from langchain_core.messages import HumanMessage

# conversation_history = []

while(True):
    user_input = input("Enter: ")
    if(user_input == "quit"):
        break
    # conversation_history.append(HumanMessage(content=user_input))

    # result = graph.invoke({"messages": conversation_history})

    result = graph.invoke({"messages":HumanMessage(content=user_input)})
    
    print(result["messages"][-1].content)


    conversation_history = result["messages"]


def main():
    pass


if __name__ == "__main__":
    main()
