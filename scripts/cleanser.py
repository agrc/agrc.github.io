import os
import sys
import re


def replace(walk_dir):
  print('walk_dir = ' + walk_dir)
  print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

  for root, subdirs, files in os.walk(walk_dir):
      if (root.startswith(walk_dir + 'images') or
         root.startswith(walk_dir + '_site') or
         root.startswith(walk_dir + 'downloads') or
         root.startswith(walk_dir + '.grunt')):
          continue

      for filename in files:
          _, extension = os.path.splitext(filename)
          if extension.lower() not in ['.html', '.scss', '.py']:
              continue

          file_path = os.path.join(root, filename)

          print('\t- file %s (full path: %s)' % (filename, file_path))

          with open(file_path, 'r') as original, open(file_path + '.bak', 'w') as updated:
              file_content = []
              for line_content in original.readlines():
                  replaced = update_image_url(line_content)
                  replaced = update_gallery_links(replaced)
                  replaced = update_css_links(replaced)
                  replaced = update_page_links(replaced)
                  replaced = update_download_asset_links(replaced)
                  replaced = update_data_download_button(replaced)
                  replaced = update_caption(replaced)
                  replaced = update_columns(replaced)
                  replaced = update_divider(replaced)
                  replaced = update_icons(replaced)
                  replaced = update_tables(replaced)

                  file_content.append(replaced)

              replaced = update_tabs(file_content)
              updated.write(replaced)

          os.rename(file_path + '.bak', file_path)

def update_image_url(content):
  return re.sub(r'src=[\"\']http:\/\/gis\.utah\.gov\/wp-content\/uploads\/(.*?)["\']',
                'src="{{ "/images/\g<1>" | prepend: site.baseurl }}"',
                content)

def update_gallery_links(content):
  return re.sub(r'src=[\"\']http:\/\/gis\.utah\.gov\/gallery\/(.*?)["\']',
                'src="{{ "/images/gallery/\g<1>" | prepend: site.baseurl }}"',
                content)

def update_css_links(content):
  return re.sub(r'url\([\"\']http:\/\/gis\.utah\.gov\/wp-content\/uploads\/(.*?)[\"\']\)',
                'url(../images/\g<1>)',
                content)

def update_page_links(content):
  return re.sub(r'href=[\"\']http:\/\/gis\.utah\.gov\/(.*?)[\"\']',
                'href="{{ "/\g<1>" | prepend: site.baseurl }}"',
                content)

def update_download_asset_links(content):
  return re.sub(r'[\"\']\/wp-content\/uploads\/(.*?)[\"\']',
                '"/downloads/\g<1>"',
                content)

def update_data_download_button(content):
  return re.sub(r'\[button size=\"medium\" color=\"white\" textColor=\"#923922"\ link=\"(.*?)\"\](Download.*?)\[\/button\]',
                '<a href="\g<1>" class="button medium white"><span class="button-text">\g<2></span></a>',
                content)

def update_caption(content):
  try:
    replace = re.sub(r'<p>\[caption id=.*? caption=\"(.*?)\".*?\](.*?/>)\[/caption\]<\/p>',
                      '<div class="caption">\g<2><p class="caption-text">\g<1></p></div>',
                      content)
  except:
    #: handle captions with no caption..... ....
    pass

  return re.sub(r'<p>\[caption id=.*?\](.*?/>)\[/caption\]<\/p>',
                    '<div class="caption">\g<1></div>',
                    replace)

def update_columns(content):
  replaced = re.sub(r'<p>\[one_half\]<\/p>',
                   '<div class="grid"><div class="grid__col grid__col--1-of-2">',
                   content)
  replaced = re.sub(r'<p>\[\/one_half\](<\/p>)?',
                   '</div>',
                   replaced)
  replaced = re.sub(r'(<p>)?\[one_half_last\]<\/p>',
                   '<div class="grid__col grid__col--1-of-2">',
                   replaced)
  replaced = re.sub(r'(<p>)?\[\/one_half_last\]<\/p>',
                   '</div></div>',
                   replaced)

  return replaced

def update_divider(content):
    replaced = re.sub(r'<p>\[divider_advanced.*\]<\/p>',
                      '<div class="divider"></div>',
                      content)
    replaced = re.sub(r'<p>\[divider_padding\](<br \/>|<\/p>)',
                      '<div class="divider-padding"></div>',
                      replaced)

    return replaced

def update_icons(content):
    return re.sub(r'(.*)\[icon(?:_link)? style=\"(.*?)\".*\](.*)\[\/icon(?:_link)?\](.*)',
                  '\g<1><span class="icon-text icon-\g<2>">\g<3></span>\g<4>',
                  content)

def update_tables(content):
  replaced = re.sub(r'<p>\[styled_table\]<br.*?\/>',
                    ' ',
                    content)
  replaced = re.sub(r'(<p>)?\[styled_table\]<\/p>',
                    '<div class="table-style">',
                    replaced)
  replaced = re.sub(r'<p>\[\/styled_table\]<\/p>',
                    '</div>',
                    replaced)

  return replaced

def update_tabs(content):
    import yaml

    def add_content(key, product, package, html_content):
        if key in package[product]:
            html_content.append(package[product][key])

    # yaml_content = re.match('(---.*?---)', content, flags=re.S)
    # content = re.sub('---.*?---', '', content, flags=re.S)
    # front_matter = yaml.safe_load(yaml_content.group(1))

    html = []
    package = {}

    ignore_list = ['<div class="clear"></div>\n',
                   '\n',
                   '<p>[/tab]</p>\n',
                   '<p>[/tab] [/tabs]</p>\n',
                   '<br />\n'
                  ]
    data = enumerate(content)
    i, line = data.next()

    #: look for h4 product header
    while line is not None:
        print('looking for product')
        match = re.search('class=\"product\">(.*?)<\/h4>', line, flags=re.S)
        if not match:
            #: we have some upfront data page stuff. abstract etc
            if line not in ignore_list:
                print(line)
                html.append(line)

            try:
                i, line = data.next()
                continue
            except StopIteration:
                break

        #: we have a product dataset
        product = match.group(1)
        package[product] = {}

        #: create new package grid
        html.append('''<div class="grid package">
    <div class="grid__col grid__col--12-of-12">
        <h3>{}</h3>
    </div>
    <div class="grid__col grid__col--12-of-12 package-content">
'''.format(product))

        print('working on {}'.format(product))

        working_on_product = True
        while working_on_product:
            print('working on product')
            try:
                i, line = data.next()
            except StopIteration:
                break

            #: look for tab header
            match = re.search('\[tab title=\"(.*?)\"\](.*)', line, flags=re.S)
            if not match:
                print('no match, continuing', line)
                continue

            tab = match.group(1).lower()
            tab_data = match.group(2)

            print('working on {}.{}'.format(product, tab))

            package[product][tab] = ''
            if tab_data not in ignore_list:
                package[product][tab] = tab_data

            working_on_tabs = True
            while working_on_tabs:
                try:
                    i, line = data.next()
                except StopIteration:
                    break

                if re.search('\[\/tabs\]', line, flags=re.S):
                    print('end of product', product, i)
                    working_on_tabs = False
                    working_on_product = False
                elif re.search('\[\/tab\]', line, flags=re.S):
                    working_on_tabs = False
                    print('end of tab', tab, i)
                else:
                    if line in ignore_list:
                        try:
                            i, line = data.next()
                            print('get tab info', i)
                            continue
                        except StopIteration as ex:
                            print('stop iteration', i)
                            break

                    line = re.sub('<p>\[tab[ ]title=\"(.*?)\"\]<br[ ]\/>\n', '', line)
                    package[product][tab] += line

            if working_on_product:
                continue

            add_content('description', product, package, html)
            add_content('usage', product, package, html)
            add_content('contact', product, package, html)

            html.append('''</div>
    <div class="grid__col grid__col--1-of-2">
    <div class="panel">
        <i class="fa fa-pull-right fa-download fa-2x"></i>
        <h5>Downloads</h5>
    </div>
    <div class="panel-content">''')
            add_content('links | download', product, package, html)

            html.append('''
        </div>
    </div>
    <div class="grid__col grid__col--1-of-2">
        <div class="panel update">
            <i class="fa fa-pull-right fa-calendar fa-2x"></i>
            <h5>Updates</h5>
        </div>
        <div class="panel-content">''')

            add_content('updates', product, package, html)

            html.append('''
        </div>
    </div>
    </div>''')

    return ''.join(html)

    # return yaml.dump(front_matter, explicit_start=True, explicit_end=True) + content
    return yaml_content.group(1) + '\n' + content

if __name__ == '__main__':
    replace(sys.argv[1])
