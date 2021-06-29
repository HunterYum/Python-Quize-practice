#1
names = ["유튜버1", "유튜버2", "유튜버3", "유튜버4"]
for name in names:
    with open("{}.txt".format(name), "w", encoding="utf8") as email_file:
        email_file.write(f"""
        hi? {name}.
        """)