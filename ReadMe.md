# Job interview uloha
Pre spustenie projektu je potrebné nainštalovať si Python knižnice príkazom

```zsh
python3 -m pip install -r requirements.txt
```

Program sa spustí na locallhoste na porte 8000 \
http://127.0.0.1:8000/

Aplikacia je rozdelená na jednoduchý FrontEnd a na Restové rozhranie, ktoré zabezpečuje DjangoRestFramework

## Rest API

V priečinku app nájdeš dva súbory s views. Jeden sa volá func_based_views.py, v ňom som používal funkcie, pretože FunctionBasedView som do teraz používal pri každom z mojich django projektov. Druhý súbor sa volá views.py a v ňom je naprogramované to isté, len som tam použil triedy, teda ClassBasedView. 

K dátam uloženým vo formáte json sa dostaneš cez následujúce url adresy
- zobrazenie všetkých dát: http://127.0.0.1:8000/api/posts/
- zobrazenie konkrétneho príspevku: http://127.0.0.1:8000/api/posts/1/ 
- edit alebo zmazanie konkrétneho príspevku: http://127.0.0.1:8000/api/posts/1/edit/ 
- pridávanie príspevku: http://127.0.0.1:8000/api/posts/create/

## FrontEnd
K frontendu stačí prejsť na base locallhost url http://127.0.0.1:8000/

Môžeš pomocou neho si 
- zobraziť konkretny príspevok alebo vyhladať ho v externej api,
na vyhladávanie slúži okno, do ktorého napíš len číslo id-čka príspevku, ktorý chceš zobraziť
- vytvoriť nový, zmazať alebo upraviť
- toto všetko je možné robiť aj cez UI interface, ktorý ponúka django rest framework, cez url adresy spomenuté vyššie
