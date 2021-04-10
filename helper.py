from carMarket import db
from carMarket.models import Item
from csv import reader

with open('MOCK_DATA.csv', 'r') as csv_file:
    csv_file_cursor = reader(csv_file)
    header = next(csv_file_cursor)
    print(header)
    db.create_all()
    for row in csv_file_cursor:
        item = Item(first_name=row[0], last_name=row[1],
                    email=row[2], gender=row[3], ip_address=row[4])
        db.session.add(item)
    db.session.commit()
