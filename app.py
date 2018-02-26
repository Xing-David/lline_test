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
from linebot.models import *

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
	if event.message.text == "11":
		line_bot_api.reply_message(	event.reply_token,TextSendMessage(text='\n接收 : '+forShow(event) ))
	elif event.message.text == "12":
		line_bot_api.reply_message(event.reply_token,StickerSendMessage(package_id=1, sticker_id=2))
	elif event.message.text == "13":	
		line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://adpic.pchome.com.tw/adpics/pic_1137534_667488.png', preview_image_url='https://adpic.pchome.com.tw/adpics/pic_1137534_667488.png'))
	elif event.message.text == "14":
		line_bot_api.reply_message(event.reply_token,VideoSendMessage(original_content_url='https://www.paypalobjects.com/webstatic/mktg/videos/PayPal_AustinSMB_baseline.mp4', preview_image_url='https://d1dwq032kyr03c.cloudfront.net/upload/images/20180103/20107144BJM2zuA9l7.png'))		
    elif event.message.text == "15":	#	位置
        line_bot_api.reply_message(event.reply_token,LocationSendMessage(title='my location', address='Tainan', latitude=22.994821, longitude=120.196452))
    elif event.message.text == "16":	#	位置2
        imagemap_message = ImagemapSendMessage(
                        base_url='',
                        alt_text='this is an imagemap',
                        base_size=BaseSize(height=520, width=520),
                        actions=[
                            URIImagemapAction(
                                link_uri='',
                                area=ImagemapArea(
                                    x=174, y=65, width=707, height=416
                                )
                            ),
                            MessageImagemapAction(
                                text='hello',
                                area=ImagemapArea(
                                    x=520, y=0, width=520, height=520
                                )
                            )
                        ]
                    )
        line_bot_api.reply_message(event.reply_token,imagemap_message)
    elif event.message.text == "17":	#	樣板
        buttons_template = TemplateSendMessage(
        alt_text='目錄 template',
        template=ButtonsTemplate(
            title='Template-樣板介紹',
            text='Template分為四種，也就是以下四種：',
            thumbnail_image_url='https://ithelp.ithome.com.tw/upload/images/20180103/20107144G0upTRUk1K.png',
            actions=[
                MessageTemplateAction(
                    label='Buttons Template1',
                    text='Buttons Template1'
                ),
                MessageTemplateAction(
                    label='Confirm template2',
                    text='Confirm template3'
                ),
                MessageTemplateAction(
                    label='Carousel template4',
                    text='Carousel template4'
                ),
                MessageTemplateAction(
                    label='Image Carousel5',
                    text='Image Carousel5'
                )
            ]
        )
    )
        line_bot_api.reply_message(event.reply_token, buttons_template)
    elif event.message.text == "18":  	#Buttons Template     
        buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='這是ButtonsTemplate',
            text='ButtonsTemplate可以傳送text,uri',
            thumbnail_image_url='https://ithelp.ithome.com.tw/upload/images/20180103/20107144BJM2zuA9l7.png,
            actions=[
                MessageTemplateAction(
                    label='ButtonsTemplate',
                    text='ButtonsTemplate'
                ),
                URITemplateAction(
                    label='VIDEO1',
                    uri='影片網址'
                ),
                PostbackTemplateAction(
                label='postback',
                text='postback text',
                data='postback1'
                )
            ]
        )
    )
        line_bot_api.reply_message(event.reply_token, buttons_template)
    elif event.message.text == "19":	#Carousel template
        print("Carousel template")       
        Carousel_template = TemplateSendMessage(
        alt_text='目錄 template',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='https://ithelp.ithome.com.tw/upload/images/20180117/20107144ukLu929m7M.png',
                title='this is menu1',
                text='description1',
                actions=[
                    PostbackTemplateAction(
                        label='postback1',
                        text='postback text1',
                        data='action=buy&itemid=1'
                    ),
                    MessageTemplateAction(
                        label='message1',
                        text='message text1'
                    ),
                    URITemplateAction(
                        label='uri1',
                        uri='網址'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://ithelp.ithome.com.tw/upload/images/20180117/20107144ZrLLGZbvAy.png',
                title='this is menu2',
                text='description2',
                actions=[
                    PostbackTemplateAction(
                        label='postback2',
                        text='postback text2',
                        data='action=buy&itemid=2'
                    ),
                    MessageTemplateAction(
                        label='message2',
                        text='message text2'
                    ),
                    URITemplateAction(
                        label='連結2',
                        uri='網址'
                    )
                ]
            )
        ]
    )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)
    elif event.message.text == "20":	#Confirm template
        print("Confirm template")       
        Confirm_template = TemplateSendMessage(
        alt_text='目錄 template',
        template=ConfirmTemplate(
            title='這是ConfirmTemplate',
            text='這就是ConfirmTemplate,用於兩種按鈕選擇',
            actions=[                              
                PostbackTemplateAction(
                    label='Y',
                    text='Y',
                    data='action=buy&itemid=1'
                ),
                MessageTemplateAction(
                    label='N',
                    text='N'
                )
            ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Confirm_template)
    elif event.message.text == "21":	#Image Carousel
        print("Image Carousel")       
        Image_Carousel = TemplateSendMessage(
        alt_text='Image Carousel template',
        template=ImageCarouselTemplate(
        columns=[
            ImageCarouselColumn(
                image_url='https://ithelp.ithome.com.tw/upload/images/20180117/20107144LtlhGWuxTy.png',
                action=PostbackTemplateAction(
                    label='postback1',
                    text='postback text1',
                    data='action=buy&itemid=1'
                )
            ),
            ImageCarouselColumn(
                image_url='https://ithelp.ithome.com.tw/upload/images/20180103/20107144nFRc5tsPkp.png',
                action=PostbackTemplateAction(
                    label='postback2',
                    text='postback text2',
                    data='action=buy&itemid=2'
                )
            )
        ]
    )
    )
        line_bot_api.reply_message(event.reply_token,Image_Carousel)
    	
		
if __name__ == "__main__":
	app.run()

def forShow(tex ):	
	shoow =  '\ntext : ' + str( tex.message.text)+'\nid : '+str( tex.message.id) + '\ntype : ' +str( tex.message.type) 	
	shoow = shoow + '\nsource_type : ' + str( tex.source.type)  
	return shoow