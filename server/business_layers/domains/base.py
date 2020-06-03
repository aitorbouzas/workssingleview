from abc import ABCMeta, abstractmethod


class BaseDomain(metaclass=ABCMeta):
    internals = []

    @abstractmethod
    def __init__(self, **kwargs):
        pass

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self, internal=False):
        res = {}
        for attr in self.__dict__:
            attr_flag = False
            value = None
            if internal:
                value = getattr(self, attr)
                attr_flag = True
            elif attr not in self.internals:
                value = getattr(self, attr)
                attr_flag = True

            if attr_flag:
                attr_value = value
                if isinstance(value, list):
                    value_list = []
                    for val in value:
                        if hasattr(val, "to_dict"):
                            value_list.append(val.to_dict(internal=internal))
                    attr_value = value_list
                elif isinstance(value, object) and hasattr(value, "to_dict"):
                    attr_value = value.to_dict(internal=internal)

                res[attr] = attr_value
        return res

    def __eq__(self, other):
        self_dict = self.to_dict()
        other_dict = other.to_dict()

        return self_dict == other_dict
