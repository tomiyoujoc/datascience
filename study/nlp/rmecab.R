library("RMeCab")
library("purrr")
library("magrittr")

#わかち書き
rmc <- RMeCabC("すももももものもものうち")
unlist(rmc)

#単語だけ取り出す
map_chr(rmc, extract(1))

#
rmct <- RMeCabText("./data/merosu.txt")
head(rmct)

#頻度表の作成
rmcf <- RMeCabFreq("./data/merosu.txt")
head(rmcf)
arrange(rmcf, desc(Freq))

rmcf_meishi <- rmcf %>%
  filter(Info1 == "名詞")
