# Ex.05 Design a Website for Server Side Processing
# Date: 19.04.25
# AIM:
To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side.

# FORMULA:
P = I2R
P --> Power (in watts)
 I --> Intensity
 R --> Resistance

# DESIGN STEPS:
## Step 1:
Clone the repository from GitHub.

## Step 2:
Create Django Admin project.

## Step 3:
Create a New App under the Django Admin project.

## Step 4:
Create python programs for views and urls to perform server side processing.

## Step 5:
Create a HTML file to implement form based input and output.

## Step 6:
Publish the website in the given URL.

# PROGRAM :
```
power.html

<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Document</title>

<meta name='viewport' content='width=device-width, initial-scale=1'>

<style type="text/css">

    body{
    
           background-color: rgb(34, 152, 175);
       
        }
    
    .edge {
    
            width: 1440px;

            margin-left: auto;

            margin-right: auto;

            padding-top: 250px;

            padding-left: 500px;

          }

   .box {

            display:block;

            border: Thick dashed rgb(118, 88, 182);

            width: 500px;

            min-height: 300px;

            font-size: 20px;

            background-color:hsl(142, 87%, 50%);

        }

   .formelt{

             color:rgba(159, 159, 35, 0.934);

             text-align: center;

             margin-top: 7px;

            margin-bottom: 6px;

          }

    h1{

          color:rgb(10, 12, 10);

          text-align: center;

          padding-top: 20px;
      }

</style>
<div class="edge">

    <div class="box">
    
    <h1 align="center">CALCULATING THE POWER OF A LAMP</h1>
    
    <form action="{% url 'power' %}" method="post">
    
        {% csrf_token %}
        
        <div class="formelt">
        
        <label>Intensity</label>
        
        <input type="number" name="intensity">
        
        <br>
        
        </div>
        
        <div class="formelt">
        
        <label>Resistance</label>
        
        <input type="number" name="resistance">
        
        <br>
        
        </div>
        
        <div>
        
        <button type="submit">Calculate</button>
        
        </div>
        
        <p align="center">The Power of the lamp is: {{ output }}</p>
        
    </div>
    
    </div>    
    
    </form>

    views.py

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

urls.py

from django.contrib import admin

from django.urls import path

from mathapp import views

urlpatterns = [ path('admin/', admin.site.urls), path('',views.power,name='power'),

]
```
# SERVER SIDE PROCESSING:
![alt text](<server/Screenshot 2025-04-19 143153.png>)
# HOMEPAGE:
![alt text](<server/Screenshot 2025-04-19 142542.png>)

# RESULT:
The program for performing server side processing is completed successfully.
