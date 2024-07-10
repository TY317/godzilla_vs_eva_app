import streamlit as st
import pandas as pd
from Top import columns_at_pic, index_at_pic, path_at_pic
from PIL import Image

##### ページの内容 #####
# AT終了画面のメモ

########################################
##### 各種変数名を共通のものに置き換えておく
########################################
columns = columns_at_pic
index = index_at_pic
path = path_at_pic

########################################
##### マイナス、1行削除のための変数・関数定義
########################################

#マイナス、1行削除のチェック状態用の変数
if "minus_check" not in st.session_state:
    st.session_state["minus_check"] = False
    minus_check = st.session_state["minus_check"]

def toggle_minus_check():
    st.session_state["minus_check"] = not st.session_state["minus_check"]

#ボタンの表示文字列の設定
if st.session_state["minus_check"]:
    button_str = "マイナス"
    button_type = "primary"
else:
    button_str = "カウント"
    button_type = "secondary"

#################################
##### csvファイルの読み込み
#################################
try:
    df = pd.read_csv(path, index_col=0)

except FileNotFoundError:
    st.caption("Topページで新規作成を押して下さい")

#開発時の動作確認用
# st.dataframe(df)


#################################
##### ボーナス後画面のカウント
#################################

st.subheader("AT終了画面")
st.caption("・AT終了画面で示唆を確認")

#画面の選択肢をセッション管理するための変数設定
if "at_pic_select" not in st.session_state:
    st.session_state.at_pic_select = ""

#セレクトボックスを作成
st.session_state.at_pic_select = st.selectbox("AT終了画面", columns)

#選択肢に応じて画像を参考として表示させる
if st.session_state.at_pic_select == columns[0]:
    im = Image.open("./image/at_pic_shogoki.jpg")
    st.image(im)

elif st.session_state.at_pic_select == columns[1]:
    im = Image.open("./image/at_pic_zerogoki.jpg")
    st.image(im)

elif st.session_state.at_pic_select == columns[2]:
    im = Image.open("./image/at_pic_hachigoki.jpg")
    st.image(im)

elif st.session_state.at_pic_select == columns[3]:
    im = Image.open("./image/at_pic_nigoki.jpg")
    st.image(im)

elif st.session_state.at_pic_select == columns[4]:
    im = Image.open("./image/at_pic_mosura.jpg")
    st.image(im)

elif st.session_state.at_pic_select == columns[5]:
    im = Image.open("./image/at_pic_godzieva.jpg")
    st.image(im)

elif st.session_state.at_pic_select == columns[6]:
    im = Image.open("./image/at_pic_kaoru.jpg")
    st.image(im)

#登録ボタン
submit_btn = st.button(button_str, type=button_type)

#登録ボタンが押されたら選択内容に応じてカウントアップ
if submit_btn:
    
    #画面の種類ごとに一致確認
    for column in df.columns:
        
        #選択内容とカラム名が一致したらカウントアップ処理
        if column == st.session_state.at_pic_select:
            ##### マイナスチェックの状態に合わせてカウントを変更
            if st.session_state["minus_check"]:
                #指定のカラムの数値を-1する
                df.at[df.index[0], column] -= 1
                if df.at[df.index[0], column] < 0:
                    df.at[df.index[0], column] = 0

            else:
                #指定のカラムの数値を+1する
                df.at[df.index[0], column] += 1

            #csvに保存する
            df.to_csv(path)
        else:
            pass

# st.dataframe(df)


######################################
##### カウント結果とパーセントの現在値表示
######################################

#表示用のデータフレームを起こす
df_result = df.copy()

##### 各ボイスの出現確率をデータフレームに追加する
#全画面の回数を出しておく
pic_sum = df_result.loc[df.index[0]].sum()
# st.caption(pic_sum)

#各ボイスの出現確率をリストに格納しておく
probability_list = []

for column in columns:
    #出現確率の計算
    probability_occurrence = df_result.at[df.index[0], column] / pic_sum

    #％表記の文字列にする
    probability_occurrence = f"{probability_occurrence * 100:.1f}%"

    #リストに追加する
    probability_list.append(probability_occurrence)

#データフレームに追加する
df_result.loc["出現確率"] = probability_list

##### 各画面の説明を追加する
df_result.loc["備考"] = ["デフォルト","偶数示唆","高設定示唆(弱)","高設定示唆(高)","設定4以上","設定5以上","設定6"]

st.dataframe(df_result)

##################################
##### 解析情報の表示 #########
##################################
st.caption("解析値はなし")
st.caption("[参考] 過去の実戦結果")

#過去の実戦結果画像の表示
im_result = Image.open("./image/at_pic_56result.bmp")
st.image(im_result, use_column_width=True)

##### マイナスのチェックボックス表示
st.checkbox("マイナスカウント、1行削除", value=st.session_state["minus_check"], on_change=toggle_minus_check)