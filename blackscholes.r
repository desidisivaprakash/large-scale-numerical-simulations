blackscholes <- function(s,x,rf,T,sigma){
  values <- c(2)
  d1 <- (log(s/x)+(rf+sigma^2/2)*T)/sigma*sqrt(T)
  d2 <- d1-sigma*sqrt(T)
  values[1] <- s*pnorm(d1) - x*exp(-rf*T)*pnorm(d2)
  values[2] <- x*exp(-rf*T)*pnorm(-d2)-s*pnorm(-d1)
  values
}


