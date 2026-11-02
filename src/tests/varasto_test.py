import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_konstruktori_nollaa_negatiivisen_tilavuuden(self):
        varasto = Varasto(-5)
        self.assertAlmostEqual(varasto.tilavuus, 0.0)

    def test_konstruktori_nollaa_nollatilavuuden(self):
        varasto = Varasto(0)
        self.assertAlmostEqual(varasto.tilavuus, 0.0)

    def test_konstruktori_nollaa_negatiivisen_alkusaldon(self):
        varasto = Varasto(10, -5)
        self.assertAlmostEqual(varasto.saldo, 0.0)

    def test_konstruktori_rajoittaa_alkusaldon_tilavuuteen(self):
        varasto = Varasto(10, 15)
        self.assertAlmostEqual(varasto.saldo, 10.0)

    def test_lisays_ei_hyvaksy_negatiivista_maaraa(self):
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)

    def test_lisays_yli_tilavuuden_tayttaa_varaston(self):
        self.varasto.lisaa_varastoon(15)
        self.assertAlmostEqual(self.varasto.saldo, 10.0)

    def test_ottaminen_ei_hyvaksy_negatiivista_maaraa(self):
        tulos = self.varasto.ota_varastosta(-5)
        self.assertAlmostEqual(tulos, 0.0)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)
        
    def test_ottaminen_yli_saldon_palauttaa_kaiken(self):
        self.varasto.lisaa_varastoon(5)
        tulos = self.varasto.ota_varastosta(8)
        self.assertAlmostEqual(tulos, 5.0)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)

    def test_ottaminen_tasmalleen_koko_saldon(self):
        self.varasto.lisaa_varastoon(5)
        tulos = self.varasto.ota_varastosta(5)
        self.assertAlmostEqual(tulos, 5.0)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)