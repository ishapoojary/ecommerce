import mysql.connector
connection = mysql.connector.connect(
host='localhost',
user='ecommerce_user',
password='EUNWOO@123#',
database='ecommerce')
cursor = connection.cursor()

cursor.execute("INSERT INTO products (name, description, price, image_url) VALUES('Journal','Papboo Journals Are Crafted To Perfection, Keeping Our Consumers Needs In Mind. Its Designed To Preserve Personal Records Or Simply Keeping Track Of Personal Thoughts At A Pocket Friendly Price, Without Compromising On The Quality. Papboo Knows That Every One Of You Is Unique And Thats Why We Offer A Wide Range Of Cover Art To Match Your Personality From Quirky To Cute,'224.00','/static/images/product6.webp')")