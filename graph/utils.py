from math import cos, asin, sqrt


def haversine(lat1, lon1, lat2, lon2):
    """
    Fórmula de Haversine
    """

    p = 0.017453292519943295  # Pi/180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * \
        cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    # return Decimal(12742) * Decimal(asin(sqrt(a))) #2*R*asin
    return 12742 * asin(sqrt(a))  # 2*R*asin
