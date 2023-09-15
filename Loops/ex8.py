story = ''  #empty string
while story != 'the end' not in story:
    line = input('Enter a line: ')
    story += line + '\n'
print('Ye rahi kahani')
print(story)
    