import os
import qrcode

# Caminho relativo - agora apontando para apps/base/static/img
qr_dir = os.path.join(os.path.dirname(__file__), '..', 'base', 'static', 'img')
os.makedirs(qr_dir, exist_ok=True)

# Gerar e salvar o QR Code
img = qrcode.make('https://www.example.com')
img_path = os.path.join(qr_dir, 'site.png')
img.save(img_path)

print(f"QR Code salvo em: {img_path}")