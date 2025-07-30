import streamlit as st
import os

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

# LLMの初期化
@st.cache_resource
def init_llm():
    # Streamlit SecretsからOpenAI APIキーを取得
    try:
        openai_api_key = st.secrets["OPENAI_API_KEY"]
        return ChatOpenAI(
            model_name="gpt-4o-mini", 
            temperature=0,
            api_key=openai_api_key
        )
    except KeyError:
        st.error("⚠️ OpenAI APIキーが設定されていません。")
        st.info("Streamlit Cloud の Secrets で OPENAI_API_KEY を設定してください。")
        st.stop()

# 専門家の種類とシステムメッセージの定義
EXPERTS = {
    "プログラミング専門家": "あなたは経験豊富なプログラミング専門家です。プログラミングに関する質問に対して、実用的で詳細なアドバイスを提供してください。",
    "料理専門家": "あなたは料理のプロフェッショナルです。料理のレシピ、調理技術、食材の選び方について専門的なアドバイスを提供してください。",
    "健康・フィットネス専門家": "あなたは健康とフィットネスの専門家です。運動、栄養、健康維持について科学的根拠に基づいたアドバイスを提供してください。",
    "旅行専門家": "あなたは旅行のエキスパートです。旅行計画、観光地の情報、旅行のコツについて詳しいアドバイスを提供してください。"
}

def get_expert_response(input_text: str, selected_expert: str) -> str:
    """
    入力テキストと選択された専門家に基づいてLLMからの回答を取得する関数
    
    Args:
        input_text (str): ユーザーからの入力テキスト
        selected_expert (str): 選択された専門家の種類
    
    Returns:
        str: LLMからの回答
    """
    llm = init_llm()
    
    # 選択された専門家に応じたシステムメッセージを設定
    system_message = EXPERTS.get(selected_expert, EXPERTS["プログラミング専門家"])
    
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=input_text)
    ]
    
    try:
        response = llm.invoke(messages)
        return response.content
    except Exception as e:
        return f"エラーが発生しました: {str(e)}"

# Streamlitアプリケーションのメイン部分
def main():
    st.set_page_config(
        page_title="AI専門家相談アプリ",
        page_icon="🤖",
        layout="wide"
    )
    
    # タイトルと説明
    st.title("🤖 AI専門家相談アプリ")
    st.markdown("---")
    
    # アプリの概要
    st.markdown("""
    ## 📋 アプリの概要
    このアプリでは、異なる分野の専門家AIと相談することができます。
    質問したい分野の専門家を選択して、自由に質問してください。
    
    ## 🔧 操作方法
    1. **専門家を選択**: ラジオボタンから相談したい分野の専門家を選択してください
    2. **質問を入力**: テキストエリアに質問や相談内容を入力してください  
    3. **回答を取得**: 「回答を取得」ボタンをクリックすると、選択した専門家AIが回答します
    """)
    
    st.markdown("---")
    
    # メインのインターフェース
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("🎯 専門家を選択")
        selected_expert = st.radio(
            "相談したい分野の専門家を選択してください:",
            list(EXPERTS.keys()),
            index=0
        )
        
        # 選択された専門家の説明を表示
        st.info(f"**{selected_expert}**\n\n{EXPERTS[selected_expert]}")
    
    with col2:
        st.subheader("💬 質問・相談内容")
        input_text = st.text_area(
            "質問や相談内容を入力してください:",
            height=150,
            placeholder="例: Pythonでファイルを読み込む方法を教えてください"
        )
        
        # 回答取得ボタン
        if st.button("🚀 回答を取得", type="primary"):
            if input_text.strip():
                with st.spinner("回答を生成中..."):
                    response = get_expert_response(input_text, selected_expert)
                
                st.markdown("---")
                st.subheader("📝 回答")
                st.markdown(response)
            else:
                st.warning("質問を入力してください。")

if __name__ == "__main__":
    main()
