# Boardgame play predictor

Built this `Streamlit` app as a birthday present to my wife to use it to predict the winner of our boardgame plays and then play for/against the prediction. 

Based on data collected with the [Board Game Stats app](https://www.bgstatsapp.com/) from January 2019 to August 2021. 
Board game information comes from [the bgg data from Board Game data set on kaggle](https://www.kaggle.com/mshepherd/board-games).  

The model is a random forest classifier trained to predict the winner between to classes `[Jul, Paula]` taking the features:
- `Game: Bgg Name` [list](https://boardgamegeek.com/browse/boardgame) 
- `Game: Complexity`
- `Game: Bgg Game Types`
- `Game: Bgg Categories` [list](https://boardgamegeek.com/browse/boardgamecategory)
- `Game: Bgg Mechanics`[list](https://boardgamegeek.com/browse/boardgamemechanic)
- `Game: Year Published`
- `Play: Day`
- `Play: Hour`

-------------------

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
