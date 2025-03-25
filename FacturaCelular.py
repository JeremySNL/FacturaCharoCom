from fpdf import FPDF
from datetime import date, time, datetime

class FacturaPDF(FPDF):
    def header(self):
        self.ln(10)
        self.set_font("Arial", size=14, style="B")
        self.cell(0, 5, "Charo Comunicaciones", ln=True, align="C")
        self.cell(0, 5, "Tel: 849-403-8743", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.ln(10)
        self.set_font("Arial", size=12)
        self.cell(0, 5, "¡Gracias por su compra!", ln=True, align="C")
        self.cell(0, 5, "Garantía: 1 mes", ln=True, align="C")
        #Firma
        self.ln(20)
        self.cell(0, 5, "--------------------------------", align="C", ln=True)
        self.cell(0, 5, "Firma", align="C", ln=True)
        self.ln(2)

        #Garantía
        self.set_font("Arial", size=11, style="B")
        self.cell(0, 5, "---Garantía---", align="C", ln=True)
        self.ln(2)
        self.set_font("Arial", size=10)
        self.multi_cell(0, 5, "La garantía cubre exclusivamente defectos de fabricación y funcionamiento del producto durante un período de 1 mes desde la fecha de compra. ", align="C")
        self.cell(0, 5, "...", align="C")

def crear_factura(cliente, IMEI, nombre, precio, fecha, descripcion):
    pdf = FacturaPDF("P", "mm", (58, 300))  # 58 mm de ancho
    pdf.add_page()
    pdf.set_margins(left = 0, top = 0, right = 0)

    # Fecha y cliente
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 5, f"Fecha: {fecha}", ln=True, align="L")
    pdf.cell(0, 5, f"Cliente: {cliente}", ln=True, align="C")
    pdf.ln(10)
    pdf.cell(0, 0, f"------------------------------------------------------------------", ln=True)
    pdf.ln(2)

    # Detalles de los productos
    pdf.set_font("Arial", size=11, style="B")
    pdf.cell(0, 5, "IMEI:", align="L")
    pdf.set_font("Arial", size=10)
    pdf.cell(0, 5, str(IMEI), align="R", ln=True)

    pdf.set_font("Arial", size=11, style="B")
    pdf.cell(0, 5, "Producto:", align="L")
    pdf.set_font("Arial", size=10)
    pdf.cell(0, 5, nombre, align="R", ln=True)

    pdf.set_font("Arial", size=11, style="B")
    pdf.cell(0, 5, "Precio:", align="L")
    pdf.set_font("Arial", size=10)
    pdf.cell(0, 5, f"${precio:.2f}", align="R", ln=True)

    pdf.set_font("Arial", size=11, style="B")
    pdf.cell(0, 5, "Descripcion:", align="L", ln = True)
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0, 5, descripcion, align="L")
    
    pdf.ln(2)
    pdf.cell(0, 0, f"---------------------------------------------------------------", ln=True)
    pdf.ln(10)

    # Total final
    pdf.set_font("Arial", size=14, style="B")
    pdf.cell(0, 5, f"Total: ${precio:.2f}", align="R", ln=True)

    return pdf

def verificarIMEI():
    IMEI = int(input("Digite los ultimos 4 numeros del IMEI: "))
    if(IMEI > 9999):
        print("Solo los ultimos 4 digitos del IMEI.")
        IMEI = verificarIMEI()
    if(IMEI <= 9999):
        return IMEI

# Datos para la factura
cliente = input("Digite el nombre del cliente: ")
IMEI = verificarIMEI()
nombre = input("Nombre del producto: ")
precio = float(input("Precio del producto: "))
descripcion = input("Descripcion del producto: ")

dt = datetime.now()
fecha = dt.strftime('%d-%m-%y %I:%M')

# Crear y guardar el PDF
pdf = crear_factura(cliente, IMEI, nombre, precio, fecha, descripcion)
pdf.output(f"Facturas/factura_{dt.strftime('%d-%m-%y_%I-%M-%S')}.pdf")