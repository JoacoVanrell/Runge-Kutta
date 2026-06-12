import math

def obtener_funcion():
    """
    Solicita al usuario que ingrese la ecuación diferencial a resolver.

    La función se ingresa como texto (string) y se evalúa dinámicamente
    usando eval(), lo que permite resolver cualquier EDO de primer orden
    de la forma y' = f(x, y).

    Retorna:
        f       : función Python evaluable que representa f(x, y)
        formula : string original ingresado por el usuario
    """
    print("\n---METODO DE RUNGE-KUTTA 4---")
    print("Ingresa la funcion f(x, y) donde y' = f(x, y)")
    print("Operadores disponibles: +, -, *, /, ** (potencia)")
    print("Funciones disponibles: sin, cos, tan, exp, log, sqrt")

    formula = input("\nIngresá la funcion que quieres resolver f(x, y): ")

    def f(x, y):
        """
        Evalúa la expresión ingresada por el usuario para valores concretos de x e y.
        Se le pasa un diccionario de contexto para que el usuario pueda usar
        funciones matemáticas como sin, cos, exp, etc., directamente en su fórmula.
        """
        return eval(formula, {"x": x, "y": y, "math": math,
                              "sin": math.sin, "cos": math.cos,
                              "tan": math.tan, "exp": math.exp,
                              "log": math.log, "sqrt": math.sqrt})
    return f, formula


def obtener_condiciones():
    """
    Solicita al usuario las condiciones iniciales y parámetros del método.

    La condición inicial establece el punto de partida (x0, y0) 
    a partir del cual se construye la solución.
    El paso h determina la distancia entre cada punto calculado.

    Retorna:
        x0      : valor inicial de la variable independiente
        y0      : valor inicial de la variable dependiente (condición inicial)
        x_final : valor de x hasta donde se quiere aproximar la solución
        h       : tamaño del paso entre puntos consecutivos
    """
    print("\n--- CONDICIONES INICIALES Y PARÁMETROS ---")
    x0 = float(input("Valor inicial de x (x0): "))
    y0 = float(input("Valor inicial de y (y0): "))
    x_final = float(input("Valor final de x hasta donde resolver: "))
    h = float(input("Tamaño del paso (h): "))
    return x0, y0, x_final, h


def runge_kutta_4(f, x0, y0, h, n_pasos):
    """
    Implementa el Método de Runge-Kutta de 4° orden para resolver EDOs.

    El método aproxima la solución calculando cuatro pendientes (k1, k2, k3, k4)
    en cada paso y combinándolas en un promedio ponderado:

        phi = (k1 + 2*k2 + 2*k3 + k4) / 6

    Donde:
        k1 = f(x, y)                        
        k2 = f(x + h/2, y + h/2 * k1)      
        k3 = f(x + h/2, y + h/2 * k2)      
        k4 = f(x + h,   y + h   * k3)      

    La fórmula de recurrencia es:
        y(i+1) = y(i) + h * phi

    Parámetros:
        f       : función f(x, y) que define la EDO
        x0      : valor inicial de x
        y0      : valor inicial de y
        h       : tamaño del paso
        n_pasos : cantidad de pasos a calcular

    Retorna:
        ((xs, ys), None)  si el cálculo se completó correctamente
        (None, mensaje)   si la solución diverge o desborda, con descripción del error
    """
    xs = [x0]
    ys = [y0]

    x = x0
    y = y0

    for i in range(n_pasos):
        try:
            # Cálculo de las cuatro pendientes características del método RK4
            k1 = f(x,         y)
            k2 = f(x + h/2,   y + h/2 * k1)
            k3 = f(x + h/2,   y + h/2 * k2)
            k4 = f(x + h,     y + h   * k3)

            # Promedio ponderado de las pendientes
            phi = (k1 + 2*k2 + 2*k3 + k4) / 6

            # Aplicación de la fórmula de recurrencia
            y_nuevo = y + h * phi

            # Verificación de que el resultado sea un número válido y finito.
            if math.isnan(y_nuevo) or math.isinf(y_nuevo):
                return None, f"La solución diverge en x = {round(x + h, 6)}. Reducí el intervalo o el paso h."

            y = y_nuevo
            x = round(x + h, 10)
            xs.append(x)
            ys.append(y)

        except OverflowError:
            # Ocurre cuando y crece tan rápido que supera el límite
            return None, f"Desbordamiento numérico en x = {round(x + h, 6)}. La solución crece demasiado rápido para estos parámetros."

    return (xs, ys), None


def mostrar_resultados(xs, ys, formula):
    """
    Muestra en pantalla la tabla de resultados obtenidos por el método RK4.

    Cada fila representa un punto (x, y) de la solución aproximada,
    donde el paso indica el número de iteración del método.

    Parámetros:
        xs      : lista de valores de x calculados
        ys      : lista de valores aproximados de y en cada x
        formula : string de la EDO resuelta, para mostrar en el encabezado
    """
    print(f"\n--- RESULTADOS ---")
    print(f"EDO resuelta: y' = {formula}")
    print(f"\n{'Paso':>5}  {'x':>10}  {'y':>15}")
    print("-" * 35)
    for i, (x, y) in enumerate(zip(xs, ys)):
        print(f"{i:>5}  {x:>10.4f}  {y:>15.8f}")


def main():
    """
    Función principal del programa.

    Coordina el flujo completo:
        1. Solicita la EDO al usuario y valida que sea una expresión correcta
        2. Solicita las condiciones iniciales y valida los parámetros
        3. Ejecuta el método de Runge-Kutta de 4° orden
        4. Muestra los resultados o un mensaje de error si la solución no es válida
    """
    print("=" * 45)
    print("   RESOLUCIÓN DE EDO - MÉTODO RUNGE-KUTTA 4")
    print("=" * 45)

    # Bucle de validación de la fórmula: se repite hasta que el usuario
    # ingrese una expresión matemáticamente válida
    while True:
        try:
            f, formula = obtener_funcion()
            f(0, 1)  # prueba con valores arbitrarios para detectar errores de sintaxis
            break
        except Exception as e:
            print(f"\nError en la fórmula: {e}")
            print("Por favor, reingresá la función.\n")

    # Bucle de validación de condiciones: se repite hasta que los parámetros
    # sean coherentes (x_final > x0, h positivo, valores numéricos)
    while True:
        try:
            x0, y0, x_final, h = obtener_condiciones()
            if x_final <= x0:
                print("\nEl valor final de x debe ser mayor que x0.\n")
                continue
            if h <= 0:
                print("\nEl paso h debe ser un número positivo.\n")
                continue
            break
        except ValueError:
            print("\nPor favor ingresá solo números válidos.\n")

    # Cálculo de la cantidad de pasos necesarios para cubrir el intervalo [x0, x_final]
    n_pasos = round((x_final - x0) / h)

    resultado, error = runge_kutta_4(f, x0, y0, h, n_pasos)

    if error:
        print(f"\nNo se pudo completar el cálculo: {error}")
    else:
        xs, ys = resultado
        mostrar_resultados(xs, ys, formula)


if __name__ == "__main__":
    main()