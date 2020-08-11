def run_path():
    save_file =  open('out/mane_patch.html','w')
    with open('out/mane.html','r') as html_file:
        for html_insite_line in html_file:
            html_insite_line = html_insite_line.replace("<pre",'<pre style="white-space: pre-wrap;word-wrap: break-word;" ')
            html_insite_line = html_insite_line.replace("<code",'<mane')
            html_insite_line = html_insite_line.replace("</code>",'</mane>')
            save_file.writelines(html_insite_line)
