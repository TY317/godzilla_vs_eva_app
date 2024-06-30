import streamlit as st
import pandas as pd

st.title("ゴジラvsエヴァンゲリオン")

################################################
##### データフレームの定義 #######################
################################################

# 通常時　スイカからのCZ当選率用
columns_normal_suika = ["スイカ"]
index_normal_suika = ["出現回数", "CZ当選回数"]
data_normal_suika = [[0],[0]]
path_normal_suika = "./pages/normal_suika_count_df.csv"

#ボーナス終了画面用
columns_bonus_pic = ["シンジ","レイ","マリ","アスカ","レイ背景","ゴジラ＆エヴァ"]
index_bonus_pic = ["出現回数"]
data_bonus_pic = [[0,0,0,0,0,0]]
path_bonus_pic = "./pages/bonus_pic_count_df.csv"

#AT中スイカからのCZ関連用
columns_at_suika = ["スイカ"]
index_at_suika = ["出現回数", "殲滅作成 当選回数","勝利回数"]
data_at_suika = [[0],[0],[0]]
path_at_suika = "./pages/at_suika_count_df.csv"

#AT終了画面用
columns_at_pic = ["初号機","零号機","8号機","2号機","モスラ","ゴジラ＆エヴァ","カヲル"]
index_at_pic = ["出現回数"]
data_at_pic = [[0,0,0,0,0,0,0]]
path_at_pic = "./pages/at_pic_count_df.csv"


##################################################
##### 新規作成ボタンを押すとデータをすべてリセットする
##################################################

#フォームの作成
with st.form(key='new_play'):

    #説明書き
    st.caption("※ 新規作成ボタンを押すとデータがすべて0リセットされます!")
    st.caption("※ 同時に他の人が利用しているとその人のデータも0リセットされます!恨みっこなしです!")

    #新規作成ボタンの設定
    start_btn = st.form_submit_button("新規作成")

    #ボタンが押されたらcsvファイルをリセットし保存
    if start_btn:

        ##### 通常時スイカからのCZ当選確率用
        normal_suika_count_df = pd.DataFrame(data_normal_suika,
                                             index=index_normal_suika,
                                             columns=columns_normal_suika)
        normal_suika_count_df.to_csv(path_normal_suika)
        
        ##### ボーナス終了画面用
        bonus_pic_count_df = pd.DataFrame(data_bonus_pic,
                                          index=index_bonus_pic,
                                          columns=columns_bonus_pic)
        bonus_pic_count_df.to_csv(path_bonus_pic)

        #AT中スイカからのCZ関連用
        at_suika_count_df = pd.DataFrame(data_at_suika,
                                         index=index_at_suika,
                                         columns=columns_at_suika)
        at_suika_count_df.to_csv(path_at_suika)

        #AT終了画面用
        at_pic_count_df = pd.DataFrame(data_at_pic,
                                       index=index_at_pic,
                                       columns=columns_at_pic)
        at_pic_count_df.to_csv(path_at_pic)

st.caption("ver1.0.0")
st.caption("   ・新規作成")