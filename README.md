# bfx_order_kaskade
Kleines Python Programm, um eine Kaskade in Bitmex zu erstellen

zunächst muss der Bitmex API Key und das Secret in die config.py eingetragen werden.
Der Key benötigt alle Rechte.

Unter Python 3.6 müssen die Requirements installiert werden.
Kommando: pip install -r requirements.txt

Beim Start erscheint ein Fenster, in dem folgendes eingetragen werden muss:
 
 Seite: Long oder Short
 Typ: Limit, Market (eigentlich quatsch :D), Stop, StopLimit
 Ordergröße: Wie viel sollen die Orders insgesamt betragen
 Preis: Der Preis um den die Orders herum gelegt werden sollen
 Range: Der Bereich definiert, wo die Orders gelegt werden.
 Anzahl Orders: Dies definiert, in wie viele Orders die Ordergröße aufgeteilt wird.
 
 Das Skript legt dann die Orders an:
 
 Preis +- Range
 Jeder Order gleiche größe (Ordergröße / Anzahl Orders)