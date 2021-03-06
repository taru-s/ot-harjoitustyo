
## Testausdokumentti

### Yksikkö- ja integraatiotestaus

#### Fabric
Kankaiden tiedto kapseloivalle Fabric-luokalle on muutama oma testi esimerkiksi varmistamaan merkkijonoesitysten oikea palautus.

#### Sovelluslogiikan testaus
FabricSevice luokkaa testataan TestFabricService-luokalla. Testejä varten luodun FabricService olion repositorio alustetaan ja tyhjennetään, ja siihen tallennetaan testausta varten yhden kankaan tiedot. Testauksen aikana käytetään erillistä testi-tietokantaa, joka on määritelty .env.test tiedostossa. Sovelluslogiikkaa testaavan luokan testien avulla on samalla testattu FabricRepostitory -luokan toimintaa yhdessä FabricService luokan kanssa.

#### Testikattavuus
![](./kuvat/testikattavuus.png)

### Järjestelmätestaus
Sovelluksen toimintaa ja käyttöliittymää on testattu manuaalisesti.

#### Asennus
Sovelluksen asennus on testattu käyttöohjeen mukaan Linux-ympäristössä.
#### Toiminnallisuudet
Kaikkia sovelluksen käyttöliittymästä käytettäviä toiminnallisuuksia on testattu käsin. Sovelluksen toimintaa on testattu myös virheellisillä syötteillä.

### Testauksen puutteet
Tietokannan alustamista ei ole erikseen testattu.
