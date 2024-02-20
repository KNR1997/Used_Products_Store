from django.db.models import F
from django.shortcuts import get_object_or_404
from ..models import Product, Review

def update_product_rating(product_id, rating):
    try:
        # Use get() instead of get_object_or_404 for more flexibility
        product = Product.objects.get(id=product_id)

        # Fetch the current value of reviews from the database
        current_reviews = product.reviews

        # Use F expression to handle concurrency issues
        product.reviews = F('reviews') + 1

        if current_reviews == 0:
            # If it's the first review, set the initial rating
            product.rating = rating
        else:
            # Calculate the updated rating
            product.rating = (F('rating') + rating) / (F('reviews') + 1)

        # Save the changes atomically
        product.save()

    except Product.DoesNotExist:
        # Handle the case where the product does not exist
        print(f"Product with id={product_id} does not exist.")

    except Exception as e:
        # Handle other exceptions as needed
        print(f"Error updating product rating: {e}")