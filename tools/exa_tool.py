import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def exa_search(
    query,
    num_results=10,
    include_domains=None,
    exclude_domains=None,
    start_crawl_date=None,
    end_crawl_date=None,
    start_published_date=None,
    end_published_date=None,
    include_text=None,
    exclude_text=None,
):
    """
    Perform a search using the Exa API.

    Args:
        query (str): The search query
        num_results (int, optional): Number of results to return. Defaults to 10.
        include_domains (list, optional): List of domains to include in search
        exclude_domains (list, optional): List of domains to exclude from search
        start_crawl_date (str, optional): Start date for crawl in ISO format
        end_crawl_date (str, optional): End date for crawl in ISO format
        start_published_date (str, optional): Start date for publication in ISO format
        end_published_date (str, optional): End date for publication in ISO format
        include_text (list, optional): List of text strings that must be included
        exclude_text (list, optional): List of text strings that must be excluded

    Returns:
        dict: The API response
    """
    url = "https://api.exa.ai/search"

    payload = {
        "query": query,
        "useAutoprompt": True,
        "numResults": num_results,
        "contents": {
            "text": {"maxCharacters": 1000, "includeHtmlTags": True},
            "highlights": {"numSentences": 3, "highlightsPerUrl": 3, "query": query},
            "summary": {"query": query},
        },
    }

    # Add optional parameters if provided
    if include_domains:
        payload["includeDomains"] = include_domains
    if exclude_domains:
        payload["excludeDomains"] = exclude_domains
    if start_crawl_date:
        payload["startCrawlDate"] = start_crawl_date
    if end_crawl_date:
        payload["endCrawlDate"] = end_crawl_date
    if start_published_date:
        payload["startPublishedDate"] = start_published_date
    if end_published_date:
        payload["endPublishedDate"] = end_published_date
    if include_text:
        payload["includeText"] = include_text
    if exclude_text:
        payload["excludeText"] = exclude_text

    # Get API key from environment variable
    api_key = os.getenv("EXA_API_KEY")
    if not api_key:
        raise ValueError("EXA_API_KEY environment variable is not set")

    headers = {"x-api-key": api_key, "Content-Type": "application/json"}

    response = requests.request("POST", url, json=payload, headers=headers)
    return response.json()


def exa_content(
    ids,
    query=None,
    max_characters=1000,
    include_html_tags=True,
    highlight_sentences=3,
    highlights_per_url=3,
):
    """
    Retrieve content details for specific IDs from the Exa API.

    Args:
        ids (list): List of content IDs to retrieve
        query (str, optional): Query for highlights and summary
        max_characters (int, optional): Maximum characters to return in text. Defaults to 1000
        include_html_tags (bool, optional): Whether to include HTML tags in text. Defaults to True
        highlight_sentences (int, optional): Number of sentences to highlight. Defaults to 3
        highlights_per_url (int, optional): Number of highlights per URL. Defaults to 3

    Returns:
        dict: The API response containing content details
    """
    url = "https://api.exa.ai/contents"

    payload = {
        "ids": ids,
        "text": {"maxCharacters": max_characters, "includeHtmlTags": include_html_tags},
    }

    # Add highlights and summary if query is provided
    if query:
        payload["highlights"] = {
            "numSentences": highlight_sentences,
            "highlightsPerUrl": highlights_per_url,
            "query": query,
        }
        payload["summary"] = {"query": query}

    # Get API key from environment variable
    api_key = os.getenv("EXA_API_KEY")
    if not api_key:
        raise ValueError("EXA_API_KEY environment variable is not set")

    headers = {"x-api-key": api_key, "Content-Type": "application/json"}

    response = requests.request("POST", url, json=payload, headers=headers)
    return response.json()


def exa_find_similar_links(
    url,
    num_results=10,
    include_domains=None,
    exclude_domains=None,
    start_crawl_date=None,
    end_crawl_date=None,
    start_published_date=None,
    end_published_date=None,
    include_text=None,
    exclude_text=None,
    max_characters=1000,
    include_html_tags=True,
    highlight_sentences=3,
    highlights_per_url=3,
    highlight_query=None,
):
    """
    Find similar links to a given URL using the Exa API.

    Args:
        url (str): The URL to find similar content for
        num_results (int, optional): Number of results to return. Defaults to 10
        include_domains (list, optional): List of domains to include in search
        exclude_domains (list, optional): List of domains to exclude from search
        start_crawl_date (str, optional): Start date for crawl in ISO format
        end_crawl_date (str, optional): End date for crawl in ISO format
        start_published_date (str, optional): Start date for publication in ISO format
        end_published_date (str, optional): End date for publication in ISO format
        include_text (list, optional): List of text strings that must be included
        exclude_text (list, optional): List of text strings that must be excluded
        max_characters (int, optional): Maximum characters to return in text. Defaults to 1000
        include_html_tags (bool, optional): Whether to include HTML tags in text. Defaults to True
        highlight_sentences (int, optional): Number of sentences to highlight. Defaults to 3
        highlights_per_url (int, optional): Number of highlights per URL. Defaults to 3
        highlight_query (str, optional): Query for generating highlights

    Returns:
        dict: The API response containing similar links
    """
    url_endpoint = "https://api.exa.ai/findSimilar"

    payload = {
        "url": url,
        "numResults": num_results,
        "contents": {
            "text": {
                "maxCharacters": max_characters,
                "includeHtmlTags": include_html_tags,
            },
        },
    }

    # Add optional parameters if provided
    if include_domains:
        payload["includeDomains"] = include_domains
    if exclude_domains:
        payload["excludeDomains"] = exclude_domains
    if start_crawl_date:
        payload["startCrawlDate"] = start_crawl_date
    if end_crawl_date:
        payload["endCrawlDate"] = end_crawl_date
    if start_published_date:
        payload["startPublishedDate"] = start_published_date
    if end_published_date:
        payload["endPublishedDate"] = end_published_date
    if include_text:
        payload["includeText"] = include_text
    if exclude_text:
        payload["excludeText"] = exclude_text

    # Add highlights and summary if highlight_query is provided
    if highlight_query:
        payload["contents"]["highlights"] = {
            "numSentences": highlight_sentences,
            "highlightsPerUrl": highlights_per_url,
            "query": highlight_query,
        }
        payload["contents"]["summary"] = {"query": highlight_query}

    # Get API key from environment variable
    api_key = os.getenv("EXA_API_KEY")
    if not api_key:
        raise ValueError("EXA_API_KEY environment variable is not set")

    headers = {"x-api-key": api_key, "Content-Type": "application/json"}

    response = requests.request("POST", url_endpoint, json=payload, headers=headers)
    return response.json()
