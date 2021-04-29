# Pipenv -- Python in abgeschotteter Umgebung


## Was heißt abgeschottet?

Im Zusammenhang mit Programmierung bedeutet "abgeschottet" eigentlich nichts
anderes als "ungestört":

- ungestört von Updates, die funktionierende Programme nicht mehr funktionieren
  lassen.
- ungestört von globalen Neuinstallationen, die sich auf erfolgreiche Programme
  auswirken wie Störfeuer, weil sie hinter unserem Rücken Bibliotheken updaten.
- ungestört von verschiedenen Python-Versionen, von denen die Projekte abhängig
  sind.

"Abgeschottet" bewirkt aber auch, dass Python-Packages, die wir nur für unser
Projekt brauchen, auf unser projekt beschränkt bleiben und unsere globale
Python-Installation unbehelligt lassen. Alle Pakete, die wir für ein
Webserver-Projekt brauchen, wirken sich nicht mehr auf unsere
Python-Installation aus. Wenn wir das Projekt beenden und von unserem Rechner
löschen, verschwinden auch alle Webserver-Erweiterungen, die wir nirgendwo
sonst brauchen.




