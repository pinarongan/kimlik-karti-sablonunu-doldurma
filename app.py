from PIL import Image, ImageDraw, ImageFont

# 1. ADIM: Vesikalık fotoğrafı kimliğin üzerine yapıştırmak.

temp = Image.open("mavikimlik.jpg")   # mavi kimlik kartı şablonu
#temp.show()

foto = "vesikalik.jpg"                # kimliğe yapıştırılacak vesikalık foto

pic = Image.open(foto).resize((110, 130))   # vesikalığın boyutlarını şablona yerleşecek şekilde ayarlayalım
#pic.show()
temp.paste(pic, (174, 49))      # vesikalığı kimlik kartının üstüne yapıştıralım
#temp.show()


# 2. ADIM: Kimlik bilgilerini kimliğin üzerine yazdırmak.

draw = ImageDraw.Draw(temp)        # üzerine bilgi girilecek şablonumuz
font = ImageFont.truetype('times.ttf', size=15)     # bilgileri girerken kullanacağımız font ve yazı boyutu

tc_kimlik_no = "11345608374"
isim = "METİN"
soyisim = "SEZAİGİL"
baba_ismi = "AHMET MÜMTAZ"
anne_ismi = "FADİK"
dogum_yeri = "AYDIN"
dogum_tarihi = "18.11.2005"

draw.text((60, 217), tc_kimlik_no, font=font, fill='black')
#temp.show()
draw.text((60, 244), soyisim, font=font, fill='black')
#temp.show()
draw.text((60, 273), isim, font=font, fill='black')
#temp.show()
draw.text((60, 300), baba_ismi, font=font, fill='black')
#temp.show()
draw.text((60, 330), anne_ismi, font=font, fill='black')
#temp.show()
draw.text((60, 360), dogum_yeri, font=font, fill='black')
#temp.show()
draw.text((200, 360), dogum_tarihi, font=font, fill='black')
#temp.show()

# 3. ADIM: Kimliğin son halini kaydetmek.
temp.save("metin_sezaigil_kimlik_karti.jpg")

