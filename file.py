def query(Brand  , model):
    the_cars = cars[Brand][model]
    for the_car in the_cars:
        print(the_car)
    
cars = {
    
    "Toyota":{
        
        
        "camery":[
            
            {
                "2020":{
                    "Engine-type": "v6"
                    , "tank":6 ,
                    "electric": True
                }
            } ,
            
            {
                "2021":{
                    "Engine-type": "v8"
                    , "tank":10,
                    "electric": False
                }
            }
            
            
        ] ,
        "corrola":[
            {
                "2020":{
                    "Engine-type": "v12"
                    , "tank":5 ,
                    "electric": True
                }
            }  
            ]
        
    
    } ,
    "kia":{
       "rio": [
           {
                "2019":{
                    "Engine-type": None
                    , "tank":5 ,
                    "electric": True
                }
            } 
           
       ] 
    }
    
}

query("Toyota" , "camery")