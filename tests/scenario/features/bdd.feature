Feature: BDD
    Logging of pyigata

    Scenario: デバッグログ出力
        Given level=0のログレベルがロガーに与えられる

        # When level=0のログの出力を実行する

        Then level=0のログが出力される

    Scenario: インフォメーションログ出力
        Given level=1のログレベルがロガーに与えられる

        # When level=1のログの出力を実行する

        Then level=1のログが出力される
