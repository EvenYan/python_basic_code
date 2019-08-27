from PIL import Image
import pytesseract

# Simple image to string
print(pytesseract.image_to_string(Image.open('./images_ocr/8502.jpg')))

# # French text image to string
# print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra'))

# # Get bounding box estimates
# print(pytesseract.image_to_boxes(Image.open('images_ocr/V9Am.jpg')))

# # Get verbose data including boxes, confidences, line and page numbers
# print(pytesseract.image_to_data(Image.open('images_ocr/V9Am.jpg')))

# # Get information about orientation and script detection
# print(pytesseract.image_to_osd(Image.open('images_ocr/V9Am.jpg')))

# # In order to bypass the internal image conversions, just use relative or absolute image path
# # NOTE: If you don't use supported images, tesseract will return error
# print(pytesseract.image_to_string('test.png'))

# # get a searchable PDF
# pdf = pytesseract.image_to_pdf_or_hocr('test.png', extension='pdf')

# # get HOCR output
# hocr = pytesseract.image_to_pdf_or_hocr('test.png', extension='hocr')
