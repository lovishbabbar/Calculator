data = ['{"Gender":"Male","WeightKg":60,"HeightCm":10}'] 
 
correctdata = [[6.0, 'Underweight', 'Malnutrition risk']]
 
def test_array_formation():  
    assert main1(data) == correctdata, "It should be [[6.0, 'Underweight', 'Malnutrition risk'], [23.0, 'Normal weight', 'Low risk'], [5.333333333333333, 'Underweight', 'Malnutrition risk'], [6.5, 'Underweight', 'Malnutrition risk'], [3.2, 'Underweight', 'Malnutrition risk']]"  
  
if name == "_main_":  
    test_array_formation()  
    print("Everything passed")
