import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Data entered by user!!
student_file=pd.read_excel(r"C:\Users\Shashank\Desktop\testZB1.xlsx")
question_file=pd.read_excel(r"C:\Users\Shashank\Desktop\testZB2.xlsx")
comment_file=pd.read_excel(r"C:\Users\Shashank\Desktop\testZB3.xlsx")
personality_file=pd.read_excel(r"C:\Users\Shashank\Desktop\testZB4.xlsx")
no_of_tags=5
tags=["a","b","c","d","e"]
diff_in_range=5
range_of_total=50
base_score=[0,0,0,0,0]

#DO NOT GO BELOW THIS LINE!!

student_dataframe=pd.DataFrame(student_file)
question_dataframe=pd.DataFrame(question_file)
comment_dataframe=pd.DataFrame(comment_file)
personality_dataframe=pd.DataFrame(personality_file)
no_of_students=student_dataframe.shape[0]
second_file_rows=question_dataframe.shape[0]
second_file_col=question_dataframe.shape[1]
no_of_questions=student_dataframe.shape[1]
tag_file_col=comment_dataframe.shape[1]
for i in range(no_of_students):
	student_score=base_score.copy()
	total_score=0
	comment=""
	personality_tag=""
	print(no_of_questions)
	for j in range(2,no_of_questions):
		tag=question_dataframe.iloc[j-2,2]
		tag=tag.lower()
		# print(tag)
		if(tag==tags[0]):
			student_score[0]+=student_dataframe.iloc[i,j]
			total_score+=student_dataframe.iloc[i,j]
		elif(tag==tags[1]):
			student_score[1]+=student_dataframe.iloc[i,j]
			total_score+=student_dataframe.iloc[i,j]
		elif(tag==tags[2]):
			student_score[2]+=student_dataframe.iloc[i,j]
			total_score+=student_dataframe.iloc[i,j]
		elif(tag==tags[3]):
			student_score[3]+=student_dataframe.iloc[i,j]
			total_score+=student_dataframe.iloc[i,j]
		elif(tag==tags[4]):
			student_score[4]+=student_dataframe.iloc[i,j]
			total_score+=student_dataframe.iloc[i,j]
	print(student_score)
	print(total_score)
	for j in range(no_of_tags):
		tag_score=student_score[j]
		if tag_score%diff_in_range==0:
			temp=(int)(tag_score/diff_in_range+1)
		else:
			tag_score-=tag_score%diff_in_range
			temp=(int)(tag_score/diff_in_range+2)
		print(temp)
		comment+=comment_dataframe.iloc[j,temp]
	if total_score%total_score==0:
		temp2=(int)(total_score/range_of_total+1)
	else:
		total_score-=total_score%range_of_total
		temp2=(int)(total_score/range_of_total+2)
	personality_tag=personality_dataframe.iloc[0,temp2]
	print(comment)
	print(personality_tag)
	#printPdf(comment,personality_tag)