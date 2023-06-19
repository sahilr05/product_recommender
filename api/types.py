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
    FASHION = "FASHION"
    HOME_UTILITIES = "HOME_UTILITIES"
    HEALTH_AND_BEAUTY = "HEALTH_AND_BEAUTY"


def states_as_list(state_type: BaseState):
    return list(map(lambda c: (c.value, c.name), state_type))
