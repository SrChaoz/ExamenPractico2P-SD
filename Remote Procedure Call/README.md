# Examen Práctico: Debugging de Sistema Distribuido gRPC

## Descripción
Bienvenido desarrollador. Se te ha entregado el código fuente de un sistema de conversión de divisas basado en gRPC.
Lamentablemente, el desarrollador anterior dejó el proyecto incompleto y lleno de errores.

Tu misión, si decides aceptarla, es identificar y corregir los **5 errores** que impiden que el sistema funcione correctamente.

## Instrucciones
1.  Analiza el código del archivo `server.py` y `client.py`. (Y revisa `proto/currency.proto` para contexto).
2.  Intenta ejecutar el servidor y el cliente.
3.  Usa los logs de error y el comportamiento del programa para deducir qué está mal.
4.  Corrige los errores uno por uno hasta que el cliente pueda completar todas sus operaciones exitosamente.

## Pistas (Los 5 Errores)

Aquí tienes el reporte de QA con los síntomas detectados. Debes solucionar cada uno:

1.  **Conexión Rechazada:** El cliente ni siquiera logra conectarse al servidor. Parece que están hablando en frecuencias distintos.
2.  **Cálculos Extraños:** La conversión de moneda funciona, pero los resultados no tienen sentido (son inversamente proporcionales a lo esperado).
3.  **Sensibilidad de Mayúsculas:** El servidor no reconoce la modenda 'usd', lo cual rompe la robustez esperada, deberias asegurarte que el es servidor no tenga problema en manejar  USD, usd o Usd, todas deberina ser formas validas
4.  **Crash del Servidor:** Al intentar usar ciertas funciones del stream, el servidor se cae repentinamente con un error de variable no definida relacionado con el tiempo.
5.  **Stream Silencioso:** La función de `StreamRates` parece conectar, pero el cliente se queda esperando eternamente y nunca recibe datos. Es acaso una coneccion bloqueante que no recibe respuesta?

## Ejecución
Para probar tu solución:

**Terminal 1 (Servidor):**
```bash
python server.py
```

**Terminal 2 (Cliente):**
```bash
python client.py
```

¡Buena suerte!
