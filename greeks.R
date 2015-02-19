BinomialTreeGreeks<- function (S0,K,sigma,r,div,T,n) {
  # parameters of the binomial tree
  dt<-T/n
  u<-exp(sigma*sqrt(dt))
  
  
  d<-1/u
  
  p<-(exp((r-div)*dt)-d)/(u-d)
  
  q<-1-p
  
  disc<-exp(-r*dt);
  
  #initialize matrices
  
  stockM<-matrix(0,nrow=n+1,ncol=n+1)
  
  optionM<-matrix(0,nrow=n+1,ncol=n+1)
  stockM[1,1]<-S0
  x = dim(stockM)
  for(j in 2:x[2]){
    for(i in 1:j-1){
      stockM[i,j]<-(stockM[i,j-1]*u)
    }
    stockM[i+1,j]<-stockM[i,j-1]*d
    
  }
  optionM[,x[2]]<- (stockM[,x[2]]-K)
  for(i in 1:x[1]){
    if(optionM[i,x[2]]< 0){
      optionM[i,x[2]]<-0
    }
  }
 
  
  c = x[2]-1;
  for(j in c:-1:1){
    for(i in j:-1:1){
      optionM[i,j]<-disc*(p*optionM[i,j+1]+q*optionM[i+1,j+1])
    }
  }
  value<-optionM[1,1]
  w1<-optionM[1,2]
  w2<-optionM[2,2]
  s1<-stockM[1,2]
  s2<-stockM[2,2]
  w3<-optionM[1,3]
  w4<-optionM[2,3]
  s3<-stockM[2,3]
  s4<-stockM[3,3]
  s5<-stockM[1,3]
  w5<-optionM[3,3]
  
  
  #print(value)
  
  print(stockM)
  print(optionM)
  #######
  
  delta = (w1-w2)/(s1-s2);
  print(delta)
  
  
  ######
  deltaUp = (w3-w4)/(s5-s3);
  deltaDown = (w4-w5)/(s3-s4);
  gamma = (deltaUp-deltaDown)/((s5-s4)/2);
  print(gamma)
  #######
  theta = (w4-value)/(2*dt);
  
  print(theta)
  
  #####
  #vegaUp = do.call(BinomialTreeGreek,S0,K,sigma+0.01,r,div,T,n);
  #vegaUp=2.816119;
  for (sigma=sigma+0.01){
    vegaUp<-value
  }
  
  #vegaDown = do.call(BinomialTreeGreek,S0,K,sigma-0.01,r,div,T,n);
  vegaDown=2.598555;
  
  vega = (vegaUp - vegaDown)/(2*0.01);
  
  print(vega)
  ##########
  rhoUp = do.call(BinomialTreeGreek,S0,K,sigma,r+0.01,div,T,n);
  
  rhoDown = do.call(BinomialTreeGreek,S0,K,sigma,r-0.01,div,T,n);
  
  rho = (rhoUp - rhoDown)/(2*0.01);
  
  print(rho)
  ######
}
BinomialTreeGreeks(50,60,0.4,0.1,0.05,0.5,5)
