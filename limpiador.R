# tiempoInicio <- Sys.time()
prepararAmbiente <- function(){
  if (!is.element("tidyverse", installed.packages())){
    install.packages("tidyverse")
  }
  if (!is.element("jsonlite", installed.packages())){
    install.packages("jsonlite")
  }
}

prepararAmbiente()

library("tidyverse")
library("jsonlite")

args = commandArgs(trailingOnly=TRUE)
path_loc <- args[1]
archivoOrigen <- args[2]
setwd(path_loc)

dataOriginal <- fromJSON(archivoOrigen) %>% as_tibble()
dataOriginal$TotalCharges <- as.numeric(dataOriginal$TotalCharges)
#reemplazar los nulos con la media
dataMCLimpio <- dataOriginal %>% mutate(MonthlyCharges = replace(MonthlyCharges, is.na(MonthlyCharges), median(MonthlyCharges, na.rm= TRUE)))

#reemplazar lo q hayan puesto para decir q es nulo por un nulo real
dataTCLimpio <- dataMCLimpio %>% mutate(TotalCharges = replace(TotalCharges, TotalCharges == "na", NA)) %>% mutate(
  TotalCharges = replace(TotalCharges, TotalCharges == "N/A", NA)) %>% mutate(
    TotalCharges = replace(TotalCharges, is.na(TotalCharges), median(TotalCharges, na.rm = TRUE)))
#reemplazar lo q hayan puesto para decir q es nulo por un nulo real
dataFinal <- dataTCLimpio %>% mutate(PaymentMethod = replace(PaymentMethod, PaymentMethod == "--", NA)) %>% mutate(
  PaymentMethod = replace(PaymentMethod, PaymentMethod == "", NA)) %>% mutate(
    PaymentMethod = replace(PaymentMethod, is.na(PaymentMethod), "No encontrado"))

path_loc <- args[3]
setwd(path_loc)
nombreArchivoFinal <- "resultado.json"

# nombreArchivoFinal <- str_glue("resultado.json")
write_json(dataFinal, nombreArchivoFinal)