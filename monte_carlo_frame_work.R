T = 1000
theta = 0

norm1 = matrix(rnorm(3*T,mean=0,sd=1), 1, T)
norm2 = matrix(rnorm(3*T,mean=1,sd=2), 1, T)
norm3 = matrix(rnorm(3*T,mean=2,sd=sqrt(2)), 1, T)
norm = rbind(norm1,norm2,norm3)
h = norm[1,]
for (i in 1:T){
  h[i] = (norm[1,i] + norm[2,i] + norm[3,i])/3
  theta <- theta + h[i]
}
theta = theta/T

print(theta)