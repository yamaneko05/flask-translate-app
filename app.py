import flask
from flask.templating import render_template
from googletrans import Translator


src_text_error_image = 'https://lh3.googleusercontent.com/Y8qtCEUkgzyGT_aq0EoJkS9swB4kVfQ4Rlif61Y58Ok82GclNIlcdejK11HjGVpYVKr1ItCcL8Of98mdlGGm18qH7EzGMMx_2lSmMiarbV6qwdNHVvcZFW4RboBlBu8IJaHy-cBp4ENznV3xEliiZoSnuJyi9WuH7q2l7JBantRyOQtJWDkASmuhGc2zNegSNU6UjrPgLD38fWGVkF5mZ53EO_U4Cf4Y-McASksdJvnSL8G2luB-mjcDYdMmxAoZDnRs0A0qob-sagRaNXIaiiKVl3funYV4NFwDYvQ9E742eGCNLYBzo6i0SZBRHz9DZfASjCYx_eTiOzmU-bMwqKqbULxrhHnUumN_EzxDPjtzwCsa5diYp-SMa-pPdJpa3AtbzljulubyAHBsjxwxNLmYAukRB7o3WPanIv4nIhjbYHgIOlFzEmXh0EDwvoE0ZmTtcQ9BjUuiRjx3e2z930Y-EfaW3N23mqOICykTe8zKd_vgycdtHkbCTKAnz5wSXMgTo6uyBlX92Xwju7uBRxfPfQTXkFPVpJKIesiGAi8G2I_gEwDgyRH2vopoQxwhGHurHAV9XTDm0jQtt7zZrNTUfoU-TkemJ8Jp5XkipOPFVKBWjXBhyDkQ9ZletkNv7IuYHNCkmc0A0DIZAvTUOy-38wVr3Ga2oNIVbOUCT7xfyuiAYmGFF1oI7X6mFOlt8qTljkqvsjtywjNYUOD81Jw=w568-h426-no?authuser=0'
src_text_error_text = '入力した文字もしくは選択した言語がバグってるンゴ！ヘッダーのリンクから管理人TwitterにDMしてね！'
success_report_image = 'https://lh3.googleusercontent.com/dcmMS-dQfmYl0quRvQ_T0c1fwSfmN7NDlPnhZiAex6kcxt8MIsks3TXtHdEUZMRJPY5LLQ0sAsjgF_x7hvEJ_zLQMLi03PBln-tHYJnHFqOEyTErcpA4ipg-2L7TOJjXNMMzXK1RKhmlHK_QP-Dox-_mPXD9FOm4xZfwvGGVV5zLrJva1NI_2oDgcqvbIBnKBtDSklvHQCcAcMS_cVWP2-_qJjouc6Y41Q3oUu-YC4q_LTmtN0dt8cowBucWDgwWdNsWFB2_yNC3snSTzvO2PQNLMRYyrL94g3VAlAAfV-2BCN_6h7YauIYBqXnsqwFLY6tIVLQo-lzTY4h0FaiYstRcWoeOJFEcIri9-LqiUlouxH6WjqP9H_t03eO7NXfTa671xdbES4h66i7HZmlYlNVY5vdaABolo5B5nyowoS_QMS59hEb9icelsZw1CnNcsO0vYy-FTrm4ELZ2HuyAtEhYa-Syxn80Yj98GVmhrrKMu-mMG0TJd08eOQXkmIaUpWNmjv7NJ4Hwt4SM-uOztoSaYsrsuE4Cti-nYNSUbnHfTcpLdJiTwoZElgof8DtB9rhkHvzsp23MIaxCrfk5t__xclcP81o6vK51mq0u7GGR93kuY1ZJY7MeF_QF3Ht21thDo3evaELzz1xqSoc3cG0TcoDuBvGs0IyWc_DdgBIeOAI_o-4KKDHYQ5PCvpaVRpKQBGA6HUS0DOYQAXL0TdU=w391-h220-no?authuser=0'
success_report_text = 'いい感じに翻訳できたンゴ！ヘッダーのリンクからtwitterフォローしてくれたら嬉しいンゴ！'

app = flask.Flask(__name__)
translator = Translator()

@app.route('/')
def index():
  src_lang = 'en'
  dest_lang = 'ja'
  return flask.render_template('index.html', detect_src_lang=src_lang, select_dest_lang=dest_lang)

@app.route('/translate', methods=['POST'])
def translate():
  src_text = flask.request.form.get('japanese')
  src_lang = flask.request.form.get('src-lang')
  dest_lang = flask.request.form.get('dest-lang')
  if flask.request.form.get('auto') == 'on':
      try:
        src_lang = translator.detect(str(src_text)).lang
      except:
        return flask.render_template('index.html', last_src_text=src_text, image=src_text_error_image,
                                                  text=src_text_error_text, select_dest_lang=dest_lang)
  try:
    dest_text = translator.translate(src_text, src=src_lang, dest=dest_lang).text
  except:
    return flask.render_template('index.html', last_src_text=src_text, image=src_text_error_image,
                                               text=src_text_error_text, select_dest_lang=dest_lang)
  return flask.render_template('index.html', last_src_text=src_text.strip(), image=success_report_image,
                                             text=success_report_text, result=dest_text,
                                             detect_src_lang=src_lang, select_dest_lang=dest_lang)

if __name__ == '__main__':
  app.run()