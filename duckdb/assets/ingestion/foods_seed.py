import pandas as pd


def main():
    data = [
        {
            "food_id": 1,
            "food_name": "Oats",
            "category": "Grains",
            "nutrient": "Iron",
            "value_per_100g": 4.3,
        },
        {
            "food_id": 2,
            "food_name": "Spinach",
            "category": "Vegetables",
            "nutrient": "Iron",
            "value_per_100g": 2.7,
        },
        {
            "food_id": 3,
            "food_name": "Salmon",
            "category": "Fish",
            "nutrient": "Protein",
            "value_per_100g": 20.4,
        },
        {
            "food_id": 4,
            "food_name": "Greek Yogurt",
            "category": "Dairy",
            "nutrient": "Calcium",
            "value_per_100g": 110.0,
        },
        {
            "food_id": 5,
            "food_name": "Lentils",
            "category": "Legumes",
            "nutrient": "Protein",
            "value_per_100g": 9.0,
        },
    ]

    return pd.DataFrame(data)


if __name__ == "__main__":
    print(main().head())