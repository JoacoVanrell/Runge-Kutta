# Método de Runge-Kutta de 4° Orden

**Universidad de Mendoza — Facultad de Ingeniería**  
**Análisis Numérico — 2026**

---

## Descripción

Implementación en Python del **Método de Runge-Kutta de 4° Orden (RK4)** para la resolución numérica de Ecuaciones Diferenciales Ordinarias (EDO) de primer orden de la forma:

```
y' = f(x, y),    y(x₀) = y₀
```

El programa acepta cualquier función `f(x, y)` ingresada por el usuario y calcula la solución aproximada paso a paso mediante la fórmula de recurrencia RK4, con un error de truncamiento local del orden O(h⁵).

---

## Integrantes

| Nombre | Carrera |
|---|---|
| Tomas Villar | Ingeniería en Informática |
| Joaquin Vanrrel | Ingeniería en Informática |

---

## Archivos

| Archivo | Descripción |
|---|---|
| `Runge-Kutta.py` | Código fuente principal del programa |
| `Documentacion.txt` | Explicación completa del método, aplicación a la carrera y resultados |

---

## Uso

**Linux / macOS**
```bash
python3 Runge-Kutta.py
```

**Windows**
```bash
python Runge-Kutta.py
```

## Funciones matemáticas disponibles

`sin`, `cos`, `tan`, `exp`, `log`, `sqrt` y operadores `+`, `-`, `*`, `/`, `**`