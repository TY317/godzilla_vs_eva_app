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

    #####################################
    ##### csvの最終更新日を確認し、本日内に更新あれば「使用中」表示をする機能を追加
    #####################################
    st.caption("※ データの最終更新が本日だと「本日使用中」表示になります")
    import os
    from datetime import datetime, timedelta

    #csvが保存されているフォルダのパスを定義
    csv_folder_path = "./pages/"

    #フォルダ内の全ファイルリストを取得
    files = os.listdir(csv_folder_path)
    # st.write(files)

    #csvファイルのみを対象にしたリストを作る
    csv_files = [file for file in files if file.endswith(".csv")]
    # st.write(csv_files)

    # 最も最近の更新日時を保存する変数を初期化
    most_recent_date = None

    #最も最近の更新日時を取得する
    for csv_file in csv_files:
        file_path = os.path.join(csv_folder_path, csv_file)

        #最終更新日時を取得
        mtime = os.path.getmtime(file_path)

        #人間が読める形式に変換
        last_modified_date = datetime.fromtimestamp(mtime)

        #9時間を加算して日本時間に変換
        last_modified_date = last_modified_date + timedelta(hours=9)
        # st.write(last_modified_date)

        #更新日時が最も最近だったら変数に入れる
        if most_recent_date is None or last_modified_date > most_recent_date:
            most_recent_date = last_modified_date
    # st.write(most_recent_date)

    #現在日時を取得
    today = datetime.now()

    #9時間を加算して日本時間に変換
    today = today + timedelta(hours=9)
    
    #本日の日付を取得
    today = today.date()

    # st.write(today)

    #最新更新日が本日と同じなら「本日使用中」、違えば「本日未使用」を表示
    if most_recent_date is not None and most_recent_date.date() == today:
        st.markdown(":red-background[本日使用中]")
    else:
        st.markdown(":green-background[本日未使用]")

    ###################################
    ###################################
    ###################################

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

########################################
##### バージョン情報 ####################
########################################
st.caption("ver1.0.1")
st.caption("   ・本日未使用・使用中の表示機能追加")
st.caption("ver1.0.0")
st.caption("   ・新規作成")