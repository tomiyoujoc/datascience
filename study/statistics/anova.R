#分散分析
# 3つ以上の群の間の平均に差があるかを調べる
# t検定を繰り返す場合、差が出る確率が高くなってしまうため
# 分散分析を使う

#帰無仮説：「群の母平均は等しい」
#対立仮説：「群の母平均は等しくない」
#検定統計量Fを用いる

#(参考)F分布のグラフ
curve(df(x, 6, 18), 0, 5)

#1要因の分散分析
oneway.test(iris$Sepal.Length~iris$Species,
            var.equal = TRUE)

#分散分析表
summary(aov(iris$Sepal.Length~iris$Species))
anova(lm(iris$Sepal.Length~iris$Species))

#多重比較
TukeyHSD(aov(iris$Sepal.Length~iris$Species))

#2要因の分散分析
titanic <- read.csv("data/titanic.csv")
summary(aov(titanic$Survived~titanic$Sex*titanic$Pclass))

interaction.plot(titanic$Sex, titanic$Pclass, titanic$Survived)
