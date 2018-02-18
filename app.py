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
	#if event.message.text='id':    
	#	res = requests.get('http://tw.myrenta.com/search?bcg=a&t=' + event.message.text)
	#else
		#res = '黑:' + event.message.text
	#res = "白:"
    line_bot_api.reply_message(	event.reply_token,
		#TextSendMessage(text=res.text))
		 TextSendMessage(text=sum(event.message.text)+'灰 : '+event.message.text))

if __name__ == "__main__":
	app.run()


def sum(tex ):
	i = 1
	sum = 0
	while i <= 100:
		sum += i
		i += 1
	sun = str(sum/50) + '白\n'+tex+'go  LINE emoji 太陽\uDBC0\uDCA9'	+'\t熊\uDBC0\uDC84'
	
	if (tex.find('設定'))!=-1:
		sun = '設定模式:\n1.主題\n2.外框\n3.內裡'
	elif (tex.find('輔助'))!=-1:
		sun = '輔助模式:\n1.補血\n2.撐防\n3.加速'
	return sun