import json


def query(Brand  , model):
    the_cars = cars[Brand][model]
    for the_car in the_cars:
        print(the_car)

def save_db(data):
    
    with open("test.json" , "w+") as open_file:
        json.dump(data , open_file)
        
def new_model_db(car_brand ,car_model ):
    vehicles = cars[car_brand][car_model] 
    vehicles.append(car_data)
    cars[car_brand][car_model] = vehicles



def add_db(car_brand ,car_model ):
    vehicles = cars[car_brand] 
    pint()
    vehicles.update(car_model)
    cars[car_brand] = vehicles


def load_db():
    with open("test.json", "r+") as file_open:
        cars = json.load(file_open) 
        
    return cars

cars = load_db()

print(cars)   
  
add_db("Toyota" , {"tacoma":[{
    "engine": "v8",
    "tank":8,
    "electric": False
}]})
save_db(cars)
# print(cars)
      
    
        
   
        
    
        


