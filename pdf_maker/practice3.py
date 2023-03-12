import json

#[1] key-value pair 형태로 저장
#[2] 다양한 프로그래밍 언어 사용 가능
#[3] 인터넷에서 자료를 주고 받을때 이용됨

pdf_components = {
    'text' : [
        {
            'color':(0,0,0), 
            'fontScale':20, 
            'fontType':'DarkGarden', 
            'location':(100,100), 
            'message': 'Anabelle'
            },
        {
            'color':(255,0,0), 
            'fontScale':30, 
            'fontType':'DarkGarden', 
            'location':(400,300), 
            'message': 'AGold Award'
            },
        ],
    'image' : [
        {
            'image_path' : 'gold_png',
            'width' : 200,
            'height' : 200,
            'location':(0,100)

        }

    ]
}



for k,v in pdf_components.items():
    for elem in v:
        for attr_name, value in elem.items():
            print(attr_name, value)
with open('uder_defined_layout.json','w') as f:
    json.dump(pdf_components, f,indent = '\t')

