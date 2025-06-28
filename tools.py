from langchain.tools import tool
from langchain_community.tools import Tool
from langchain_tavily import TavilySearch
from typing import Optional, Any, cast
from sympy import *
import requests
from settings import settings

@tool
def weather_tool(city: str) -> str:
    """
        Tool Name: weather

        Description:
        Fetches the current weather information for a given city using a weather API (e.g., OpenWeatherMap).

        Input:
            - city (str): The name of the city to retrieve weather data for. Can also include country code (e.g., "London,UK").

        Output:
            - A string describing the current weather conditions, temperature, humidity, and wind speed in the given city.
    """

    api_key = settings.OPEN_WEATHER_API_KEY
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200:
        return f"خطا: {data.get('message', 'مشکلی پیش آمد')}"
    return f"{data['weather'][0]['description']}، دما: {data['main']['temp']} درجه"

@tool
def derivative_tool(expression: str, variable: str = "x") -> str:
    """
    Calculates the derivative of the given expression with respect to the variable.

    Args:
        expression (str): Mathematical expression, e.g. "x**2 + 3*x".
        variable (str, optional): Variable to differentiate by. Defaults to "x".

    Returns:
        str: The derivative as a string.
    """
    try:
        x = symbols(variable)
        expr = sympify(expression)
        deriv = diff(expr, x)
        return str(deriv)
    except Exception as e:
        return f"Error calculating derivative: {e}"

@tool
def integral_tool(expression: str, variable: str = "x") -> str:
    """
    Calculates the integral of the given expression with respect to the variable.

    Args:
        expression (str): Mathematical expression, e.g. "x**2 + 3*x".
        variable (str, optional): Variable to integrate by. Defaults to "x".

    Returns:
        str: The integral as a string.
    """
    try:
        x = symbols(variable)
        expr = sympify(expression)
        integral = integrate(expr, x)
        return str(integral)
    except Exception as e:
        return f"Error calculating integral: {e}"

@tool
def solve_equation_tool(equation: str, variable: str = "x") -> str:
    """
    Solves the equation for the given variable.

    Args:
        equation (str): Equation as a string, e.g. "x**2 - 4 = 0".
        variable (str, optional): Variable to solve for. Defaults to "x".

    Returns:
        str: List of solutions as string.
    """
    try:
        x = symbols(variable)
        left, right = equation.split("=")
        eq = Eq(sympify(left), sympify(right))
        solutions = solve(eq, x)
        return str(solutions)
    except Exception as e:
        return f"Error solving equation: {e}"

@tool
def calculator_tool(expression: str) -> str:
    """
    Evaluates a mathematical expression.

    Args:
        expression (str): Expression to evaluate, e.g. "2 + 3*4".

    Returns:
        str: Result of evaluation.
    """
    try:
        expr = sympify(expression)
        return str(expr.evalf())
    except Exception as e:
        return f"Error evaluating expression: {e}"

from langchain.tools import tool

@tool
def store_file_tool(text: str, filename: str = "memory_store.txt") -> str:
    """
    Stores a key-value pair as a new line in a file in the format: key:value

    Args:
        text (str): The value to store.
        filename (str, optional): File name to store data. Defaults to "memory_store.txt".

    Returns:
        str: Confirmation message.
    """
    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"{text}\n")
        return f"Data stored in file '{filename}'."
    except Exception as e:
        return f"Error storing data: {e}"

@tool
def read_file_tool(filename: str = "memory_store.txt") -> str:
    """
    Reads the entire content of a text file and returns it as a string.

    Args:
        filename (str): The name of the file to read. Defaults to "memory_store.txt".

    Returns:
        str: The content of the file, or an error message if it can't be read.
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        return content if content else "(File is empty)"
    except Exception as e:
        return f"Error reading file: {e}"

@tool
def tavily_search_tool(query: str) -> Optional[dict[str, Any]]:
    """Search for general web results using Tavily.
        Args:
            query (str): the text that you wanna search the web about it.
        Returns:
            Optional[Dict[str, Any]]: The search results dictionary or None if error occurs.
        
    """
    try:
        wrapped = TavilySearch(max_results=settings.MAX_SEARCH_RESULTS)
        result = wrapped.invoke({"query": query})

    except Exception as e:
        print(e)
        

    return cast(dict[str, Any], result)



def get_tools():    
    __tools_list = [
        tavily_search_tool,        
        weather_tool,            
        derivative_tool,         
        integral_tool,           
        solve_equation_tool,     
        calculator_tool,
        read_file_tool,
        store_file_tool   
    ]
    
    return __tools_list