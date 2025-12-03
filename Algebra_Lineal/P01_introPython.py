
# EN PYTHON NO ES NECESARIO EL PUNTO Y COMA PARA TERMINAR INSTRUCCIONES

print("Hola ");
print("Oscar");
print(",Cómo estas?");

print("\r\n") #salto de linea \n = new line
print("Hola ", end="");
print("Oscar", end="-");
print(",Cómo estas?");

#Tipado dinamico!
#El tipo de dato de una variable puede cambiar en tiempo de ejecucion
#nombre  = 5
nombre = "Oscar"
print("Hola " + str(nombre) + ", Cómo estas?") #casteo
print("Hola", nombre,", Cómo estas?")


