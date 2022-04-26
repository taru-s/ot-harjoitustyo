# READ ME


[vaatimusmaarittely](https://github.com/taru-s/ot-harjoitustyo/blob/master/fabric-stash/dokumentaatio/vaatimusmaarittely.md)

[työaikakirjanpito](https://github.com/taru-s/ot-harjoitustyo/blob/master/fabric-stash/dokumentaatio/tuntikirjanpito.md)

[changelog](https://github.com/taru-s/ot-harjoitustyo/blob/master/fabric-stash/dokumentaatio/changelog.md)

[arkkitehtuurikuvaus](https://github.com/taru-s/ot-harjoitustyo/blob/master/fabric-stash/dokumentaatio/arkkitehtuuri.md)

[viikko5 release](https://github.com/taru-s/ot-harjoitustyo/releases/tag/viikko5)


.

.
### Viikko5 release asennus
1. Lataa ja pura viikko5 releasen zip-tiedosto
2. mene hakemistoon ot-harjoitustyo-viikko5/fabric-stash/
3. asenna riippuvuudet ajamalla komento `poetry install` 
4. käynnistä sovellus komennolla `poetry run invoke start`

### Poetry komennot
**käynnistys:** `poetry run invoke start`

**testaus:** `poetry run invoke test`

**testikattavuusraportti:** `poetry run invoke coverage-report`

**pylint tarkistus:** `poetry run invoke lint`

