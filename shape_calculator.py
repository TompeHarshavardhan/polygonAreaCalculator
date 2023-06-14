class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def get_amount_inside(self,shape):
        a=int(self.width/shape.width)
        b=int(self.height/shape.height)
        return a*b
    def set_width(self,a):
        self.width=a
        self.side=a
    def set_height(self,a):
        self.height=a
        self.side=a
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    def get_area(self):
        return self.width*self.height
    def get_perimeter(self):
        return(2*(self.width+self.height))    
    def get_picture(self):
        string=''
        if self.width >50 or self.height>50:
            string='Too big for picture.'
        else:   
            for i in range(self.height):
                string+='*'*self.width
                string+='\n'
        return string
    def __str__(self) -> str:
        return "Rectangle(width="+str(self.width)+", height="+str(self.height)+')'
class Square(Rectangle):
    def __init__(self, side):
        self.side=side
        self.width=side
        self.height=side
    def set_side(self,a):
        self.side=a
        self.width=a
        self.height=a
    def __str__(self):
        return "Square(side="+str(self.side)+')'
    