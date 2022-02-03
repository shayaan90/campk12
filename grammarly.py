from textblob import TextBlob

a = TextBlob("campk12 is good copany and vlue theeeir emplllloyees.")

# using TextBlob.correct() method
a = a.correct()

print(a)
