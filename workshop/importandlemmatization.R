require(quanteda)
SDF$text <- gsub("[^[:alnum:][:space:][:punct:]]", "", SDF$text)
workcorpus2 <- corpus(SDF) #<< 
texts(workcorpus2) <- iconv(texts(workcorpus2), from = "UTF-8", to = "ASCII", sub = "")
#summary(workcorpus2, n = 3, tolower = FALSE, showmeta = TRUE)
require(quanteda)
toksworkcorpus2 <- tokens(workcorpus2, remove_punct = FALSE, remove_numbers = FALSE, remove_symbols = FALSE, remove_separators = TRUE, split_hyphens = FALSE, remove_url = FALSE)


data <- read.csv("./lemmatization-en.txt", sep = '\t', as.is = TRUE,
                 header = FALSE)
dict <- dictionary(split(data[,2], data[,1])) #dictionary of lemmas
  
tokslemmasubworkcorpus <- tokens_lookup(toksworkcorpus2, dict, valuetype = 'fixed', exclusive = FALSE, capkeys = FALSE, case_insensitive = TRUE) #lemmatization of the corpus

lemmanostoptokssubworkcorpus <- tokens_select(tokslemmasubworkcorpus, pattern = stopwords('en'), selection = 'remove', case_insensitive = TRUE) #removal of stopwords

lemmanotpuncnostoptokssubworkcorpus <- lemmanostoptokssubworkcorpus %>% tokens_remove('[\\p{P}\\p{S}]', valuetype = 'regex', padding = TRUE) #removal of math signs as well as punctuatioN

DTM_L <- dfm(lemmanotpuncnostoptokssubworkcorpus, remove_punct = FALSE, tolower = FALSE, dictionary_regex=TRUE, language = "english", stem = FALSE, clean = FALSE, verbose= TRUE)
