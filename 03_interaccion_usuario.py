# Solitar informacion personal al usuario 
Nombres = input ("Ingrese sus nombres completos: ")
Apellidos = input ("Ingrese sus apellidos completos: ")
Profesion = input (" Ingrese el nombre de su profesion: ")
Año_nacimiento = input ("Ingrese su año de nacimiento: ")

# Calcular edad 
Año_actual = 2023
Edad = Año_actual - int(Año_nacimiento)

# Informacion Personal
print ("El (La)", Profesion, Nombres, Apellidos, "tiene" , Edad, " años.")
