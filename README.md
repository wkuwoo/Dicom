# DICOM
Summary of what I studied about DICOM

## **DICOM File의 구성요소**
![DICOM File의 구성요소에 대한 표](https://user-images.githubusercontent.com/66043707/131494675-e55744fd-8f99-41d5-92b7-787639ee0186.png)

### **Information Object Definitions (IOD)**
- CT Image, MR Image, Digital X-Ray Image 등 영상의 종류에 따라 데이터를 규정하기 위해 필요한 **Attribute**들이 다를 수 있는데, 이에 따라 각 영상의 종류는 **Information Object Definitions**라는 것으로 정의되고, 각 **Information Object Definitions**마다 필요한 **Attribute**들이 각각 정의 (**Table 1.** 와 같이 **Information Object Definitions**는 각 영상의 종류를 정의)

### **Information Entity (IE), Module, Attribute**
- **Attribute**는 환자의 신상 정보, 수행한 검사 정보, 영상 자체의 정보 등 “의료용 영상 파일” 데이터를 규정하기 위해 필요한 다양한 속성들을 의미 (쉽게 말해, **Information Entity**의 구체적인 정보)
  - Attribute는 수천 개 가량이 존재하고, 각각은 아래 4가지 사항으로 정의(Table 2. 참조)
    - Unique **Attribute Name**: 속성 이름
    - Unique Attribute **Tag**: 시스템이 해당 속성을 식별하는 용도로 사용하는 4byte의 값
    - **Type** classification: 속성 입력의 필수/선택 여부 관련 정보
    - **Attribute Description**: 해당 속성에 대한 상세한 설명

![DICOM File Attribute의 예시](https://user-images.githubusercontent.com/66043707/131492423-6d168613-94cd-41a8-a6bf-eeaa1480f61c.png)
- 수천 개 가량의 Attribute는 연관성에 따라 소분류인 “Module”, 대분류인 “Information Entity(IE)”로 분류 (**Table 1.** 참조)

## **DICOM Data Format**
![DICOM Data Format에 대한 이미지](https://user-images.githubusercontent.com/66043707/131492408-fd439b91-8005-4809-8bf9-37cb839fb75b.png)
- **File Preamble** (128 byte): 특별한 사용이나 Application Profile을 위해 사용될 수 있음
- **DICOM Prefix** (4 Byte): File Preamble 다음에 나오는 Prefix로 해당 파일이 DICOM이라는 것을 명시함
- **File Meta Element:** 파일에 대한 Attribute를 Data Element의 모음으로 나타냄
- **Information Object:** 이미지/영상 데이터

![File Meta Elements 부분 구성 이미지](https://user-images.githubusercontent.com/66043707/131492420-c930675e-0098-4c41-afa5-e0592d1f7ccf.png)
- **Fig 1.**에서 **File Meta elements** 부분은 **Fig 2.**와 같은 방식으로 구성되는데, 각 **Data element** 마다 순서대로 **Attribute** 정보가 저장되며 각 Data element는 아래 4가지 사항으로 구성
  - **Tag** (4 byte): 앞서 정의된 Attribute의 Tag로 어떠한 Attribute인지를 명시
  - **VR** (Value Representation, 2 byte): 속상 값의 타입을 명시
  - **Value Length** (2 or 4 byte): Value Field의 길이를 명시
  - **Value Field**: 해당 Attribute에 대해 실제로 담긴 정보

## **References**
- https://github.com/vuno-bmkim/dicom
- http://dicom.nema.org/Dicom/2011/11_06pu.pdf
- http://dicom.nema.org/medical/dicom/2016d/output/chtml/part03/sect_C.2.2.html
- https://dicom.innolitics.com/ciods
- http://dicom.nema.org/Dicom/2013/output/chtml/part05/sect_6.2.html
- https://libertegrace.tistory.com/m/entry/Medical-Image-DICOMDigital-Imaging-and-Communications-in-Medicine?category=905970
