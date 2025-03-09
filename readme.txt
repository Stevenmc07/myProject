El presente proyecto se basa en un sistema que permite cálcular una forma de pago para el cliente (empresa contratante)
para una o varias ordenes de compras que el cliente desea realizar a una fábrica de refacciones.

Para esto el algoritmo realiza lo siguiente: 

Solicita al número de piezas que desea comprar y el valor unitario de la pieza.
Calcula el monto total multiplicando el número de piezas por el valor unitario de la pieza.

Si el monto total es mayor a 500000:

Calcula el 55% del monto total, valor que puede pagarle el cliente a la fábrica de refacciones.
Calcula el 30% del monto total, valor que le solicitará prestado al banco.
Calcula el 15% restante del monto total, valor en base al cual se le solictará al fabricante un crédito.
Cálcula el 20% del crédito solicitado al fabricante, el cual será el interés solicitado por el fabricante para efectuar el crédito.

Por último muestra en pantalla:
Número de piezas a comprar, valor unitario de la pieza, monto total de la compra, inversión de la compra, préstamo al banco,
crédito al fabricante y crédito al fabricante sumando el 20% de interés.


Si el monto total es menor o igual a 500000:

Calcula el 70% del monto total, valor que puede pagarle el cliente a la fábrica de refacciones.
Calcula el 30% restante del monto total, valor en base al cual se le solictará al fabricante un crédito.
Cálcula el 20% del crédito solicitado al fabricante, el cual será el interés solicitado por el fabricante para efectuar el crédito.

Por último muestra en pantalla:
Número de piezas a comprar, valor unitario de la pieza, monto total de la compra, inversión de la compra, crédito al fabricante
y crédito al fabricante sumando el 20% de interés.