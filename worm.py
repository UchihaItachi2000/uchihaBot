from  bs4 import BeautifulSoup
import  os
import  requests
import  json
import  re

headers = {"User-Agent": "Mozilla/5.0 "
                         "(Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0"}
#腾讯星座爬取今年运势
save_file_path="./TencentConstellation/"
label_num=0

class TencentConstellation:
    #从文件中获取网页的url
    def GetUrlList(self):
       UrlList=[]
       with open("data.txt","r",encoding="utf-8")as fr:
            UrlTempList=fr.readlines()
       for  tempUrl in UrlTempList:
            UrlList.append(tempUrl.rstrip('\n'))
       return UrlList
    #获取网页中的内容
    def GetWebContent(self,html,name,class_):
        soup = BeautifulSoup(html, "lxml")
        current_content = (soup.find(name, class_=class_))
        if current_content is None:
            return ""
        return repr(current_content)
    #去除一些网页内容中自己的不需要的一些杂质
    def pirity_content(self, origi_str):
        origi_str = repr(origi_str)
        r_e = re.compile(r"(<center>.*?</center>)|(<a.*?>)|(</a>)|")
        new_str = re.sub(r_e, "", origi_str)
        return new_str
    #解析网页中的内容，并且写入一个json文件中
    def ParserContent(self):
        try:
            review_dict={}
            UrlLinkList=self.GetUrlList()
            i=label_num
            for url in UrlLinkList:
                html=requests.get(url,headers=headers)
                html=html.content.decode("gb2312","ignore")
                soup=BeautifulSoup(html,"lxml")
                title=soup.find("title").text
                repr=re.compile("_腾讯星座频道")
                title=re.sub(repr,"",title)
                #print(title)
                review_dict["title"]=title
                review_dict["description"]=str(soup.find("meta", {'name':'description'}).get("content"))
                review_dict["keywords"]=str(soup.find("meta", {'name':'keywords'}).get("content"))
                #review_dict["keywords"]=str(soup.find("meta", {'name':'tags'}).get("content"))
                #获取网页的相关内容
                content=self.GetWebContent(html,name="div",class_="duanluo")
                content=self.pirity_content(content)
                review_dict["content"]=content
                #写入Json文件中
                path = save_file_path + "my" + str(i) + ".json"
                with open(path,"w",encoding="utf-8") as fw:
                    json.dump(review_dict, fw, ensure_ascii=False, indent=3)
                i=i+1

        except Exception as e:
            print(e)


if __name__=="__main__":
    TencentSpide=TencentConstellation()
    TencentSpide.ParserContent()
    pass
