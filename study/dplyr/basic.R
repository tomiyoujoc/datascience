library("dplyr")
library("tibble")
library("ca")

author.df <- data.frame(author)
author.df <- rownames_to_column(author.df, "text")

#行抽出
filter(author.df, text=="east wind (buck)")
filter(author.df, a > 100, b > 100)

#列抽出
select(author.df, text, z)
select(author.df, text, a, i, u, e, o)
select(author.df, text, c(a:e))
select(author.df, -c(a:w))

#列追加
mutate(author.df, new_col=x+y+z)

#並び替え
arrange(author.df, a)
