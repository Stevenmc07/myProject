#Estudiante: Steven Muñoz - Cálculos de formas de pago.

def forma_pago(n_piezas,v_unitario_pieza,monto_total):
    
    if monto_total > 500000:
        dinero_empresa = (monto_total * 55)/100
        prestamo_banco = (monto_total * 30)/100
        credito_fabricante = (monto_total * 15)/100
        interes_fabricante = (credito_fabricante * 20)/100
        print(f"\n- Número de piezas a comprar: {n_piezas} - Precio unitario de cada pieza: {v_unitario_pieza}")
        print(f"- Monto total de la compra: {monto_total} - Inversión de la compra: {dinero_empresa}")
        print(f"- Préstamo al banco: {prestamo_banco} - Crédito al fabricante: {credito_fabricante}")
        print(f"- Crédito al fabricante sumando el interés del 20%: {credito_fabricante + interes_fabricante}\n")
        
    elif monto_total <= 500000:
        dinero_empresa = (monto_total * 70)/100
        credito_fabricante = (monto_total * 30)/100
        interes_fabricante = (credito_fabricante * 20)/100
        print(f"\n- Número de piezas a comprar: {n_piezas} - Precio unitario de cada pieza: {v_unitario_pieza}")
        print(f"- Monto total de la compra: {monto_total} - Inversión de la compra: {dinero_empresa}")
        print(f"- Crédito al fabricante: {credito_fabricante}")
        print(f"- Crédito al fabricante sumando el interés del 20%: {credito_fabricante + interes_fabricante}\n")
        
while True:
    print("\n1. Agregar la cantidad y el valor unitario de la pieza que desea comprar.")
    print("2. Salir del programa.")
    opcion = input("Ingrese la opción que desea: ")
    
    if opcion == "1":
        n_piezas = int(input("\nIngrese el numero de piezas a comprar: "))
        v_unitario_pieza = float(input("Ingrese el valor unitario de la pieza: "))
        monto_total = n_piezas * v_unitario_pieza
        
        forma_pago(n_piezas,v_unitario_pieza,monto_total)
    
    elif opcion == "2":
        break
    
    else:
        print("\nIngrese una opción válida.")