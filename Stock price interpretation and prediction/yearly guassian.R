data  <- read.csv ("~/Downloads/mygeodata/stock_prices.csv")
# Convert the Date column to Date format
data$Date <- as.Date(data$Date, format = "%d %b %Y")

# Check the structure again to confirm the conversion
str(data$Date)
# Filter the data for the year 2021
library(lubridate)
data_2021 <- data[year(data$Date) == 2021, ]

# Calculate max, min, and bin width for the filtered data
max_closing_price_2021 <- max(data_2021$Closing_Price, na.rm = TRUE)
min_closing_price_2021 <- min(data_2021$Closing_Price, na.rm = TRUE)
bin_width_2021 <- (max_closing_price_2021 - min_closing_price_2021) / 500

# Ensure the bin width has a difference of 10
bin_width_adjusted_2021 <- max(10, bin_width_2021)

# Plot the histogram of Closing_Price for 2021
library(ggplot2)
ggplot(data_2021, aes(x = Closing_Price)) +
  geom_histogram(binwidth = bin_width_adjusted_2021, fill = "skyblue", color = "black") +
  labs(title = "Closing Price Distribution for 2021",
       x = "Closing Price",
       y = "Frequency") +
  theme_minimal()







data  <- read.csv ("~/Downloads/mygeodata/stock_prices.csv")
# Convert the Date column to Date format
data$Date <- as.Date(data$Date, format = "%d %b %Y")

# Check the structure again to confirm the conversion
str(data$Date)
# Filter the data for the year 2020
library(lubridate)
data_2020 <- data[year(data$Date) == 2020, ]

# Calculate max, min, and bin width for the filtered data
max_closing_price_2020 <- max(data_2020$Closing_Price, na.rm = TRUE)
min_closing_price_2020 <- min(data_2020$Closing_Price, na.rm = TRUE)
bin_width_2020 <- (max_closing_price_2020 - min_closing_price_2020) / 10

# Ensure the bin width has a difference of 10
bin_width_adjusted_2020 <- max(10, bin_width_2020)




# Plot the histogram of Closing_Price for 2020
library(ggplot2)
ggplot(data_2019, aes(x = Closing_Price)) +
  geom_histogram(binwidth = bin_width_adjusted_2019, fill = "skyblue", color = "black") +
  labs(title = "Closing Price Distribution for 2019",
       x = "Closing Price",
       y = "Frequency") +
  theme_minimal()

data  <- read.csv ("~/Downloads/mygeodata/stock_prices.csv")
# Convert the Date column to Date format
data$Date <- as.Date(data$Date, format = "%d %b %Y")

# Check the structure again to confirm the conversion
str(data$Date)
# Filter the data for the year 2019
library(lubridate)
data_2019 <- data[year(data$Date) == 2019, ]

# Calculate max, min, and bin width for the filtered data
max_closing_price_2019<- max(data_2019$Closing_Price, na.rm = TRUE)
min_closing_price_2019 <- min(data_2019$Closing_Price, na.rm = TRUE)
bin_width_2019 <- (max_closing_price_2019 - min_closing_price_2020) / 10

# Ensure the bin width has a difference of 10
bin_width_adjusted_2019 <- max(10, bin_width_2019)

# Plot the histogram of Closing_Price for 2020
library(ggplot2)
ggplot(data_2020, aes(x = Closing_Price)) +
  geom_histogram(binwidth = bin_width_adjusted_2019, fill = "skyblue", color = "black") +
  labs(title = "Closing Price Distribution for 2019",
       x = "Closing Price",
       y = "Frequency") +
  theme_minimal()

  





data  <- read.csv ("~/Downloads/mygeodata/stock_prices.csv")
# Convert the Date column to Date format (assuming it's in "DD Mon YYYY" format)
data$Date <- as.Date(data$Date, format = "%d %b %Y")

# Check the structure to confirm the conversion
str(data$Date)

# Filter data for November 2019 to November 2020
library(dplyr)
data_filtered <- data %>%
  filter(Date >= as.Date("2019-11-01") & Date <= as.Date("2020-11-30"))

# Check the first few rows of the filtered data
head(data_filtered)
max_data_filtered<- max(data_filtered$Closing_Price, na.rm = TRUE)
min_data_filtered <- min(data_filtered$Closing_Price, na.rm = TRUE)
bin_width_data_filtered <- (max_data_filtered - min_data_filtered) / 500

# Ensure the bin width has a difference of 10
bin_width_adjusted_data_filtered <- max(10, bin_width_data_filtered)

# Plot the histogram of Closing_Price for 2020
library(ggplot2)
ggplot(data_filtered, aes(x = Closing_Price)) +
  geom_histogram(binwidth = bin_width_adjusted_data_filtered, fill = "skyblue", color = "black") +
  labs(title = "Closing Price Distribution for 2019-20",
       x = "Closing Price",
       y = "Frequency") +
  theme_minimal()




data  <- read.csv ("~/Downloads/mygeodata/stock_prices.csv")
# Convert the Date column to Date format (assuming it's in "DD Mon YYYY" format)
data$Date <- as.Date(data$Date, format = "%d %b %Y")

# Check the structure to confirm the conversion
str(data$Date)

# Filter data for November 2020 to November 2021
library(dplyr)
data_filtered <- data %>%
  filter(Date >= as.Date("2020-11-01") & Date <= as.Date("2021-11-30"))

# Check the first few rows of the filtered data
head(data_filtered)
max_data_filtered<- max(data_filtered$Closing_Price, na.rm = TRUE)
min_data_filtered <- min(data_filtered$Closing_Price, na.rm = TRUE)
bin_width_data_filtered <- (max_data_filtered - min_data_filtered) / 500

# Ensure the bin width has a difference of 10
bin_width_adjusted_data_filtered <- max(10, bin_width_data_filtered)

# Plot the histogram of Closing_Price for 2020-21
library(ggplot2)
ggplot(data_filtered, aes(x = Closing_Price)) +
  geom_histogram(binwidth = bin_width_adjusted_data_filtered, fill = "skyblue", color = "black") +
  labs(title = "Closing Price Distribution for 2020-21",
       x = "Closing Price",
       y = "Frequency") +
  theme_minimal()




data  <- read.csv ("~/Downloads/mygeodata/stock_prices.csv")
# Convert the Date column to Date format (assuming it's in "DD Mon YYYY" format)
data$Date <- as.Date(data$Date, format = "%d %b %Y")

# Check the structure to confirm the conversion
str(data$Date)

# Filter data for November 2021 to November 2022
library(dplyr)
data_filtered <- data %>%
  filter(Date >= as.Date("2021-11-01") & Date <= as.Date("2022-11-30"))

# Check the first few rows of the filtered data
head(data_filtered)
max_data_filtered<- max(data_filtered$Closing_Price, na.rm = TRUE)
min_data_filtered <- min(data_filtered$Closing_Price, na.rm = TRUE)
bin_width_data_filtered <- (max_data_filtered - min_data_filtered) / 100

# Ensure the bin width has a difference of 10
bin_width_adjusted_data_filtered <- max(10, bin_width_data_filtered)

# Plot the histogram of Closing_Price for 2020-21
library(ggplot2)
ggplot(data_filtered, aes(x = Closing_Price)) +
  geom_histogram(binwidth = bin_width_adjusted_data_filtered, fill = "skyblue", color = "black") +
  labs(title = "Closing Price Distribution for 2021-22",
       x = "Closing Price",
       y = "Frequency") +
  theme_minimal()




data  <- read.csv ("~/Downloads/mygeodata/stock_prices.csv")
# Convert the Date column to Date format (assuming it's in "DD Mon YYYY" format)
data$Date <- as.Date(data$Date, format = "%d %b %Y")

# Check the structure to confirm the conversion
str(data$Date)

# Filter data for November 2022 to November 2023
library(dplyr)
data_filtered <- data %>%
  filter(Date >= as.Date("2022-11-01") & Date <= as.Date("2023-11-30"))

# Check the first few rows of the filtered data
head(data_filtered)
max_data_filtered<- max(data_filtered$Closing_Price, na.rm = TRUE)
min_data_filtered <- min(data_filtered$Closing_Price, na.rm = TRUE)
bin_width_data_filtered <- (max_data_filtered - min_data_filtered) / 500

# Ensure the bin width has a difference of 10
bin_width_adjusted_data_filtered <- max(10, bin_width_data_filtered)

# Plot the histogram of Closing_Price for 2022-23
library(ggplot2)
ggplot(data_filtered, aes(x = Closing_Price)) +
  geom_histogram(binwidth = bin_width_adjusted_data_filtered, fill = "skyblue", color = "black") +
  labs(title = "Closing Price Distribution for 2023-22",
       x = "Closing Price",
       y = "Frequency") +
  theme_minimal()




data  <- read.csv ("~/Downloads/mygeodata/stock_prices.csv")
# Convert the Date column to Date format (assuming it's in "DD Mon YYYY" format)
data$Date <- as.Date(data$Date, format = "%d %b %Y")

# Check the structure to confirm the conversion
str(data$Date)

# Filter data for November 2023 to November 2024
library(dplyr)
data_filtered <- data %>%
  filter(Date >= as.Date("2023-11-01") & Date <= as.Date("2024-11-30"))

# Check the first few rows of the filtered data
head(data_filtered)
max_data_filtered<- max(data_filtered$Closing_Price, na.rm = TRUE)
min_data_filtered <- min(data_filtered$Closing_Price, na.rm = TRUE)
bin_width_data_filtered <- (max_data_filtered - min_data_filtered) / 500

# Ensure the bin width has a difference of 10
bin_width_adjusted_data_filtered <- max(10, bin_width_data_filtered)

# Plot the histogram of Closing_Price for 2023-24
library(ggplot2)
ggplot(data_filtered, aes(x = Closing_Price)) +
  geom_histogram(binwidth = bin_width_adjusted_data_filtered, fill = "skyblue", color = "black") +
  labs(title = "Closing Price Distribution for 2023-24",
       x = "Closing Price",
       y = "Frequency") +
  theme_minimal()






