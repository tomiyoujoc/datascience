#Rを用いた回帰分析の練習
summary(anscombe)
plot(anscombe$x1, anscombe$y1)

#線形回帰
anscombe.lm1 <- lm(y1~x1, anscombe)
summary(anscombe.lm1)

#係数x1はp=0.00217で有意
#自由度調整済み決定係数は0.6295で7割くらい説明できている
#F値はp=0.00217で有意

#Call:
#  lm(formula = y1 ~ x1, data = anscombe)
#
#Residuals:
#  Min       1Q   Median       3Q      Max 
#-1.92127 -0.45577 -0.04136  0.70941  1.83882 
#
#Coefficients:
#  Estimate Std. Error t value Pr(>|t|)   
#(Intercept)   3.0001     1.1247   2.667  0.02573 * 
#  x1            0.5001     0.1179   4.241  0.00217 **
#  ---
#  Signif. codes:  
#  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
#
#Residual standard error: 1.237 on 9 degrees of freedom
#Multiple R-squared:  0.6665,	Adjusted R-squared:  0.6295 
#F-statistic: 17.99 on 1 and 9 DF,  p-value: 0.00217

plot(anscombe$x1, anscombe$y1)
abline(anscombe.lm1)

#予測
test <- data.frame(x1=c(4,5))
predict(anscombe.lm1, test)

#結果のプロット
par(mfrow=c(2,2))
plot(anscombe.lm1)

#重回帰分析
anscombe.lm2 <- lm(y1~x1+x2+x3+x4, anscombe)
summary(anscombe.lm2)

#Call:
#  lm(formula = y1 ~ x1 + x2 + x3 + x4, data = anscombe)
#
#Residuals:
#  Min       1Q   Median       3Q      Max 
#-1.87818 -0.18500 -0.01036  0.54964  1.88818 
#
#Coefficients: (2 not defined because of singularities)
#Estimate Std. Error t value
#(Intercept)  4.33291    2.21774   1.954
#x1           0.45073    0.14012   3.217
#x2                NA         NA      NA
#x3                NA         NA      NA
#x4          -0.09873    0.14012  -0.705
#Pr(>|t|)  
#(Intercept)   0.0865 .
#x1            0.0123 *
#  x2                NA  
#x3                NA  
#x4            0.5011  
#---
#  Signif. codes:  
#  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05
#‘.’ 0.1 ‘ ’ 1
#
#Residual standard error: 1.273 on 8 degrees of freedom
#Multiple R-squared:  0.686,	Adjusted R-squared:  0.6075 
#F-statistic:  8.74 on 2 and 8 DF,  p-value: 0.009718

#期待正規ランクスコアをプロット
qqnorm(resid(anscombe.lm2))
qqline(resid(anscombe.lm2), lwd=2, col="red")

#反復特徴量選択
anscombe.lm3 <- step(anscombe.lm2)
summary(anscombe.lm3)

qqnorm(resid(anscombe.lm3))
qqline(resid(anscombe.lm3), lwd=2, col="red")
