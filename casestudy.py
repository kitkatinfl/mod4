#kathleen Hambrick 9/7/24
# Mod 3 Case Study

# superclass
class vehicle():
    def __init__(self,type):
        self.type=type

# class
class auto(vehicle):
    def __init__(self,type,year,make,model,doors,roof):
        super().__init__(type)
        self.year=year
        self.make=make
        self.model=model
        self.doors=doors
        self.roof=roof

#enter data
type='0'
while type!='car':
    type = input('Vehicle Type : ')
    if type!='car':
        print("Only 'car' types accepted at this time.")

year='0'
while True:
    year=input("Vehicle Year: ")
    try:
        ans=int(year)
        break
    except ValueError:
        print("This was not a valid input please try again")

#year = input('Vehicle Year : ')
#try:
#    ans=int(year)
#except Exception:
#    print("invalid year entry")
make = input('Vehicle Make : ')
model = input('Vehicle Model : ')

doors='0'
while True:
    doors = input('Vehicle # Doors : ')
    try:
       ans=int(doors)
       break
    except Exception:
       print("invalid #doors entry")

roof = input('Vehicle Roof : ')

auto_1=auto(type,year,make,model,doors,roof)

#print out data
print()
print("Vehicle type: ",type)
print("Year:         ",year)
print("Make:         ",make)
print("Model:        ",model)
print("# of doors:   ",doors)
print("Type of roof: ",roof)
