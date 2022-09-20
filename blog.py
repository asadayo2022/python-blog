import sys
from datetime import date

if sys.argv[1] == "setup":
    title = input("- Enter a title for the main page: ")
    read_html_file = open(("index-model.html"), "r")
    read_html = read_html_file.read()
    index_of_title = read_html.find("<title>") + 7
    read_html = read_html[:index_of_title] + title + read_html[index_of_title:]
    html_file = open("index.html", "x")
    html_file.write(read_html)
    html_file.close()
    read_html_file.close()
    print("  Index.html has been created.")

if sys.argv[1] == "post":
    d2 = date.today().strftime("%B %d, %Y")
    title = input("- Enter the title of the post: ")
    title2 = title.replace(' ', '')
    stuff_to_write = '			\n			<div style="margin-left:12px;"><a class="nav" href="' + title2 + '.html' + '">〇 ' + title + " - " + d2 + '</a><br></div>'
    f = open(("index.html"), "r")
    read_html = f.read()
    index_of_post = read_html.find("</div><!-- Do not delete or move this comment -->") - 1
    stuff_to_write = read_html[:index_of_post] + stuff_to_write + read_html[index_of_post:]
    f.close()
    f = open(("index.html"), "w")
    f.write(stuff_to_write)
    f.close()

    post_text_file = open((sys.argv[2]), "r")
    post_text = post_text_file.read()
    post_file = open((title2 +".html"), "x")
    read_model = open(("post-model.html"), "r").read()
    index_of_title = read_model.find("<title>") + 7
    read_model = read_model[:index_of_title] + title + read_model[index_of_title:]
    index_of_h2 = read_model.find("<!-- pls no delet -->")
    read_model = read_model[:index_of_h2] + title + read_model[index_of_h2:]
    index_of_post = read_model.find("<!-- Don't delete this comment -->")
    read_model = read_model[:index_of_post] + post_text + read_model[index_of_post:]
    post_file.write(read_model)
    post_file.close()
    post_text_file.close()
    print("  New post has been added.")