from app.lib import create_apartment, search_apartment, add_apartment, search_price


def test_create_apartment():
    data = {
        'rooms': 1,
        'square': 25,
        'price': 4_444_000,
        'district': 'Советский'
    }

    result = {'rooms': 1, 'square': 25, 'price': 4_444_000, 'district': 'Советский'}
    assert result == data


def test_add_apartment():
    container = []
    apartment = create_apartment(2, 22, 1_000_000, 'Московский')
    add_apartment(container, apartment)

    assert len(container) == 1
    assert apartment in container

def test_search_apartment():
    apartments = []
    one_room = create_apartment(1, 23, 1_500_000, 'Ново-Савиноский')
    three_rooms = create_apartment(3, 90, 4_400_000, 'Московский')
    two_rooms = create_apartment(2, 20, 2_700_000, 'Советский')

    add_apartment(apartments, one_room)
    add_apartment(apartments, three_rooms)
    add_apartment(apartments, two_rooms)

    founded_apartment = [{'rooms': 2, 'square': 20, 'price': 2700000, 'district': 'Советский'}]
    result = search_apartment(apartments, 'Советский')
    assert founded_apartment == result

def test_search_price():
    apartments = []

    one_room = create_apartment(1, 23, 1_500_000, 'Ново-Савиноский')
    three_rooms = create_apartment(3, 90, 4_400_000, 'Московский')
    two_rooms = create_apartment(2, 20, 2_700_000, 'Советский')

    add_apartment(apartments, one_room)
    add_apartment(apartments, three_rooms)
    add_apartment(apartments, two_rooms)
    founded_apartments = [{'rooms': 1, 'square': 23, 'price': 1500000, 'district': 'Ново-Савиноский'}]
    result = search_price(apartments, 1_500_000)

    assert founded_apartments == result
