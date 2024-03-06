import requests
    
# IFTTT_Webhook
def ifttt_webhook(eventid):
    payload = {"value1": "Internet",
                "value2": "Of",
                "value3": "Things" }
    url = "https://maker.ifttt.com/trigger/" + eventid + "/with/key/[IFTTTキー入力]"
    response = requests.post(url, data=payload)

# ここからスタート
if __name__ == '__main__':
        print ("IFTTT連携開始")

        # IFTTT_Webhook
        ifttt_webhook("line_event")

        print ("IFTTT連携終了")
