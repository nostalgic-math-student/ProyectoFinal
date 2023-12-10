### SamirSecretSharingSchemeApp - S4 App

Este proyecto se trata de una WebApp desarrollada en React.js para reproducir el modelo planteado por "Shamir" para cifrar archivos de manera secreta. 

Frameworks principales utilizados: 
- React.js + Tailwind.css + DaisyUI (Frontend)
- Flask (backend)

## Para ejecutar

Se necesita ejecutar servicio de carpetas `backend` y `frontend`, de preferencia empezar por `backend`, las instrucciones están en `backend/README.md`.

# Propuesta de valor:

El modelo propuesto en este proyecto fue modificado dada la inestabilidad que presenta el esquema planteado por Shamir. Esto ocurre dado que el propone dar un polinomio basado en un entero generado por el encriptado SHA256, el cual nos da un entero en su mayoría de veces muy grande, lo cual hace que en la práctica el evaluar polinomios de Lagrange para obtener este factor sea casi imposible para n,t>= 15 , por la aritmetica de punto flotante lo cual entorpece bastante. Sin embargo, se plantea usar el hash de la `password` planteada por Shamir como un entero entre `0` y `2^31 - 1` dado por la ecuación diofantina `sha256(password) = x mod(2^31 - 1)`, siendo `x` no el término independiente del polinomio sino la semilla generadora de números aleatorios y por ende generadora de las secuencias de polinomios. Es más seguro de generar y mucho más precisión numérica al evaluar los polinomios de Lagrange generados.  

