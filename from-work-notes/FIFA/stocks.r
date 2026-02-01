# Get quantmod
if (!require("quantmod")) {
    install.packages("quantmod")
    library(quantmod)
}

start <- as.Date("2016-01-01")
end <- as.Date("2016-10-01")
