from django.shortcuts import render
import qrcode
import base64
from io  import BytesIO

def home(request):
	if request.method == "POST":
		txt = request.POST.get("txt")

		qr = qrcode.make(txt)

		buffer = BytesIO()
		qr.save(buffer,format="PNG")
		buffer.seek(0)
	
		qr_code_data = base64.b64encode(buffer.getvalue()).decode("utf-8")

		return render(request,"home.html",{"qr_code_data":qr_code_data})
	else:
		return render(request,"home.html")