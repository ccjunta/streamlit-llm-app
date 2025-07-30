# 🤖 AI専門家相談アプリ

StreamlitとLangChainを使用した、異なる分野の専門家AIと相談できるWebアプリケーションです。

## 🌟 機能

- 複数の専門分野（プログラミング、料理、健康・フィットネス、旅行）から選択可能
- OpenAI GPT-4o-miniを使用したAI回答
- 直感的なWebインターフェース

## 🚀 Streamlit Cloudでのデプロイ

### 1. レポジトリをフォーク/クローン

### 2. Streamlit Cloudでアプリを作成
1. [Streamlit Cloud](https://streamlit.io/cloud)にアクセス
2. GitHubアカウントでログイン
3. 「New app」をクリック
4. このレポジトリを選択

### 3. Secretsの設定
Streamlit Cloudのアプリ設定で、以下のSecretsを追加してください：

```toml
[secrets]
OPENAI_API_KEY = "your-openai-api-key-here"
```

### 4. デプロイ
設定完了後、自動的にデプロイが開始されます。

## 🛠️ ローカル開発

### 前提条件
- Python 3.8以上
- OpenAI APIキー

### インストール
```bash
git clone https://github.com/yourusername/streamlit-llm-app.git
cd streamlit-llm-app
pip install -r requirements.txt
```

### 環境変数の設定
`.env`ファイルを作成：
```
OPENAI_API_KEY=your-openai-api-key-here
```

### 実行
```bash
streamlit run app.py
```

## 📋 依存関係

主要なライブラリ：
- `streamlit`: Webアプリフレームワーク
- `langchain-openai`: OpenAI LLM integration
- `langchain-core`: LangChain核心機能
- `python-dotenv`: 環境変数管理（ローカル開発用）

## 🔒 セキュリティ

- APIキーは環境変数またはStreamlit Secretsで管理
- 機密情報がコードに直接含まれることはありません

## 📄 ライセンス

MIT License