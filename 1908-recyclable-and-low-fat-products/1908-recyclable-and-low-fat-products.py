import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    filtered = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    df = pd.DataFrame(filtered['product_id'])
    return df