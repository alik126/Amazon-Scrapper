
class Product:
    def __init__(self, title, rating, rating_count, price, image_url, updated_time):
        self.title = title
        self.rating = rating
        self.rating_count = rating_count
        self.price = price
        self.image_url = image_url
        self.updated_time = updated_time

    def __repr__(self):
        return f"Product(title='{self.title}', rating='{self.rating}', rating_count='{self.rating_count}', " \
               f"price='{self.price}', image_url='{self.image_url}', updated_time='{self.updated_time}')"
