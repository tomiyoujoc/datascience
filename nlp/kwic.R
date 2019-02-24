#Rによるやさしいテキストマイニング[活用事例編]の学習
library("RMeCab")
library("dplyr")

dat <- read.csv("data/merosu.txt", header=FALSE) %>%
  RMeCabDF()

head(dat)
list(dat)
length(dat)

#語数を確認
summary(dat) %>%
  head()

#分析データ全体の語数を確認
summary(dat)[, 1] %>%
  as.numeric() %>%
  sum()

summary(dat)[, 1] %>%
  as.numeric() %>%
  summary()

library("ggplot2")

summary(dat)[, 1] %>%
  as.numeric() %>%
  data.frame() %>%
  rename(., value=.) %>%
  ggplot(., aes(x=value)) +
  geom_histogram()

dat.2 <- unlist(dat)
head(dat.2)

dat.3 <- data.frame(dat.2, names(dat.2))
colnames(dat.3) <- c("Morphemes", "POS")
head(dat.3)

table(dat.3[, 1]) %>% 
  sort(., decreasing = TRUE) %>%
  data.frame()

table(dat.3[, 2]) %>%
  sort(., decreasing = TRUE) %>%
  data.frame()

filter(dat.3, POS == "名詞") %>%
  head()

nouns <- filter(dat.3, POS == "名詞")
top.nouns <- as.vector(nouns[, 1]) %>%
  table() %>%
  sort(decreasing = TRUE) %>%
  head(20) %>%
  data.frame()

top.nouns %>%
  ggplot(aes(x=., y=Freq)) +
  geom_bar(stat = "identity") +
  xlab("Nouns") +
  theme_gray(base_family = "HiraKakuPro-W3") +
  theme(axis.text.x = element_text(angle = 90, hjust=1))
  
nouns <- filter(dat.3, POS=="副詞")
top.nouns <- as.vector(nouns[, 1]) %>%
  table() %>%
  sort(decreasing = TRUE) %>%
  head(20) %>%
  data.frame()
top.nouns %>%
  ggplot(aes(x=., y=Freq)) +
  geom_bar(stat = "identity") +
  xlab("Nouns") +
  theme_gray(base_family = "HiraKakuPro-W3") +
  theme(axis.text.x = element_text(angle = 90, hjust=1))

#KWICコンコーダンスを実装
#  注目する単語を中央に置き左右の文脈を表示する
kwic.conc <- function(vector, word, span){
  word.vector <- vector
  word.positions <- which(word.vector == word)
  context <- span
  for(i in seq(word.positions)){
    if(word.positions[i] == 1){
      before <- NULL
    } else {
      start <- word.positions[i] - context
      start <- max(start, 1)
      before <- word.vector[start: (word.positions[i]-1)]
    }
    end <- word.positions[i] + context
    after <- word.vector[(word.positions[i] + 1):end]
    after[is.na(after)] <- ""
    keyword <- word.vector[word.positions[i]]
    cat("------------------", i, "--------------------\n")
    cat(before, "[", keyword, "]", after, "\n")
  }
}

kwic.conc(dat.2, "もう", 5)
kwic.conc(dat.2, "メロス", 5)
