class RoseDictionary:
    def __init__(self):
        self.dictionary = []

    def __getitem__(self, key):
        for tupple in self.dictionary:
            if tupple[0] == key:
                return tupple[1]
        else:
            return "Value was not found"

    def __setitem__(self, key, value):
        index = -1
        for tupple in self.dictionary:
            if tupple[0] == key:
                index = self.dictionary.index(tupple)
        if index != -1:
            del self.dictionary[index]
        self.dictionary.append((key, value))

    def pop_item(self, raise_error=False, error_msg="", default=""):
        if len(self.dictionary) == 0:
            if raise_error:
                if error_msg == "":
                    return "KeyError: \'error_msg\'"
                else:
                    return "KeyError: \'" + error_msg + "\'"
            else:
                if default == "":
                    return "Dictionary was empty and no default value/message was specified."
                else:
                    return default
        else:
            tupple = self.dictionary.pop()
            return tupple[1]

    def get_item(self, key, raise_error=False, error_msg="", default=""):
        for tupple in self.dictionary:
            if tupple[0] == key:
                return self.dictionary[key]
        if raise_error:
            if error_msg == "":
                return "KeyError: \'error_msg\'"
            else:
                return "KeyError: \'" + error_msg + "\'"
        else:
            if default == "":
                return "Value was not found and no default value/message was specified."
            else:
                return default
# d = RoseDictionary()
# d["mike"] = "report1"
# d["mike"] = "report2"
# print(d["mike"])
# print(d["mikre"])
# print(d.pop_item())
# print(d.pop_item())
# d["mike"] = "report1"
# print(d["mike"])
# print(d.pop_item())
# print(d.pop_item())
# print(d.pop_item(default="fesfesf"))
# print(d.pop_item(raise_error=True))
# print(d.pop_item(raise_error=True, error_msg="Ribabrrs"))
# print(d.get_item("fef"))
# print(d.get_item("fef", default="fesfesf"))
# print(d.get_item("fef", raise_error=True))
# print(d.get_item("fef", raise_error=True, error_msg="Ribabrrs"))
