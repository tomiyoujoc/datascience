library("dplyr")

iris %>%
  group_by(Species) %>%
  summarise(count = n(),
            Sepal.Length.mean=mean(Sepal.Length),
            Sepal.Width.mean=mean(Sepal.Width))
