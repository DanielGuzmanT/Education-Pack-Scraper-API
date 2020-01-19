
class Tool:
    def __init__(self, business, benefits=[], tags=[]):
        self.business = business
        self.benefits = benefits
        self.tags     = tags


class Business:
    def __init__(self, name, description, logo=None):
        self.name = name
        self.description = description
        self.logo = logo


class Logo:
    def __init__(self, url):
        self.url = url


class Tag:
    def __init__(self, name, description):
        self.name = name
        self.description = description
