 
 ```mermaid
 classDiagram
 
      Noppa "2" -- "1" Monopoli
      Pelaaja "2..8" -- "1" Monopoli
      Ruutu "40" -- "1" Pelilauta
      Pelilauta "1" -- "1" Monopoli
      Pelinappula "1" -- "1" Pelaaja
      Ruutu ..> "1" Ruutu
      Pelinappula ..> Ruutu
      
      class Monopoli{
      }
      
      class Noppa{
      }
      
      class Pelaaja{
      }
      
      class Pelilauta{
      }
      
      class Ruutu{
        Ruutu seuraava
      }
      
      class Pelinappula{
        Ruutu sijainti
      }
      
      
```
