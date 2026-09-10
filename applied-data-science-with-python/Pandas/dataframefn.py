import pandas as pd

dict1 = {
            'course' : ['aa', 'bb', 'cc'],
            'age' : [40,50,60],
            'Name' : ['DS', 'ML', 'DL'],
            'day' : [10, 11,12]
        }
# df = pd.DataFrame(data=dict1)
# df = pd.DataFrame(data = dict1, index=[10,11,12])
# print(df)
# print(type(df))

# pandas.core.frame.DataFrame
df = pd.read_csv('tips.csv')
# print(df)
# print(df.ndim)
# print(df.sample()) #give one row randomly
# print(df.sample(5)) # 5 rows randomly
# print(df.shape)
# print(df.shape)
# print(df.info())
# print(df.values)
# print(df.describe())
# print(df.columns)
# print(list(df.columns))
# print(df['tip'])
# print(df.tip) #not recommended
# print(type(df['tip']))
# print(df[ ['tip', 'gender', 'smoker'] ])
# print(df['gender'].unique())
# print(df['gender'].nunique()) #give the unique values in that column
# print(df['gender'].value_counts()) #gives the count of each unique value
# print(df['gender'].value_counts(normalize=True)) #give percentage
# df['percent_tip_wrt_total_bill'] = 1
# print(df)
# print(df.sample(3))
# df['percent_tip_wrt_total_bill'] = ((df['tip'] / df['total_bill']) * 100).round(2)
# print(df.sample(3))
# df['monthly_bill'] = (df['total_bill']) * 30
# print(df.sample(3))
# df2 = df.copy()
# print(df.drop(columns=['percent_tip_total_bill',]))
# print(df.sample(3))
# df.drop('percent_tip_total_bill', axis = 1) #axis = 1 is column
# df.sample(3)
# df.drop('percent_tip_total_bill', axis = 1, inplace = True)
# print(df.sample(3))
# df.drop(['smoker','gender'], axis = 1) # use list to drop multiple cols
#row dropping
# df.drop(4, axis = 0) # axis=0 is rows, by default it will look for rows
# df.drop([2,3]) # dropping multiple rows, no need to give axis=0 because by default it will look for row indexes
# df['gender_smoker'] = df['gender'] + '_' + df['smoker']
# df['day_time'] = df['day'] + '_' + df['time']
# print(df)

#----------indexing using loc function--------------------
#Indexing - loc
#loc - column names only
#df.loc[row_names, col_names]
# print(df.loc[100, 'total_bill']) #1 row, 1 column
# print(df.loc[ [100,101], 'total_bill' ]) # with multiple rows & 1 column
# print(df.loc[ [100,101], ['total_bill', 'smoker']]) # with multiple rows & columns
# print(df.loc[ [100,101], ['total_bill', 'smoker', 'time']]) # with multiple rows & columns

#----------indexing using iloc function--------------------
#Indexing - iloc
#iloc - column indexes not on column names
#df.loc[row_index, col_index]
# print(df.iloc[8,2]) #row-8 and column-2
# print(df.iloc[[0,4],3:5]) #rows 0 & 4 and columns from 3 to 4; 5 being the upper bound is not included
# print(df)
# print(df.iloc[:6, 5:]) #rows from 0 to 6 and columns from 5 till the end
# print(df.iloc[8:10, [2,-1,3]])

#---iat()---
#used for selecting data but can only select a single value
# print(df.iat[3,5])

#--sum()--
# print(df[['total_bill', 'tip', 'size']].sum())

#mean
# print(df['total_bill'].mean())
# print(df['total_bill'].median())
# print(df['total_bill'].unique())
# print(df['total_bill'].var())
# print(df['total_bill'].cumsum()) #this will give the cumulative sum of the column 
# print(df['gender'].mode()) #it will give the most frequently occuring value in that column
# df['percent_tip_wrt_total_bill'] = ((df['tip'] / df['total_bill']) * 100).round(2)
# print(df)
# df.sort_values(by = 'percent_tip_wrt_total_bill', ascending=True)
# print(df)
# df.sort_values(by = ['size', 'tip'], ascending=[False, True], inplace = True)
# print(df)

# df.reset_index(drop=True, inplace=True)
# print(df)
#null check - detect missing values isna() and isnull() are same
# print(df.isna())
# print(df.isnull())
# print(df.isna().sum()) #False=0 ; True=1

#None, np.nan --->null vaules
null_df = pd.DataFrame(data = {'grade' : [10,3,None],
                                'dept_id' : [9, None, None],
                                'block_id' : [15,20,None],
                                'class_room' : [15,30,None]})
# print(null_df)
# print(null_df.isna().sum())
# null_df.dropna()
# print(null_df.dropna())
# null_df.dropna(how="all", inplace=True) #all values are missing then drop the row
# print(null_df)
# null_df.dropna(how="any", inplace=True) #default - even one single value is missing then drop it
# print(null_df)
# null_df.dropna(thresh = 3, inplace=True) #3 not null values should be there in a row
# print(null_df)

# print(null_df.fillna(0))
# null_df.fillna(0, inplace=True)
# print(null_df)
null_df2 = null_df.copy()

# null_df2['dept_id'] = null_df2['dept_id'].fillna(0).astype(int)
# null_df2['grade'] = null_df2['grade'].fillna(null_df2['grade'].mean())
# null_df2['block_id'] = null_df2['block_id'].fillna(null_df2['block_id'].mean())
# null_df2['class_room'] = null_df2['class_room'].fillna(null_df2['class_room'].mean())
# print(null_df2)
# print(null_df2)

# test = null_df2[["grade", "dept_id"]] = (
#     null_df2[["grade", "dept_id"]]
#     .fillna(null_df2[["grade", "dept_id"]].mean())
# )
# test


for col in null_df2:
        grade = null_df2['grade']
        # dept_id = col[1]
        # block_id = col[2]
        
        # dept_id = null_df2['dept_id'].fillna(100)
        # block_id = null_df2['block_id'].fillna(100)
        grade = null_df2['grade'].fillna(100).astype(int)

# print(null_df2)

# dt = {'grade' : 200, 'block_id' : 999, 'class_room' : 111}
# for k,v in dt.items():
#     null_df2[k] = null_df2[k].fillna(v)
# print(null_df2)
# print(df)
# print(df.duplicated())
# print(df.duplicated().sum())
# print(df[df.duplicated()])#filtering the duplicate rows
# df.drop_duplicates(inplace=True) #drop duplicates from the data
# print(df)
# print(df.duplicated(keep = False)) #keep = False will mark all the duplicates as True
# print(df.duplicated(keep = False).sum())

# print(df[df.duplicated(keep = False)])#filtering the duplicate rows
# print(df.duplicated(subset = ['gender', 'smoker']).sum()) #check duplicates based on specific columns
# df.drop_duplicates(keep = 'first', inplace = True, ignore_index = True) #keep='last' , keep = False
# print(df)
# print(df['day'].unique())
# print(df.transpose())
# print(df.T)
# df2 = df.T
#Dummy Encoding - used when data is categorical and cannot be ordered
# df3 = pd.get_dummies(data = df, columns = ['day', 'gender', 'smoker', 'time']) # one hot encoding
# print(df3)
# print(pd.get_dummies(data = df, columns = ['day', 'gender', 'smoker', 'time'], drop_first=True))

grouped = df.groupby(['gender','time'])
# print(grouped.groups)
# print(grouped.groups.keys())
# print(grouped.get_group(('Female', 'Dinner')))
# print(df.groupby(['gender','time']).mean(numeric_only=True))
# print(df.groupby('gender')['total_bill'].mean())
# print(df.groupby('smoker')['total_bill'].mean())
# print(df.groupby('day')['total_bill'].mean())
# print(df.groupby('time')['total_bill'].mean())
# print(df.groupby('time')['smoker'].value_counts())
# print(pd.DataFrame(df.groupby(['day','time'])['gender'].value_counts()))
# print(pd.DataFrame(df.groupby(['day','time'])['gender'].count())) #count returns total row count for each group

# print(df.pivot_table(index = 'time', columns = 'day', values = 'total_bill', aggfunc = 'sum'))

# print(df.groupby(['time', 'day']).agg({'total_bill' :'sum'}))

# print(df.groupby(['gender', 'day', 'smoker'])[['total_bill', 'tip']].mean())

# print(df.pivot_table(index = ['gender', 'day'], columns = 'smoker', values = ['total_bill', 'tip'], aggfunc = 'mean'))

# print(df.pivot_table(index = ['gender'], columns = ['smoker', 'day'], values = ['total_bill', 'tip'], aggfunc = 'mean'))    

#apply function
# def change_name(x):
#         if x == 'Sun':
#                 return 'Sunday'
#         if x == 'Mon':
#                 return 'Monday'
#         if x == 'Tue':
#                 return 'Tuesday'
#         if x == 'Fri':
#                 return 'Friday'
#         if x == 'Sat':
#                 return 'Saturday'
#         else:
#                 return x

# df['day'] = df['day'].apply(change_name)
# print(df.head(10))

# def analyze_total_bill(x):
#         if 0 >= x <= 10:
#                 return 'Low'
#         elif 10 < x <= 25:
#                 return 'Medium'
#         else:
#                 return 'High'
        
# df['total_bill_analysis'] = df['total_bill'].apply(analyze_total_bill)

# def day_type(x):
#         if x == 'Sun' or x == 'Sat':
#                 return 'Weekend'
#         else:
#                 return 'Weekday'
# df['day_type'] = df['day'].apply(day_type)
# print(df.groupby(['day_type']).agg({'total_bill' : 'sum'}))

# df['_lambda_day'] = df['day'].apply(lambda x: 'Weekend' if x in ['Sun', 'Sat'] else 'Weekday')
# print(df.head(10))

# df['_lambda_bill'] = df['total_bill'].apply(lambda x: 'inexpensive' if x <= 10 else 'moderate' if x <= 25 else 'expensive') 

# df['gender_bool'] = df['gender'].apply(lambda x: 1 if x == 'Female' else 0)
# print(df.head(10))
df['combo'] = df['gender'] + '_' + df['smoker']
# print(df.head(10))
# #string function
# print('Female_No'.split('_'))

df['split_gender'] = df['combo'].apply(lambda x: x.split('_')[0])
df['split_smoker'] = df['combo'].apply(lambda x: x.split('_')[1])
# print(df.head(10))
# print(df['combo'].str.split('_').head(2))
# print(df['combo'].str.split('_', expand=True).head(2))
df[['split_gender', 'split_smoker']] = df['combo'].str.split('_', expand=True)
print(df.head(10))