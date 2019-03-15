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
            continue

        if search_lowercased in apartment > ['price']:
            result.append(apartment)

    return result