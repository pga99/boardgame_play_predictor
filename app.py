import streamlit as st
import pandas as pd
from datetime import datetime
import pickle
import re


def get_name(id_, dict_):
    id_ = int(id_)
    return dict_[id_]


def get_str_list(game, items_col, items_dict, games_df):
    if games_df.loc[games_df['bggName'] == game, items_col].isnull().values.any():
        items = "NA"
    else:
        items_list = games_df.loc[games_df['bggName'] == game, items_col].iloc[0]
        items = [get_name(item, items_dict) for item in re.split(',', items_list)]
        items = re.sub("[\[\]\']*", "", str(items))
    return items


games = pd.read_csv('data/games_expanded_clean.csv', index_col=0)
games_info = pd.read_csv('data/games_compact.csv', index_col=0)
plays = pd.read_csv('data/plays_jp.csv')

rf_pipeline = pickle.load(open('models/rf_pipeline', 'rb'))
game_category_dict = pickle.load(open('data/game_category_dict', 'rb'))
game_type_dict = pickle.load(open('data/game_type_dict', 'rb'))
game_mechanic_dict = pickle.load(open('data/game_mechanic_dict', 'rb'))


st.title(":crystal_ball: Will Jul or Paula win this game? :crystal_ball:")
st.header("or...playing boardgames against the prediction ")

game = st.selectbox("Choose a boardgame you've played:", plays['bggName'].unique())

if st.checkbox("We're playing a new boardgame"):
    game = st.selectbox('Choose a new boardgame:', games['bggName'], index=31256)

if st.button('Predict the winner'):
    now = datetime.now()
    entry = games.loc[games['bggName'] == game, :]
    entry['day'] = now.day
    entry['time'] = now.hour
    entry['year'] = now.year
    # st.write(entry)
    st.subheader(f'The model predicts that the `winner` will be:')
    st.header(f':raising_hand: :trophy: {rf_pipeline.predict(entry)[0]} :trophy:')
    st.write(f'with `{round(max(rf_pipeline.predict_proba(entry)[0])*100)} %` probability')
    st.write('---')

    col1, col2 = st.columns(2)
    col1.subheader(f'Some stats for **{game}**:')
    if game in plays['bggName'].unique():
        col1.write(f"- Times played: `{plays.loc[plays.bggName == game, 'winner'].count()}`")
        col1.write(f"- Winners:")
        col1.bar_chart(plays.loc[plays.bggName == game, 'winner'].value_counts(),
                       height=150, width=200, use_container_width=False)
    else:
        col1.write("There are no `stats` for this game yet :no_mouth: ")

    col2.subheader(f'**{game}** Info:')

    complexity = round(games_info.loc[games_info['bggName'] == game, 'complexity'].iloc[0], 1)
    col2.write(f"- Game complexity: `{complexity}/5`")

    types = get_str_list(game, 'game_type', game_type_dict, games_info)
    col2.write(f'- Game type: `{types}`')

    categories = get_str_list(game, 'category', game_category_dict, games_info)
    col2.write(f'- Game categories: `{categories}`')

    mechanics = get_str_list(game, 'mechanic', game_mechanic_dict, games_info)
    col2.write(f'- Game mechanics: `{mechanics}`')
