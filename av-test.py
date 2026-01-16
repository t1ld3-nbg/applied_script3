import platform
import time
import os

system = platform.system()

if system == "Windows":
    # Fortsätt med Windows-specifik kod
    print("Windows upptäckt. Scriptet fortsätter...")

elif system == "Linux":
    print("Linux upptäckt. Detta script är avsett för Windows.")
    exit()

elif system == "Darwin":
    print("macOS upptäckt. Detta script är avsett för Windows.")
    exit()

else: 
    print(f"Okänt operativsystem: {system}. Detta script är avsett för Windows. Avbryter körning")
    exit()
    
# Skriv AV test signaturen baserad på EICAR-testfil, innehållet är helt ofarligt och kommer inte att skada systemet.
eicar_str = "X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"

# Skapa fil och placera den på desktop
file = "AV-TEST.txt"
desktop =   os.path.join(os.path.join(os.path.expanduser("~"), 'Desktop'))
path = os.path.join(desktop, file)

with open(path, "w") as f:
    f.write(eicar_str)

print("Filen skapad.")
print("Väntar på AV/EDR-svar...")
time.sleep(3)   # Väntar några sekunder på AV/EDR-respons
print("Klart.\n")

print("Kontrollerar om filen fortfarande kan avläsas...")
try:
     with open(path, "r") as f:
        fil_innehall = f.read()

        # Kontrollera om innehållet matchar EICAR-strängen
        if fil_innehall == eicar_str:
            print("Filen är fortfarande läsbar. Antivirus/EDR har inte reagerat.")

except Exception as e:
            print("Filen har ändrats eller skadats.")
            print("Antivirus/EDR har troligtvis reagerat och tagit bort eller ändrat filen.")
            print("Testet är lyckat! Din AV/EDR-lösning är helt fungerande.")
