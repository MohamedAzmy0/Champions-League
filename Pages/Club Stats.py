import streamlit as st
import pandas as pd
import plotly.express as px


# Load Data
attacking = pd.read_csv('./Sources//attacking.csv').drop('serial' , axis=1)
attempts = pd.read_csv('./Sources//attempts.csv').drop('serial' , axis=1)
defending = pd.read_csv('./Sources//defending.csv').drop('serial' , axis=1)
disciplinary = pd.read_csv('./Sources//disciplinary.csv').drop('serial' , axis=1)
distribution = pd.read_csv('./Sources//distribution.csv').drop('serial' , axis=1)
goalkeeping = pd.read_csv('./Sources//goalkeeping.csv').drop('serial' , axis=1)
goals = pd.read_csv('./Sources//goals.csv').drop('serial' , axis=1)
key_stats = pd.read_csv('./Sources//key_stats.csv')



st.title('Club Stats for Goals')

col1 , col2= st.columns([1,2])
with col1:
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')

    st.dataframe(goals.groupby(['club']).agg({'goals':'sum'}).sort_values(by='goals', ascending=False).reset_index().head(5))
with col2:
    Most_Club_goals = goals.groupby(['club']).agg({'goals':'sum'}).sort_values(by='goals', ascending=False).reset_index()
    st.plotly_chart(px.bar(Most_Club_goals.head(5), x='club', y='goals'))

st.title('Club Stats for Assists')

col1,col2 = st.columns([1,2])
with col1:
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')

    st.dataframe(attacking.groupby(['club']).agg({'assists':'sum'}).nlargest(5,'assists').reset_index())
with col2:
    assist=attacking.groupby(['club']).agg({'assists':'sum'}).nlargest(5,'assists').reset_index()
    st.plotly_chart(px.funnel(assist, x='club', y='assists'))

st.title('Club Stats for attempts')

col1 , col2= st.columns([1,2])
with col1:
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')

    st.dataframe(attempts.groupby(['club']).agg({'total_attempts':'sum'}).nlargest(5,'total_attempts').reset_index())
with col2:
    total=attempts.groupby(['club']).agg({'total_attempts':'sum','on_target':'sum','off_target':'sum'}).nlargest(5,'total_attempts').reset_index()
    st.plotly_chart(px.bar(total, y=['total_attempts','on_target','off_target'], x='club',barmode='group'))


st.title('Club Stats for Dribbles')

col1 , col2= st.columns([1,2])
with col1:
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')

    st.dataframe(attacking.groupby(['club']).agg({'dribbles':'sum'}).nlargest(5,'dribbles').reset_index())
with col2:
    dribbles=attacking.groupby(['club']).agg({'dribbles':'sum'}).nlargest(5,'dribbles').reset_index()
    st.plotly_chart(px.funnel(dribbles, x='dribbles', y='club'))



st.title('Cleansheet Stats')

col1 , col2= st.columns([1,2])
with col1:
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')

    st.dataframe(goalkeeping.groupby(['club']).agg({'cleansheets':'sum'}).sort_values(by='cleansheets', ascending=False).reset_index().head(5))
with col2:
    Goalkeeper = goalkeeping.groupby(['club']).agg({'cleansheets':'sum'}).sort_values(by='cleansheets', ascending=False).reset_index()
    st.plotly_chart(px.histogram(Goalkeeper.head(5), x='club', y='cleansheets' ))



st.title('Club Stats for Tackles')

col1 , col2= st.columns([1,2])
with col1:
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')

    st.dataframe(defending.groupby(['club']).agg({'tackles':'sum','t_won':'sum'}).sort_values(by='tackles', ascending=False).reset_index().head(5))
with col2:
    Club_tackles_won = defending.groupby(['club']).agg({'tackles':'sum','t_won':'sum','t_lost':'sum'}).sort_values(by='tackles', ascending=False).reset_index()
    st.plotly_chart(px.bar(Club_tackles_won.head(10), x='club', y=['tackles','t_won','t_lost'] ,barmode='group'))


st.title('Most Club Recover the ball in the whole season')

col1 , col2= st.columns([1,2])
with col1:
    st.write('')
    st.write('')
    st.write('')

    st.dataframe(defending.groupby(['club']).agg({'balls_recoverd':'sum'}).sort_values(by='balls_recoverd', ascending=False).reset_index().head(10))
with col2:
    recover = defending.groupby(['club']).agg({'balls_recoverd':'sum'}).sort_values(by='balls_recoverd', ascending=False).reset_index()
    st.plotly_chart(px.funnel(recover.head(10), y='club', x='balls_recoverd' ))


disciplinary['total_cards']=disciplinary['red'] + disciplinary['yellow']

col1 , col2= st.columns(2)
with col1:
    st.title('Fair Play')
    fair=disciplinary.groupby('club').agg({'total_cards':'sum'}).sort_values(by='total_cards', ascending=True).reset_index().head(5)
    st.dataframe(fair)
with col2:
    st.title('Aggressive Play')
    unfair=disciplinary.groupby('club').agg({'total_cards':'sum'}).sort_values(by='total_cards', ascending=False).reset_index().head(5)
    st.dataframe(unfair)
