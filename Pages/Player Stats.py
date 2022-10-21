import streamlit as st
import pandas as pd
import plotly.express as px


# Load Data
attacking = pd.read_csv('.\Sources\\attacking.csv').drop('serial' , axis=1)
attempts = pd.read_csv('.\Sources\\attempts.csv').drop('serial' , axis=1)
defending = pd.read_csv('.\Sources\\defending.csv').drop('serial' , axis=1)
disciplinary = pd.read_csv('.\Sources\\disciplinary.csv').drop('serial' , axis=1)
distribution = pd.read_csv('.\Sources\\distribution.csv').drop('serial' , axis=1)
goalkeeping = pd.read_csv('.\Sources\\goalkeeping.csv').drop('serial' , axis=1)
goals = pd.read_csv('.\Sources\\goals.csv').drop('serial' , axis=1)
key_stats = pd.read_csv('.\Sources\\key_stats.csv')



st.title('Player Stats for Goals')

col1 , col2= st.columns([1,2])
with col1:
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')

    st.dataframe(goals.groupby(['player_name']).agg({'goals':'max'}).sort_values(by='goals', ascending=False).reset_index().head(5))
with col2:
    Most_player_goals = key_stats.groupby(['player_name']).agg({'goals':'max', 'assists':'max'}).sort_values(by='goals', ascending=False).reset_index()
    st.plotly_chart(px.bar(Most_player_goals.head(5), x='player_name', y='goals'))

st.title('Player Stats for Assists')

col1,col2 = st.columns([1,2])
with col1:
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')

    st.dataframe(attacking.groupby(['player_name']).agg({'assists':'max'}).nlargest(5,'assists').reset_index())
with col2:
    assist=attacking.groupby(['player_name']).agg({'assists':'max'}).nlargest(5,'assists').reset_index()
    st.plotly_chart(px.funnel(assist, x='player_name', y='assists'))

st.title('Player Stats for Dribbles')

col1 , col2= st.columns([1,2])
with col1:
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')

    st.dataframe(attacking.groupby(['player_name']).agg({'dribbles':'max'}).nlargest(5,'dribbles').reset_index())
with col2:
    dribbles=attacking.groupby(['player_name']).agg({'dribbles':'max'}).nlargest(5,'dribbles').reset_index()
    st.plotly_chart(px.funnel(dribbles, x='dribbles', y='player_name'))



st.title('Goalkeepers Stats')

col1 , col2= st.columns([1,2])
with col1:
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')

    st.dataframe(goalkeeping.groupby(['player_name']).agg({'saved':'max'}).sort_values(by='saved', ascending=False).reset_index().head(5))
with col2:
    Goalkeeper = goalkeeping.groupby(['player_name']).agg({'saved':'max'}).sort_values(by='saved', ascending=False).reset_index()
    st.plotly_chart(px.funnel(Goalkeeper.head(5), x='player_name', y='saved' ))



st.title('Player Stats for Tackles')

col1 , col2= st.columns([1,2])
with col1:
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')

    st.dataframe(defending.groupby(['player_name']).agg({'tackles':'sum','t_won':'sum'}).sort_values(by='tackles', ascending=False).reset_index().head(5))
with col2:
    player_tackles_won = defending.groupby(['player_name']).agg({'tackles':'sum','t_won':'sum'}).sort_values(by='tackles', ascending=False).reset_index()
    st.plotly_chart(px.bar(player_tackles_won.head(10), x='player_name', y=['tackles','t_won'] ,barmode='group'))


st.title('Most Player Recover the ball in the whole season')

col1 , col2= st.columns([1,2])
with col1:
    st.write('')
    st.write('')
    st.write('')

    st.dataframe(defending.groupby(['player_name']).agg({'balls_recoverd':'max'}).sort_values(by='balls_recoverd', ascending=False).reset_index().head(10))
with col2:
    recover = defending.groupby(['player_name']).agg({'balls_recoverd':'max'}).sort_values(by='balls_recoverd', ascending=False).reset_index()
    st.plotly_chart(px.funnel(recover.head(10), y='player_name', x='balls_recoverd' ))


disciplinary['total_cards']=disciplinary['red'] + disciplinary['yellow']

col1 , col2= st.columns([2,2])
with col1:
    st.title('Fair Play')
    fair=disciplinary.groupby(['player_name','match_played']).agg({'total_cards':'sum'}).sort_values(by='total_cards', ascending=True).reset_index().head(5)
    st.dataframe(fair)
with col2:
    st.title('Aggressive Play')
    unfair=disciplinary.groupby(['player_name','match_played']).agg({'total_cards':'sum'}).sort_values(by='total_cards', ascending=False).reset_index().head(5)
    st.dataframe(unfair)
