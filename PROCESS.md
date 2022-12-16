# PROCESBOEK COMMERCE


## Caio Smidi


### 12-12:

Vandaag ben ik begonnen aan deze module met het kijken van het SQL college. Omdat ik bij de Wiki assignment achteraf merkte dat ik best veel terug moest kijken naar het college, had ik besloten er bij dit college de eerste keer iets langzamer over te doen zodat ik het gelijk wat beter zou onthouden.

De SQL commands waren voor mij vrijwel allemaal bekend van de Movies en de Fiftyville opdrachten van Datarepresentaties. De vertaling van Django code naar SQL weet ik nog niet zeker of ik het helemaal doorheb. Als ik het goed begrijp is het maken van een TABLE in SQL equivalent aan in een nieuwe Class(models.Model) toevoegen in de models.py file in het Django framework. Voor iedere kolom in je datatabel kan je dan een variabele binnen de Class maken. Vervolgens moeten alle aanpassingen/toevoegingen aan models.py gemigreerd worden via makemigrations en migrate?
Op deze manier kun je dus je eigen database creëren en daar een website mee maken.

Ook het idee van Primary en Foreign Keys was voor mij nog duidelijk uit voorgaand werk met SQL, en als ik het goed begrijp worden Primary Keys (vaak de id) automatisch aangemaakt bij het creëren van een nieuwe model class, en kunnen Foreign Keys makkelijk worden gelinkt door middel van models.ForeignKey(<Link>,…).
Het selecteren van specifieke rows uit de dataset is voor mij wel duidelijker in SQL dan in Django, aangezien er in het college maar een aantal equivalenten in het Django framework waren gegeven van de SQL commands als SELECT, WHERE, COUNT, etc. Maar ik ga ervan uit dat ik er met de Django documentatie op het internet wel uit moet komen.


### 13-12:

Vandaag ben ik begonnen met de Commerce opdracht. Allereerst ben ik begonnen met het maken van het Design Document. Naast het uittekenen van alle benodigde pagina’s heb ik hier ook de opzet van de benodigde modellen uitgedacht. Ook heb ik meteen geprobeerd na te denken over eventuele extra modellen naast de verplichte 3. Het leek mij wellicht een goed idee om voor de Watchlist zelf ook een apart model te maken, maar hier ben ik tot nu nog steeds niet helemaal over uit. Dit is namelijk wel een categorie waarbij specifieke gevallen van Users en Listings aan elkaar worden gekoppeld, dus dit zou ik misschien met 2 Foreign Keys in een aparte tabel (model) kunnen zetten. Maar ook is het misschien mogelijk om een nieuwe variabele/kolom aan mijn Listing of User Class toe te voegen, waarin ik dan gebruik zou maken van een ManyToManyField.

Ik heb vervolgens eerst geprobeerd qua volgorde min of meer de Specification van de opdracht te volgen. Ik heb dus eerst de 3 noodzakelijke models (Listing, Bid, Comment) gemaakt, en dit was na mijn schetsen van het Design Document alleen een kwestie van mijn opzet met de juiste code in Python schrijven. Het schrijven van een Watchlist model heb ik nog even gelaten voor wat het is, hier kom ik hopelijk later nog op terug. Daarnaast leek het mij handig om meteen de Django Admin Interface aan te maken, omdat dit mij uit het college heel handig leek om handmatig snel dingen te kunnen fixen. Dit ging zonder problemen.

Vervolgens wilde ik per pagina alle verschillende models gelijk goed implementeren, en dan vervolgens pas verder gaan naar de volgende pagina. Dit was qua design duidelijk een verkeerde keuze. Na meermaals te zijn vastgelopen doordat de combinatie van alle verschillende functionaliteiten te ingewikkeld werd, besloot ik het anders aan te pakken en juist de verschillende features eerst één voor één te implementeren. Dit bleek achteraf een veel betere (en best logische) keuze, want hierdoor werd het een stuk overzichtelijker waar ik mee bezig was en makkelijker mijn fouten op te sporen bij het fixen van bugs/errors. Los van dat ik de classes dus wel al had gemaakt in models.py, heb ik de verdere implementaties van Bids, Comments en de Watchlist voor vandaag helemaal gelaten. Aan het einde van de dag is het me gelukt om op de Active Listings Page (zonder enige opmaak) de benodigde informatie voor aangemaakte listings (via de Admin Interface) weer te geven.


### 14-12:

Vandaag ben ik begonnen met het maken van de Create Listing Page. Van eerdere opdrachten begreep ik dat het een pagina moest zijn waarop verschillende input fields zijn, die vervolgens met een POST method gestuurd worden naar de achterkant van de applicatie waar de database vervolgens aangepast moet worden. Na te hebben besloten welke velden informatie aanwezig moesten zijn, was het de vraag hoe ik deze form ging maken.

Gezien ik dit in de Wiki opdracht ook had gedaan, leek het mij het handigst om deze form niet handmatig in HTML te maken, maar dit via een Django Form te doen. Het enige verschil was dat nu de invoer in de form ook teruggestuurd moet worden naar mijn models, dus hier heb ik het een en ander over moeten opzoeken. Na de Django documentatie goed te lezen kwam ik erachter dat de django.forms module een ModelForm class heeft die ik hiervoor kan gebruiken.

Ook vond ik een handige ontdekking dat ik via widgets makkelijk preciezere specificatie van alle input fields kon vastleggen, zonder dat dit erg ingewikkeld werd. Het duurde wel even voordat logisch was welke soort forms.fields (TextInput, Textarea, NumberInput, Select, etc.) welke HTML genereert, maar dit heb ik uiteindelijk ook in de Django documentatie kunnen vinden. Ook heb ik bij het creëren van deze form class gebruik gemaakt van de Meta Class, zodat ik makkelijk kan koppelen met mijn model fields. Toen ik eenmaal een beetje doorhad hoe dit werkte, was eigenlijk het meeste werk al gedaan. Indien je deze goed gebruikt doet de Django Form veel van het werk voor je, wat denk ik ook de bedoeling zal zijn van Django Forms. Na een aantal tests ben ik tot de conclusie gekomen dat de pagina naar behoren werkte, alleen aan de styling moet ik nog het een en ander aanpassen gezien dit nog heel basic is.
Ook heb in mijn models.py toch de Watchlist class toegevoegd, omdat dit mij de meest logische manier lijkt om dit bij te houden in de database.


### 15-12:

Vandaag ben ik aan de slag gegaan met het maken van de Listing Page, waar dus eindelijk ook de andere classes uit models.py (Bid, Comment, Watchlist) aan te pas komen. Gezien de vele bulletpoints in de specificatie leek mij dit wel een lastige pagina, en dat bleek ook wel gezien het feit dat ik deze aan het einde van de dag nog steeds niet naar wens heb af kunnen maken.
Hier ben ik tot nu toe verreweg mijn grootste struikel/frustratiemoment tegengekomen. Mijn doel was om in views.py weer een aantal form classes aan te maken (net zoals ik heb gedaan voor de Create Listing Page), en op die manier de informatie door te spelen naar de backend en de database te manipuleren. Ondanks het feit dat ik dit voor de ‘Add to Watchlist’ op vrijwel exact dezelfde manier als mijn NewListingForm van gister, en ik er ook wel van overtuigd was dat mijn change_watch functie in views.py werkte, gebeurde er gek genoeg niks bij het klikken van de ‘Add to Watchlist’ button. Hetzelfde gold voor mijn implementaties van de Bidform en PlaceCommentForm classes. De code (keuze voor welke fields in classes, select queries in functies, creëren van nieuwe instances,  en verschillende stappen qua if/else) leek in mijn hoofd te moeten kloppen, maar toch gebeurde er niks. De buttons en classes leken goed in elkaar te zitten, maar enige output of verandering miste bij het gebruik hiervan.

De crux zat hem uiteindelijk toch (ondanks dat ik dit ook had nagekeken) in mijn urls.py. Ik had de url paths van de verschillende view functies allemaal gezet op <int:listing_id>, niet wetende dat dit ervoor zorgt dat het oproepen van de functies geen effect hebben op de pagina die ik te zien krijg. Ik snap nog steeds niet helemaal hoe het kan dat er in de database dan ook geen nieuwe instances worden aangemaakt als dat in de functie wel zou moeten gebeuren. Ik denk dat het dus dan betekent dat de functie helemaal niet wordt aangeroepen.

In ieder geval kreeg ik na het veranderen van de url paths (zodat er geen paths met identieke url’s waren) wel het idee dat het aanklikken van buttons of invullen van de forms er tenminste voor zorgde dat er iets in de database gebeurde. Vooralsnog lijkt het dus alsof deze onderdelen in de basis wel hun werk doen, alleen moet ik nu nog in mijn functie voor de verschillende soorten users en staten van activiteit verschillende scenario’s onderscheiden en zorgen dat dit klopt.

In de tussentijd dat ik voor mijn gevoel ook niet echt verder kon met het implementeren van de functionaliteit van mijn website, heb ik begin gemaakt aan het verbeteren van de style van de pages, en hier wil ik morgen nog zo ver mogelijk verder mee komen. Wel ga ik er eerst voor zorgen dat alle minimale vereisten zeker naar behoren werken.


### 16-12:
