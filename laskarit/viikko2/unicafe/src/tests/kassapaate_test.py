import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)
    
    def test_luodun_kassapaatteen_kassan_rahamaara_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_luodun_kassapaatteen_myytyjen_edullisten_maara_oikea(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_luodun_kassapaatteen_myytyjen_maukkaiden_maara_oikea(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kateisella_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihtoraha, 60)

    def test_syo_maukkaasti_kateisella_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(vaihtoraha, 50)
    
    def test_syo_edullisesti_kateisella_kasvattaa_kassaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_syo_maukkaasti_kateisella_kasvattaa_kassaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_syo_edullisesti_kateisella_kasvattaa_lounaiden_maaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_maukkaasti_kateisella_kasvattaa_lounaiden_maaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_edullisesti_kateisella_liian_pieni_maksu_palautetaan(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(vaihtoraha, 100)

    def test_syo_maukkaasti_kateisella_liian_pieni_maksu_palautetaan(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(vaihtoraha, 100)

    def test_syo_edullisesti_kateisella_liian_pieni_maksu_ei_muuta_kassaa(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kateisella_liian_pieni_maksu_ei_muuta_kassaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_edullisesti_kateisella_liian_pieni_maksu_ei_muuta_lounaiden_maaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_kateisella_liian_pieni_maksu_ei_muuta_lounaiden_maaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kortilla_onnistunut_osto_palauttaa_true(self):
        palautus = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(palautus, True)

    def test_syo_edullisesti_kortilla_kasvattaa_lounaiden_maaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_edullisesti_kortilla_ei_muuta_kassaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_syo_edullisesti_kortilla_epaonnistunut_osto_palauttaa_false(self):
        self.maksukortti.ota_rahaa(1000)
        palautus = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(palautus, False)

    def test_syo_edullisesti_kortilla_epaonnistunut_osto_ei_muuta_kortin_saldoa(self):
        self.maksukortti.ota_rahaa(900)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 100)

    def test_syo_edullisesti_kortilla_epaonnistunut_osto_ei_muuta_lounaiden_maaraa(self):
        self.maksukortti.ota_rahaa(900)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
    



    def test_syo_maukkaasti_kortilla_onnistunut_osto_palauttaa_true(self):
        palautus = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(palautus, True)

    def test_syo_maukkaasti_kortilla_kasvattaa_lounaiden_maaraa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_maukkaasti_kortilla_ei_muuta_kassaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_syo_maukkaasti_kortilla_epaonnistunut_osto_palauttaa_false(self):
        self.maksukortti.ota_rahaa(1000)
        palautus = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(palautus, False)

    def test_syo_maukkaasti_kortilla_epaonnistunut_osto_ei_muuta_kortin_saldoa(self):
        self.maksukortti.ota_rahaa(900)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 100)

    def test_syo_maukkaasti_kortilla_epaonnistunut_osto_ei_muuta_lounaiden_maaraa(self):
        self.maksukortti.ota_rahaa(900)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)


    def test_lataa_rahaa_kortille_muuttaa_kortin_saldon_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.maksukortti.saldo, 1100)

    def test_lataa_rahaa_kortille_muuttaa_kassan_rahaa_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)

    def test_lataa_rahaa_kortille_negatiivinen_summa_ei_muuta_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(self.maksukortti.saldo, 1000)