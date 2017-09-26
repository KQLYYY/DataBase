class TypeOfGoods(object):
    def __init__(self, id_of_type, name, description):
        self.id_of_type = id_of_type
        self.name = name
        self.description = description

    def set_id_of_type(self, idd):
        self.id_of_type = idd

    def set_name(self, n):
        self.name = n

    def set_amount(self, d):
        self.description = d

    def __str__(self):
        return "ID of type is: %d\nName is: %s\ndescription is: %s\n" % (self.id_of_type, self.name, self.description)