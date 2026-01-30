# Programa 3: invertir_numero
programa en Python para invetir un numero de 4 cifras

## Análisis

### Variables de entrada
- n: numero a procesar o invertir

### Variables de Procesamiento
- d1: numero 1
- d2: numero 2
- d3: numero 3
- d4: numero 4
### Operaciones
- d1 = n % 10    * 1000   
- d2 = n // 10 % 10   * 100  
- d3 = n // 100 % 10   * 10 
- d4 = n // 1000       
- invertido =d1+d2+d3+d4


## Diseño

![diagrama de flujo](diagrama.png)

## Construcción
- codigo implementado en el archivo invertir_numero.py
