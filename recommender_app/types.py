import enum
from typing import List
from typing import Tuple


class StateEnumMeta(enum.EnumMeta):
    """Metaclass for enums that allows checking if a value is a valid member."""

    def __contains__(self, item):
        try:
            self(item)
        except ValueError:
            return False
        else:
            return True


class BaseState(enum.Enum, metaclass=StateEnumMeta):
    """Base class for enums with metaclass StateEnumMeta."""

    pass


class ProductCategory(str, BaseState):
    """Enum for product categories."""

    ELECTRONICS = "ELECTRONICS"
    CASES_AND_COVERS = "CASES_AND_COVERS"
    FASHION = "FASHION"
    HOME_UTILITIES = "HOME_UTILITIES"
    HEALTH_AND_BEAUTY = "HEALTH_AND_BEAUTY"


class PaymentMode(str, BaseState):
    """Enum for payment modes."""

    CASH_ON_DELIVERY = "CASH_ON_DELIVERY"
    ONLINE = "ONLINE"


class CurrencyCode(str, BaseState):
    """Enum for currency codes."""

    INR = "INR"
    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"


def states_as_list(state_type: BaseState) -> List[Tuple[str, str]]:
    """Return a list of (value, name) tuples for the given enum type."""
    return list(map(lambda c: (c.value, c.name), state_type))


def states_as_values(state_type: BaseState) -> List[str]:
    """Return a list of values for the given enum type."""
    return list(map(lambda c: c.value, state_type))
