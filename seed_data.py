"""
Seed script to populate the database with sample products
Run this after starting the backend for the first time
"""
import requests
import json

API_BASE_URL = "http://localhost:8000"

# Login as admin
login_response = requests.post(
    f"{API_BASE_URL}/auth/login",
    json={"email": "admin@timberpunk.com", "password": "admin123"}
)
token = login_response.json()["access_token"]
headers = {"Authorization": f"Bearer {token}"}

# Sample products
products = [
    {
        "name": "Rustic Oak Wall Art",
        "description": "Beautiful handcrafted wall art made from reclaimed oak. Each piece is unique with natural grain patterns and can be customized with your choice of engraving.",
        "short_description": "Handcrafted oak wall art with custom engraving",
        "price": 89.99,
        "category": "wall art",
        "image_url": "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?w=600",
        "options": '{"sizes": ["12x12", "16x16", "20x20"], "finishes": ["Natural", "Dark Walnut", "Honey Oak"]}'
    },
    {
        "name": "Walnut Coaster Set",
        "description": "Set of 4 premium walnut coasters with laser-engraved designs. Perfect for protecting your furniture while adding a touch of natural elegance to your home.",
        "short_description": "Set of 4 premium walnut coasters",
        "price": 34.99,
        "category": "coasters",
        "image_url": "https://images.unsplash.com/photo-1565193566173-7a0ee3dbe261?w=600",
        "options": '{"designs": ["Geometric", "Nature", "Abstract", "Custom"]}'
    },
    {
        "name": "Personalized Family Sign",
        "description": "Custom wooden family sign perfect for your entryway or living room. Made from solid maple with your family name beautifully engraved.",
        "short_description": "Custom family name sign in solid maple",
        "price": 124.99,
        "category": "signs",
        "image_url": "https://images.unsplash.com/photo-1599930113854-d6d7fd521f10?w=600",
        "options": '{"sizes": ["18x6", "24x8", "30x10"]}'
    },
    {
        "name": "Cutting Board - Maple",
        "description": "Professional-grade maple cutting board with juice groove. Food-safe finish. Can be personalized with custom engraving on the back.",
        "short_description": "Professional maple cutting board",
        "price": 64.99,
        "category": "gifts",
        "image_url": "https://images.unsplash.com/photo-1594317334584-b23c6a71c21b?w=600",
        "options": '{"sizes": ["Small (10x14)", "Medium (12x18)", "Large (14x20)"]}'
    },
    {
        "name": "Wooden Phone Stand",
        "description": "Sleek and modern phone stand made from cherry wood. Holds your device at the perfect angle for video calls or watching content. Compatible with all phone sizes.",
        "short_description": "Modern cherry wood phone stand",
        "price": 29.99,
        "category": "gifts",
        "image_url": "https://images.unsplash.com/photo-1581368135153-a506cf13b1e1?w=600",
        "options": '{"woods": ["Cherry", "Walnut", "Maple"]}'
    },
    {
        "name": "Mountain Scene Wall Art",
        "description": "Layered mountain landscape wall art with depth and dimension. Made from sustainably sourced wood with hand-painted details. A stunning centerpiece for any room.",
        "short_description": "Layered mountain landscape art",
        "price": 149.99,
        "category": "wall art",
        "image_url": "https://images.unsplash.com/photo-1505798577917-a65157d3320a?w=600",
        "options": '{"sizes": ["Small (16x12)", "Medium (24x18)", "Large (36x24)"]}'
    }
]

print("Creating sample products...")
for product in products:
    try:
        response = requests.post(
            f"{API_BASE_URL}/products",
            json=product,
            headers=headers
        )
        if response.status_code == 201:
            print(f"✓ Created: {product['name']}")
        else:
            print(f"✗ Failed to create {product['name']}: {response.status_code}")
    except Exception as e:
        print(f"✗ Error creating {product['name']}: {str(e)}")

print("\nSample data seeding complete!")
print(f"Created {len(products)} products")
print("\nYou can now view them at http://localhost:5173")
