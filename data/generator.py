from data.data import Food, NewUser
from faker import Faker

faker_en = Faker('En')
Faker.seed()


def generated_new_user():
    yield NewUser(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        email=faker_en.email(),
        comments=faker_en.text(),
    )


def generated_food():
    yield Food(
        food_name=["Asparagus", "Avacado", "Almond", "Artichoke", "Apple", "Bruscetta", "Bacon", "Black beans",
                   "Bagels", "Barley", "Cabbage", "Carrots", "Celery", "Chicken", "Catfish", "Chips", "Coffee",
                   "Cookies", "Dates", "Dips", "Duck", "Donuts", "Eggs", "Fondu", "French toast", "French dip",
                   "Garlic", "Ginger", "Granola", "Grapes", "Green beans", "Honey", "Ham", "Hash browns", "Hummus",
                   "Ice cream", "Irish stew", "Italian bread", "Jerky", "Kale", "Kiwi", "Kidney beans", "Kingfish",
                   "Lobster", "Lamb", "Linguine", "Lasagna", "Meatballs", "Milk", "Milkshake", "Noodles", "Pizza",
                   "Pepperoni", "Pancakes", "Quiche", "Reuben", "Spinach", "Spaghetti", "Toast", "Venison", "Waffles",
                   "Wine", "Walnuts", "Yogurt", "Zucchini"]
    )
