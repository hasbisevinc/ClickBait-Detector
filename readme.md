# ClickBait Detector!

This repo represent an AI method to classify an article as clickbait or non-clickbait. To classify article we extract some features from both title and body paragraphs. We applied gradient boosting decision tree into these features and we measured accuracy of the model. Lastly, we create a web service that provide clickbait score of provided article by user. Using this web service, news application or web sites such as Bundle FlipBoard can provide better content to their users
# DEMO
https://clickbaitdetection.herokuapp.com/
# Machine Learning Results
```
```
| Method| Accuracy Score| F-Score|
| ------------- |:-------------:| -----:|
| Naive Bayes      | 0.74 | 0.72 |
| KNN-3      | 0.85|   0.84 |
| KNN-5 | 0.82     |    0.80 |
| SGDClassifier | 0.77     |    0.77 |
| SVM | 0.78     |    0.78 |
| Decision Tree | 0.78     |    0.70 
```
```


# Files

**/Training**-> Extracting features from dataset and train them for machine learning models
**/performance_test**-> Training extracted features with different machine learning methods to compare their performances
**/server**-> codes for webservice. demo: https://clickbaitdetection.herokuapp.com/

## Use WebService

**With Curl**
curl -X POST -H 'Content-Type: application/x-www-form-urlencoded' -H 'charset: UTF-8' -d 'title=[title]&body=[body]' -v -i 'https://clickbaitdetection.herokuapp.com/classify.ai'

With Javascript:
```
    var title = document.getElementById("fname").value
    var body = document.getElementById("subject").value

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "https://clickbaitdetection.herokuapp.com/classify.ai", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8");
    xhr.send("title="+title+"&body="+body);

    xhr.onreadystatechange = function() { 
        if (xhr.readyState == 4 && xhr.status == 200) {
            console.log(xhr.responseText);
            result = document.getElementById("result")
            result.style.visibility= 'visible'
            if (xhr.responseText == "1") {
                //clicbait
            }
            else if (xhr.responseText == "0") {
                //non-clickbait
            }
            else {
                //server error
            }
        }
    }
```


## WebService Responses

1-> Clickbait
0->Non-clickbait
-1->Server error (check input values)

## Limitations

Body text input should be more than five paragraphs.

## References
0.  Dataset: https://clickbait-challenge.org/#data
    
1.  Ntoulas, A.; Najork, M.; Manasse, M.; and Fetterly, D. 2006. Detecting spam web pages through content analysis. In WWW, 83–92. ACM.
    
2.  Becchetti, L.; Castillo, C.; Donato, D.; Leonardi, S.; and Baeza-Yates, R. A. 2006. Link-based characterization and detection of web spam. In AIRWeb, 1–8.
    
3.  Lau, R. Y.; Liao, S.; Kwok, R. C. W.; Xu, K.; Xia, Y.; and Li, Y. 2011. Text mining and probabilistic language modeling for online review spam detecting. ACM TMIS 2(4):1–30.
    
4.  Minqing Hu and Bing Liu. "Mining and Summarizing Customer Reviews." Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD-2004), Aug 22-25, 2004, Seattle, Washington, USA
    
5.  Bing Liu, Minqing Hu and Junsheng Cheng. "Opinion Observer: Analyzing and Comparing Opinions on the Web." Proceedings of the 14th International World Wide Web conference (WWW-2005), May 10-14, 2005, Chiba, Japan.
    
6.  Biyani, P., Tsioutsiouliklis K., Blackmer J.. “8 Amazing Secrets for Getting More Clicks”: Detecting Clickbaits in News Streams Using Article Informality Proceedings of the Thirtieth AAAI Conference on Artificial Intelligence (AAAI-16), February 12–17, 2016, Phoenix, Arizona USA
    
7.  Coleman, M., and Liau, T. L. 1975. A computer readability formula designed for machine scoring. Journal of Applied Psychology 60(2):283.
    
8.  Anderson, J. 1983. Lix and rix: Variations on a little-known readability index. Journal of Reading 490–496.
    
9.  Heylighen, F., and Dewaele, J.-M. 1999. Formality of language: definition, measurement and behavioral determinants. Interner Bericht, Center Leo Apostel, Vrije Universiteit Brussel.