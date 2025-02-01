# photo-sharing-app
📷 Djangoで写真共有＆コラージュアプリを作る！（オープンソース） A photo-sharing and collage creation app using Django! (Open Source)
# 📷 Photo Sharing App - 写真共有アプリ

## 🌟 Overview - 概要
This is an open-source project using Django to create a **photo-sharing and collage app**.  
家族や友人と写真を共有し、自動でコラージュを作成できる **写真共有＆コラージュアプリ** をDjangoで開発しています。

## 🚀 Features - 機能
- 🖼️ **Upload one photo per day** - 1日1枚の写真アップロード
- 🎨 **Generate automatic collages** - 自動コラージュ作成
- 🔒 **Private group sharing** - クローズドなグループ共有
- 📆 **View in calendar format** - カレンダー形式で表示

## 🛠 Tech Stack - 技術スタック
- **Backend:** Django, Django REST Framework
- **Frontend:** HTMX, Bootstrap
- **Infrastructure:** Docker, AWS S3

## 📦 Installation - インストール
To set up the project locally, follow these steps:  
ローカル環境でプロジェクトをセットアップするには、以下の手順を実行してください。

```bash
git clone https://github.com/your-username/photo-sharing-app.git
cd photo-sharing-app
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
