def create_apartment(rooms, square, price, district):
    return {
        'rooms': rooms,
        'square': square,
        'price': price,
        'district': district
    }


def add_apartment(container, apartment):
    container.append(apartment)


def search_apartment(container, search):
    search_lowercased = search.strip().lower()
    result = []

    for apartment in container:
        if search_lowercased in apartment['district'].lower():
            result.append(apartment)
    return result


def search_price(container, search):
    result = []
    for apartment in container:
        if search >= apartment['price']:
            result.append(apartment)
    return result
