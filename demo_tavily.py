from tavily import TavilyClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def demo_tavily_search():
    print("\n=== Demonstrating tavily_search ===")

    # Initialize the Tavily client
    tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

    # Perform a search about earned wage access to match the example in demo_exa.py
    query = "how earned wage access helps low income workers financial wellbeing"
    response = tavily_client.search(query)

    print("Search Results:")
    if isinstance(response, dict) and "results" in response:
        for result in response["results"]:
            print(f"\nTitle: {result.get('title', 'No title')}")
            print(f"URL: {result.get('url', 'No URL')}")
            print(f"Content: {result.get('content', 'No content available')}")
            print("-" * 80)
    else:
        print("No results found or unexpected response format")


def demo_tavily_context():
    print("\n=== Demonstrating tavily_context ===")

    # Initialize the Tavily client
    tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

    # Get search context about earned wage access
    query = "What are the main benefits of earned wage access for workers?"
    context = tavily_client.get_search_context(query=query)

    print(f"Query: {query}")
    print("\nContext:")
    print(context)
    print("-" * 80)


def demo_tavily_qna():
    print("\n=== Demonstrating tavily_qna ===")

    # Initialize the Tavily client
    tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

    # Perform a Q&A search about earned wage access
    query = "What problems does earned wage access solve for workers?"
    answer = tavily_client.qna_search(query=query)

    print(f"Question: {query}")
    print("\nAnswer:")
    print(answer)
    print("-" * 80)


if __name__ == "__main__":
    # Run all demonstrations
    demo_tavily_search()
    demo_tavily_context()
    demo_tavily_qna()
