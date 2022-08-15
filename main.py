from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.graphics.shapes import Drawing
import calendar
doc = SimpleDocTemplate('cal.pdf', pagesize=A4)
items = []
cal = [['Monday', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']]
cal.extend(calendar.monthcalendar(2021,2))
table = Table(cal, 7*[inch], len(cal) * [inch])
table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, -1), 'Helvetica'),
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.blue),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.red),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
items.append(table)
doc.build([table])