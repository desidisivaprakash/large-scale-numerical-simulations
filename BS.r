BS <- function(s,k,T,r,sig,type="c"){
  d1 <- (log(s/k)+(r+sig^2/2)*T)/(sig*sqrt(T))
  d2 <- d1 -sig*sqrt(T)
  if (type=="c") {
    value <- s*pnorm(d1)-k*exp(-r*T)*pnorm(d2)
  }
  if(type=="p"){
    value <-k*exp(-r*T)*pnorm(-d2)-s*pnorm(-d1)
  }
  return(value)
}

