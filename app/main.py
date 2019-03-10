from app.lib import create_apartment, add_apartment, search_apartment

apartments = []

one_room = create_apartment(1, 23, '1_500_000', 'Ново-Савиноский')
three_rooms = create_apartment(3, 90, '4_400_000', 'Московский')
two_rooms = create_apartment(2, 20, '2_700_000', 'Советский')

print(add_apartment(apartments, one_room))
print(add_apartment(apartments, two_rooms))
print(add_apartment(apartments, three_rooms))



print(search_apartment(apartments, 'советский'))
print(search_apartment(apartments, 'московск'))
print(search_apartment(apartments, '4_500_000'))


