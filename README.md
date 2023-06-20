# Product Recommender

This project is a web application that provides product recommendations based on various factors such as previous orders, frequently bought together, and similar products.

## Installation and Setup

To install and run this application, follow these steps:

1. Clone this repository to your local machine.
2. Install Docker and Docker Compose if you haven't already.
3. Run `docker-compose up` to spin up the project.
4. Run `docker-compose exec web python manage.py runscript populate_products` to populate the database with sample products.
5. Run `docker-compose exec web python manage.py runscript populate_orders` to populate the database with sample orders.

### System Requirements

- Docker
- Docker Compose

# API Documentation

## Note
#### Recommendations are precomputed every hour using Celery Beat scheduler. However, you can use this endpoint to trigger the population process manually if needed.

### Manually precompute recommendations

`POST /api/precompute-recommendations/`

### Get Product Recommendations API
Get recommendations for a product with the given ID.

`GET /api/products/<uuid:product_id>/recommendations/`

### Create Order API
Create an order with the given data.

`POST /api/orders/create/`

#### Request Body:
```
{
"product_id": "<uuid>",
"price": <decimal>,
"currency_code": <ENUM> ("INR", "GBP", "USD", "EUR"),
"quantity": <integer>,
"address": "<str>",
"payment_mode": <ENUM> ("CASH_ON_DELIVERY", "ONLINE")
}
```

### Detail Order API
Fetch Order details

`GET /api/orders/<uuid:order_id>/`


### Remove Product from Order API
Remove a product with the given ID from an order with the given ID.

`DELETE /api/orders/<uuid:order_id>/products/<uuid:product_id>/remove/`

### Add Product to Order API
Add a product to an order with the given ID.

`POST /api/orders/<uuid:order_id>/products/add/`

#### Request Body:
```
{
"product_id": "<uuid>",
"price": <decimal>,
"currency_code": <ENUM> ("INR", "GBP", "USD", "EUR")
"quantity": <integer>
}
```

## Additional improvements that can be made to enhance the product recommendations:

- User Location: Incorporate user location data to provide location-based product recommendations. This can be achieved by utilizing user IP address, GPS coordinates, or user-provided address information. By considering the user's location, the system can suggest products that are popular or relevant in their specific region.

- Age Group: Introduce age group information to tailor recommendations based on different demographic segments. By considering the age group of users, the system can suggest products that are more suitable for specific age ranges. This can be achieved by capturing user age during the registration process or by analyzing user behavior and preferences to estimate their age group.

- Product Ratings and Reviews: Utilize product ratings and reviews to influence the recommendations. By incorporating user feedback and sentiment analysis of reviews, the system can prioritize products with higher ratings and positive reviews. This can help users discover products that are well-received by other customers and align with their preferences.

- Personalized User Profiles: Implement personalized user profiles to capture individual preferences, such as preferred categories, brands, or price ranges. By allowing users to customize their profiles and indicating their preferences, the system can generate recommendations that align with their specific interests.
