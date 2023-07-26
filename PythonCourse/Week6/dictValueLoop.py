# if you only wanted to loop through the values...
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
for language in favorite_languages.values():
    print(language.title())