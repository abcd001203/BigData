#공통
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font',family=font_name)

data='train.csv'
df=pd.read_csv(data)


# 생존자와 사망자 수
dead = df['Survived'].value_counts()[0]  # 사망자 수
survived = df['Survived'].value_counts()[1]  # 생존자 수
new_df=pd.DataFrame([survived,dead])
new_df.index=['생존자','사망자']
new_df.columns=['인원']

new_df.plot(kind='bar',stacked=True)
plt.title('생존자와 사망자 수')
plt.ylabel('수')
plt.show()


# 승객의 나이 분포(히스토그램)
new_df = df['Age'].dropna() # 승객 나이 데이터에서 NaN 제거

new_df.plot(kind='hist', bins=40, color='skyblue', edgecolor='black')
plt.title('승객의 나이 분포', fontsize=16)
plt.xlabel('나이', fontsize=14)
plt.ylabel('빈도수', fontsize=14)
plt.show()


# 승객의 나이 분포(파이그래프)
age_df = df['Age'].dropna()# 승객 나이 데이터에서 NaN 제거
teenager = age_df[age_df < 20].count()  # 0~10대
s2030 = age_df[(age_df >= 20) & (age_df < 40)].count()  # 20~30대
s4050 = age_df[(age_df >= 40) & (age_df < 60)].count()  # 40~50대
s60 = age_df[(age_df >= 60) & (age_df < 70)].count()  # 60대
senior = age_df[age_df >= 70].count()  # 70세 이상

new_df = pd.DataFrame([teenager, s2030, s4050, s60, senior])
new_df.index = ['0-10대', '20-30대', '40-50대', '60대', '70세 이상']
new_df.columns=['']

new_df.plot(kind='pie',subplots=True, autopct='%1.1f%%')
plt.legend(loc='upper left')
plt.title('승객의 나이 분포', fontsize=16)
plt.show()


#승객의 성별 비율
female = df['Sex'].value_counts()['female']  # 여자 수
male = df['Sex'].value_counts()['male']  # 남자 수
new_df=pd.DataFrame([female,male])
new_df.index=['여성','남성']
new_df.columns=['인원']

new_df.plot(kind='pie',subplots=True, autopct='%1.1f%%',startangle=90,colors=['coral', 'lightblue'])
plt.title('승객의 성별 비율', fontsize=16)
plt.show()


#승객의 티켓 등급 비율
first = df['Pclass'].value_counts()[1]  # 1등급
second = df['Pclass'].value_counts()[2]  # 2등급
third = df['Pclass'].value_counts()[3]  # 3등급
new_df=pd.DataFrame([first,second,third])
new_df.index=['1등급','2등급','3등급']
new_df.columns=['']

new_df.plot(kind='pie',subplots=True, autopct='%1.1f%%',startangle=90)
plt.title('티켓 등급 비율', fontsize=16)
plt.show()


#성별에 따른 생존자와 사망자 수
dead = df[df['Survived']==0]['Sex'].value_counts()  # 사망자 수
survived = df[df['Survived']==1]['Sex'].value_counts()  # 생존자 수
new_df=pd.DataFrame([survived,dead])
new_df.index=['생존자','사망자']
new_df.columns = ['여성', '남성']

new_df.plot(kind='bar',stacked=True,color=['coral','lightblue'])
plt.title('성별에 따른 생존자와 사망자 수')
plt.ylabel('수')
plt.show()


#성별에 따른 생존자와 사망자 비율
dead = df[df['Survived']==0]['Sex'].value_counts()  # 사망자 수
survived = df[df['Survived']==1]['Sex'].value_counts()  # 생존자 수
new_df=pd.DataFrame([survived,dead])
new_df.index=['생존자','사망자']
new_df.columns = ['여성', '남성']

fig, axes = plt.subplots(1, 2, figsize=(5, 3))  # 서브플롯 생성 (1행 2열)

for i, ax in enumerate(axes):
    new_df.iloc[:, i].plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax)
    ax.set_ylabel('')  # y축 레이블 제거
    ax.set_title(new_df.columns[i], fontsize=12) 
    
plt.suptitle('성별에 따른 생존자와 사망자 비율',fontsize=13, y=1)
plt.show()


# 생존자와 사망자 연령
teenager = df[df['Age'] < 20]['Survived'].value_counts()  # 0~10대
s2030 = df[(df['Age'] >= 20) & (df['Age'] < 40)]['Survived'].value_counts()  # 20~30대
s4050 = df[(df['Age'] >= 40) & (df['Age'] < 60)]['Survived'].value_counts()  # 40~50대
s60 = df[(df['Age'] >= 60) & (df['Age'] < 70)]['Survived'].value_counts()  # 60대
senior = df[df['Age'] >= 70]['Survived'].value_counts()  # 70세 이상
new_df = pd.DataFrame([teenager, s2030, s4050, s60, senior])
new_df.columns = ['사망자', '생존자']
new_df.index = ['0-10대', '20-30대', '40-50대', '60대', '70세 이상']
new_df = new_df.reindex(columns=['생존자','사망자'])#열 재정렬
new_df=new_df.T

new_df.plot(kind='bar',stacked=True)
plt.title('생존자와 사망자의 연령')
plt.ylabel('수')
plt.show()


# 연령대에 따른 생존자와 사망자 비율
teenager = df[df['Age'] < 20]['Survived'].value_counts()  # 0~10대
s2030 = df[(df['Age'] >= 20) & (df['Age'] < 40)]['Survived'].value_counts()  # 20~30대
s4050 = df[(df['Age'] >= 40) & (df['Age'] < 60)]['Survived'].value_counts()  # 40~50대
s60 = df[(df['Age'] >= 60) & (df['Age'] < 70)]['Survived'].value_counts()  # 60대
senior = df[df['Age'] >= 70]['Survived'].value_counts()  # 70세 이상
new_df = pd.DataFrame([teenager, s2030, s4050, s60, senior])
new_df.columns = ['사망자', '생존자']
new_df.index = ['0-10대', '20-30대', '40-50대', '60대', '70세 이상']
new_df=new_df.T

fig, axes = plt.subplots(1, 5, figsize=(10, 3))  # 서브플롯 생성 (1행 5열)

for i, ax in enumerate(axes):
    new_df.iloc[:, i].plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax)
    ax.set_ylabel('')  # y축 레이블 제거
    ax.set_title(new_df.columns[i], fontsize=12) 
    
plt.suptitle('연령대에 따른 생존자와 사망자 비율',fontsize=13, y=1)
plt.show()


#탑승지별 평균 요금
Southampton = df[df['Embarked'] == 'S']['Fare'].mean()  # 사우샘프턴
Queenstown = df[df['Embarked'] == 'Q']['Fare'].mean()  # 퀸즈타운
Cherbourg = df[df['Embarked'] == 'C']['Fare'].mean()  # 셰르부르
new_df = pd.DataFrame([Queenstown, Cherbourg, Southampton])
new_df.index = [ '퀸즈타운','셰르부르','사우샘프턴']
new_df.columns = ['가격']

new_df.plot(kind='bar')
plt.legend(loc='upper left')
plt.title('탑승지별 평균 요금')
plt.ylabel('가격')
plt.show()


#탑승지에 따른 티켓 등급 비율
Southampton = df[df['Embarked'] == 'S']['Pclass'].value_counts()  # 사우샘프턴
Queenstown = df[df['Embarked'] == 'Q']['Pclass'].value_counts()  # 퀸즈타운
Cherbourg = df[df['Embarked'] == 'C']['Pclass'].value_counts()  # 셰르부르

new_df = pd.DataFrame([Queenstown, Cherbourg, Southampton])
new_df.index = [ '퀸즈타운','셰르부르','사우샘프턴']
new_df.columns = ['3등급', '2등급', '1등급']
new_df = new_df.reindex(columns=['1등급', '2등급', '3등급'])  # 열 재정렬

new_df=new_df.T
fig, axes = plt.subplots(1, 3, figsize=(10, 3))  # 서브플롯 생성 (1행 3열)

for i, ax in enumerate(axes):
    new_df.iloc[:, i].plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax)
    ax.set_ylabel('')  # y축 레이블 제거
    ax.set_title(new_df.columns[i], fontsize=12) 

plt.suptitle('탑승지에 따른 티켓 등급 비율', fontsize=12, y=1.1)
plt.show()


#탑승지에 따른 티켓 등급
Southampton = df[df['Embarked'] == 'S']['Pclass'].value_counts()  # 사우샘프턴
Queenstown = df[df['Embarked'] == 'Q']['Pclass'].value_counts()  # 퀸즈타운
Cherbourg = df[df['Embarked'] == 'C']['Pclass'].value_counts()  # 셰르부르

new_df = pd.DataFrame([Queenstown, Cherbourg, Southampton])
new_df.index = [ '퀸즈타운','셰르부르','사우샘프턴']
new_df.columns = ['3등급', '2등급', '1등급']
new_df = new_df.reindex(columns=['1등급', '2등급', '3등급'])  # 열 재정렬

new_df.plot(kind='bar',stacked=True)
plt.legend(loc='upper left')
plt.title('탑승지에 따른 티켓 등급')
plt.ylabel('수')
plt.show()


#티켓 등급에 따른 생존사와 사망자 수
dead = df[df['Survived']==0]['Pclass'].value_counts()  # 사망자 수
survived = df[df['Survived']==1]['Pclass'].value_counts()  # 생존자 수
new_df=pd.DataFrame([survived,dead])
new_df.index=['생존자','사망자']
new_df.columns = ['1등급', '3등급', '2등급']
new_df = new_df.reindex(columns=['1등급', '2등급', '3등급'])#열 재정렬


new_df.plot(kind='bar',stacked=True)
plt.title('티켓 등급에 따른 생존자와 사망자 수')
plt.ylabel('수')
plt.show()


# 티켓 등급별 생존자와 사망자 비율
dead = df[df['Survived'] == 0]['Pclass'].value_counts()  # 사망자 수
survived = df[df['Survived'] == 1]['Pclass'].value_counts()  # 생존자 수
new_df = pd.DataFrame([survived, dead])
new_df.index = ['생존자', '사망자']
new_df.columns = ['1등급', '3등급', '2등급']
new_df = new_df.reindex(columns=['1등급', '2등급', '3등급'])  # 열 재정렬

fig, axes = plt.subplots(1, 3, figsize=(10, 3))  # 서브플롯 생성 (1행 3열)

for i, ax in enumerate(axes):
    new_df.iloc[:, i].plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax)
    ax.set_ylabel('')  # y축 레이블 제거
    ax.set_title(new_df.columns[i], fontsize=12) 

plt.suptitle('티켓 등급별 생존자와 사망자 비율', fontsize=12, y=1.1)
plt.show()


#티켓 등급별 남녀 수
female = df[df['Sex']=='female']['Pclass'].value_counts()  # 여성
male = df[df['Sex']=='male']['Pclass'].value_counts()  # 남성
new_df=pd.DataFrame([female,male])
new_df.index=['여성','남성']
new_df.columns = ['3등급', '1등급', '2등급']
new_df = new_df.reindex(columns=['1등급', '2등급', '3등급'])#열 재정렬
new_df=new_df.T

new_df.plot(kind='bar',stacked=True,color=['coral','lightblue'])
plt.title('티켓 등급별 남녀 수')
plt.ylabel('수')
plt.show()


#동승한 가족 수에 따른 생존자, 사망자 수
df['FamilySize'] = df['SibSp'] + df['Parch']
dead = df[df['Survived']==0]['FamilySize'].value_counts()  # 사망자 수
survived = df[df['Survived']==1]['FamilySize'].value_counts()  # 생존자 수
new_df=pd.DataFrame([survived,dead])
new_df.index=['생존자','사망자']
new_df=new_df.T

new_df.plot(kind='area')
plt.title('동승한 가족 수에 따른 생존자, 사망자 수')
plt.ylabel('수')
plt.show()
new_df


#혼자 탑승한 승객과 가족이 있는 승객의 생존율
df['FamilySize'] = df['SibSp'] + df['Parch']
solo = df[df['FamilySize']==0]['Survived'].value_counts()  # 혼자
family = df[df['FamilySize']>0]['Survived'].value_counts()  # 가족
new_df=pd.DataFrame([solo,family])
new_df.index=['단독','동승']
new_df.columns=['사망','생존']
new_df = new_df.reindex(columns=['생존', '사망'])#열 재정렬

new_df=new_df.T

fig, axes = plt.subplots(1, 2, figsize=(5, 3))  # 서브플롯 생성 (1행 2열)

for i, ax in enumerate(axes):
    new_df.iloc[:, i].plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax)
    ax.set_ylabel('')  # y축 레이블 제거
    ax.set_title(new_df.columns[i], fontsize=12) 
    
plt.suptitle('동승한 가족 여부에 따른 생존율',fontsize=13, y=1)
plt.show()


#혼자 탑승한 승객의 남녀 비율
df['FamilySize'] = df['SibSp'] + df['Parch']
solo_df= df[df['FamilySize']==0]['Sex'].value_counts()  # 혼자
solo_df.index=['남성','여성']
solo_df.columns=['']

solo_df.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.legend(loc='upper left')
plt.title('혼자 탑승한 승객의 남녀 비율', fontsize=16)
plt.show()


#혼자 탑승한 승객의 티켓 등급 비율
df['FamilySize'] = df['SibSp'] + df['Parch']
solo_df= df[df['FamilySize']==0]['Pclass'].value_counts()  # 혼자
solo_df.index=['3등급','1등급','2등급']
new_df = new_df.reindex(columns=['1등급','2등급','3등급'])#열 재정렬
solo_df.columns=['']

solo_df.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.legend(loc='upper left')
plt.title('혼자 탑승한 승객의 티켓 등급 비율', fontsize=16)
plt.show()


#혼자 탑승한 여성과 남성의 생존자와 사망자 수
solo_passengers= df[(df['SibSp'] == 0) & (df['Parch'] == 0)]
dead = solo_passengers[solo_passengers['Survived']==0]['Sex'].value_counts()  # 사망자 수
survived = solo_passengers[solo_passengers['Survived']==1]['Sex'].value_counts()  # 생존자 수
new_df=pd.DataFrame([survived,dead])
new_df.index=['생존자','사망자']
new_df.columns=['여성','남성']

new_df.plot(kind='bar', stacked=True, color=['coral','lightblue'])
plt.title('혼자 탑승한 여성과 남성의 생존자와 사망자 수')
plt.ylabel('수')
plt.show()


#승객의 나이, 성별에 따른 생존 여부를 바이올린 차트로 시각화
plt.figure(figsize=(10, 6))
sns.violinplot(x='Sex', y='Age', hue='Survived', data=df, palette='Set2', split=True, inner='quartile')

plt.title('성별, 나이에 따른 생존 및 사망 여부 분포', fontsize=16)
plt.xlabel('성별', fontsize=14)
plt.ylabel('나이', fontsize=14)
plt.show()


#승객의 티켓 등급과 나이에 따른 생존 여부를 바이올린 차트로 시각화
plt.figure(figsize=(12, 6))
sns.violinplot(x='Pclass', y='Age', hue='Survived', data=df, split=True, palette='Set2', inner='quartile')

plt.title('티켓 등급과 나이에 따른 생존 및 사망 여부 분포', fontsize=16)
plt.xlabel('티켓 등급', fontsize=14)
plt.ylabel('나이', fontsize=14)
plt.show()


#승객의 티켓 등급과 성별에 따른 생존 여부를 바이올린 차트로 시각화
plt.figure(figsize=(12, 6))
sns.violinplot(x='Sex', y='Pclass', hue='Survived', data=df, split=True, palette='Set2', inner='quartile')

plt.title('티켓 등급과 성별에 따른 생존 및 사망 여부 분포', fontsize=16)
plt.xlabel('성별', fontsize=14)
plt.ylabel('티켓 등급', fontsize=14)
plt.show()


# 승객 나이대별 티켓 등급
teenager = df[df['Age'] < 20]['Pclass'].value_counts()  # 0~10대
s2030 = df[(df['Age'] >= 20) & (df['Age'] < 40)]['Pclass'].value_counts()  # 20~30대
s4050 = df[(df['Age'] >= 40) & (df['Age'] < 60)]['Pclass'].value_counts()  # 40~50대
s60 = df[(df['Age'] >= 60) & (df['Age'] < 70)]['Pclass'].value_counts()  # 60대
senior = df[df['Age'] >= 70]['Pclass'].value_counts()  # 70세 이상

new_df = pd.DataFrame([teenager, s2030, s4050, s60, senior])
new_df.index = ['0-10대', '20-30대', '40-50대', '60대', '70세 이상']
new_df.columns = ['3등급', '2등급','1등급']
new_df = new_df.reindex(columns=['1등급', '2등급', '3등급'])#열 재정렬
new_df=new_df.T

fig, axes = plt.subplots(1, 5, figsize=(12, 3))  # 서브플롯 생성 (1행 5열)

for i, ax in enumerate(axes):
    new_df.iloc[:, i].plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax)
    ax.set_ylabel('')  # y축 레이블 제거
    ax.set_title(new_df.columns[i], fontsize=12) 
    
plt.suptitle('승객 나이대별 티켓 등급',fontsize=13, y=1)
plt.show()


#티켓 등급별 객실 구역 분포
df['Cabin_Zone'] = df['Cabin'].str[0]  # 첫 글자 추출 (객실 구역)
pclass_cabin = df.groupby(['Pclass', 'Cabin_Zone']).size().unstack()
pclass_cabin = pclass_cabin.fillna(0)# 결측치(NaN)를 0으로 채우기 (시각화에 사용)

plt.figure(figsize=(8, 6))
sns.heatmap(pclass_cabin, annot=True, fmt='.0f', cmap='Blues')#히트맵
plt.title('티켓 등급별 객실 구역 분포', fontsize=16)
plt.xlabel('객실 구역', fontsize=14)
plt.ylabel('티켓 등급', fontsize=14)
plt.show()



# 객실 구역별 생존율
df['Cabin_Zone'] = df['Cabin'].str[0]  # Cabin의 첫 글자 추출
cabin_survival_rate = df.groupby('Cabin_Zone')['Survived'].mean()

cabin_survival_rate.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('객실 구역별 생존율', fontsize=16)
plt.xlabel('객실 구역', fontsize=14)
plt.ylabel('생존율', fontsize=14)
plt.xticks(rotation=0)  # x축 레이블 가독성을 위한 회전
plt.show()
