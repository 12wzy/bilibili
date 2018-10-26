import pymysql
import time


class MySQL():

    def __init__(self):
        self.host = "localhost"
        self.user = 'root'
        self.password = 'root'
        self.dbname = 'bili'
        self.charset = 'utf8mb4'
        self.cursorclass = pymysql.cursors.DictCursor
        self.dateFormat = "%Y-%m-%d %H:%M:%S"

    def createConnection(self):

        connection = pymysql.connect(host=self.host,
                                     user=self.user,
                                     password=self.password,
                                     db=self.dbname,
                                     charset=self.charset,
                                     cursorclass=self.cursorclass)
        return connection

    def insert2video(self, item, connection):
        s = "123'123"
        s.replace("'", "")
        insertIntoVideo = "INSERT INTO bili.video (`videoId`, `videoLabelId`, `videoLabelName`, `videoTitle`, `pubDate`, `view`, `danmaku`, `reply`, `favorite`, `coin`, `share`, `ownerId`, `ownerName`) VALUES ({}, {}, '{}', '{}', '{}', {}, {}, {}, {}, {}, {}, {}, '{}')"
        videoId = item['videoId']
        videoLabelId = item['videoLabelId']
        videoLabelName = item['videoLabelName'].replace("'", "")
        videoTitle = item['videoTitle'].replace("'", "")
        pubDate = time.strftime(self.dateFormat, time.localtime(item['pubDate']))
        view = item['view']
        danmaku = item['danmaku']
        reply = item['reply']
        favorite = item['favorite']
        coin = item['coin']
        share = item['share']
        ownerId = item['ownerId']
        ownerName = item['ownerName'].replace("'", "")

        sql = insertIntoVideo.format(videoId, videoLabelId, videoLabelName, videoTitle, pubDate, view, danmaku, reply,
                                     favorite, coin, share, ownerId, ownerName)

        with connection.cursor() as cursor:
            cursor.execute(sql)
            connection.commit()

        return sql

    def insert2tag(self, item, connection):
        insertIntoTag = "INSERT INTO bili.tag (`videoId`, `tagId`, `tagName`) VALUES ({}, {}, '{}')"
        videoId = item['videoId']
        tagId = item['tagId']
        tagName = item['tagName'].replace("'", "")
        sql = insertIntoTag.format(videoId, tagId, tagName)
        with connection.cursor() as cursor:
            cursor.execute(sql)
            connection.commit()
        return sql

    def closeConnection(self, connection):
        connection.close()