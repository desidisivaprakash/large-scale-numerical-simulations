eps <- matrix(c(3,0,0,2,3,0,-5,2,6),3,3)

nu <- matrix(c(0.042,-0.007, 0.015),3,1)
nut <- t(nu)
colnames(nut)<-c("A","B","C")



a <- matrix(c(2*eps,t(nu),1,nu,0,0,1,0,0),5,5)

invA <- solve(A)

b <- matrix(c(0,0,0,0.05,1),5,1)

weight_matrix <- invA%*%b


