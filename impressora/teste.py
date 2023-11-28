from escpos.printer import Usb

# Substitua os valores pelos identificadores da sua impressora


from escpos.printer import Usb

""" Seiko Epson Corp. Receipt Printer (EPSON TM-T88III) """
p = Usb(0x048B8, 0x0E27, 0, profile="TM-T88III")
p.text("Hello World\n")

p.cut()