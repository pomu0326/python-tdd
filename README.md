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

- $5 + 10CHF = $10(レートが2:1の場合)
- $5 * 2 = $10
- amountをprivateにする
- Dollerの副作用をどうするか
- moneyの丸め処理をどうするか
