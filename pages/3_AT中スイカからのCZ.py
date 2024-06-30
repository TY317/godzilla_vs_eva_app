import streamlit as st
import pandas as pd
from Top import columns_at_suika, index_at_suika, path_at_suika

##### ページの内容 #####
# AT中のスイカとCZ 殲滅作成の回数、勝利回数をカウント
# 当選率と勝利率を解析値と比較

########################################
##### 各種変数名を共通のものに置き換えておく
########################################
columns = columns_at_suika
index = index_at_suika
path = path_at_suika

#################################
##### csvファイルの読み込み
#################################
try:
    df = pd.read_csv(path, index_col=0)

except FileNotFoundError:
    st.caption("Topページで新規作成を押して下さい")

#開発時の動作確認用
# st.dataframe(df)

##################################
##### AT中スイカ回数のカウント #########
##################################
st.subheader("AT中スイカからのCZ当選率と勝利率")
st.caption("・スイカ回数とCZ 殲滅作戦の当選回数と勝利回数をカウントし確率を確認する")

##### 通常時のスイカ回数カウント
with st.form(key="at_suika_count"):

    #2列に画面分割
    col1, col2 = st.columns(2)

    ##### 左画面
    with col1:
        st.caption("スイカ回数カウント")
    
    #カウントボタン
        suika_count_btn = st.form_submit_button("カウント")
    
    ####カウントボタンが押されたらカウントアップさせてcsv保存
        if suika_count_btn:

            #現在のカウント数を取得する
            current_count = df.at[index[0], columns[0]]
            # st.caption(current_count)

            #現在のカウントに1を足す
            new_count = current_count + 1

            #データフレーム内の数値データを置き換える
            df.at[index[0], columns[0]] = new_count

            #csvに保存する
            df.to_csv(path)
    
    ##### 右画面
    with col2:
        #現在回数の表示
        st.caption("スイカ回数")
        st.info(df.at[index[0], columns[0]])

##################################
##### CZ当選回数のカウント #########
##################################
##### AT中のCZ回数カウント
with st.form(key="at_cz_count"):

    #2列に画面分割
    col1, col2 = st.columns(2)

    ##### 左画面
    with col1:
        st.caption("CZ 殲滅作戦 回数カウント")
    
    #カウントボタン
        cz_count_btn = st.form_submit_button("カウント")
    
    ####カウントボタンが押されたらカウントアップさせてcsv保存
        if cz_count_btn:

            #現在のカウント数を取得する
            current_count = df.at[index[1], columns[0]]
            # st.caption(current_count)

            #現在のカウントに1を足す
            new_count = current_count + 1

            #データフレーム内の数値データを置き換える
            df.at[index[1], columns[0]] = new_count

            #csvに保存する
            df.to_csv(path)
    
    ##### 右画面
    with col2:
        #現在回数の表示
        st.caption("CZ 殲滅作戦 回数")
        st.info(df.at[index[1], columns[0]])

##################################
##### CZ勝利回数のカウント #########
##################################
##### CZ勝利回数カウント
with st.form(key="cz_win_count"):

    #2列に画面分割
    col1, col2 = st.columns(2)

    ##### 左画面
    with col1:
        st.caption("CZ 殲滅作戦 勝利回数カウント")
    
    #カウントボタン
        win_count_btn = st.form_submit_button("カウント")
    
    ####カウントボタンが押されたらカウントアップさせてcsv保存
        if win_count_btn:

            #現在のカウント数を取得する
            current_count = df.at[index[2], columns[0]]
            # st.caption(current_count)

            #現在のカウントに1を足す
            new_count = current_count + 1

            #データフレーム内の数値データを置き換える
            df.at[index[2], columns[0]] = new_count

            #csvに保存する
            df.to_csv(path)
    
    ##### 右画面
    with col2:
        #現在回数の表示
        st.caption("CZ 殲滅作戦 勝利回数")
        st.info(df.at[index[2], columns[0]])

#############################################
##### CZ当選確率の算出と表示 ####################
#############################################
#2列に画面分割
col1, col2 = st.columns(2)

##### 左画面：CZ当選率の表示
with col1:

    ##### スイカ回数が1以上なら現在の当選確率算出
    if df.at[index[0], columns[0]] > 0:
        #当選確率の算出
        probability = df.at[index[1], columns[0]] / df.at[index[0], columns[0]]
        # st.caption(probability)

        #結果の表示
        st.caption("現在値")
        st.info(f"{probability*100:.1f}%")

##### 右画面：解析値の参考表示
with col2:
    st.caption("解析値")

    #解析値のデータフレーム作成
    columns_list_theoretical = ["CZ当選率"]
    index_list_theoretical = ["設定1", "設定2", "設定4", "設定5", "設定6"]
    data_list_theoretical = [["30.1%"],
                            ["30.1%"],
                            ["37.5%"],
                            ["37.5%"],
                            ["39.1%"]]
    df_theoretical = pd.DataFrame(data_list_theoretical, index=index_list_theoretical, columns=columns_list_theoretical)

    #データフレームの表示
    st.dataframe(df_theoretical)


#############################################
##### CZ勝利確率の算出と表示 ####################
#############################################
#2列に画面分割
col1, col2 = st.columns(2)

##### 左画面：CZ勝利率の表示
with col1:

    ##### CZ回数が1以上なら現在の当選確率算出
    if df.at[index[1], columns[0]] > 0:
        #当選確率の算出
        probability = df.at[index[2], columns[0]] / df.at[index[1], columns[0]]
        # st.caption(probability)

        #結果の表示
        st.caption("現在値")
        st.info(f"{probability*100:.1f}%")

##### 右画面：解析値の参考表示
with col2:
    st.caption("解析値")
    
    #解析値のデータフレーム作成
    columns_list_theoretical = ["CZ勝利率"]
    index_list_theoretical = ["設定1", "設定2", "設定4", "設定5", "設定6"]
    data_list_theoretical = [["49.3%"],
                            ["50.4%"],
                            ["51.7%"],
                            ["52.9%"],
                            ["65.3%"]]
    df_theoretical = pd.DataFrame(data_list_theoretical, index=index_list_theoretical, columns=columns_list_theoretical)

    #データフレームの表示
    st.dataframe(df_theoretical)