#!/usr/bin/env python3  
# -*- coding: utf-8 -*-  
"""  
@desc:  
@author: TsungHan Yu  
@contact: nick.yu@hzn.com.tw  
@software: PyCharm  @since:python 3.6.0 on 2017/7/13
"""

import os
import requests
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

showlog = 'Hello' 

app = Flask(__name__)

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
SECRET = os.environ.get('SECRET')

line_bot_api = LineBotApi(ACCESS_TOKEN)
handler = WebhookHandler(SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(	event.reply_token,
		 TextSendMessage(text=sum(event.message.text)+'\n接收 : '+forShow(event) ))

if __name__ == "__main__":
	app.run()


def sum(tex ):
	i = 1
	sum = 0
	while i <= 100:
		sum += i
		i += 1
	
	if (tex.find('1'))!=-1:
		sun = '\nreplyToken : ' + str( tex.replyToken)
	elif (tex.find('2'))!=-1:
		sun = '\ntype : '+str( tex.type)
	elif (tex.find('3'))!=-1:	
		sun = '\ntimestamp : ' +str( tex.timestamp)
	elif (tex.find('4'))!=-1:	
		sun = '\nsource_userId : ' + str( tex.source.userId)	
	elif (tex.find('5'))!=-1:	
		sun = '\nOK'
	elif (tex.find('6'))!=-1:	
		sun = showlog
	elif (tex.find('7'))!=-1:	
		sun = '\nOK'		
	else:
		sun = str(sum/50) + '太陽\uDBC0\uDCA9'	+'\t熊\uDBC0\uDC84'
		showlog = sun + 'CC'
	return sun

def forShow(tex ):	
	shoow =  '\ntext : ' + str( tex.message.text)+'\nid : '+str( tex.message.id) + '\ntype : ' +str( tex.message.type) 	
	shoow = shoow + '\nsource_type : ' + str( tex.source.type)  
	return shoow