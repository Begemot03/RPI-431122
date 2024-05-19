import requests # type: ignore

# 75036840

env = {
    "domain" : "https://api.vk.com/method",
    "v" : "5.199",
    "token" : "vasdfsk1.a.XRMasYCpbhtaPv3Hjs8fasdfdas6tCVasdfsaLnzsx1UsLqt7ttBk512XtuDv2ohuwRaltCOVgwV1TMhcasfasdfaasdfcx5Rqh0NG9inFtzkx9ONU99h1uSC0fRXq-UjUjOnzI--TXWdasdfasdffJTpIuMc8gEnBnfhx7ksIOasdfasdfsdwDfDPSdWnSaty8H0q9DLMaAiHIgmBQ7E4T81-8VLlQ-WWUV0aB9q_KA0YegtTudJmLH6MxH6RiFgvg"
}

def get_friends(user_id):
    url = 'https://api.vk.com/method/friends.get'
    params = {
        'user_id': user_id,
        'fields': 'bdate',
        'access_token': env["token"],
        'v': env["v"],
    }

    response = requests.get(url, params=params)
    data = response.json()

    ages = []
    for friend in data['response']['items']:
        if 'bdate' in friend:
            bdate = friend['bdate'].split('.')
            if len(bdate) == 3:
                age = 2024 - int(bdate[2])
                ages.append(age)

    if ages:
        predicted_age = sum(ages) // len(ages)
        return predicted_age
    else:
        return None



if __name__ == "__main__":
    print(get_friends(345006376))
