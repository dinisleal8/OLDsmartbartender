from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import RPi.GPIO as GPIO
import time

@csrf_exempt

def drink1(request):  #Sex on the Beach
    bombas = [17, 21, 22, 23, 24, 25]
    led = 26

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(bombas, GPIO.OUT)

    try:
        print("A começar... Sex on the Beach ")
        loading_response = render(request, "loading.html")

        return loading_response
        GPIO.output(luz, GPIO.LOW)
        print("Luz LIGADA")

        GPIO.output(bombas[0], GPIO.LOW)
        print("Cola LIGADA")

        time.sleep(2)
        GPIO.output(bombas[0], GPIO.HIGH)
        print("Cola DESLIGADA")

        GPIO.output(bombas[1], GPIO.LOW)
        print("Vodka LIGADA")
        GPIO.output(bombas[2], GPIO.LOW)
        print("Sumo LIGADO")
        GPIO.output(bombas[3], GPIO.LOW)
        print("Licor LIGADO")

        time.sleep(1)

        GPIO.output(bombas[1], GPIO.HIGH)
        print("Vodka DESLIGADA")
        GPIO.output(bombas[2], GPIO.HIGH)
        print("Sumo DESLIGADA")
        GPIO.output(bombas[3], GPIO.HIGH)
        print("Licor DESLIGADA")

        GPIO.output(luz, GPIO.HIGH)
        print("Luz DESLIGADA")

    except Exception as e:
        return HttpResponse(f"ERRO: {str(e)}")

    finally:
        print("SUCESSO!")
        GPIO.cleanup()
        return render(request, "conclued.html")
    

def drink2(request): #Cuba Libre Tropical

    print("A começar... Cuba Libre Tropical ")
    bombas = [17, 21, 22, 23, 24, 25]
    led = 26

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(bombas, GPIO.OUT)

    try:
        loading_response = render(request, "loading.html")

        return loading_response
    
        GPIO.output(bombas[0], GPIO.LOW)
        print("Cola LIGADA")

        time.sleep(2)

        GPIO.output(bombas[5], GPIO.LOW)
        print("Rum LIGADA")

    except Exception as e:
        return HttpResponse(f"ERRO: {str(e)}")

    finally:
        print("SUCESSO!")
        GPIO.cleanup()
        return render(request, "conclued.html") 