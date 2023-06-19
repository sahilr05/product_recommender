import enum

class StateEnumMeta(enum.EnumMeta):
    def __contains__(self, item):
        try:
            self(item)
        except ValueError:
            return False
        else:
            return True


class BaseState(enum.Enum, metaclass=StateEnumMeta):
    pass


class ProductCategory(str, BaseState):
    ELECTRONICS = "ELECTRONICS"
    CASES_AND_COVERS = "CASES_AND_COVERS"
    FASHION = "FASHION"
    HOME_UTILITIES = "HOME_UTILITIES"
    HEALTH_AND_BEAUTY = "HEALTH_AND_BEAUTY"


class PaymentMode(str, BaseState):
    CASH_ON_DELIVERY = "CASH_ON_DELIVERY"
    ONLINE = "ONLINE"


class CurrencyCode(str, BaseState):
    INR = "INR"
    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"

def states_as_list(state_type: BaseState):
    return list(map(lambda c: (c.value, c.name), state_type))

def states_as_values(state_type: BaseState):
    return list(map(lambda c: c.value, state_type))
