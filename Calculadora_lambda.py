
# coding: utf-8

# Calculadora con decisión de operación

# Para comprender las expresiones lambda, se hizo el siguiente ejercicio.   
# Se le pide al usuario ingresar la operación que desea realizar.  
# Luego, que ingrese dos números.  
# 
# 
# suma = lambda n1, n2: n1 + n2  
#   
# Explicación:  
# 
# suma   : nombre de la expresión lambda.  
# lambda : palabra reservada para declarar la expresión lambda.  
# n1, n2 : corresponden a los parámetros que utilizaremos en el momento de llamar a la expresión lambda.  
# n1 + n2: es la operación que se llevará a cabo.


try:
    eleccion = int(input("1: suma | 2: resta | 3: multiplicación | 4: división\n"))

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    
    if eleccion == 1:
        print("***************Usted eligió SUMAR***************")
        suma = lambda n1, n2: n1 + n2
        print("Resultado: ", suma(num1, num2))
    elif eleccion == 2:
        print("***************Usted eligió RESTAR***************")
        resta = lambda n1, n2: n1 - n2
        print("Resultado: ", resta(num1, num2))
    elif eleccion == 3:
        print("***************Usted eligió MULTIPLICAR***************")
        multiplicacion = lambda n1, n2: n1 * n2
        print("Resultado: ", multiplicacion(num1, num2))
    elif eleccion == 4:
        print("***************Usted eligió DIVIDIR***************")
        division = lambda n1, n2: n1 / n2
        print("Resultado: ", division(num1, num2))
    else:
        print("***************SU ELECCIÓN NO ES VÁLIDA***************")
        
except ZeroDivisionError:
    print("Error de división por 0")
except ValueError:
    print("El argumento que ingresó no es válido.")


# Tip:  
# Otro ejemplo de cómo evitar la división por cero utilizando expresión lambda es  
#   
# div = lambda n1, n2: "Error de división por 0" if n2 == 0 else n1 / n2  
# 
# donde lo que está al lado derecho de los dos puntos, es una condición.
