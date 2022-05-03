

### asentaminen
1. Lataa ja pura releasen zip-tiedosto
2. mene hakemistoon ot-harjoitustyo-viikko5/fabric-stash/
3. asenna riippuvuudet ajamalla komento `poetry install` 
4. käynnistä sovellus komennolla `poetry run invoke start`

### Poetry komennot
**käynnistys:** `poetry run invoke start`

**testaus:** `poetry run invoke test`

**testikattavuusraportti:** `poetry run invoke coverage-report`

**pylint tarkistus:** `poetry run invoke lint`

### Sovelluksen käyttäminen

Sovellus käynnistyy listanäkymään, jossa näet kaikki tallennetut kankaat. Jos kankaita ei ole vielä tallennettu, näkyy listassa vain painike uuden kankaan lisäämiseen.

Lisää uusi kangas painamalla "add fabric" painiketta. Tämän jälkeen voit syöttää uuden kankaan tiedot. Painamalla "save" tiedot tallentuvat ja näet tallennetut tiedot. Painikkeesta "delete" voit poistaa tallennetun kankaan. Sovellus varmistaa, haluatko todella poistaa kankaan. Valitsemalla "yes", tallennettu kangas ja kaikki sen tiedto poistetaan pysyvästi.

Listanäkymästä voit kankaan nimeä painamalla katsoa sen tarkempia tietoja, ja halutessasi muokata niitä painikkeesta "edit".

Listanäkymän "search" painikkeesta voit hakea kankaita nimen perusteella.
