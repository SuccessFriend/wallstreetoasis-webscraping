import requests
from datetime import datetime
import csv
from selenium.webdriver.common.by import By
import time
from seleniumbase import Driver
from selenium.webdriver.support.ui import Select
driver = Driver(uc=True)
import json
    
# initial = ["Channel Number", "Channel Name", "Start Time", "Duration", "Program Name"]
# with open('data.csv', mode='w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(initial)

results = []

with open('test.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        url = row[0]
        
        driver.get(url)
        
        upvoteCount = ""
        downvoteCount = ""
        post_details = []
        result_post_comments = []

        post_article = driver.find_element(By.XPATH, '//*[@id="wso-content-outer"]/div[3]/div[1]/article')
        try:
            postID = driver.find_element(By.XPATH, '//*[@id="wso-content-outer"]/div[3]/div[1]').get_attribute('data-history-node-id')
        except:
            postID = ""
        try:
            postUrl = driver.find_elements(By.CSS_SELECTOR, '.post-wrap div')[0].get_attribute('itemid')
        except:
            postUrl = ""
        try:
            postTitle = driver.find_elements(By.CLASS_NAME, 'wso-forum-title')[0].text
        except:
            postTitle = ""
        try:
            postCounts = driver.find_elements(By.CSS_SELECTOR, 'div.post-wrap div meta')

            for postCount in postCounts:
                itemprop = postCount.get_attribute('itemprop')
                if itemprop == 'upvoteCount':
                    upvoteCount = postCount.get_attribute('content')
                    print("upvoteCount : ", upvoteCount)
                if itemprop == 'downvoteCount':
                    downvoteCount = postCount.get_attribute('content')
                    print("downvoteCount : ", downvoteCount)
        except:
            upvoteCount = ""
            downvoteCount = ""
        try:
            postContent = post_article.find_elements(By.CLASS_NAME, 'content')[0].text
        except:
            postContent = ""
        try:
            createdDate = driver.find_elements(By.CLASS_NAME, 'created')[0].text
        except:
            createdDate = ""
        modifiedDate = createdDate
        audience = "Real Estate"
        try:
            authorName = post_article.find_elements(By.CSS_SELECTOR, '.author-details-position .pc')[0].text
        except:
            authorName = ""
        try:
            authorUrl = post_article.find_elements(By.CLASS_NAME, 'username')[0].get_attribute('href')
        except:
            authorUrl = ""
        try:
            authorAvatar = post_article.find_elements(By.CLASS_NAME, 'author-details-avatar')[0].get_attribute('href')
        except:
            authorAvatar = ""
        
        try:
            memberRanking = post_article.find_elements(By.CLASS_NAME, 'member-ranking__wrapper')[0].text
        except:
            memberRanking = ""
        try:
            bananaPoints = post_article.find_elements(By.CLASS_NAME, 'author-details__banana_points')[0].text
        except:
            bananaPoints = ""
        try:
            industryTitle = post_article.find_elements(By.CSS_SELECTOR, '.author-details__industry-icon a')[0].get_attribute('title')
        except:
            industryTitle = ""
        keywords = ""
        
        try:
            region = post_article.find_elements(By.CSS_SELECTOR, '.post-region-tags div div.field--items')[0].text
        except:
            region = ""
        try:
            totalCommentCnt = driver.find_elements(By.CSS_SELECTOR, '.comments-stats span')[0].text
        except:
            totalCommentCnt = ""
        displayedCommentCnt = totalCommentCnt
        
        print("post details >>> ", postID, postUrl, postTitle, upvoteCount, downvoteCount, postContent, createdDate, modifiedDate, audience, authorName, authorUrl, authorAvatar, memberRanking, bananaPoints, industryTitle, region, totalCommentCnt, displayedCommentCnt)

        post_details.append({postID, postUrl, postTitle, upvoteCount, downvoteCount, postContent, createdDate, modifiedDate, audience, authorName, authorUrl, authorAvatar, memberRanking, bananaPoints, industryTitle, region, totalCommentCnt, displayedCommentCnt })

        try:
            post_comments = driver.find_elements(By.CLASS_NAME, 'comment-forum-wrapper')[0]
            comment_contents = post_comments.find_elements(By.TAG_NAME, 'article')
            for i in range(len(comment_contents)):
                comment_content = comment_contents[i]
                
                position = i
                try:
                    commentId = comment_content.get_attribute('id').replace("comment-id-", "")
                except:
                    commentId = ""
                try:
                    parentId = ""
                except:
                    parentId = ""
                try:
                    contentText = comment_content.find_elements(By.CLASS_NAME, 'comment-content')[0].text
                except:
                    contentText = ""
                try:
                    contentHtml = comment_content.find_elements(By.CLASS_NAME, 'comment-content')[0].innerHTML
                except:
                    contentHtml = ""
                try:
                    authorName = comment_content.find_elements(By.CLASS_NAME, 'author-details__username')[0].text
                except:
                    authorName = ""
                try:
                    authorId = comment_content.find_elements(By.CSS_SELECTOR, '.author-details__username a')[0].get_attribute('href').replace("/user/", "")
                except:
                    authorId = ""
                try:
                    authorRanking = comment_content.find_elements(By.CLASS_NAME, '.member-ranking__wrapper')[0].text
                except:
                    authorRanking = ""
                try:
                    comment_bananaPoints = comment_content.find_elements(By.CLASS_NAME, '.author-details__banana_points')[0].text
                except:
                    comment_bananaPoints = ""
                try:
                    comment_time = comment_content.find_elements(By.CSS_SELECTOR, '.post-time-container .post-when span')[0].get_attribute('title')
                except:
                    comment_time = ""
                try:
                    labels = comment_content.find_elements(By.CLASS_NAME, 'post-header__labels')[0].text
                except:
                    labels = ""
                try:
                    comment_upvoteCount = ""
                except:
                    comment_upvoteCount = ""
                try:
                    comment_downvoteCount = ""
                except:
                    comment_downvoteCount = ""
                
                print("post comments >>> ", position, commentId, parentId, contentText, contentHtml, authorName, authorId, authorRanking, comment_bananaPoints, comment_time, labels, comment_upvoteCount, comment_downvoteCount)

                result_post_comments.append({position, commentId, parentId, contentText, contentHtml, authorName, authorId, authorRanking, comment_bananaPoints, comment_time, labels, comment_upvoteCount, comment_downvoteCount})

        except:
            pass
        
        results.append({'post_details': post_details, 'post_comments': result_post_comments})
        print("-----------------------------------------------------------------------------------------")

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(results)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

write_data = {'results':results}

with open("result.json", 'w') as json_file:
    json.dump(write_data, json_file, indent=4)

        