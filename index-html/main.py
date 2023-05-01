import streamlit as st
st.title('ダメージ計算')
# ポケモンの情報を入力するフォームを作成する
st.sidebar.header("ポケモンの情報")
level = st.sidebar.slider("レベル", 1, 100, 50)
attack_type = st.sidebar.selectbox("攻撃ポケモンのタイプ", ["ノーマル", "ほのお", "みず", "でんき", "くさ", "こおり", "かくとう", "どく", "じめん", "ひこう", "エスパー", "むし", "いわ", "ゴースト", "ドラゴン", "あく", "はがね", "フェアリー"])
attack_stat = st.sidebar.slider("こうげき/とくこう", 0, 400, 200)
defense_stat = st.sidebar.slider("ぼうぎょ/とくぼう", 0, 400, 150)

# 技の情報を入力するフォームを作成する
st.sidebar.header("技の情報")
power = st.sidebar.slider("威力", 0, 300, 150)
move_type = st.sidebar.selectbox("技タイプ", ["ノーマル", "ほのお", "みず", "でんき", "くさ", "こおり", "かくとう", "どく", "じめん", "ひこう", "エスパー", "むし", "いわ", "ゴースト", "ドラゴン", "あく", "はがね", "フェアリー"])

# ダメージ計算式を使ってダメージを計算する
damage = int((((2 * level / 5 + 2) * power * attack_stat / defense_stat) / 50 + 2) * (1.5 if attack_type == move_type else 1) / 100)

# 計算結果を出力する
st.header("ダメージ計算結果")
st.write("ダメージ: ", damage)
