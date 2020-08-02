import sys
import os
import subprocess
import json
import getpass
import codecs
from PTTLibrary import PTT
import time
import schedule

def showPost(Post):
    #PTTBot.Log('文章代碼: ' + Post.getID())
    #PTTBot.Log('作者: ' + Post.getAuthor())
    PTTBot.Log('標題: ' + Post.getTitle())
    #PTTBot.Log('時間: ' + Post.getDate())
    #PTTBot.Log('價錢: ' + str(Post.getMoney()))
    #PTTBot.Log('IP: ' + Post.getIP())
    #PTTBot.Log('網址: ' + Post.getWebUrl())

    #PTTBot.Log('內文:\n' + Post.getContent())

    #PushCount = 0
    #BooCount = 0
    #ArrowCount = 0

    #for Push in Post.getPushList():
    #    PushType = Push.getType()

    #    if PushType == PTT.PushType.Push:
    #        PushCount += 1
    #    elif PushType == PTT.PushType.Boo:
    #        BooCount += 1
    #    elif PushType == PTT.PushType.Arrow:
    #        ArrowCount += 1
    #    
    #    Author = Push.getAuthor()
    #    Content = Push.getContent()
    #    # IP = Push.getIP()
    #    PTTBot.Log('推文: ' + Author + ': ' + Content)
    #    
    #PTTBot.Log('共有 ' + str(PushCount) + ' 推 ' + str(BooCount) + ' 噓 ' + str(ArrowCount) + ' 箭頭')


def postHandler(Post):
    with codecs.open("./outputs/ieee_cc.txt", "a", 'utf-8') as ResultFile:
        ResultFile.write(Post.getContent())
        ResultFile.write('\n\n\n--------------------------------------------------------\n\n\n')
 
def run_all():
	
    #with codecs.open("./outputs/ieee_cc.txt", "w", 'utf-8') as ResultFile:
    #    ResultFile.write('new\n\n')
    try:
        os.remove("./outputs/ieee_cc.txt")
    except:
        pass

    ID = 'istale'
    Password = 'kevin0930'
    
    PTTBot = PTT.Library(kickOtherLogin=False)
    
    # login test
    ErrCode = PTTBot.login(ID, Password)
    if ErrCode != PTT.ErrorCode.Success:
        PTTBot.Log('Login failed.')
        sys.exit()
    
    # get post
    input_search_board = 'C_Chat'
    input_search_type = PTT.PostSearchType.Keyword 
    input_search_string = '柯'
    ErrCode, NewestIndex = PTTBot.getNewestIndex(Board=input_search_board)
    #ErrCode, NewestIndex = PTTBot.getNewestIndex(Board=input_search_board, SearchType=input_search_type, Search=input_search_string)
    
    print('NewestIndex: ' + str(NewestIndex))
    
    input_crawl_post_count = 50
    ErrCode, SuccessCount, DeleteCount = PTTBot.crawlBoard(input_search_board, postHandler, StartIndex=NewestIndex - input_crawl_post_count + 1, EndIndex=NewestIndex)
    #ErrCode, SuccessCount, DeleteCount = PTTBot.crawlBoard(input_search_board, postHandler, StartIndex=NewestIndex - input_crawl_post_count + 1, EndIndex=NewestIndex, SearchType=input_search_type, Search=input_search_string)
    
    #ErrCode, Post = PTTBot.getPost(input_search_board, PostIndex=NewestIndex, SearchType=input_search_type, Search=input_search_string)
    #if ErrCode == PTT.ErrorCode.PostDeleted:
    #    if Post.getDeleteStatus() == PTT.PostDeleteStatus.ByAuthor:
    #        PTTBot.Log('文章被原 PO 刪掉了')
    #    elif Post.getDeleteStatus() == PTT.PostDeleteStatus.ByModerator:
    #        PTTBot.Log('文章被版主刪掉了')
    #    PTTBot.Log('作者: ' + Post.getAuthor())
    #    sys.exit()
    #elif ErrCode != PTT.ErrorCode.Success:
    #    PTTBot.Log('取得文章詳細資訊失敗 錯誤碼: ' + str(ErrCode))
    #    sys.exit()
    #else:
    #    showPost(Post)
    
    # 登出
    PTTBot.logout()
    
    #os.chdir('./outputs')
    #subprocess.call("./git.sh", shell=True)
    #os.chdir('../')


if __name__ == '__main__':
    run_all()

    schedule.every(1).minutes.do(run_all)
    run_flag = 0
    while True:
        schedule.run_pending()
        time.sleep(1)
        run_flag = run_flag + 1
        if run_flag > 10: 
            run_flag = 1
        output_sring = ' (^(00)^) ' * run_flag
        print(' '* 100, end='\r')
        print(output_sring, end='\r' )

