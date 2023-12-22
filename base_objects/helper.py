
# def split_tags(tags_string):
#     if tags_string is None or (isinstance(tags_string, str) and len(tags_string) < 2):
#         return tags_string

#     if isinstance(tags_string, list) and len(tags_string) == 1:
#         splitted = tags_string[0].split()
#     elif isinstance(tags_string, str):
#         splitted = tags_string.split()
#     else:
#         return tags_string
#     tags = []
#     for s in splitted:
#         tags.extend(s.split(","))

#     tags = [tag.strip() for tag in tags if tag.strip()]

#     return tags
