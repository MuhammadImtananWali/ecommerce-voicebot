from livekit.agents import function_tool
from .services.product_search import search_products

@function_tool
async def find_product(query: str) -> list:
    """Searches for products by name, category, or description."""
    results = search_products(query)
    if not results:
        return [{"message": f"No products found for '{query}'."}]
    return results