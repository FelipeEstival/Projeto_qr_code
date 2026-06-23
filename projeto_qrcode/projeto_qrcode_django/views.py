from django.shortcuts import render
from django.http import JsonResponse # Importe o JsonResponse
import qrcode
import io
import base64

def gerar_qrcode(request):
    if request.method == 'POST':
        link = request.POST.get('url_qrcode')
        if link: 
            img = qrcode.make(link)
            buffer = io.BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)
            img_em_texto = base64.b64encode(buffer.getvalue()).decode('utf-8')
            
            return JsonResponse({'qr_code': img_em_texto})

    return render(request, 'tarefas/index.html')
