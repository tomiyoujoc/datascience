library("tm")
library("stringr")
library("stringi")

#記号を削除
s <- "Hello, World! おはよう。こんにちは、世界！"
s <- stri_trans_nfkc(s)
s <- removePunctuation(s)
s <- str_replace_all(s, "、|。", "") 
cat(s)

#数字を削除
s <- "1年2ヶ月ぶり"
s <- removeNumbers(s)
cat(s)

#大文字、小文字変換
s <- "Hello World."
str_to_upper(s)
str_to_lower(s)

#ひらがなを削除
s <- "Hello, World! おはよう。こんにちは、世界！"
str_replace_all(s, "\\p{Hiragana}", "")

#複数の表記体系で使用される共通の語を削除
s <- "Hello, World! おはようニューヨーク。こんにちは、世界！"
s <- str_replace_all(s, "\\p{Katakana}", "")
cat(s)
s <- str_replace_all(s, "\\p{Common}", "")
cat(s)

#漢字だけを抽出
s <- "Hello, World! おはようニューヨーク。こんにちは、世界！"
str_match_all(s, "\\p{Han}")

