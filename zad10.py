import re
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris pellentesque venenatis nunc vel ultricies. " \
       "Morbii quis elit eu ipsum sodales pulvinar. Ut tempus eros ac facilisis bibendum. Sed tellus nulla, " \
       "euidfsdfssmod eget varius eu, tristique quis mauris. Phasellus sollicitudin pretium tellus et pretium. Vestibulum " \
       "luctus velit nec tortor frisdfsdfsdngilla venenatis ut vitae diam. Nam aliquet iaculis purus et fringilla. Mauris " \
       "pulvinar cursus lorem sit amet feugiat. Quisque ac mollis ex. "

print(re.findall(r"\b\w{4,}\b", text))

