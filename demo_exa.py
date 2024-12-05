from tools.exa_tool import exa_search, exa_content, exa_find_similar_links
import json
from pprint import pprint

def demo_exa_search():
    print("\n=== Demonstrating exa_search ===")
    # Search for articles about earned wage access and its impact on low-income workers
    results = exa_search(
        query="how earned wage access helps low income workers financial wellbeing",
        num_results=3,
        include_domains=["forbes.com", "cnbc.com", "bloomberg.com"]
    )
    
    print("Search Results:")
    for result in results.get('results', []):
        print(f"\nTitle: {result.get('title', 'No title')}")
        print(f"URL: {result.get('url', 'No URL')}")
        summary = result.get('summary', {})
        if isinstance(summary, dict):
            print(f"Summary: {summary.get('text', 'No summary available')}")
        else:
            print(f"Summary: {summary}")
        print("-" * 80)

def demo_exa_content():
    print("\n=== Demonstrating exa_content ===")
    # First get some IDs from a search
    search_results = exa_search(
        query="earned wage access benefits for low income workers",
        num_results=2
    )
    
    # Extract IDs from the search results
    ids = [result.get('id') for result in search_results.get('results', [])]
    
    if ids:
        # Get detailed content for these IDs
        content_results = exa_content(
            ids=ids,
            query="financial benefits",
            max_characters=500,
            highlight_sentences=2
        )
        
        print("Content Details:")
        for result in content_results.get('results', []):
            print(f"\nTitle: {result.get('title', 'No title')}")
            print(f"URL: {result.get('url', 'No URL')}")
            highlights = result.get('highlights', [])
            if highlights:
                print("Highlights:")
                for highlight in highlights:
                    if isinstance(highlight, dict):
                        print(f"- {highlight.get('text', 'No highlight text')}")
                    else:
                        print(f"- {highlight}")
            print("-" * 80)
    else:
        print("No IDs found in search results")

def demo_find_similar_links():
    print("\n=== Demonstrating exa_find_similar_links ===")
    # Use a relevant article about earned wage access as our starting point
    initial_results = exa_search(
        query="earned wage access platform benefits",
        num_results=1
    )
    
    results = initial_results.get('results', [])
    if results and results[0].get('url'):
        url = results[0]['url']
        print(f"Finding similar articles to: {url}")
        
        similar_results = exa_find_similar_links(
            url=url,
            num_results=3,
            highlight_query="financial wellness impact"
        )
        
        print("\nSimilar Articles:")
        for result in similar_results.get('results', []):
            print(f"\nTitle: {result.get('title', 'No title')}")
            print(f"URL: {result.get('url', 'No URL')}")
            highlights = result.get('highlights', [])
            if highlights:
                print("Relevant Highlights:")
                for highlight in highlights:
                    if isinstance(highlight, dict):
                        print(f"- {highlight.get('text', 'No highlight text')}")
                    else:
                        print(f"- {highlight}")
            print("-" * 80)
    else:
        print("No initial article found to find similar links")

if __name__ == "__main__":
    # Run all demonstrations
    demo_exa_search()
    demo_exa_content()
    demo_find_similar_links()
