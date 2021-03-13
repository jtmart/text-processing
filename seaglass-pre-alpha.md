# _seaglass_: interpretive text analysis for big data

[![Inline docs](https://camo.githubusercontent.com/3d9beaf849d692cea2ba130f1dbd4a637b4de36eae39da8a484163649b3c0ec5/687474703a2f2f696e63682d63692e6f72672f6769746875622f6477796c2f686170692d617574682d6a7774322e7376673f6272616e63683d6d6173746572)](http://inch-ci.org/github/jtmartelli/seaglass) This document sketches a tentative development outline of a prospective R package 🚀 



## Repo

- 📁 You can clone it from [here](https://github.com/jtmart/seaglass).

- 📈 The flowchart is in the folder `flowchart` (.mm format, edit it with Docear)
- &#128220; the statistical resources are in `references`
- &#128269; original functions are in `base-functions`
- &#128293; our work is in `seaglass-functions`
- &#127775; Evaluate documentation badges (for later): [here](https://inch-ci.org/projects). 
- 🚸 We need to read on the difference between S3 and S4 classes in R ([example](https://stat.ethz.ch/R-manual/R-devel/library/methods/html/Methods_for_S3.html))
- 💡 you can push commits from your device as collaborator or from the VM using the `terminal window` within Rstudio. I configured ssh access (should work):

```
git commit -am "vm 11/01/2021" #check branching
git remote add origin git@github.com:jtmart/seaglass.git
```



## Functions

☑️ Here is a technical outline of the `five` intended functions and one test `dataset` (Modi's Mann ki Baats because it's not too voluminous)



### F1: worduse

- &#128230; *What?* `worduse` generates a new dfm from an original dfm. It computes how likely it is for words in a sub-corpus to be overrepresented or underrepresented when compared to the entire corpus.

- &#128142; *Why?* `worduse` is simple yet powerful function to identify the lexicon specific to a speaker, an institution, a period etc.

- &#128125; Alt name: **pebble**

- ⚡ Requires: `quanteda` and (probably) `dplyr`

- &#128302; Usage of `worduse`:

  ```R
  output <- worduse(adfm, 
                    method = c("score", "prop", "chi2", "exact", "lr", "pmi"), 
                    output = c("dfm", "data.frame", "matrix", "tripletlist", "lda", "tm", "stm", "austin", "topicmodels"), 
                    #sort = c("descending", "ascending", "none"),
                    correction = c("default", "yates", "williams", "none"),
                    na.rm = TRUE,
                    group = NULL, 
                    parallel = TRUE,
                    verbose = TRUE,
                    target = 1L)
  ```

- &#127912; Arguments of `worduse`:

  - **adfm**: a [dfm](https://www.rdocumentation.org/link/dfm?package=quanteda&version=2.1.2) containing the words (tokens/features) to be examined for overrepresentation/underrepresentation (we we call that `representation`, in quanteda the call that `keyness`).

  - **method**: association measure to be used for computing representation (more below). `score` is default if nothing is specified.
  - **sort**: sorts features scored in descending order of the measure, or in ascending order, or leaves in original feature order. `descending` is default if nothing is specified.

  - **correction**: if `"default"`, Yates correction is applied to `"chi2"`; William's correction is applied to `"lr"`; and no correction is applied for the `"score"`, `"frequency"`, `"exact"` and `"pmi"` measures. Specifying a value other than the default can be used to override the defaults, for instance to apply the Williams correction to the chi2 measure.  Specifying a correction for the `"exact"` and `"pmi"` measures has no effect and produces a warning.
  - **na.rm**: logical; if `TRUE` missing values (including NaN) are omitted from the calculations. `TRUE` is default if nothing is specified.
  - **group**: calls the `dfm_group` function described [here](https://www.rdocumentation.org/packages/quanteda/versions/2.0.1/topics/dfm_group). `NULL` is default.
  - **parallel**: logical; if `TRUE` all the cores are used for computation. `TRUE` is default if nothing is specified.
  - **verbose**: logical; provides some sense of the progress of the computation.

  - **target**: the document index (numeric, character or logical) identifying the document forming the "target" for computing keyness; all other documents' feature frequencies will be combined for use as a reference.

- &#128207; Description of the `method` parameters: 

  Calculate the representation of a word being present `f` times in a sub-corpus of `t` words given that it appears a total of `F` times in a whole corpus of `T` words. The function calculates <u>representation in six different ways</u>. 

  1. Default is `score`, i.e. the specificity - or association or surprise - score. 👉 See _Leon_ pp.80- and _TXM_ manual pp.95- for the statistical model (other relevant material is in French only). For other kind of calculations see *Tribble* and *Bondi* and *J93*.

  - Existing R family of functions is called `specificities` in the package `textometry`  available [here](https://github.com/cran/textometry) and [here](https://cran.r-project.org/web/packages/textometry/index.html).

  - To open the function in Rstudio: 

    ```R
    library(textometry)
    View("specificities.distribution.plot") #for an overview of the calculation
    View("specificities.probabilities") #for an overview of the implementation in a dfm (see below)
    # ❗ the object "lexicaltable" is a dataframe that has been produced by the software TXM. It's a dataframe where words are in rows and variables in columns. What we want is a transposed version of variables in rows and words in columns. The data type should be dfm.
    ```

  2. The first alternative is `prop` (relative frequencies aka proportions):

  - The idea is to reuse the function `adorn_percentages` of the package janitor available [here](https://rdrr.io/cran/janitor/man/adorn_percentages.html) and apply it to a dfm object. No need of creating an additional dependency, we could take the function and rewrite our own.
  - Outputs are going to be very small numbers: should we implement a multiplier?

  3. Other alternatives can be taken from quanteda's function `textstat_keyness` available [here](https://www.rdocumentation.org/packages/quanteda/versions/2.1.2/topics/textstat_keyness). ✅ Idem for arguments `correction` and `target`, we can replicate that function. 

- &#128208; Description of the `output` parameters: 

  1. Default is `dfm`, that means that no additional computation is needed
  2. Alternative parameters will be covered through calling the `convert` function of quanteda [here](https://www.rdocumentation.org/packages/quanteda/versions/2.1.2/topics/convert). We need to pipe the computation like this: `original-dfm %>% new-dfm %>% converted-dfm` (ideally without having to call the `dplyr/tidyverse` package).



### F2: wordcontext

- &#128230; *What?* ` wordcontext` returns a list of categories words associated to another list of categories words (dictionary) in a dfm. 

- &#128142; *Why?* `wordcontext` identifies related words of a dictionary based on their distance or association. It acts as a contextualizer of generic seed words proxying a particular theme, emotion, ideology, psychological state etc.

- &#128125; Alt name: **seastar**

- ⚡ Requires: `quanteda` and (again probably) `dplyr`

- &#128302; Usage of `wordcontext`: 

  ```R
  output <- worduse(adfm,
                    adictionary,
                    method = c("txm", "mi", "dice", "ll", "context.xxx"), 
                    sort = c("descending", "ascending", "none"),
                    threshold = NULL, integer,
                    window = NULL, integer,
                    na.rm = TRUE,
                    parallel = TRUE,
                    verbose = TRUE)
  ```

  &#127912; Arguments of `wordconext`:

  - **adfm**: *ibid.* (see supra).

  - **adictionary**: it is a nested list built using the function `dictionary` of quanteda ([here](https://quanteda.io/reference/dictionary.html)). &#128165; Few caveats here: 
    - For testing purposes, we should make this function work with character vectors first. Then we can generalize.
    - We have a quasi-working `python script` (thanks to Nirav) to turn a CSV into a YML dictionary. We could consider taking enabling the integration of the raw CSV (for later).

  - **method**: significance measurement method used to extract semantic links between words. `txm` is default if nothing is specified (even though it will not be developed after the others).
  - **sort**: *ibid.* (see supra).
  - **threshold**: defines a cut-off point defined by the user. `NULL` (no cut-off) is default if nothing is specified.
  - **window**: how many words from both (left and right) sides of a word are checked for cooccurrence. `NULL` (no window) is default if nothing is specified. &#128681; We need an integer here when using the `context.xxx` parameter in `method` argument. We might have to stick to `NULL` for other parameters.
  - **na.rm**:  *ibid.* (see supra).
  - **parallel**:  *ibid.* (see supra).

  &#128207; Description of the `method` parameters: 

  In order to not only count joint occurrence we have to determine their significance. Different significance-measures can be used. 

  1. For `mi`, `dice` and `ll` we can implement [this](https://tm4ss.github.io/docs/Tutorial_5_Co-occurrence.html) tutorial. I believe it is the easiest way, so we can start with that.

  2. For `context.xxx` we can implement [this](https://tutorials.quanteda.io/advanced-operations/target-word-collocations/) tutorial, but instead of nesting the function `textstat_keyness` we are going to nest our fresh `worduse` one 🥳 ! `xxx` has to be one of the `method` parameters of the function `worduse`.   I copy-paste an example taken from a recent work I did (don't pay attention to object names):

     ```R
     nostoptokssubworkcorpus <- tokens_select(ngramstokssubworkcorpus, pattern = stopwords('en'), selection = 'remove', case_insensitive = TRUE)
     notpuncnostoptokssubworkcorpus <- nostoptokssubworkcorpus %>% tokens_remove('[\\p{P}\\p{S}]', valuetype = 'regex', padding = TRUE)
     v2.1 <- c("abnormal", "abnormality", "absolute",	"absolutely",	"accept",	"acceptance",	"accepted",	"accepting",	"accepts",	"accountability",	"accurate","accurately",	"acknowledge", "acknowledge", "activate","activate", "actually",	"adjust", "adjusting","adjusting", "admit",	"admits",	"admitted",	"admitting",	"affect",	"affected",	"affecting",	"affects",	"afterthought",	"afterthoughts",	"against",	"aggravate","aggravates","aggravating", "aggravated",	"ain't",	"aint",	"all",	"allot",	"almost",	"allow", "allows", "allowing", "allowed",	"alot",	"alternative", "alternatives", "although",	"altogether",	"always",	"ambiguous", "ambiguity", "ambiguity", "analysis","analyses",	"analytical", "analytic", "answer", "answers",	"any",	"anybody",	"anyhow",	"anyone","anyones",	"anything",	"anytime",	"anywhere",	"apart",	"apparent",	"apparently",	"appear",	"appeared",	"appearing",	"appears",	"appreciate","appreciated",	"apprehensive",	"approximate", "approximated", "approximation", "approximatively",	"arbitrary",	"aren't",	"arent",	"assume", "assumes",	"assure","assures", "assurance",	"attention", "attentive", "attentionate",	"attribute","attributes",	"aware", "awareness", "barely",	"based",	"basis",	"bc",	"became",	"because",	"become",	"becomes",	"becoming",	"belief", "beliefs", "believe",	"believed",	"believes",	"believing",	"besides",	"bet",	"bets",	"betting",	"blatant", "blatantely",	"blur","blurred",	"bosses",	"but",	"can't",	"cannot",	"cant", "category", "categories",	"cause", "caused", "causes", "causing", "certain",	"chance",	"chances", "change",	"change","changed",	"changes",	"changing",	"choice", "choices",	"choose", "chooses",	"clarify", "clarified", "clarification",	"clear",	"clearly",	"closure",	"clue",	"coherent", "coherence",	"commit",	"commited", "commitment", "commitments",	"commits",	"committed",	"committing",	"compel", "compels", "compelling",	"complete",	"completed",	"completely",	"completes",	"complex",	"complexity",	"compliance",	"compliant",	"complicate",	"complicated",	"complicates",	"complicating",	"complication", "complications",	"complied",	"complies",	"comply", "complies", "complying",	"comprehsive", "comprehend", "comprehending",	"concentrate", "concentrating", "concentrated",	"conclude", "concluded", "concluding",	"conclusion", "conclusions", "concluded", "conclusive",	"confess", "confessed", "confession",	"confidence",	"confident",	"confidently",	"confuse",	"confused",	"confuses",	"confusing",	"confusion", "confusions",	"conscious", "consciously",	"consequence", "consequences",	"consider",	"consideration",	"considered",	"considering",	"considers",	"contemplate", "contemplating",	"contingent",	"control",	"convince", "convinces", "convinced", "convincing", "correct", "correction", "corrections",	"correlate", "correlates", "correlation",	"cos",	"could",	"could've",	"couldn't",	"couldnt",	"couldve",	"coz",	"create",	"created",	"creates",	"creating",	"creation",	"creations",	"creative",	"creativity",	"curious", "curiosity", "curiosly",	"cuz",	"deceive", "deceives", "deceiving",	"decide", "decides", "deciding",	"decided",	"decides",	"deciding",	"decision", "decisions", "decisive",	"deduction", "deductive", "deductions", "deductively",	"define",	"defined",	"defines",	"defining",	"definite",	"definitely",	"definition",	"definitive", "definitively",	"depend",	"depended",	"depending",	"depends", "desire", "desires", "desirable",	"despite",	"determination",	"determine",	"determined",	"determines",	"determining",	"diagnose", "diagnoses", "diagnosed",	"diagnosis",	"didn't",	"didnt",	"differ",	"differed",	"difference", "differences",	"different", "differential",	"differentiation", "differentiated",	"differently",	"differing",	"differs",	"directly",	"discern", "discerns", "discerning",	"disclose", "disclosed", "disclosing",	"discover", "discovers", "discovering",	"disillusion", "disillusions",	"disorient", "disorients", "disorienting",	"dissimilar",	"distinct", "distinctive",	"distinguish", "distinguishes", "distinguishing",  "distract", "distracted", "distraction",  "doubt", "doubts", "doubting", "dreams", "dubious")
               
     toksv2.1 <- tokens_keep(notpuncnostoptokssubworkcorpus, phrase(v2.1), window = 10, valuetype="fixed")
     toksnov2.1 <- tokens_remove(notpuncnostoptokssubworkcorpus, phrase(v2.1), window = 10, valuetype="fixed")
     dfmattoksv2.1 <- dfm(toksv2.1)
     #head(toksnov2.1)
     dfmattoksv2.1perpm <- dfm_group(dfmattoksv2.1, groups = "loc")
     dfmattoksnov2.1 <- dfm(toksnov2.1)
     dfmattoksnov2.1perpm <- dfm_group(dfmattoksnov2.1, groups = "loc")
     tstatkeyv2.1 <- textstat_keyness(rbind(dfmattoksv2.1perpm, dfmattoksnov2.1perpm), seq_len(ndoc(dfmattoksv2.1perpm)))
     tstatkeyv2.1subset <- tstatkeyv2.1[tstatkeyv2.1$n_target > 10, ]
     #head(tstatkeyv2.1subset, 1000)
         
     bon<-c()
     bon2<-tstatkeyv2.1subset
     for(j in 1:length(v2.1)){
         bon <- c(bon,which(tstatkeyv2.1subset[,1]==v2.1[j]))
     }
     bon<-sort(bon, decreasing=TRUE)
     bon2<-bon2[-c(bon),]
     ```

  3. For `txm` we have to somehow implement the code flow of point 1 with the `ll` parameter (details [here](https://www.rdocumentation.org/packages/polmineR/versions/0.8.5/topics/ll)), except that instead of a *log-base* we have to take a *log-10* as explained [here](https://groupes.renater.fr/sympa/arc/txm-users/2012-07/msg00032.html). Additional hints [here](http://txm.sourceforge.net/javadoc/TXM/TBX/org/txm/functions/cooccurrences/Cooccurrence.html) and maybe around [here](https://rdrr.io/cran/polmineR/man/cooccurrences.html).



### F3: wordclusters

- &#128230; *What?* `wordclusters` generates latent semantic contexts, and outputs from a `corpus` (not a `dfm` this time)  two sets of contributions: contributions of words to topics, and contributions of topics to sub-corpuses. 

- &#128142; *Why?* `wordclusters` helps identifying the lexicon specific to a speaker, an institution, a period etc.

- &#128125; Alt name: **atoll**

- ⚡ Requires: `quanteda`, `stm`...for visualisation we additionally need`dplyr`, `ggplot2`, `ca` (alternatives to `stm` are `topicmodels` and `cluster`)

- &#128302; Usage of `wordclusters`:

  ```R
  output <- wordclusters(acorpus,
                    method = c("chd", "lda"), 
                    k = FALSE, integer,
                    segmentation = FALSE, integer,
                    minfreq = [0:1],
                    maxfreq = [0:1],
                    cleaning = c("ocr", "numbers", "punctuation", "symbols", "twitter", "url", "hyphens", "docvars", "stem", "clean", "verbose", "stopwords", "tolower"), #see NB1
                    no.words = integer,
   				  sort.gamma = c("descending", "ascending", "none"),
                    plot = NULL, c("ca","dendrogram"),
                    plot.param = [1:3],
                    window = NULL, integer,
                    parallel = TRUE,
                    na.rm = TRUE,
                    verbose = TRUE)
  ```

- NB1: an upcoming tutorial for this cluster should mention cleaning procedures of the corpus ahead of calling the function. Examples can be found [here](https://medium.com/@methods_bites/advancing-text-mining-with-r-and-quanteda-fffc27020de4), [here](https://tm4ss.github.io/docs/Tutorial_6_Topic_Models.html), [here](https://www.r-bloggers.com/2019/10/advancing-text-mining-with-r-and-quanteda/), [here](https://juba.github.io/rainette/) (I also have done some cleaning, can provide my method). Otherwise, we can be ambitious and integrate the cleaning in the argument `cleaning`. Four options will be wrappers of various parameters of three quanteda functions: `tokens`, `tokens_select`, `dfm` and `dfm_trim`. Here is an example:

  ```R
  # Preprocess the text# Create tokens
  token <-
    tokens(
      mycorpus,
      remove_numbers = TRUE,
      remove_punct = TRUE,
      remove_symbols = TRUE,
      remove_twitter = TRUE,
      remove_url = TRUE,
      remove_hyphens = TRUE,
      include_docvars = TRUE
    )
  
  # Clean tokens created by OCR
  token_ungd <- tokens_select(
    token,
    c("[\\d-]", "[[:punct:]]", "^.{1,2}$"),
    selection = "remove",
    valuetype = "regex",
    verbose = TRUE
  )
  
  mydfm <- dfm(token_ungd,
               tolower = TRUE,
               stem = TRUE,
               remove = stopwords("english")
               )
  
  # Filter words that appear less than 7.5% and more than 90%.
  
  mydfm.trim <-
    dfm_trim(
      mydfm,
      min_docfreq = 0.075,
      # min 7.5%
      max_docfreq = 0.90,
      #  max 90%
      docfreq_type = "prop"
    )
  ```

- NB2: We want to be able to generate two forms of graphical output right after running `wordclusters`. We can deal with that at the end when the rest is ready. They will look like this, or like a combination of `beta` and `gamma` visualisation (more on that later):

  <img src="C:\Users\jtmartelli\AppData\Roaming\Typora\typora-user-images\image-20210113075703009.png" alt="image-20210113075703009" style="zoom:50%;" /><img src="C:\Users\jtmartelli\AppData\Roaming\Typora\typora-user-images\image-20210113075944459.png" alt="image-20210113075944459" style="zoom:33%;" />

  - NB3: We will start by implementing the `lda` parameter in `method` because I think it is the easiest one.

&#127912; Arguments of `wordclusters`:

- **acorpus**: The corpus is passed some cleaning arguments (if we take that route) and is segmented (only in the `method` 's parameter `chd`) before being converted into a dfm with the quanteda function `dfm`. All the other arguments will pass the dfm.

- **method**: clustering measurement method. `chd` is default if nothing is specified (even though it will not be developed after the `lda` parameter).
- **k**: the number of clusters to be generated. `likelihood` will take the number of topics that has the highest Held-out likelihood and `residuals` will take the number of topics that has the lowest residuals as explained [here](https://www.r-bloggers.com/2018/09/training-evaluating-and-interpreting-topic-models/). `Silhouette` and `gap_statistics` method will take the number of topics that has the highest average silhouette width ([implemented here](https://bradleyboehmke.github.io/HOML/hierarchical.html)). Alternative for `gap_statistics` [here](https://www.statology.org/hierarchical-clustering-in-r/). Default should be `silhouette` or `gap_statistics` because they are in base R.
- **segmentation**: this option applies to `chd` method only. For the latter, default is 40 words as indicated [here](https://juba.github.io/rainette/). 

- **minfreq** and **maxfreq**: they filter out words that have a very high frequency (banality) or a very low frequency (insignificance) in each document of the dfm. It is based on the function `dfm_trim` of quanteda available [here](https://quanteda.io/reference/dfm_trim.html). 🛑 we have to to some test to understand what default should be. My feeling is to have not too conservative bounds, but only if the rest is computationally efficient.
- **cleaning**: see supra.
- **no.words**: how many words per topic to generate. I am of the opinion that the default number should be low, i.e. 20.
- **sort.beta**: sort the highest or lowest contributing words to a topic. Default is `descending`.
- **sort.gamma**: sort the highest or lowest contributing topics to a document. Default is `descending`.
- **na.rm**:  *ibid.* (see supra).
- **parallel**:  *ibid.* (see supra).

&#128207; Description of the `method` parameters: 

1. For `lda` we can implement [this](https://juliasilge.com/blog/sherlock-holmes-stm/) tutorial. I believe it is the easiest way, so we can start with that. Additional info [here](https://rstudio-conf-2020.github.io/text-mining/materials/slides/modeling.html#92), and [here](https://medium.com/@methods_bites/advancing-text-mining-with-r-and-quanteda-fffc27020de4). Other methods we will probably not use: [here](https://tm4ss.github.io/docs/Tutorial_6_Topic_Models.html), [here](https://bradleyboehmke.github.io/HOML/hierarchical.html) and [here](https://www.statology.org/hierarchical-clustering-in-r/).

2. For `chd` we can implement in part [this](https://juba.github.io/rainette/) technique but make it work with a dfm out of the box. A hint of the visualisation route with the `ca` package is described below:

   ```R
   # Prerequisite 1: open the folder Rscripts and open the file CHD.R
   # Prerequisite 2: open the folder DF and check the outputs
   
   
   source("/usr/share/iramuteq/Rscripts/CHD.R")
   source("/usr/share/iramuteq/Rscripts/chdtxt.R")
   source("/usr/share/iramuteq/Rscripts/anacor.R")
   source("/usr/share/iramuteq/Rscripts/Rgraph.R")
   
   nbt <- 9
   
   library(irlba)
   svd.method <- 'irlba'
   libsvdc.path <- NULL
   
   mode.patate = FALSE
   
   library(Matrix)
   data1 <- readMM("/data/ir/imports/b/bm_1/bmk_1/pmga12_alphanumerical_mini_compact_noempty_alceste_5/TableUc1.csv")
   data1 <- as(data1, "dgCMatrix")
   row.names(data1) <- 1:nrow(data1)
   
   chd1<-CHD(data1, x = nbt, mode.patate = mode.patate, svd.method = svd.method, libsvdc.path = libsvdc.path)
   
   #lecture des uce
   listuce1<-read.csv2("/data/ir/imports/b/bm_1/bmk_1/pmga12_alphanumerical_mini_compact_noempty_alceste_5/listeUCE1.csv")
   
   rm(data1)
   
   classif_mode <- 1
   mincl <- 2
   uceout <- "/data/ir/imports/b/bm_1/bmk_1/pmga12_alphanumerical_mini_compact_noempty_alceste_5/uce.csv"
   if (classif_mode == 0) {
     chd.result <- Rchdtxt(uceout, chd1, chd2 = chd2, mincl = mincl,classif_mode = classif_mode, nbt = nbt)
   } else {
     chd.result <- Rchdtxt(uceout, chd1, chd2 = chd1, mincl = mincl,classif_mode = classif_mode, nbt = nbt)
   }
   n1 <- chd.result$n1
   classeuce1 <- chd.result$cuce1
   classes<-n1[,ncol(n1)]
   write.csv2(n1, file="/data/ir/imports/b/bm_1/bmk_1/pmga12_alphanumerical_mini_compact_noempty_alceste_5/n1.csv")
   rm(n1)
   
   tree.tot1 <- make_tree_tot(chd1)
   #    open_file_graph("/data/ir/imports/b/bm_1/bmk_1/pmga12_alphanumerical_mini_compact_noempty_alceste_5/arbre_1.png", widt = 600, height=400)
   #    plot(tree.tot1$tree.cl)
   #    dev.off()
   
   tree.cut1 <- make_dendro_cut_tuple(tree.tot1$dendro_tuple, chd.result$coord_ok, classeuce1, 1, nbt)
   save(tree.cut1, file="/data/ir/imports/b/bm_1/bmk_1/pmga12_alphanumerical_mini_compact_noempty_alceste_5/dendrogramme.RData")
   
   open_file_graph("/data/ir/imports/b/bm_1/bmk_1/pmga12_alphanumerical_mini_compact_noempty_alceste_5/dendro1.png", width = 600, height=400)
   plot.dendropr(tree.cut1$tree.cl,classes, histo=TRUE)
   open_file_graph("/data/ir/imports/b/bm_1/bmk_1/pmga12_alphanumerical_mini_compact_noempty_alceste_5/arbre_1.png", width = 600, height=400)
   plot(tree.cut1$dendro_tot_cl)
   dev.off()
   
   #save.image(file="/data/ir/imports/b/bm_1/bmk_1/pmga12_alphanumerical_mini_compact_noempty_alceste_5/RData.RData")
   ```



### F4: cosinedocs

- &#128230; *What?* `cosinedocs` determines how close two documents to each other in lexical, semantic and stylistic senses.

- &#128142; *Why?* `wordclusters` applies the Python Doc2Vec vectorised approach and implement it in R. A pre-implementation has been already developed by Srija Anand. 

- &#128125; Alt name: **remora**

- ⚡ Requires: `reticulate` and `dplyr` (R),  and few Python libraries (see below)

- &#128302; Usage of `wordclusters`:

  ```R
  output <- worduse(adataframe,
                    groupbywhat = NULL, columnname,
                    mostsimilar = integer, #default is 2
                    outpurdir = "/path/nameofdir"
                    max_epochs = integer, #default is 20
  				  vec_size = integer, #default is 250
                    alpha = integer, #default is 0.025
                    min_alpha= integer, #default is 0.00025
                    min_count= integer, #default is 1
                    dm = integer) #default is 1
  ```

  &#127912; Arguments of `cosinedocs`:

  - **adataframe**: a data frame in which the text is in one column.
  - **groupbywhat**: calls the `group_by` function of `dplyr` and merges rows accordingly. Default is `NULL`. 
  - **mostsimilar**: tells in the python script how many similar documents to print for each queried document.
  - **outputdit**: tells where to store the output models of Doc2Vec. 
  - the other arguments are `training` paramaters of the `doc2vec` implementation with `gensim` in Python.

  &#128207; Description of the preliminary `R` part:

  1. Calls the `group_by` function and store the output in a temporary object:

     ```R
     tempdataframe <- adataframe %>% group_by(columnname)
     ```

  2. Exports the `tempdataframe` to a `tempdirectory`:

     ```R
     mkdir(/path/nameofdir)
     
     tempdataframe <- tempdataframe %>% select(columnname, text) #text is the column name where the text is
     setwd("/path/nameofdir")
     invisible(lapply(1:nrow(tempdataframe), function(i) write.table(tempdataframe[i,2], 
                                                         file = paste0(tempdataframe[i,1], ".txt"),
                                                         row.names = FALSE, col.names = FALSE,
                                                         quote = FALSE)))
     rm(tempdataframe)
     ```

  3. Trains the model in Python though reticulate:

     ```python
     from gensim.models.doc2vec import Doc2Vec, TaggedDocument
     from nltk.tokenize import word_tokenize
     import nltk
     import os.path
     import multiprocessing
     nltk.download('punkt')
     
     directory=r'/path/nameofdir'
     docLabels=[]
     docLabels=[f for f in os.listdir(directory)]
     # print (docLabels)
     data=[]
     for doc in docLabels:
     	words=open(directory+'//'+ doc, encoding='utf-8').read()
     	words=words.strip()
     	words=words.split()
     	# print (words)
     	tags = [doc]
     	data.append(TaggedDocument(words=words, tags=tags))
     # print (data[0])
     
     # encoding='cp1252'
     # tagged_data = [TaggedDocument(words=word_tokenize(_d.lower()), tags=[str(i)]) for i, _d in enumerate(data)]
     
     cores=multiprocessing.cpu_count()
     print (cores)
     max_epochs = 20
     vec_size = 250
     alpha = 0.025
     
     model = Doc2Vec(vector_size=vec_size,
     				workers=cores,
                     alpha=alpha, 
                     min_alpha=0.00025,
                     min_count=1,
                     dm =1)
       
     model.build_vocab(data)
     # train_documents,total_examples=len(train_documents), epochs=30
     
     model.train(data,total_examples=model.corpus_count,epochs=max_epochs)
                     # =model.iter)
         # # decrease the learning rate
         # model.alpha -= 0.0002
         # # fix the learning rate, no decay
         # model.min_alpha = model.alpha
     model.save("/path/nameofdir2/d2v.model") 
     print("Model Saved")
     ```

  4. Trains the model in Python though reticulate:

     ```python
     from gensim.models.doc2vec import Doc2Vec
     from nltk.tokenize import word_tokenize
     import nltk
     import os
     nltk.download('punkt')
     
     model= Doc2Vec.load("/path/nameofdir2/d2v.model")
     #to find the vector of a document which is not in training data
     # test_data = word_tokenize("Six days ago, my colleagues and I sat on the chairs of high office in the Government of India.".lower())
     directory=r'/path/nameofdir'
     docLabels=[]
     docLabels=[f for f in os.listdir(directory)]
     for doc in docLabels:
     	test_data=open(directory+'//'+ doc, encoding='utf-8').read()
     	print (doc)
     	test_data=test_data.strip()
     	test_data=test_data.split()
     	test_data=list(test_data)
     	v1 = model.infer_vector(test_data)
     	similar_doc = model.docvecs.most_similar([v1])
         #print(similar_doc[0], similar_doc[1])
     	print(similar_doc[0:10]) #will print the 10 most similar per locutor
     ```

  5. Remove temp files:

     ```R
     clean(dirs = c("/path/nameofdir"), force = TRUE)
     ```

  &#127774; Some useful resources: [here](https://medium.com/@tarekseif0/document-similarity-using-word-movers-distance-and-cosine-similarity-d698ad435422), [here](https://medium.com/wisio/a-gentle-introduction-to-doc2vec-db3e8c0cce5e), [here](https://www.youtube.com/watch?v=zFScws0mb7M&t=1219s).



### F5: wordexplorer

- &#128230; *What?* `wordexplorer` is a simple shiny explorer for browsing the context of a word, phrase or regular expression. It offers the possibility to examine in a split screen two different search queries in two different corpuses. This is particularly useful to translated corpuses.

- &#128142; *Why?* `wordexplorer` takes words, glob or regular expressions and displays their left and right context

- &#128125; Alt name: **scuba**

- ⚡ Requires: `shiny` , `quanteda` 

- &#128302; Usage of `wordexplorer`:

  ```R
  wordexplorer:::wordexplorer(kwic(acorpus, #we could simplify it here
  			  pattern = "love", #an example
  			  window = 3,
  			  valuetype = c("glob", "regex", "fixed"),
                case_insensitive = TRUE,
  			  rowname = NULL, c("minister", "covidtw"),
                tr.pattern = NULL, acorpustranslated,
                tr.pattern = NULL,"प्यार", #an example
  			  tr.window = NULL, 3,
  			  tr.valuetype = NULL, c("glob", "regex", "fixed"),
                tr.case_insensitive = NULL, TRUE,
  			  tr.rowname = NULL, c("minister", "covidtw"),        
                                  )) #these are examples
  ```

  &#127912; Arguments of `wordexplorer`:

  - `rowname` is passed first, it calls the function `filter ` from `dyplyr`. 

    ```R
    acorpustemporary <- acorpus %>% filter(type == "minister" | type == "covidtw")
    ```

  - all the other arguments ones are based on the function `kwic` of quanteda; they are explained [here](https://www.rdocumentation.org/packages/quanteda/versions/2.1.2/topics/kwic) and [here](https://quanteda.io/reference/kwic.html).

  - When the shiny window is exited, the temporary object is removed: `rm(acorpustemporary)`.

  - If any of the `tr.xxx` parameters are other than `NULL` the shiny window opens in split screen (left/right). `tr.xxx` parameters are based similarly on the `kwic` function of quanteda.

  

## Appendix

🌓 Tutorials to do parallel computing in R: [probably the best](https://learn.datacamp.com/courses/parallel-programming-in-r), [here](https://nceas.github.io/oss-lessons/parallel-computing-in-r/parallel-computing-in-r.html), [here](https://dept.stat.lsa.umich.edu/~jerrick/courses/stat701/notes/parallel.html), [here](https://bookdown.org/rdpeng/rprogdatascience/parallel-computation.html)

🌗 Tutorials to build a Shiny app: [probably the simpliest](https://shiny.rstudio.com/articles/build.html), [here](https://towardsdatascience.com/build-your-first-shiny-web-app-in-r-72f9538f9868), [here](https://shiny.rstudio.com/tutorial/).