 
 ```mermaid
 classDiagram
      direction RL
 
      Noppa "2" -- "1" Monopoli
      Pelaaja "2..8" -- "1" Monopoli
      Ruutu "40" -- "1" Pelilauta
      Pelilauta "1" -- "1" Monopoli
      Pelinappula "1" -- "1" Pelaaja
      Ruutu ..> "1" Ruutu
      Pelinappula ..> Ruutu
      Raha "*" -- Monopoli
      Raha "*" -- Pelaaja
      Ruutu -- Toiminto
      Kortti -- Toiminto
      Toiminto <|-- Toiminto1
      Toiminto <|-- Toiminto2
      Toiminto <|-- Toiminto3
      
      Ruutu <|-- Aloitusruutu
      Ruutu <|-- Vankila
      Ruutu <|-- Sattuma
      Ruutu <|-- Yhteismaa
      Ruutu <|-- Asema
      Ruutu <|-- Laitos
      Ruutu <|-- Katu
      
      Monopoli ..> Aloitusruutu
      Monopoli ..> Vankila
      
      Sattuma -- "*" Kortti
      Yhteismaa -- "*" Kortti
      
      Katu --> Nimi
      Katu "0..*" -- "1" Pelaaja
      Katu "1" -- "0..4" Talo
      Katu "1" -- "0..1" Hotelli
      
      Rakennus <|-- Talo
      Rakennus <|-- Hotelli
      
      class Monopoli{
      }
      
      class Noppa{
      }
      
      class Pelaaja{
       Pelinappula pelinappula
      }
      
      class Pelinappula{
        Ruutu sijainti
      }
      
      class Pelilauta{
      }
      
      class Kortti{
      }
      
      class Rakennus{
      }
      
      class Talo{
      }
      
      class Hotelli{
      }
      
      class Raha{
      }
      
      class Ruutu{
        Ruutu seuraava
      }
      
      class Aloitusruutu{
      }
      
      class Katu{
       Nimi kadunnimi
      }
      
      class Nimi{
      }
      
      class Toiminto{
      }
      
      
      
      
      
```
