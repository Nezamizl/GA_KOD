

#!usr/bin/env python   	 										# Anger att programmet skrivs i python
import RPi.GPIO as GPIO     										# Anger fumktioner som sköter GPIO pinnarna på raspberrypin
import keyboard     											# Bibliotek för vissa programrader
import time         											# Bibliotek som sköter tiden i programmet
from mfrc522 import SimpleMFRC522       								# Bibliotek för RFID chipet MFRC522



def Read_Func():       			 								# detta är läs funktionen
    reader = SimpleMFRC522()     									# Variabel som lagrar värdet av funktionen   
    try:    												# Try och finally gör så att GPIO.cleanup körs oavsett resultat från rfid
        id1, text = reader.read() 									# Läser id och text från kort
        print(id1)
        print(text)    	 										# Skriver dessa på skärmen då kortet är läst
        
    finally:
        GPIO.cleanup()      										# Är viktig för att programmet ska fungera korrekt
    return text.strip() 										# Returnar text, så att det kan användas senare


    
    
def main():   
   
    from datetime import datetime   									# Importerar biblioteket datetime
    
    while True:              
        print('____________________________')
        print(' To log morning arrival, write LMA,') 
        print(' To log morning departure, write LMD') 							# Vi har fyra olika filer, för att göra datan lättare att läsa
        print('\t' + '---')
        print(' To log morning arrival, write LAA,')
        print(' To log morning departure, write LAD')
        ord = input(' Input:' )  
        
        
        if ord == 'LMA': 
            try:
                while True:
                    nu = datetime.now()
                    nuvarande_tid = nu.strftime("%D:%H:%M:%S") 						# Array för datum, timme, minut och sekund
                    print('Logging morning Arrival. Place card or tag on the scanner')
                    deltagare = Read_Func() # Deltagare antar värdet från Read_Func
                    with open('logg_LMA.txt', 'a') as f: # Filen Logg_LMA öppnas
                        f.write(deltagare + '\t' + '\t' +nuvarande_tid+ '\n' ) 				# texten från läsfunktionen och tiden skrivs in
                        f.write('______________________________________________' + '\n') 		# Gör dokumentet lättare att läsa
                        print('Please wait')        
                        time.sleep(1) # Väntar i en sekund
                        print('---')
                        print('Attendance registered')
            except KeyboardInterrupt: 									# Genom att klicka control C kommer programmet att återgå till "huvudmenyn"
               pass
     
        
        if ord == 'LMD':
            try:
                while True:
                    nu = datetime.now()
                    nuvarande_tid = nu.strftime("%D:%H:%M:%S")
                    print('Logging morning departure. Place card or tag on the scanner') 		# Dessa "funktioner", gör samma sak som föregående
                    deltagare = Read_Func()                                             		# Men skriver till olika filer
                    with open('logg_LMD.txt', 'a') as f:
                        f.write(deltagare + '\t' + '\t' +nuvarande_tid+ '\n' )
                        f.write('______________________________________________' + '\n')
                        print('Please wait')
                        time.sleep(1)
                        print('---')
                        print('Attendance registered')
            except KeyboardInterrupt:
               pass
                
        
        if ord == 'LAA':
            try:
                while True:
                    nu = datetime.now()
                    nuvarande_tid = nu.strftime("%D:%H:%M:%S")
                    print('Logging afternoon arrival. Place card or tag on the scanner')
                    deltagare = Read_Func()
                    with open('logg_LAA.txt', 'a') as f:
                        f.write(deltagare + '\t' + '\t' +nuvarande_tid+ '\n' )
                        f.write('______________________________________________' + '\n')		# Resterade del gör samma sak, men skriver till olia
                        ('Please wait')									# filer och anropas av andra ord
                        time.sleep(1)
                        print('Attendance registered')
                        print('---')
            except KeyboardInterrupt:
                pass
                
                
        
        if ord == 'LAD':
            try:
                while True:
                    nu = datetime.now()
                    nuvarande_tid = nu.strftime("%D:%H:%M:%S")
                    print('Logging afternoon arrival. Place card or tag on the scanner')
                    deltagare = Read_Func()
                    with open('logg_LAD.txt', 'a') as f:
                        f.write(deltagare + '\t' + '\t' +nuvarande_tid+ '\n' )
                        f.write('______________________________________________' + '\n')
                        ('Please wait')
                        time.sleep(1)
                        print('Attendance registered')
                        print('---')
            except KeyboardInterrupt:
               pass
                
        else:
            print('Incorrect input')
                    
        
        

main()

        






        
