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
# from linebot.models import (
    # MessageEvent, TextMessage, TextSendMessage,
# )
from linebot.models import *



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
	if event.message.text == "11":
		line_bot_api.reply_message(	event.reply_token,TextSendMessage(text='\n接收 : '+forShow(event) ))
	elif event.message.text == "12":
		line_bot_api.reply_message(event.reply_token,StickerSendMessage(package_id=1, sticker_id=2))
	elif event.message.text == "13":	
		line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://d1dwq032kyr03c.cloudfront.net/upload/images/20180103/20107144BJM2zuA9l7.png', preview_image_url='https://d1dwq032kyr03c.cloudfront.net/upload/images/20180103/20107144BJM2zuA9l7.png'))
	elif event.message.text == "14":
		line_bot_api.reply_message(event.reply_token,VideoSendMessage(original_content_url='https://www.paypalobjects.com/webstatic/mktg/videos/PayPal_AustinSMB_baseline.mp4', preview_image_url='https://d1dwq032kyr03c.cloudfront.net/upload/images/20180103/20107144BJM2zuA9l7.png'))		
	# elif event.message.text == "15":
  	
		
if __name__ == "__main__":
	app.run()


def forShow(tex ):	
	shoow =  '\ntext : ' + str( tex.message.text)+'\nid : '+str( tex.message.id) + '\ntype : ' +str( tex.message.type) 	
	shoow = shoow + '\nsource_type : ' + str( tex.source.type)  
	return shoow
	