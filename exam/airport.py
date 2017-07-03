import self as self


class nest:
    def _military_plane(self):
        print("Only for army")
    def civil_airoplane(self):
        self.color = "White"
    print("U may take it")

class airstrip(nest):
    def __init__(self):
        nest.civil_airoplane(self)
    print("Now little civil plane have lots of air")



class airplane(airstrip):
    def __init__(self):
        self.take_off()
        super(nest,self).__init__()
    def take_off(self):
        print("I will fly")

class military_airplane(airplane):
    def __init__(self):
        self.take_off()
        super(airplane,self).__init__()
    def take_off(self):
        print("I can't")
ConvairB_36 = military_airplane()
TU_144 = airplane()

