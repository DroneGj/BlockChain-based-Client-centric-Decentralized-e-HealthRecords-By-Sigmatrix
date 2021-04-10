from PyPDF2 import PdfFileWriter, PdfFileReader

pdfWriter = PdfFileWriter()

pdf = PdfFileReader("Report1.pdf")

for page_num in range(pdf.numPages):
    pdfWriter.addPage(pdf.getPage(page_num))


password = input('Enter new password: ')
pdfWriter.encrypt(password)
print('Encrypted successfully !')

encryptedName = input('What you want to put as Encrypted file name? (without Extension): ')
newPdfName = str(encryptedName) + '.pdf'

with open(newPdfName, 'wb') as f:
    pdfWriter.write(f)
    f.close()

print('This pdf is now Encrypted!')
