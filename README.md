TDD本をPythonで写経する
======================

## 環境の立ち上げ方

```bash
docker-compose run --rm tdd bash
```

## テストの実行方法

```bash
python ./testmoney.py
```

## TODO

**課題**
- $5 + 10CHF = $10(レートが2:1の場合)
- moneyの丸め処理をどうするか
- amountをprivateにする

**完了**
- Dollerの副作用をどうするか
- $5 * 2 = $10
