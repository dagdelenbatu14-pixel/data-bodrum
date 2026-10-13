#!/usr/bin/env python3
"""Data Bodrum sitesini üretir: python3 tools/build.py (site/ kökünden ya da herhangi bir yerden)."""
import json, os, html
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://databodrum.com"
NAME = "Data Bodrum"
PHONE = "0543 399 28 63"
TEL = "+905433992863"
WA = "905433992863"
EMAIL = "info@databodrum.com"
STREET = "Çırkan Mah. Hamza Sadi Özbek Cd. No:23/4"
CITY = "48400 Bodrum / Muğla"
MAPS = "https://www.google.com/maps?cid=14666570202706644658"
REVIEW = "https://g.page/r/CbKOqH3kH4rLEBM/review"
IG = "https://www.instagram.com/databodrum/"
HOURS = "Pazartesi–Cumartesi 09:00–17:00"
AREAS = ["Bodrum Merkez", "Konacık", "Gümbet", "Bitez", "Ortakent", "Yahşi", "Turgutreis", "Akyarlar",
         "Gümüşlük", "Yalıkavak", "Gündoğan", "Göltürkbükü", "Torba"]

e = html.escape

ICON = {
 "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>',
 "wa": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a9.9 9.9 0 0 0-8.5 15l-1.4 5 5.1-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-3-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.4.1-.2 0-.3 0-.5l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .1-1.3c0-.1-.2-.2-.5-.3z"/></svg>',
 "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>',
 "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>',
 "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>',
 "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>',
 "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
 "tool": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.8-3.8a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9z"/></svg>',
 "star": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/></svg>',
 "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>',
 "search": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>',
}
LOGO_MARK = ('<svg class="logo-mark" viewBox="0 0 40 40" aria-hidden="true"><rect width="40" height="40" rx="7" fill="#0F151B"/>'
             '<path d="M12 9.5h7.5a10.5 10.5 0 0 1 0 21H12z" fill="none" stroke="#D24A0E" stroke-width="4"/>'
             '<circle cx="19.5" cy="20" r="3.4" fill="#fff"/></svg>')

# ---------- görseller ----------
IMG = ROOT / "assets" / "img"
_dims = {}
def dims(fn):
    if fn not in _dims:
        with Image.open(IMG / fn) as im: _dims[fn] = im.size
    return _dims[fn]

def img(p, name, alt, sizes="(max-width: 860px) 100vw, 50vw", eager=False, cls=""):
    small = f"{name}-800.webp"; big = f"{name}-1400.webp"
    w, h = dims(small)
    srcset = f'{p}assets/img/{small} {w}w'
    if (IMG / big).exists():
        bw, _ = dims(big); srcset += f', {p}assets/img/{big} {bw}w'
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ""
    return f'<img{c} src="{p}assets/img/{small}" srcset="{srcset}" sizes="{sizes}" width="{w}" height="{h}" alt="{e(alt)}" {load}>'

def cctv(p, name, alt, cam="CAM 01", eager=False):
    return (f'<div class="cctv">{img(p, name, alt, "(max-width: 860px) 100vw, 45vw", eager)}'
            f'<div class="cctv-hud" aria-hidden="true"><span class="rec"><i></i>REC</span><span class="cam">{cam} · BODRUM</span>'
            '<span class="corner c1"></span><span class="corner c2"></span><span class="corner c3"></span><span class="corner c4"></span>'
            '<span class="ts" data-clock>--.--.---- --:--:--</span></div></div>')

ART_FIRE = ('<div class="art-fire" aria-hidden="true"><div class="tag-card"><b>KONTROL ETİKETİ</b>'
            '<div class="line"><span>Cihaz</span><span>KKT 6 kg</span></div>'
            '<div class="line"><span>Son kontrol</span><span>__.__.____</span></div>'
            '<div class="line"><span>Sonraki</span><span>12 ay</span></div></div></div>')
ART_SHUTTER = '<div class="art-shutter" aria-hidden="true"><span>MOTORLU KEPENK</span></div>'

# ---------- hizmetler ----------
SERVICES = {
 "kamera": dict(slug="bodrum-guvenlik-kamera-sistemleri", short="Güvenlik kamerası", nav="Kamera", key="cam",
   title="Bodrum Güvenlik Kamerası Sistemleri | IP Kamera Kurulumu – Data Bodrum",
   desc="Bodrum'da villa, site, otel ve işyerleri için IP ve analog güvenlik kamerası kurulumu, telefondan izleme, plaka tanıma ve bakım. Ücretsiz keşif: 0543 399 28 63",
   h1="Bodrum güvenlik kamerası sistemleri",
   lead="Villa, site, otel ve işyerleri için IP ve analog kamera sistemleri kuruyoruz. Kamerayı yerleştirmeden önce yeri görüyor, kör noktaları ve gece görüşünü hesaba katıyoruz.",
   card="IP ve analog kamera, kayıt cihazı, telefondan canlı izleme, plaka tanıma.",
   hero=("kamera-direk", "Direk üzerine monte edilmiş iki dış mekân güvenlik kamerası"),
   items=[("IP kamera sistemleri","Mevcut ağ altyapısını kullanır, yüksek çözünürlük ve net görüntü verir."),
          ("Analog ve HD kamera","Düşük kablolama maliyetiyle ev, dükkân ve küçük işletmeler için."),
          ("Kayıt cihazı ve disk","NVR/DVR kurulumu; ihtiyaç duyulan gün sayısına göre disk kapasitesi."),
          ("Telefondan izleme","Canlı görüntü ve kayıtları telefondan izleme kurulumu ve kullanım eğitimi."),
          ("Plaka ve yüz tanıma","Site girişleri ve otoparklar için kamera ile bilgisayar entegrasyonu."),
          ("Direk ve dış cephe montajı","Bahçe, sahil ve otopark gibi açık alanlara direk üstü montaj."),
          ("Bakım, onarım ve yükseltme","Mevcut sisteminizin arızası, kamera ekleme ve eski sistemin yenilenmesi.")],
   spec_title="Keşifte neye bakıyoruz",
   spec=[("Çözünürlük","2–8 MP"),("Gece görüşü","IR mesafesi"),("Dış mekân koruma","IP66 / IP67"),("Kayıt süresi","disk kapasitesi"),("Uzaktan izleme","telefon / bilgisayar")],
   where=["Villa bahçesi ve giriş","Site girişi ve otopark","Otel ve restoran","Mağaza ve ofis","Depo ve şantiye","Sahil ve iskele"],
   gallery=[("kamera-montaj-dukkan","Dükkân cephesine kamera montajı"),("kamera-sahil","Sahil işletmesinde dış mekân kamera"),
            ("kamera-direk-deniz","Deniz kenarında direk üstü kamera"),("kamera-kayit-cihazi","Kayıt cihazı ve izleme ekranı"),
            ("kamera-izleme","Bahçe yolu kamera görüntüsü"),("kamera-yakin","Dış mekân bullet kamera")],
   faq=[("Kaç kamera gerekir?","Keşifte giriş, otopark, bahçe ve kör noktaları birlikte gezip kamera sayısını ve yerini belirliyoruz."),
        ("Kayıtlar kaç gün saklanır?","Kamera sayısına, çözünürlüğe ve kayıt cihazındaki diskin kapasitesine bağlıdır. İstediğiniz gün sayısına göre disk boyutunu hesaplıyoruz."),
        ("İnternet kesilince kayıt durur mu?","Hayır. Kayıt cihazı yerel olarak kaydetmeye devam eder; yalnızca telefondan uzaktan izleme bağlantı gelene kadar kesilir."),
        ("Elektrik kesintisinde ne olur?","Kesintisiz güç kaynağı (UPS) eklenirse kameralar ve kayıt cihazı kesinti süresince çalışmaya devam eder."),
        ("Mevcut kameralarıma bakım yapıyor musunuz?","Evet. Başka firmanın kurduğu sistemlerde de arıza tespiti, onarım, kamera ekleme ve yenileme yapıyoruz.")]),
 "yangin": dict(slug="yangin-sistemleri", short="Yangın sistemleri", nav="Yangın", key="fire",
   title="Bodrum Yangın Söndürme ve Algılama Sistemleri | Data Bodrum",
   desc="Bodrum'da yangın algılama, duman dedektörü, yangın tüpü satışı ve periyodik bakım, dolap ve hidrant, sprinkler, davlumbaz söndürme. Ücretsiz danışmanlık: 0543 399 28 63",
   h1="Bodrum yangın söndürme ve algılama sistemleri",
   lead="İşletmenizin, otelinizin ya da villanızın yangın güvenliğini keşiften periyodik bakıma kadar tek ekiple sağlıyoruz. Yangın yönetmeliği (2007/12937) kapsamındaki ihtiyaçlar için ücretsiz danışmanlık veriyoruz.",
   card="Duman dedektörü, yangın tüpü ve periyodik bakım, dolap ve hidrant, sprinkler, davlumbaz söndürme.",
   hero=None,
   items=[("Yangın algılama ve duman dedektörleri","Kablolu ve kablosuz dedektörler, ihbar butonları ve siren."),
          ("Yangın söndürme tüpleri","Satış, montaj ve periyodik bakım; etiket ve kontrol kaydı."),
          ("Yangın dolapları ve hidrant","Bina ve site için dolap, hortum ve hidrant kurulumu."),
          ("Sprinkler sistemleri","Otel, depo ve işletmeler için otomatik söndürme hattı."),
          ("Davlumbaz söndürme sistemi","Restoran ve otel mutfakları için otomatik davlumbaz söndürme."),
          ("Elektrik panosu söndürme","Panoda çıkan yangını kendiliğinden söndüren otomatik sistem."),
          ("Acil çıkış ve yönlendirme levhaları","Kaçış yolları için yönlendirme ve acil çıkış işaretleri."),
          ("Yangın kapıları ve çelik kapılar","Yangına dayanıklı kapı ve çelik kapı uygulamaları."),
          ("Proje, baca temizliği ve gaz bağlantıları","Mimari proje çizimi, baca temizliği ve gaz bağlantı sistemleri.")],
   spec_title="Tüp etiketinde neye bakılır",
   spec=[("Son kontrol tarihi","yılda en az 1"),("Basınç göstergesi","yeşil bölge"),("Mühür ve pim","yerinde"),("Hortum ve nozul","çatlaksız"),("Erişim","önü açık")],
   where=["Restoran ve kafe mutfakları","Otel ve pansiyon","Villa ve site","Mağaza ve ofis","Depo ve işletme","Akaryakıt ve sanayi"],
   gallery=[],
   faq=[("Yangın tüpü ne sıklıkla kontrol edilmeli?","Yılda en az bir kez. Tüpün üzerindeki etikette son kontrol tarihi yazar; tarih geçmişse bizi arayın, yerinde kontrol edip etiketini yenileyelim."),
        ("Restoran mutfağına hangi sistem gerekir?","Davlumbaz altında çıkan yağ yangınları için otomatik davlumbaz söndürme sistemi kurulur. Mutfağın ölçüsüne ve ocak düzenine göre keşifte belirliyoruz."),
        ("Danışmanlık ücretli mi?","Hayır. İlk değerlendirme ve keşif ücretsizdir; ne gerektiğini yazılı olarak iletiyoruz."),
        ("Villa için duman dedektörü kablo çekmeden takılır mı?","Evet. Kablosuz dedektörler duvar kırmadan takılır ve alarm sistemine bağlanabilir."),
        ("Periyodik bakımı siz mi yapıyorsunuz?","Evet. Kurduğumuz ya da mevcut sistemlerin periyodik bakımını, tüp kontrollerini ve dedektör testlerini yapıyoruz.")]),
 "kapi": dict(slug="otomatik-kapi", short="Otomatik kapı", nav="Otomatik Kapı", key="door",
   title="Bodrum Otomatik Kapı Sistemleri | Bahçe ve Garaj Kapısı Motoru – Data Bodrum",
   desc="Bodrum'da kayar ve açılır bahçe kapısı motoru, garaj kapısı, fotoselli kapı ve bariyer kurulumu. Mevcut kapıya motor, kumanda ve arıza servisi: 0543 399 28 63",
   h1="Bodrum otomatik kapı sistemleri",
   lead="Villa ve site girişleri için kayar ve açılır bahçe kapısı motorları, garaj kapıları ve fotoselli kapılar kuruyoruz. Mevcut kapınıza motor takıyor, arızalı motorları onarıyoruz.",
   card="Kayar ve açılır bahçe kapısı motoru, garaj kapısı, fotoselli kapı, kumanda ve arıza servisi.",
   hero=("kapi-kayar-panjur", "Taş duvar arasında koyu renkli panjur tipi kayar bahçe kapısı"),
   items=[("Kayar bahçe kapısı motoru","Ray üzerinde yana kayan kapılar için motor ve kremayer montajı."),
          ("Kanatlı (açılır) kapı motoru","Tek ve çift kanatlı bahçe kapıları için kollu ya da gömme motor."),
          ("Garaj kapısı","Seksiyonel ve kepenk tipi garaj kapıları için motorlu açma."),
          ("Fotoselli otomatik kapı","Mağaza, otel ve ofis girişleri için cam kayar kapı."),
          ("Bariyer ve otopark girişi","Site ve otopark girişleri için bariyer ve giriş-çıkış kontrolü."),
          ("Güvenlik fotoseli ve uyarı lambası","Kapı kapanırken araç ya da insan algılayınca durdurur."),
          ("Kumanda ve arıza servisi","Yeni kumanda tanıtma, motor değişimi, bakım ve onarım.")],
   spec_title="Motor seçiminde ölçülenler",
   spec=[("Kapı ağırlığı","kg"),("Kanat boyu","metre"),("Günlük kullanım","açılma sayısı"),("Elektrik kesintisi","akü / elle açma"),("Güvenlik","fotosel + lamba")],
   where=["Villa bahçe kapıları","Site girişleri","Otopark ve garajlar","Otel ve mağaza girişleri","Depo ve işletmeler"],
   gallery=[("kapi-kayar-motor","Kayar bahçe kapısına motor montajı"),("kapi-montaj","Villa girişinde kapı motoru kurulumu"),
            ("bariyer-otopark","Otopark girişinde bariyer ve kulübe"),("kapi-kayar-panjur","Panjur tipi kayar kapı")],
   faq=[("Mevcut bahçe kapıma motor takılabilir mi?","Kayar ve açılır kapıların çoğuna takılabilir. Keşifte kapının ağırlığına, kanat boyuna ve zemine bakıp uygun motoru belirliyoruz."),
        ("Elektrik kesilince kapı açılır mı?","Motorlarda kilit açma anahtarı bulunur, kapı elle açılır. İsteğe bağlı akü ile kesinti sırasında da motorla çalışır."),
        ("Kumandamı kaybettim, ne yapmalıyım?","Yeni kumandayı mevcut motorunuza tanıtıyoruz; kaybolan kumandayı sistemden silebiliriz."),
        ("Kapı kendiliğinden duruyor ya da geri açılıyor, neden?","Genellikle fotosel hizası, ray ya da limit ayarı kaynaklıdır. Arıza servisimiz yerinde kontrol edip ayarlar."),
        ("Bakım gerekir mi?","Yılda en az bir kez ray, dişli, fotosel ve limit kontrolü önerilir; Bodrum'da tuz ve toz nedeniyle sahile yakın kapılarda daha sık.")]),
 "kepenk": dict(slug="kepenk", short="Kepenk", nav="Kepenk", key="shutter",
   title="Bodrum Otomatik Kepenk | Motorlu Kepenk Kurulumu ve Servisi – Data Bodrum",
   desc="Bodrum'da dükkân, mağaza, depo ve garajlar için motorlu kepenk kurulumu, elle açılan kepenge motor takma, kumanda, bakım ve arıza servisi: 0543 399 28 63",
   h1="Bodrum otomatik kepenk sistemleri",
   lead="Dükkân, mağaza, depo ve garajlar için motorlu kepenk kuruyor, elle açılan kepengi motorlu hale getiriyoruz. Kumanda, bakım ve arıza servisi de bizden.",
   card="Motorlu kepenk kurulumu, elle açılan kepenge motor takma, kumanda ve bakım.",
   hero=("kamera-montaj-dukkan", "Kepenkli dükkân cephesinde güvenlik kamerası montajı yapan teknisyen"),
   items=[("Motorlu kepenk kurulumu","Ölçüye göre kepenk, motor ve kumandanın birlikte kurulumu."),
          ("Elle açılan kepenge motor takma","Mevcut kepengi sökmeden motorlu ve kumandalı hale getirme."),
          ("Kepenk motoru değişimi ve onarımı","Ses yapan, takılan ya da çalışmayan motorların onarımı."),
          ("Kumanda ve duvar butonu","Uzaktan kumanda, anahtarlı buton ve ek kumanda tanıtma."),
          ("Kamera ve alarm ile birlikte","Dükkânın kepengi, kamerası ve alarmı tek ekipten."),
          ("Periyodik bakım","Ray, lamel, motor ve limit ayarı kontrolü.")],
   spec_title="Keşifte ölçülenler",
   spec=[("Açıklık","en × boy"),("Kepenk ağırlığı","kg"),("Mevcut kepenk","elle / motorlu"),("Elektrik kesintisi","elle açma düzeneği"),("Kumanda","adet")],
   where=["Dükkân ve mağaza","Kuyumcu ve eczane","Restoran ve kafe","Market","Depo ve garaj","Otel lobisi ve havuz barı"],
   gallery=[("kamera-montaj-dukkan","Kepenkli dükkân cephesinde kamera montajı")],
   faq=[("Elle açılan kepengim motorlu olabilir mi?","Çoğu kepenge motor eklenebilir. Keşifte kepengin ölçüsüne ve ağırlığına göre motoru seçiyor, mümkünse mevcut kepengi kullanıyoruz."),
        ("Elektrik kesilince kepenk açılır mı?","Kepenk motorlarında elle açma düzeneği bulunur; kesinti sırasında kepenk elle açılıp kapatılabilir."),
        ("Kepenk motoru neden ses yapar ya da takılır?","Ray kirlenmesi, lamel eğilmesi ya da limit ayarı en sık sebeplerdir. Yerinde kontrol edip onarıyoruz."),
        ("Kumandayı çoğaltabilir miyim?","Evet. Ek kumandayı mevcut motorunuza tanıtıyoruz."),
        ("Bakım ne sıklıkla yapılmalı?","Yılda bir kontrol önerilir. Sezon öncesi bakım, yazın yoğun dönemde arıza riskini azaltır.")]),
 "alarm": dict(slug="alarm-sistemleri", short="Alarm sistemleri", nav="Alarm", key="cam", minor=True,
   title="Bodrum Hırsız Alarm Sistemleri | Kablolu ve Kablosuz Alarm – Data Bodrum",
   desc="Bodrum'da villa, site, işyeri ve fabrikalar için kablolu ve kablosuz hırsız alarm sistemi kurulumu, bakım ve servis. Ücretsiz keşif: 0543 399 28 63",
   h1="Bodrum hırsız alarm sistemleri",
   lead="Villa, site, işyeri ve fabrikalarda hırsızlık ve soygun gibi istenmeyen olayları caydırmak için kablolu ve kablosuz alarm sistemleri kuruyoruz.",
   card="Kablolu ve kablosuz alarm, hareket dedektörü, kapı-pencere kontağı, siren.",
   hero=("kamera-agac", "Ağaçlar arasında direk üstü güvenlik ekipmanı"),
   items=[("Kablolu alarm sistemleri","Yeni yapılarda ve tadilatta kalıcı, bakım gerektirmeyen çözüm."),
          ("Kablosuz alarm sistemleri","Duvar kırmadan, mevcut evlere ve işyerlerine hızlı kurulum."),
          ("Hareket dedektörü ve kontaklar","Kapı ve pencere manyetik kontakları, iç ve dış mekân dedektörleri."),
          ("Siren ve uyarı","İç ve dış siren, flaşör ile caydırıcılık."),
          ("Kamera ile birlikte","Alarm ve kamera sistemini tek ekip kurar, birlikte çalışır."),
          ("Bakım ve servis","Pil, dedektör ve panel kontrolü, arıza servisi.")],
   spec_title="Keşifte neye bakıyoruz",
   spec=[("Giriş noktaları","kapı / pencere"),("Kablolama","kablolu / kablosuz"),("Evcil hayvan","uygun dedektör"),("Bildirim","siren / telefon")],
   where=["Villa ve müstakil ev","Site ve apartman","Mağaza ve ofis","Depo ve fabrika"],
   gallery=[],
   faq=[("Kablolu mu kablosuz mu seçmeliyim?","Yeni yapılarda kablolu sistem kalıcıdır; mevcut ve oturulan yerlerde kablosuz sistem duvar kırmadan kurulur. Keşifte birlikte karar veriyoruz."),
        ("Evcil hayvanım dedektörü çalıştırır mı?","Evcil hayvan için uygun dedektörler küçük hayvanları algılamaz. Keşifte evdeki hayvanı sorup ona göre seçiyoruz."),
        ("Alarm kamerayla birlikte çalışır mı?","Evet. Alarm ve kamera sistemini birlikte kurup aynı anda kullanılabilir hale getiriyoruz.")]),
 "gecis": dict(slug="bariyer-gecis-kontrol", short="Bariyer ve geçiş kontrol", nav="Bariyer", key="door", minor=True,
   title="Bodrum Bariyer, Turnike ve Geçiş Kontrol Sistemleri | Data Bodrum",
   desc="Bodrum'da otopark bariyeri, ücretli otopark giriş-çıkış, plaka tanıma, turnike, kartlı geçiş ve görüntülü diafon kurulumu: 0543 399 28 63",
   h1="Bodrum bariyer, turnike ve geçiş kontrol sistemleri",
   lead="Site, otel ve otopark girişleri için bariyer, turnike, kartlı ve şifreli geçiş, plaka tanıma ve görüntülü diafon sistemleri kuruyoruz.",
   card="Otopark bariyeri, plaka tanıma, turnike, kartlı geçiş, görüntülü diafon.",
   hero=("bariyer-otopark", "Site girişinde otopark bariyerleri ve güvenlik kulübesi"),
   items=[("Otopark bariyeri","Site, otel ve işletme otoparkları için bariyer kurulumu."),
          ("Ücretli otopark giriş-çıkış","Giriş-çıkış kontrolü ve ücretli otopark sistemleri."),
          ("Plaka tanıma","Kayıtlı araçlar için bariyerin kendiliğinden açılması."),
          ("Turnike","Personel ve ziyaretçi girişleri için turnike."),
          ("Kartlı ve şifreli geçiş","Kapılar için kart, şifre ya da parmak izi ile geçiş."),
          ("Görüntülü diafon","Villa ve siteler için görüntülü diafon ve tuş takımı."),
          ("Sıramatik","Bekleme salonları için sıra numaratörü.")],
   spec_title="Keşifte neye bakıyoruz",
   spec=[("Şerit sayısı","giriş / çıkış"),("Bariyer kolu","metre"),("Kimlik","kart / plaka / şifre"),("Kayıt","giriş-çıkış raporu")],
   where=["Site ve villa kompleksi","Otel ve tatil köyü","Otopark","İşyeri ve fabrika"],
   gallery=[("bariyer-park","Park alanında bariyer"),("turnike","Gece görünümünde turnike"),("diafon","Görüntülü diafon ve tuş takımı"),("bariyer-otopark","Otopark giriş bariyerleri")],
   faq=[("Plaka tanıma nasıl çalışır?","Girişteki kamera aracın plakasını okur; kayıtlı araçsa bariyer kendiliğinden açılır, giriş-çıkışlar kaydedilir."),
        ("Mevcut bariyerime kartlı geçiş eklenir mi?","Çoğu bariyere kart okuyucu ya da plaka tanıma eklenebilir; keşifte mevcut motoru kontrol ediyoruz.")]),
 "santral": dict(slug="santral-sistemleri", short="Santral sistemleri", nav="Santral", key="cam", minor=True,
   title="Bodrum Santral Sistemleri | Analog ve IP Telefon Santrali – Data Bodrum",
   desc="Bodrum'da otel, ev ve işletmeler için analog ve IP telefon santrali kurulumu, programlama ve servis: 0543 399 28 63",
   h1="Bodrum telefon santral sistemleri",
   lead="Otellerde, evlerde ve işletmelerde birden fazla telefon kullanıcısı arasındaki iletişimi sağlayan, gelen ve giden aramaları yönlendiren analog ve IP santraller kuruyoruz.",
   card="Analog ve IP santral, otel santrali, programlama ve servis.",
   hero=("santral", "Duvara monte edilmiş Karel telefon santrali"),
   items=[("Analog telefon santrali","Küçük işletmeler için; dış hat bekletme, çağrı kısıtlama ve yönlendirme, gece servisi."),
          ("IP telefon santrali","Mevcut ağ altyapısını kullanır; şubeler arası ücretsiz görüşme, yüksek ses kalitesi."),
          ("Otel santrali","Oda telefonları, resepsiyon yönlendirme ve uyandırma servisi."),
          ("Programlama ve servis","Dahili numara, karşılama mesajı, uzaktan programlama ve arıza servisi.")],
   spec_title="Keşifte neye bakıyoruz",
   spec=[("Dahili sayısı","adet"),("Dış hat","analog / IP"),("Altyapı","kablo / ağ")],
   where=["Otel ve pansiyon","Ofis ve işyeri","Villa"], gallery=[],
   faq=[("Analog mu IP santral mi?","Az dahili ve basit ihtiyaçta analog santral yeterlidir. Birden fazla şube ya da büyük işletmede IP santral avantajlıdır.")]),
 "network": dict(slug="network-sistemleri", short="Network ve bilişim", nav="Network", key="cam", minor=True,
   title="Bodrum Network ve Kablolama Sistemleri | Wi-Fi, Bilişim – Data Bodrum",
   desc="Bodrum'da network kablolama altyapısı, Wi-Fi kapsama, kabinet, bilgisayar bakım onarım ve telefon çekmeyen yerler için mini baz istasyonu: 0543 399 28 63",
   h1="Bodrum network ve bilişim sistemleri",
   lead="Ev, otel ve işyerlerinde network altyapısını kuruyor, Wi-Fi kapsamasını genişletiyor ve bilgisayar sistemlerinin bakımını yapıyoruz.",
   card="Kablolama, Wi-Fi, kabinet, bilgisayar bakım onarım, mini baz istasyonu.",
   hero=("kamera-kafe", "Taş binalı kafe cephesinde kamera ve ağ altyapısı"),
   items=[("Yapısal kablolama","Kamera, santral ve bilgisayarlar için düzenli ağ altyapısı."),
          ("Wi-Fi kapsama","Villa ve otellerde bahçe ve havuz dahil kesintisiz kablosuz ağ."),
          ("Mini baz istasyonu","Telefonun çekmediği bölgeler için mini baz istasyonu çözümleri."),
          ("Bilgisayar bakım ve onarım","Masaüstü ve dizüstü bilgisayar arızası, bakım ve kurulum."),
          ("Barkod ve restoran yazılımları","Barkod okuyucu, stok ve kafe-restoran sistemleri."),
          ("Telsiz haberleşme","İşletmeler ve tekneler için telsiz sistemleri.")],
   spec_title="Keşifte neye bakıyoruz",
   spec=[("Alan","m² / kat"),("Kullanıcı","cihaz sayısı"),("Kapsama","bahçe / havuz")],
   where=["Villa","Otel ve pansiyon","Ofis","Restoran ve kafe"], gallery=[],
   faq=[("Bahçede ve havuz başında Wi-Fi çekmiyor, ne yapılır?","Dış mekâna uygun erişim noktalarıyla kapsama genişletilir; keşifte çekmeyen noktaları ölçüyoruz.")]),
}
MAIN = ["kamera", "yangin", "kapi", "kepenk"]
MINOR = ["alarm", "gecis", "santral", "network"]

def url(slug): return f"{BASE}/" + (f"{slug}/" if slug else "")

# ---------- ortak parçalar ----------
def head(p, title, desc, slug, extra_ld, og_img="og.jpg"):
    can = url(slug)
    ld = "\n".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in extra_ld)
    return f'''<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{can}">
<meta name="theme-color" content="#0F151B">
<meta property="og:type" content="website">
<meta property="og:locale" content="tr_TR">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{can}">
<meta property="og:image" content="{BASE}/assets/{og_img}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{p}assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{p}assets/apple-touch-icon.png">
<link rel="preload" href="{p}assets/fonts/barlow-condensed-700-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{p}assets/fonts/ibm-plex-sans-400-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{p}assets/styles.css">
{ld}
</head>
<body>
<a class="skip" href="#icerik">İçeriğe geç</a>
'''

def header(p, cur):
    links = [(SERVICES[k]["nav"], f'{p}{SERVICES[k]["slug"]}/', k) for k in MAIN]
    links += [("Diğer sistemler", f"{p}#diger", "diger"), ("Hakkımızda", f"{p}hakkimizda/", "hakkimizda"), ("İletişim", f"{p}iletisim/", "iletisim")]
    nav = "".join(f'<a href="{h}"{" aria-current=page" if k == cur else ""}>{t}</a>' for t, h, k in links)
    mob = "".join(f'<a href="{h}">{t}</a>' for t, h, k in links)
    return f'''<header class="top"><div class="wrap">
<a class="logo" href="{p or './'}" aria-label="{NAME} ana sayfa">{LOGO_MARK}<span class="logo-text"><b>DATA</b><span>BODRUM</span></span></a>
<nav class="nav" aria-label="Ana menü">{nav}</nav>
<a class="btn btn-primary top-call" href="tel:{TEL}">{ICON["phone"]}{PHONE}</a>
<details class="menu"><summary aria-label="Menüyü aç">{ICON["menu"]}</summary><nav class="menu-panel" aria-label="Mobil menü">{mob}<a href="tel:{TEL}">Ara: {PHONE}</a></nav></details>
</div></header>
<main id="icerik">
'''

def quote_section(p, preset=""):
    opts = "".join(f'<option{" selected" if SERVICES[k]["short"] == preset else ""}>{SERVICES[k]["short"]}</option>' for k in MAIN + MINOR)
    areas = "".join(f"<option>{a}</option>" for a in AREAS) + "<option>Diğer</option>"
    return f'''<section class="sec sec-dark" id="teklif" aria-labelledby="teklif-h"><div class="wrap quote">
<div>
<p class="eyebrow">Ücretsiz keşif</p>
<h2 id="teklif-h">Yerinde bakalım, doğru sistemi birlikte seçelim</h2>
<p class="lead muted" style="margin-top:14px">Formu doldurun, mesajınız WhatsApp'tan bize gelsin. Ya da doğrudan arayın.</p>
<ul class="contact-list">
<li>{ICON["phone"]}<span><a href="tel:{TEL}">{PHONE}</a><small>Telefon ve WhatsApp</small></span></li>
<li>{ICON["clock"]}<span>{HOURS}<small>Kurulu sistemler için 7/24 teknik destek</small></span></li>
<li>{ICON["pin"]}<span>{STREET}, {CITY}<small><a href="{MAPS}" rel="noopener">Haritada aç ve yol tarifi al</a></small></span></li>
</ul>
</div>
<form class="qf" id="qf" novalidate>
<div class="row">
<label for="qf-ad">Adınız<input id="qf-ad" name="ad" autocomplete="name" required></label>
<label for="qf-tel">Telefonunuz<input id="qf-tel" name="tel" type="tel" autocomplete="tel" inputmode="tel" required></label>
</div>
<div class="row">
<label for="qf-hizmet">Hizmet<select id="qf-hizmet" name="hizmet">{opts}</select></label>
<label for="qf-bolge">Bölge<select id="qf-bolge" name="bolge">{areas}</select></label>
</div>
<label for="qf-not">Kısaca ihtiyacınız<textarea id="qf-not" name="not" placeholder="Örn. villa bahçesi için 6 kamera, kayar kapıya motor"></textarea></label>
<p class="err" id="qf-err" role="alert" hidden>Lütfen adınızı ve telefonunuzu yazın.</p>
<button class="btn btn-wa" type="submit">{ICON["wa"]}WhatsApp ile gönder</button>
<p class="hint">Bilgileriniz sitede saklanmaz; yalnızca WhatsApp mesajı olarak bize iletilir.</p>
</form>
</div></section>
'''

def minis(p, skip=None):
    cards = "".join(f'<a class="mini" href="{p}{SERVICES[k]["slug"]}/"><b>{SERVICES[k]["short"]}</b><span>{SERVICES[k]["card"]}</span></a>' for k in MINOR if k != skip)
    return cards

def footer(p):
    svc = "".join(f'<li><a href="{p}{SERVICES[k]["slug"]}/">{SERVICES[k]["short"]}</a></li>' for k in MAIN + MINOR)
    return f'''</main>
<section class="cta"><div class="wrap"><h2>Keşif ücretsiz. Arayın, yerinde bakalım.</h2>
<div class="btns"><a class="btn btn-primary" href="tel:{TEL}">{ICON["phone"]}{PHONE}</a><a class="btn btn-line" href="https://wa.me/{WA}" rel="noopener">{ICON["wa"]}WhatsApp</a></div></div></section>
<footer class="foot"><div class="wrap">
<div><a class="logo" href="{p or './'}">{LOGO_MARK}<span class="logo-text"><b>DATA</b><span>BODRUM</span></span></a>
<p>Data Bilişim ve Otomasyon. 2016'dan beri Bodrum'da güvenlik ve otomasyon sistemleri.</p></div>
<div><h3>Hizmetler</h3><ul>{svc}</ul></div>
<div><h3>İletişim</h3><ul><li><a href="tel:{TEL}">{PHONE}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li>{STREET}<br>{CITY}</li><li>{HOURS}</li></ul></div>
<div><h3>Bizi bulun</h3><ul><li><a href="{MAPS}" rel="noopener">Google Haritalar</a></li><li><a href="{REVIEW}" rel="noopener">Google'da yorum yazın</a></li><li><a href="{IG}" rel="noopener">Instagram</a></li><li><a href="{p}hakkimizda/">Hakkımızda</a></li><li><a href="{p}gizlilik-politikasi/">Gizlilik</a></li></ul></div>
<div class="foot-bottom"><span>© 2016–<span data-year>2026</span> {NAME}</span><span>Bodrum yarımadasının tamamına servis</span></div>
</div></footer>
<nav class="actionbar" aria-label="Hızlı iletişim"><a href="tel:{TEL}">{ICON["phone"]}Ara</a><a class="wa" href="https://wa.me/{WA}" rel="noopener">{ICON["wa"]}WhatsApp</a><a class="ks" href="#teklif">{ICON["search"]}Keşif iste</a></nav>
<script src="{p}assets/script.js" defer></script>
</body>
</html>
'''

def faq_html(faq):
    return '<div class="faq">' + "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in faq) + "</div>"

def faq_ld(faq):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}

def crumbs_ld(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]}

BUSINESS = {
 "@context": "https://schema.org", "@type": "LocalBusiness", "@id": f"{BASE}/#isletme",
 "name": NAME, "alternateName": "Data Bilişim ve Otomasyon", "url": f"{BASE}/",
 "telephone": "+90 543 399 28 63", "email": EMAIL, "foundingDate": "2016",
 "image": f"{BASE}/assets/og.jpg", "logo": f"{BASE}/assets/apple-touch-icon.png",
 "description": "Bodrum'da güvenlik kamerası, yangın algılama ve söndürme, otomatik kapı, bariyer ve motorlu kepenk sistemleri kurulumu, bakımı ve 7/24 teknik destek.",
 "address": {"@type": "PostalAddress", "streetAddress": STREET, "addressLocality": "Bodrum", "addressRegion": "Muğla", "postalCode": "48400", "addressCountry": "TR"},
 "geo": {"@type": "GeoCoordinates", "latitude": 37.0552033, "longitude": 27.3990376},
 "hasMap": MAPS,
 "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "opens": "09:00", "closes": "17:00"}],
 "areaServed": [{"@type": "Place", "name": f"{a}, Bodrum"} for a in AREAS],
 "sameAs": [IG],
 "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Hizmetler", "itemListElement": [
     {"@type": "Offer", "itemOffered": {"@type": "Service", "name": SERVICES[k]["short"], "url": url(SERVICES[k]["slug"])}} for k in MAIN + MINOR]},
}

def write(rel, text):
    f = ROOT / rel; f.parent.mkdir(parents=True, exist_ok=True); f.write_text(text, encoding="utf-8")

# ---------- ana sayfa ----------
def home():
    p = ""
    def pillar(k, media):
        s = SERVICES[k]
        return (f'<a class="pillar k-{s["key"]}" href="{s["slug"]}/"><div class="pillar-media">{media}</div>'
                f'<div class="pillar-body"><h3>{s["short"]}</h3><p>{s["card"]}</p><span class="more">Detaylar{ICON["arrow"]}</span></div></a>')
    pillars = (pillar("kamera", img(p, "kamera-direk-deniz", "Deniz kenarında direk üstü güvenlik kameraları", "(max-width:560px) 100vw, 25vw"))
               + pillar("yangin", ART_FIRE)
               + pillar("kapi", img(p, "kapi-kayar-panjur", "Panjur tipi kayar bahçe kapısı", "(max-width:560px) 100vw, 25vw"))
               + pillar("kepenk", ART_SHUTTER))
    gal = [("kamera-direk", "Direk üstü kamera", "tall"), ("kapi-kayar-motor", "Kayar kapı motoru", ""), ("bariyer-otopark", "Otopark bariyeri", ""),
           ("kamera-montaj-dukkan", "Dükkân cephesine kamera", ""), ("turnike", "Turnike", ""), ("kamera-sahil", "Sahilde dış mekân kamera", "tall"),
           ("diafon", "Görüntülü diafon", ""), ("santral", "Telefon santrali", ""), ("kamera-kayit-cihazi", "Kayıt cihazı ve izleme", ""), ("kapi-montaj", "Villa girişinde kapı motoru", "")]
    gallery = "".join(f'<figure class="{c}">{img(p, n, cap, "(max-width:860px) 50vw, 25vw")}<figcaption>{cap}</figcaption></figure>' for n, cap, c in gal)
    reviews = [("İlgi ve alakalarından dolayı teşekkür ederim, özellikle Ersin Bey bütün sorunlarla ilgilendi ve çözüm getirdi.", "Seher Y."),
               ("Yapılan işlemler başarılı, çok memnun kaldık. Her şey istediğimiz gibi gelişti ve sonuçlandı.", "Taner G."),
               ("Evimin internetini Ersin Bey kolaylıkla halletti, çok teşekkür ederim.", "Zeynep B.")]
    rev = "".join(f'<blockquote class="review"><span class="stars" aria-label="5 üzerinden 5 yıldız">★★★★★</span><p>{e(t)}</p><footer>{n} · Google yorumu</footer></blockquote>' for t, n in reviews)
    faq = [("Keşif ücretli mi?", "Hayır. Bodrum yarımadasında keşif ücretsizdir; yerinde bakıp ihtiyacınızı birlikte belirliyoruz."),
           ("Hangi bölgelere hizmet veriyorsunuz?", "Bodrum yarımadasının tamamına: " + ", ".join(AREAS) + "."),
           ("Kamera görüntülerini telefondan izleyebilir miyim?", "Evet. Kurulumda telefon uygulamasını ayarlıyor, canlı görüntü ve kayıt izlemeyi gösteriyoruz."),
           ("Mevcut bahçe kapıma ya da kepengime motor takılır mı?", "Çoğu kapıya ve kepenge takılabilir. Keşifte ağırlık ve ölçüye göre uygun motoru belirliyoruz."),
           ("Kurduğunuz sistemlere bakım yapıyor musunuz?", "Evet. Periyodik bakım, arıza servisi ve 7/24 teknik destek veriyoruz; yangın tüplerinin yıllık kontrolü de buna dahil.")]
    title = "Bodrum Kamera, Yangın, Otomatik Kapı ve Kepenk Sistemleri | Data Bodrum"
    desc = "2016'dan beri Bodrum'da güvenlik kamerası, yangın algılama ve söndürme, otomatik kapı, bariyer ve motorlu kepenk kurulumu. Ücretsiz keşif, bakım, 7/24 destek: 0543 399 28 63"
    site_ld = {"@context": "https://schema.org", "@type": "WebSite", "name": NAME, "url": f"{BASE}/", "inLanguage": "tr-TR", "publisher": {"@id": f"{BASE}/#isletme"}}
    out = head(p, title, desc, "", [BUSINESS, site_ld, faq_ld(faq)]) + header(p, "home") + f'''
<section class="hero"><div class="wrap">
<div>
<p class="eyebrow" style="color:#FF8A4C">Data Bodrum · Bilişim ve Otomasyon</p>
<h1 style="margin-top:14px">Bodrum'da <em>kamera, yangın, otomatik kapı ve kepenk</em> sistemleri</h1>
<p class="lead">Villanıza, sitenize, otelinize ya da dükkânınıza gereken güvenlik ve otomasyon sistemlerini tek ekip kuruyor. Keşif ücretsiz, kurulu sistemlere 7/24 teknik destek.</p>
<div class="btns"><a class="btn btn-primary" href="#teklif">Ücretsiz keşif iste{ICON["arrow"]}</a><a class="btn btn-line" href="tel:{TEL}">{ICON["phone"]}{PHONE}</a></div>
<ul class="facts">
<li>{ICON["shield"]}2016'dan beri Bodrum'da</li>
<li>{ICON["pin"]}Yarımadanın her yerine servis</li>
<li>{ICON["tool"]}7/24 teknik destek</li>
<li>{ICON["star"]}Google puanı 5,0</li>
</ul>
</div>
{cctv(p, "kamera-direk", "Mavi gökyüzü önünde direk üzerindeki iki güvenlik kamerası", "CAM 01", eager=True)}
</div></section>

<section class="sec" aria-labelledby="alanlar-h"><div class="wrap">
<div class="sec-head"><p class="eyebrow">Dört ana alan</p><h2 id="alanlar-h">Güvenliği tek firmadan kurun</h2>
<p class="muted lead">Kamerayı bir firmaya, kapıyı ikincisine, yangın tüpünü üçüncüsüne yaptırmayın. Keşfi, kurulumu ve bakımı tek ekip yapsın.</p></div>
<div class="pillars">{pillars}</div>
</div></section>

<section class="sec sec-tight sec-white" id="diger" aria-labelledby="diger-h"><div class="wrap">
<div class="sec-head"><p class="eyebrow">Diğer sistemler</p><h2 id="diger-h">Alarmdan santrale</h2></div>
<div class="minis">{minis(p)}</div>
</div></section>

<section class="sec sec-dark" aria-labelledby="kim-h"><div class="wrap">
<div class="sec-head"><p class="eyebrow">Kimler için</p><h2 id="kim-h">Bodrum'un villasından beach club'ına</h2></div>
<ul class="who"><li>Villa ve müstakil ev</li><li>Site ve apartman yönetimi</li><li>Otel ve pansiyon</li><li>Restoran, kafe ve beach club</li><li>Mağaza ve ofis</li><li>Depo, sanayi ve şantiye</li><li>Marina ve tekne</li></ul>
</div></section>

<section class="sec" aria-labelledby="surec-h"><div class="wrap">
<div class="sec-head"><p class="eyebrow">Nasıl çalışıyoruz</p><h2 id="surec-h">Keşiften bakıma dört adım</h2></div>
<ol class="steps">
<li><h3>Ücretsiz keşif</h3><p>Yerinde bakıyor, ihtiyacı ve kör noktaları birlikte belirliyoruz.</p></li>
<li><h3>Yazılı teklif</h3><p>Malzeme ve işçiliği açıkça yazılı olarak iletiyoruz.</p></li>
<li><h3>Kurulum</h3><p>Kablolama, montaj, ayar ve kullanım eğitimi.</p></li>
<li><h3>Bakım ve destek</h3><p>Periyodik bakım, arıza servisi ve 7/24 teknik destek.</p></li>
</ol>
</div></section>

<section class="sec sec-white" aria-labelledby="isler-h"><div class="wrap">
<div class="sec-head"><p class="eyebrow">İşlerimizden</p><h2 id="isler-h">Bodrum'da kurduğumuz sistemler</h2></div>
<div class="gallery">{gallery}</div>
</div></section>

<section class="sec" aria-labelledby="yorum-h"><div class="wrap">
<div class="sec-head"><p class="eyebrow">Müşterilerimiz</p><h2 id="yorum-h">Google'da 5,0 puan</h2></div>
<div class="reviews">{rev}</div>
<p style="margin-top:20px"><a href="{REVIEW}" rel="noopener">Bizimle çalıştıysanız Google'da yorumunuzu yazın</a></p>
</div></section>

<section class="sec sec-tight sec-white" aria-labelledby="bolge-h"><div class="wrap">
<div class="sec-head"><p class="eyebrow">Hizmet bölgeleri</p><h2 id="bolge-h">Bodrum yarımadasının tamamı</h2></div>
<ul class="areas">{"".join(f"<li>{a}</li>" for a in AREAS)}</ul>
</div></section>

<section class="sec" aria-labelledby="sss-h"><div class="wrap">
<div class="sec-head"><p class="eyebrow">Sık sorulanlar</p><h2 id="sss-h">Merak edilenler</h2></div>
{faq_html(faq)}
</div></section>
''' + quote_section(p) + footer(p)
    write("index.html", out)

# ---------- hizmet sayfası ----------
def service(k):
    s = SERVICES[k]; p = "../"
    media = cctv(p, s["hero"][0], s["hero"][1], "CAM 02", eager=True) if s.get("hero") else f'<div class="cctv" style="aspect-ratio:4/3">{ART_FIRE}</div>'
    items = "".join(f'<li>{ICON["check"]}<span><b>{e(t)}</b><span>{e(d)}</span></span></li>' for t, d in s["items"])
    spec = "".join(f"<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>" for a, b in s["spec"])
    where = "".join(f"<li>{e(w)}</li>" for w in s["where"])
    gal = ""
    if s["gallery"]:
        figs = "".join(f'<figure>{img(p, n, cap, "(max-width:860px) 50vw, 25vw")}<figcaption>{e(cap)}</figcaption></figure>' for n, cap in s["gallery"])
        gal = f'<section class="sec sec-white" aria-labelledby="g-h"><div class="wrap"><div class="sec-head"><p class="eyebrow">İşlerimizden</p><h2 id="g-h">Sahadan fotoğraflar</h2></div><div class="gallery">{figs}</div></div></section>'
    others = "".join(f'<a class="mini" href="{p}{SERVICES[o]["slug"]}/"><b>{SERVICES[o]["short"]}</b><span>{SERVICES[o]["card"]}</span></a>' for o in MAIN + MINOR if o != k)
    svc_ld = {"@context": "https://schema.org", "@type": "Service", "name": s["h1"][0].upper() + s["h1"][1:], "serviceType": s["short"],
              "url": url(s["slug"]), "description": s["desc"], "provider": {"@id": f"{BASE}/#isletme"},
              "areaServed": [{"@type": "Place", "name": f"{a}, Bodrum"} for a in AREAS]}
    lds = [BUSINESS, svc_ld, faq_ld(s["faq"]), crumbs_ld([("Ana sayfa", f"{BASE}/"), (s["short"], url(s["slug"]))])]
    out = head(p, s["title"], s["desc"], s["slug"], lds) + header(p, k) + f'''
<section class="page-hero"><div class="wrap">
<div>
<nav class="crumbs" aria-label="Konum"><a href="../">Ana sayfa</a> / {e(s["short"])}</nav>
<p class="tagline" style="color:#fff"><i style="background:var(--{s["key"]})"></i>{e(s["short"])}</p>
<h1>{e(s["h1"][0].upper() + s["h1"][1:])}</h1>
<p class="lead">{e(s["lead"])}</p>
<div class="btns"><a class="btn btn-primary" href="#teklif">Ücretsiz keşif iste{ICON["arrow"]}</a><a class="btn btn-line" href="tel:{TEL}">{ICON["phone"]}{PHONE}</a></div>
</div>
{media}
</div></section>

<section class="sec" aria-labelledby="neler-h"><div class="wrap split k-{s["key"]}">
<div><div class="sec-head"><p class="eyebrow">Neler yapıyoruz</p><h2 id="neler-h">{e(s["short"])} hizmetlerimiz</h2></div>
<ul class="checks">{items}</ul>
<div class="sec-head" style="margin:44px 0 16px"><p class="eyebrow">Nerelerde</p><h2 style="font-size:30px">Kurduğumuz yerler</h2></div>
<ul class="areas">{where}</ul>
</div>
<aside class="aside"><h3>{e(s["spec_title"])}</h3><dl class="spec">{spec}</dl>
<p class="muted" style="font-size:15px">Keşif ücretsiz. Yerinde ölçüp yazılı teklif veriyoruz.</p>
<a class="btn btn-primary" href="#teklif">Keşif randevusu al</a></aside>
</div></section>
{gal}
<section class="sec" aria-labelledby="sss-h"><div class="wrap">
<div class="sec-head"><p class="eyebrow">Sık sorulanlar</p><h2 id="sss-h">{e(s["short"])} hakkında</h2></div>
{faq_html(s["faq"])}
</div></section>
''' + quote_section(p, s["short"]) + f'''
<section class="sec sec-tight" aria-labelledby="diger-h"><div class="wrap">
<div class="sec-head"><p class="eyebrow">Diğer hizmetlerimiz</p><h2 id="diger-h">Hepsi tek ekipten</h2></div>
<div class="minis">{others}</div></div></section>
''' + footer(p)
    write(f'{s["slug"]}/index.html', out)

# ---------- basit sayfalar ----------
def simple(slug, cur, title, desc, h1, body_html, preset=""):
    p = "../"
    lds = [BUSINESS, crumbs_ld([("Ana sayfa", f"{BASE}/"), (h1, url(slug))])]
    out = head(p, title, desc, slug, lds) + header(p, cur) + f'''
<section class="page-hero"><div class="wrap" style="grid-template-columns:minmax(0,1fr)">
<div><nav class="crumbs" aria-label="Konum"><a href="../">Ana sayfa</a> / {e(h1)}</nav><h1>{e(h1)}</h1></div>
</div></section>
<section class="sec"><div class="wrap prose">{body_html}</div></section>
''' + (quote_section(p, preset) if preset is not None else "") + footer(p)
    write(f"{slug}/index.html", out)

def redirect(slug, target):
    write(f"{slug}/index.html", f'''<!doctype html><html lang="tr"><head><meta charset="utf-8"><title>Yönlendiriliyor</title>
<link rel="canonical" href="{url(target)}"><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0; url=../{target}/">
</head><body><p><a href="../{target}/">{url(target)}</a></p></body></html>
''')

def build():
    css = (ROOT / "assets" / "_fontface.css").read_text() + "\n" + (ROOT / "assets" / "_main.css").read_text()
    write("assets/styles.css", css)
    home()
    for k in MAIN + MINOR: service(k)
    simple("hakkimizda", "hakkimizda", "Hakkımızda | Data Bodrum – 2016'dan beri Bodrum'da",
           "Data Bodrum 2016'dan beri Bodrum yarımadasında güvenlik kamerası, yangın, otomatik kapı, kepenk, alarm ve santral sistemleri kuruyor.",
           "Hakkımızda", f'''<p class="lead">Data Bodrum, 2016 yılında "müşterilerine dünya standartlarında, teknolojik çözümler sunmak" ilkesiyle Bodrum'da kuruldu.</p>
<p>O günden bu yana Bodrum yarımadasında villalardan otellere, dükkânlardan site girişlerine kadar küçük ve büyük ölçekli pek çok projede kamera, alarm, otomatik kapı, bariyer, santral ve network sistemleri kurduk. Bugün yangın algılama ve söndürme sistemleri ile motorlu kepenkleri de yapıyoruz.</p>
<h2>Nasıl çalışırız</h2>
<p>Her işe ücretsiz keşifle başlarız. Yeri görmeden fiyat vermeyiz; çünkü bir villanın bahçesinde gereken kamera sayısı da, bir kapının motoru da ancak yerinde ölçülerek doğru seçilir. Kurduğumuz sistemlerin bakımını da biz yaparız ve kurulu sistemlere 7/24 teknik destek veririz.</p>
<h2>Bize ulaşın</h2>
<p>{STREET}, {CITY}<br><a href="tel:{TEL}">{PHONE}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a><br>{HOURS}</p>''')
    simple("iletisim", "iletisim", "İletişim | Data Bodrum – 0543 399 28 63",
           "Data Bodrum iletişim: Çırkan Mah. Hamza Sadi Özbek Cd. No:23/4 Bodrum. Telefon ve WhatsApp 0543 399 28 63. Ücretsiz keşif için arayın.",
           "İletişim", f'''<p class="lead">Ücretsiz keşif ve teklif için arayın, WhatsApp'tan yazın ya da aşağıdaki formu doldurun.</p>
<p><b>Telefon ve WhatsApp:</b> <a href="tel:{TEL}">{PHONE}</a><br><b>E-posta:</b> <a href="mailto:{EMAIL}">{EMAIL}</a><br><b>Adres:</b> {STREET}, {CITY}<br><b>Çalışma saatleri:</b> {HOURS}</p>
<div class="btns"><a class="btn btn-primary" href="{MAPS}" rel="noopener">{ICON["pin"]}Haritada aç</a><a class="btn btn-wa" href="https://wa.me/{WA}" rel="noopener">{ICON["wa"]}WhatsApp</a></div>''')
    simple("gizlilik-politikasi", "", "Gizlilik Politikası | Data Bodrum",
           "Data Bodrum web sitesi gizlilik ve kişisel verilerin korunması bilgilendirmesi.",
           "Gizlilik politikası", f'''<p>Bu site çerez kullanmaz, ziyaretçi takibi ya da reklam ölçümü yapmaz. Yazı tipleri ve görseller sitenin kendi sunucusundan yüklenir.</p>
<p>Teklif formuna yazdığınız ad, telefon ve not sitede saklanmaz. "WhatsApp ile gönder" düğmesine bastığınızda bu bilgiler WhatsApp uygulamanızda mesaj olarak açılır ve yalnızca siz gönderirseniz bize ulaşır.</p>
<p>Bize ilettiğiniz kişisel veriler 6698 sayılı Kişisel Verilerin Korunması Kanunu'na uygun olarak yalnızca keşif, teklif ve hizmet amacıyla kullanılır, üçüncü kişilerle paylaşılmaz. Verilerinizle ilgili talepleriniz için <a href="mailto:{EMAIL}">{EMAIL}</a> adresine yazabilirsiniz.</p>
<p>Veri sorumlusu: {NAME}, {STREET}, {CITY}.</p>''', preset=None)
    redirect("bilgisayar-bilisim-sistemleri", "network-sistemleri")
    # 404
    write("404.html", head("/", "Sayfa bulunamadı | Data Bodrum", "Aradığınız sayfa bulunamadı.", "404", []).replace('<link rel="canonical" href="https://databodrum.com/404/">', '<meta name="robots" content="noindex">')
          + header("/", "") + f'''<section class="page-hero"><div class="wrap" style="grid-template-columns:minmax(0,1fr)"><div><h1>Bu sayfa bulunamadı</h1>
<p class="lead">Aradığınız sayfa taşınmış olabilir. Ana sayfadan devam edin ya da bizi arayın: <a style="color:#FF8A4C" href="tel:{TEL}">{PHONE}</a></p>
<div class="btns"><a class="btn btn-primary" href="/">Ana sayfa</a></div></div></div></section>''' + footer("/"))
    pages = [""] + [SERVICES[k]["slug"] for k in MAIN + MINOR] + ["hakkimizda", "iletisim", "gizlilik-politikasi"]
    sm = "".join(f"<url><loc>{url(s)}</loc></url>" for s in pages)
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm}</urlset>\n')
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    print("ok", len(pages), "sayfa")

if __name__ == "__main__":
    build()
