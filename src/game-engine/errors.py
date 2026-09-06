# Custom error classes

class IllegalActionError(Exception):
    "Error class so it's easy to debug an illegal action"
    pass

class InvalidMapError(Exception):
    "Error class so a invalid map doesn't silently load"
    pass

class InvalidCardError(Exception):
    "Raise error if the card is not valid"
    pass