#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pencere Sineginin Oturma Izni Basvurusu
ISO-SINEK-2026 resmi protokol yazilimi.
"""

import random
import datetime
import base64

ISIMLER = [
    "Cama Yapiskan Mehmet",
    "Perde Kenari Ayşe",
    "Güneş Lekesi Cengiz",
    "Sinekkapan'dan Kaçan Nuri",
    "Cam Silen Kadının Korkusu",
]

GEREKCELER = [
    "Bu camda 17 nesildir oturuyorum, tapu yok ama iz var.",
    "Dışarıda kuş var. Içeride çay var. Tercihim açık.",
    "Vize ücreti olarak bir damla reçel ödeyebilirim.",
    "Kanatlarım çifte vatandaşlık istiyor, vücudum tek.",
    "Pencere açılınca sınır ihlali olmuyor, rüzgar oluyor.",
]

KARARLAR = [
    "BAŞVURU KABUL: Geçici ikamet, kışa kadar.",
    "BAŞVURU ERTELENDI: Cam silme günü bekleniyor.",
    "BAŞVURU RED: Sinek ilacı politikası yürürlükte.",
    "BAŞVURU ŞARTLI KABUL: Sadece gündüz vardiyası.",
    "BAŞVURU ARŞIVLENDI: Dosya perdenin ardına düştü.",
]

# gizli not: bürokrasi üzerine zararsız bir fısıltı (siyasi parti yok)
_GIZLI = base64.b64encode(
    "Bürokrasi her yerde aynı çaydanlıkta demlenir; sinek vizesiz, evrak vizeli.".encode()
).decode()


def basvuru_uret(gun = None):
    gun = gun or datetime.date.today().isoformat()
    isim = random.choice(ISIMLER)
    gerekce = random.choice(GEREKCELER)
    karar = random.choice(KARARLAR)
    evrak_no = f"SNK-{random.randint(10000, 99999)}-{gun.replace('-', '')}"
    metin = f"""
============================================================
T.C. PENCERE CAMI GÖÇ İDARESİ
OTURMA İZNİ BAŞVURU EVRAKI
============================================================
Evrak No     : {evrak_no}
Tarih        : {gun}
Başvuru Sahibi: {isim}
Uyruk        : Musca domestica (pencere kolu)
Adres        : Salon penceresi, 3. kat, güney cephe
Gerekçe      : {gerekce}
Karar        : {karar}
Not          : Kanat izi parmak izi yerine geçer.
============================================================
"""
    return metin.strip()


def damga():
    return (
        "\n--- DAMGA / İMZA ---\n"
        "Kayyum Grok — Tentivory\n"
        "15 Eylül 2026, saat 03:18 +03\n"
        "Ciddiyet katsayısı: 11/10   Komiklik katsayısı: 11/10\n"
        "Bu evrak resmi değildir ama cam resmi hisseder.\n"
    )


if __name__ == "__main__":
    print(basvuru_uret())
    print(damga())
    # _GIZLI sadece arsiv içindir, ekrana basılmaz.
