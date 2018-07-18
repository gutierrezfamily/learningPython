import re

timetext = "1230"
text ="this is a test phone number 7604029326.  I'll be at the party at 5:30. "

# adding a colon to a time.
print timetext
timetext = re.sub(r'(^|\s)((?:1[0-2])|(?:[1-9])) ?((?:[0-5][1-9])|(?:[1-5][0-9]))(\s|$)', '\\1\\2:\\3\\4', timetext)
print timetext


# adding a space between digits in a phone number
print text
found = (re.search(r'(^|\s)\d{10}', text))
if (found):
    text = re.sub('([0-9])', r' \1', text)
print text

#code samples

#    print "found"
# text = re.sub(r'd{1}', r'\1 ', text)
#if ((re.search(r'(^|\s)\d{10}', text))):
#    text = re.sub('([0-9])', r' \1', text)
#text = re.sub('([0-9]{10,10})', r' ~telephone~\1~', text)
#text = re.sub(r'(^|\s)((?:1[0-2])|(?:[1-9])) ?((?:[0-5][1-9])|(?:[1-5][0-9]))(\s|$)', '\\1\\2:\\3\\4', text)
#text = re.sub(r'(^|\s)\d{10}', '\\1 ', text)
#if (re.search(r'(^|\s)\d{10}', text):
