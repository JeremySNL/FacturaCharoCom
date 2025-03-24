from fpdf import FPDF
from datetime import date, time, datetime

class FacturaPDF(FPDF):
    def header(self):
        self.set_font("Arial", size=10, style="B")
        self.cell(0, 5, "Charo Comunicaciones", ln=True, align="C")
        self.cell(0, 5, "Tel: 849-403-8743", ln=True, align="C")
        self.ln(3)

    def footer(self):
        self.set_font("Arial", size=8)
        self.cell(0, 5, "¡Gracias por su compra!", ln=True, align="C")
        self.cell(0, 5, "Garantía: 1 mes", ln=True, align="C")
        #Firma
        pdf.ln(10)
        pdf.cell(0, 5, "--------------------------------", align="C", ln=True)
        pdf.cell(0, 5, "Firma", align="C", ln=True)

def crear_factura(cliente, productos, total, fecha):
    pdf = FacturaPDF("P", "mm", (58, 200))  # 58 mm de ancho
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=0)
    pdf.set_margins(left = 0, top = 0, right = 0)

    # Fecha y cliente
    pdf.set_font("Arial", size=8)
    pdf.cell(0, 5, f"Fecha: {fecha}", ln=True, align="L")
    pdf.cell(0, 5, f"Cliente: {cliente}", ln=True, align="C")
    pdf.ln(5)

    # Detalles de los productos
    pdf.set_font("Arial", size=8)
    pdf.cell(10, 5, "Cant", align="C")
    pdf.cell(30, 5, "Producto", align="C")
    pdf.cell(18, 5, "Total", align="C")
    pdf.ln()

    for cant, producto, precio in productos:
        pdf.cell(10, 5, str(cant), align="C")
        pdf.cell(30, 5, producto, align="L")
        pdf.cell(18, 5, f"${precio:.2f}", align="R")
        pdf.ln()

    # Total final
    pdf.ln(5)
    pdf.set_font("Arial", size=10, style="B")
    pdf.cell(0, 5, f"Total: ${total:.2f}", ln=True, align="R")

    return pdf

# Datos para la factura
cliente = input("Digite el nombre del cliente: ")
añadiendo = True
productos = []
centinela = "1"
while centinela == "1":
    cantidad = int(input("Cantidad del producto: "))
    nombre = input("Nombre del producto: ")
    precioP = float(input("Precio del producto: "))
    productos.append((cantidad, nombre, precioP))
    centinela = input("Digite 1 para continuar agregando, de lo contrario digite cualquier letra: ")

total = sum(cant * precio for cant, _, precio in productos) 
dt = datetime.now()
fecha = dt.strftime('%d-%m-%y %I:%M')

# Crear y guardar el PDF
pdf = crear_factura(cliente, productos, total, fecha)
pdf.output("factura.pdf")