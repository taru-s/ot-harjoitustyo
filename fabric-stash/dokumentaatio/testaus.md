
## Testausdokumentti

### Unit test

#### Sovelluslogiikan testaus
FabricSevice luokkaa testataan TestFabricService-luokalla. Testejä varten luodun FabricService olion repositorio alustetaan ja tyhjennetään, ja siihen tallennetaan testausta varten yhden kankaan tiedot. Testauksen aikana käytetään erillistä testi-tietokantaa, joka on määritelty .env.test tiedostossa. Sovelluslogiikkaa testaavan luokan testien avulla on samalla testattu FabricRepostitory -luokan toimintaa yhdessä FabricService luokan kanssa.

#### Testikattavuus


### Järjestelmätestaus
Sovelluksen toimintaa ja käyttöliittymää on testattu manuaalisesti.

#### Asennus
Sovelluksen asennus on testattu käyttöohjeen mukaan Linux-ympäristössä.
#### Toiminnallisuudet
Kaikkia sovelluksen toiminnallisuuksia ja niihin liittyviä osia on testattu. Sovelluksen toimintaa on testattu myös virheellisillä syötteillä.

### Testauksen puutteet
