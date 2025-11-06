import pandas as pd

products_df = pd.read_csv("products.csv")

def search_products(query: str):
    """Simple keyword-based product search."""
    query = query.lower()
    results = products_df[
        products_df.apply(
            lambda row: query in row["name"].lower()
            or query in row["category"].lower()
            or query in row["brand"].lower()
            or query in row["description"].lower()
            or query in row["features"].lower(),
            axis=1
        )
    ]
    return results.to_dict(orient="records")
