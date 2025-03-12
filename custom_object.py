class CustomObject():
    def __init__(self,height:int,width:int):
        self.height = height
        self.width = width

    def __repr__(self):
        return f"CustomObject -> Height : {self.height} Width : {self.width}"

    def __eq__(self,other):
        if isinstance(other,CustomObject):
            if self.height == other.height and self.width == other.width:
                return True
            else:
                return False
        return False