import asyncio
from elasticsearch import AsyncElasticsearch
from elasticsearch.exceptions import NotFoundError, RequestError, ConnectionError

# Configure Elasticsearch client
es = AsyncElasticsearch(hosts=["http://localhost:9200"])


async def main():
    try:
        # Perform the search query
        resp = await es.search(
            index="webinars",
            body={
                "query": {
                    "match": {
                        "title": "Python"
                    }
                }
            }
        )
        # Print the search results
        print(resp)
    except NotFoundError:
        print("Index not found")
    except RequestError as e:
        print(f"Request error: {e}")
    except ConnectionError as e:
        print(f"Connection error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Close the Elasticsearch client connection
        await es.close()

# Run the async main function
if __name__ == "__main__":
    asyncio.run(main())
