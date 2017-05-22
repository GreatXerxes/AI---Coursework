testFile = "test.dat"
trainFile = "trainpred.dat"

actual = []#list of acutal instances
predicted = []#list of predicted instances
#Combine files into a single list
with open (testFile) as textFile1:# open test file
    with open(trainFile) as textFile2:# open predicted file
        for e in range(0, 120): # look at all instances
            line = textFile1.readline().rstrip('\n')#read line from test

            actual.append(int(line[0:2]))
            line = textFile2.readline().rstrip('\n')
            predicted.append(int(line[0:2]))
textFile1.close()
textFile2.close()

#Analysis
incorrect = 0
incorrectly_predicted_nondefective = 0
incorrectly_predicted_defective = 0
act_defective = 0
act_nondefective = 0
pred_defective = 0
pred_nondefective = 0

for e in range(0,120):
	original = actual[e]
	classification = predicted[e]

	if original == 1 and classification == -1:
		incorrectly_predicted_nondefective +=1

	if original == -1 and classification == 1:
		incorrectly_predicted_defective += 1

	if original == 1:
		act_defective += 1

	if original == -1:
		act_nondefective += 1

	if classification == 1:
		pred_defective += 1

	if classification == -1:
		pred_nondefective += 1


incorrect = incorrectly_predicted_nondefective + incorrectly_predicted_defective

print "No of incorrect instances: " + str(incorrect)
print "No of instances that labeled as defective and incorrectly predicted as non-defective: " + str(incorrectly_predicted_nondefective)
print "No of instances that labeled as non-defective and incorrectly predicted as defective: " + str(incorrectly_predicted_defective)
print "No of actual defective: " + str(act_defective)
print "No of actual non-defective: " + str(act_nondefective)
print "No of predicted defective: " + str(pred_defective)
print "No of predicted non-defective: " + str(pred_nondefective)
