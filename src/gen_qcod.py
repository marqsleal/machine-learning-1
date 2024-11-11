import qrcode

# URL da sua aplicação
link = "https://creditsystem-624224914913.us-central1.run.app/"

# Cria o QR Code com o link
qr = qrcode.make(link)

# Salva a imagem do QR Code
qr.save("qrcode_aplicacao.png")

print("QR Code gerado e salvo como 'qrcode_aplicacao.png'")
