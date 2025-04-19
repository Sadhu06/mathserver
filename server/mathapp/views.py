from django.shortcuts import render
def power(request):
     power=None 

     intensity = None

     resistance = None 


     if request.method == 'POST':
        print("POST method is used")
    
        intensity = request.POST.get('intensity','0')
    
        resistance = request.POST.get('resistance','0')
    

    
     if intensity and resistance:
    
        try:
        
        
            Intensity = float(intensity)
            
            Resistance = float(resistance)
            
            power = Intensity**2 * Resistance
            
            print('request=',request)
            
            print('intensity=',Intensity)
            
            print('resistance=',Resistance)
            
            print('power=',power) 
            

        except ValueError:
        
            power = "Invalid input. Please enter numerical values."


     return render(request, 'power.html', {'power': power, 'intensity': intensity, 'resistance': resistance})

