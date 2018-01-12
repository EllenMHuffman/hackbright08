############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller,
                 name):
        """Initialize a melon type."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    muskmelon.add_pairing('mint')
    all_melon_types.append(muskmelon)

    casaba = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')
    all_melon_types.append(casaba)

    crenshaw = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    crenshaw.add_pairing('proscuitto')
    all_melon_types.append(crenshaw)

    yel_watermelon = MelonType('yw', 2013, 'yellow', False, True,
                               'Yellow Watermelon')
    yel_watermelon.add_pairing('ice cream')
    all_melon_types.append(yel_watermelon)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon_type in melon_types:
        print "{} pairs with".format(melon_type.name)
        for pairing in melon_type.pairings:
            print "- {}".format(pairing)


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_codes = {}

    for melon_type in melon_types:
        melon_codes[melon_type.code] = melon_type

    return melon_codes

############
# Part 2   #
############


class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, field, harvester):
        """Initializes an individual melon."""

        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester

    def __repr__(self):
        """Provide helpful output when printing"""

        repr_str = "<Melon type={type} field={field} harvester={harvester}>"
        return repr_str.format(type=self.melon_type.name,
                               field=self.field,
                               harvester=self.harvester)

    def is_sellable(self):
        """Returns True if individual melon is sellable."""

        return (self.shape_rating > 5 and self.color_rating > 5 and
                self.field != 3)


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons_by_id = make_melon_type_lookup(melon_types)

    melons = []

    melon1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melons.append(melon1)

    melon2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melons.append(melon2)

    melon3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melons.append(melon3)

    melon4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melons.append(melon4)

    melon5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melons.append(melon5)

    melon6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melons.append(melon6)

    melon7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melons.append(melon7)

    melon8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melons.append(melon8)

    melon9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')
    melons.append(melon9)

    return melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        print "\n"
        print "{} harvested this melon.".format(melon.harvester)
        print "It is from field {}.".format(melon.field)
        if melon.is_sellable():
            print "It is not sellable."
        else:
            print "It is not sellable."
