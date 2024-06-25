class Token:
    def __init__(self, name, price, rent, owned_by, x_coordinate, y_coordinate,Width,Height,special_status,mortgage_status,mortgage_value):
        self.name = name
        self.price = price
        self.rent = rent
        self.owned_by = owned_by
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.Width = Width
        self.Height = Height
        if (self.owned_by == 0):
            self.colour = (255,255,0)
        elif (self.owned_by == 1):
            self.colour = (0,0,255)
        elif (self.owned_by == 2):
            self.colour = (0,255,0)
        elif (self.owned_by == 3):
            self.colour = (255,0,0)
        else:
            self.colour = (255,255,255)
        self.special_status = special_status
        self.mortgage_status = mortgage_status
        self.mortgage_value = mortgage_value
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def get_rent(self):
        return self.rent

    def get_owner(self):
        return self.owned_by
    
    def owner_update(self, new_owner):
        self.owned_by = new_owner
        if(new_owner == 0):
            self.colour = (255,255,0)
        elif(self.get_owner() == 1):
            self.colour = (0,0,255)
        elif(self.get_owner() == 2):
            self.colour = (0,255,0)
        elif(self.get_owner() == 3):
            self.colour = (255,0,0)
    def get_x_coordinates(self):
        return self.x_coordinate
    
    def get_y_coordinates(self):
        return self.y_coordinate
    
    def get_height(self):
        return self.Height
    
    def get_width(self):
        return self.Width
    
    def get_special_status(self):
        return self.special_status
    
    def get_mortgage_status(self):
        return self.mortgage_status
    
    def updaate_mortgage_status(self, new_status):
        self.mortgage_status = new_status

    def get_mortgage_value(self):
        return self.mortgage_value
    
    def get_colour(self):
        return self.colour

stocks_names = ["start","Wipro","HDFC","Adani","Chest","ONGC","Infosys","Crash","L&T","ITC","Chest","SBI","NTPC","HCL","Wind fall","Kotak","Nestle","Britannia","Apollo","Chest","Bajaj","Closed","ICICI","Mahindra","Chest","Airtel","Eicher","Titan"]
prices=[50,100,195,250,None,40,150,-150,285,90,None,160,60,180,150,205,230,320,345,None,360,0,120,215,None,140,300,270]
rents = []
mortgage_value =[]
owners = [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
for i in range(len(prices)):
    if prices[i] is None:
        rents.append(None)
        mortgage_value.append(None)
    else:
        rent = prices[i] * 0.15
        rent = rent // 1
        rents.append(rent)
        mortgage = prices[i] // 2
        mortgage_value.append(mortgage)

x_coordinate = [825,750,675,600,525,450,375,300,365,365,365,365,365,365,300,375,450,525,600,675,750,825,825,825,825,825,825,825]
y_coordinate = [675,675,675,675,675,675,675,675,600,525,450,375,300,225,215,215,215,215,215,215,215,215,225,300,375,450,525,600]
Width = [72,72,72,72,72,72,72,72,10,10,10,10,10,10,72,72,72,72,72,72,72,72,10,10,10,10,10,10]
Height = [10,10,10,10,10,10,10,10,72,72,72,72,72,72,10,10,10,10,10,10,10,10,72,72,72,72,72,72]
special_status = [1,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,0,0,1,0,1,0,0,1,0,0,0]
mortgage_status = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Token_list = []
for i in range(len(stocks_names)):
    Token_list.append(Token(stocks_names[i],prices[i],rents[i],owners[i],x_coordinate[i],y_coordinate[i],Width[i],Height[i],special_status[i],mortgage_status[i],mortgage_value[i]))