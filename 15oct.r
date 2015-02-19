y <- BSEyear
x <- y[,7]
l <- length(x)
r = rep(0,l-1)
for (i in 1:l-1)
{
  r[i] = (x[i+1]-x[i])/x[i]
}
r
mn=mean(r)
var =var(r)
sd =sd(r)
mn
var
sd
