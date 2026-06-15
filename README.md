Le pipeline est orchestré via un script Python inspiré d’un flow Prefect. 
À cause d’un conflit de dépendances entre dbt 1.11 et Prefect 3.4, 
l’exécution locale est assurée par subprocess afin de garantir la reproductibilité.

Le pipeline complet s’exécute jusqu’à Streamlit. Le contrôle Soda détecte volontairement une anomalie métier sur unit_price < 0, ce qui démontre que les règles de qualité fonctionnent.