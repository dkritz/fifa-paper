# I draw values for each of the variables and multiply by country characteristics
# 
# n countries in rows
# m characteristics in columns
# 
# so now we have n*m matrix of values
# 
# Model <- rnorm(11,mean=Model[,2],sd=abs(Model[,3]))

# Data will hold the characteristics of the countries

Data <- UEFA[,5:11]

# UEFA[,5:11] * rnorm(11,mean=Model[,2],sd=abs(Model[,3]))
# Data * Model
# Model saves a single draw and reuses it 
# naming it kills the seed, in other words
# 
# II now we need to calculate the FPS
# 
# Result <- Data * Model
# Make this draw new values each time it is used
# 
# this would be a single run
# 
# then square and sum up the product Data * Model as we need it
# 
# III how to refer to individual columns for squaring and adding?
# pull the index value of the maximum value
# need to know which country is which row index

# Multiply the Characteristics by a random draw from the distribution of their model coefficients

Result <- Data * rnorm(11,mean=Model[,2],sd=abs(Model[,3]))

# Carry out the sum (and sum of squares) for the calculation of FIFA points

FPS <- Result[,1]+Result[,2]+Result[,2]^2+Result[,3]+Result[,4]+Result[,5]+Result[,6]+Result[,6]^2+Results[,7]

# Identify the country index number of the highest FIFA points

UEFA[which(FPS == max(FPS)),1]

# store the value in a matrix of names and their counts

Store <- c(Data[,1], magteajf;lksajfsl ones!

# 
# IV and then do it X times
# write a loop
# 
# V and store the results 
# 
# VI at the end of X runs, calculate the odds of each team winning
