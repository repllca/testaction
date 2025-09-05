# GitHub Actions CI Workflow

このリポジトリでは、GitHub Actions を使って **Python の環境構築とテスト実行** を自動化しています。  
`main` ブランチにコードが push されると、自動的にワークフローが実行されます。

---

## ワークフローの内容

- **トリガー**
  - `main` ブランチへの push で実行

- **処理内容**
  1. リポジトリのコードをチェックアウト
  2. Python 3.8 の環境を構築
  3. `requirements.txt` に記載された依存関係をインストール
  4. `PYTHONPATH` を設定
  5. `pytest` によるテストを実行

---

## ワークフローのYAMLファイル

```yaml
name: Deploy

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: リポジトリのチェックアウト
        uses: actions/checkout@v2

      - name: pythonの環境構築
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'

      - name: 依存関係のインストール
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: PYTHONPATHの設定
        run: echo "PYTHONPATH=$PYTHONPATH:$(pwd)" >> $GITHUB_ENV

      - name: テスト実行
        run: |
          pytest
