###we are going to find means, variances and covariances
###for the continuously compounded returns on Microsoft, Nordstrom and Starbucks
###(assets A, B and C) based on sample statistics computed over the
### five-year period January, 1995 through January, 2001

c1 <- read.csv("C:/Users/siva/Desktop/dsp/lsns/c1.csv", header=FALSE)
c2 <- read.csv("C:/Users/siva/Desktop/dsp/lsns/c2.csv", header=FALSE)
c3 <- read.csv("C:/Users/siva/Desktop/dsp/lsns/c3.csv", header=FALSE)

ta = c1[2]
mta = mean(ta)
tb = c2[2]
mtb = mean(tb)
tc = c3[2]
mtc = mean(tc)


asset.names <- c("MSFT", "NORD", "SBUX")
mu.vec = c(-0.0003500696, -0.001742344, 0.008025195)
names(mu.vec) = asset.names
sigma.mat = matrix(c(var(ta),cov(tb,ta),cov(tc,ta),cov(ta,tb),var(tb),cov(tc,tb),cov(ta,tc),cov(tb,tc),var(tc)),nrow=3, ncol=3)
dimnames(sigma.mat) = list(asset.names, asset.names)

################################################################

x.vec = rep(1,3)/3
names(x.vec) = asset.names
mu.p.x = crossprod(x.vec,mu.vec)
sig2.p.x = t(x.vec)%*%sigma.mat%*%x.vec
sig.p.x = sqrt(sig2.p.x)

#######################################################

y.vec = c(0.8, 0.4, -0.2)
names(x.vec) = asset.names
sig.xy = t(x.vec)%*%sigma.mat%*%y.vec


#################
# now going to fing optimal weight matrix #################### denoted by "m"
########################################## (solve = inverse )

top.mat = cbind(2*sigma.mat, rep(1, 3))
bot.vec = c(rep(1, 3), 0)
Am.mat = rbind(top.mat, bot.vec)
b.vec = c(rep(0, 3), 1)
z.m.mat = solve(Am.mat)%*%b.vec
m.vec = z.m.mat[1:3,1]

###################################################
#####    The expected return on this portfolio,  "mu.gmin" ####


mu.gmin = as.numeric(crossprod(m.vec, mu.vec))

######################################
####  The portfolio variance and standard deviation, are sig.gmin and sig2.gmin


sig2.gmin = as.numeric(t(m.vec)%*%sigma.mat%*%m.vec)
sig.gmin = sqrt(sig2.gmin)

###############################################################
###############################################################
#####
##### Efficient portfolio with the same expected return and variance as Microsoft  with weight "x"

top.mat = cbind(2*sigma.mat, mu.vec, rep(1, 3))
mid.vec = c(mu.vec, 0, 0)
bot.vec = c(rep(1, 3), 0, 0)
A.mat = rbind(top.mat, mid.vec, bot.vec)
bmsft.vec = c(rep(0, 3), mu.vec["MSFT"], 1)
z.mat = solve(A.mat)%*%bmsft.vec
x.vec = z.mat[1:3,]

#### expected return 
mu.px = as.numeric(crossprod(x.vec, mu.vec))

##### variance  

sig2.px = as.numeric(t(x.vec)%*%sigma.mat%*%x.vec)
sig.px = sqrt(sig2.px)

###############################################################
###############################################################
#####
##### Efficient portfolio with the same expected return and variance as Microsoft  with weight "y"

bsbux.vec = c(rep(0, 3), mu.vec["SBUX"], 1)
z.mat = solve(A.mat)%*%bsbux.vec
y.vec = z.mat[1:3,]

##### Expected return

mu.py = as.numeric(crossprod(y.vec, mu.vec))

##### varinace

sig2.py = as.numeric(t(y.vec)%*%sigma.mat%*%y.vec)
sig.py = sqrt(sig2.py)
sigma.xy = as.numeric(t(x.vec)%*%sigma.mat%*%y.vec)
rho.xy = sigma.xy/(sig.px*sig.py)


###################################################################

#####  Creating an arbitrary frontier portfolio from two efficient portfolios using above "x.vec" and "y.vec"    #####

####    the new frontier portfolio is computed using   "z.vec"

a = 0.5
z.vec = a*x.vec + (1-a)*y.vec

#############################################
#####  The expected return, variance and standard deviation of this portfolio are


mu.pz = as.numeric(crossprod(z.vec, mu.vec))
sig2.pz = as.numeric(t(z.vec)%*%sigma.mat%*%z.vec)
sig.pz = sqrt(sig2.pz)

############################################
##### NOTE ######
### if we take weigth like  "a" and "1-a"  again we get same expected return, variance and standard deviation of this portfolio

# mu.pz = a*mu.px + (1-a)*mu.py
# sig.xy = as.numeric(t(x.vec)%*%sigma.mat%*%y.vec)
# sig2.pz = a^2 * sig2.px + (1-a)^2 * sig2.py + 2*a*(1-a)*sig.xy
# sig.pz = sqrt(sig2.pz)

############################################################################


###### Because mu.pz  = 0???0356 > mu.pm = 0???02489 the frontier portfolio z is an efficient portfolio #################


### now create 



a = seq(from=1, to=-1, by=-0.1)
n.a = length(a)
z.mat = matrix(0, n.a, 3)
mu.z = rep(0, n.a)
sig2.z = rep(0, n.a)
sig.mx = t(m.vec)%*%sigma.mat%*%x.vec
for (i in 1:n.a) {
  z.mat[i, ] = a[i]*m.vec + (1-a[i])*x.vec
  mu.z[i] = a[i]*mu.gmin + (1-a[i])*mu.px
  sig2.z[i] = a[i]^2 * sig2.gmin + (1-a[i])^2 * sig2.px + 2*a[i]*(1-a[i])*sig.mx
}


plot(sqrt(sig2.z), mu.z, type="b", pch=16, col="blue", ylab=expression(mu[p]),xlab=expression(sigma[p]))
text(sig.gmin, mu.gmin, labels="Global min", pos=4)
#text(sd.vec, mu.vec, labels=asset.names, pos=4)

#####################################
########## tangentancy portfolio ####

rf = 0.005
sigma.inv.mat = solve(sigma.mat)
one.vec = rep(1, 3)
mu.minus.rf = mu.vec - rf*one.vec
top.mat = sigma.inv.mat%*%mu.minus.rf
bot.val = as.numeric(t(one.vec)%*%top.mat)
t.vec = top.mat[,1]/bot.val

##### mean ########
mu.t = as.numeric(crossprod(t.vec, mu.vec))

############## variance #############
sig2.t = as.numeric(t(t.vec)%*%sigma.mat%*%t.vec)
sig.t = sqrt(sig2.t)

################ sharp ratio ##################

SRt = (mu.t-rf)/sig.t

######## wieght #############
x.t.02 = 0.02/sig.t
x.t.02
1-x.t.02

x.t.02*t.vec
mu.t.02 = x.t.02*mu.t + (1-x.t.02)*rf
sig.t.02 = x.t.02*sig.t

##########################################
###The expected return and volatility values of this portfolio are ##########
################################################

x.t.07 = (0.07 - rf)/(mu.t - rf)
x.t.07*t.vec


mu.t.07 = x.t.07*mu.t + (1-x.t.07)*rf
sig.t.07 = x.t.07*sig.t

m=(mu.t.07-mu.t.02)/(sig.t.07-sig.t.02)
c=mu.t.07-m*(sig.t.07)
abline(c,m)