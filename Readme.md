# True news
## Description
- This application provides news from selected ressources.
- The results of your search are depending on your filters.
- You will be asked for the filters when launching the application. It's possible to overwrite these filters.
- You can log in with different usernames to prevent from overwriting the filters.
## Supported Pages
- https://www.cbsnews.com
If you want to collab and add support for further reliable news pages, refer to the [Collaboration](#collaboration) section
## Installation
1. make sure python is installed
2. open cmd
3. ```> cd "project folder"```
4. ```> pip install pipreqs```
5. ```> pipreqs . --> generates ***requirements.txt*** for python scripts in the folder```
6. ```> pip install -r requirements.txt```
## Usage
1. open cmd
2. ``` cd "project folder"```
3. ```python .\src\main.py```
4. follow the instructions in the CLI
## Collaboration
We need especially collaborators for supporting further reliable news pages. We work with feature branches and pull requests which need to be approved by the core group who is working on the project.

In order to add support for new pages, you need to do the following:
1. add the url to urls.txt file
   -  make sure to add no slash at the end of the url, as this would cause issues with the crawler implementation
2. run the app and check the output for "technical" links which containly provide no news (e.g. "/contact", "/sitemap", ...). If there are any, add them to ignoreByDefault.txt
   - do not add them, if they contain buzzwords which could be used in news often
3. add a "crawlXxx.py" file for the logic to search through the specific webpage
   - "crawlCbsNews.py" is a good example on what and how to implement
   - implement at least the functions
     - printArticle(url)
     - printRelatedArticles(url)
   - inspect the webpage to figure out how the elements are added
   - make sure to search for the "h1" tag, since we want to display the headlines
4. finally, in "spider.py" file, connect the support in the functions at the pottom of the file.
   - at the example of "readNewsPage(url)":
     add 
        ```python
        elif url.startswith("https://your.url.com"):
          yourCrawler.printArticle(url)
          yourCrawler.printRelatedArticles(url)
        ```
[Example Commit](https://github.com/vigi86/StairHACK2022/commit/7de963f7a23658ac7001c336d928e7ba91e4b8cb)
