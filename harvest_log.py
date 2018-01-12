from harvest import make_melon_types, make_melon_type_lookup, Melon

input_file = 'harvest_log.txt'


def harvest_log(input_file):
    """Opens and cleans harvest log"""

    melon_types = make_melon_types()
    melons_by_id = make_melon_type_lookup(melon_types)

    melons = []

    with open(input_file) as f:
        for line in f:
            line = line.rstrip()
            melon_attributes = line.split()

            shape_rating = melon_attributes[1]
            color_rating = melon_attributes[3]
            melon_type = melon_attributes[5]
            harvester = melon_attributes[8]
            field = melon_attributes[-1]

            melon = Melon(melons_by_id[melon_type], shape_rating, color_rating,
                          field, harvester)
            melons.append(melon)

    return melons
