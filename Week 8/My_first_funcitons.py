print "Content-type: text/html"
print

def get_standard_opening_markup(title_str, css_file_str):
    if title_str==''and css_file_str=='':
        title_str='A dynamically generated webpage';
        print '<!DOCTYPE html>'
        print '<head>'
        print '<title>',title_str,'</title>'
        print '</head>'
        print '<body>'
        print '<h1>',title_str,'</h1>'
        print '<table>\
               <tr>\
               <td>Coffee</td>\
               <td>Amount of milk to<br>make 1 cup (236 ml)</td>\
               </tr>\
               <tr>\
               <td>Espresso</td>\
               <td>0 ml</td>\
               </tr>\
               <tr>\
               <td>Latte</td>\
               <td rowspan="2">100ml</td>\
               </tr>\
               <tr>\
               <td>Cappuccino</td>\
               </tr>\
               <tr>\
               <td>Americano</td>\
               <td rowspan="2">30ml</td>\
               </tr>\
               <tr>\
               <td>Macchiatto</td>\
               </tr>\
               </table>'


        

        
    elif title_str!=''and css_file_str=='':
        print '<!DOCTYPE html>'
        print '<head>'
        print '<title>',title_str,'</title>'
        print '</head>'
        print '<body>'
        print '<h1>',title_str,'</h1>'
        print '<table>\
               <tr>\
               <td>Coffee</td>\
               <td>Amount of milk to<br>make 1 cup (236 ml)</td>\
               </tr>\
               <tr>\
               <td>Espresso</td>\
               <td>0 ml</td>\
               </tr>\
               <tr>\
               <td>Latte</td>\
               <td rowspan="2">100ml</td>\
               </tr>\
               <tr>\
               <td>Cappuccino</td>\
               </tr>\
               <tr>\
               <td>Americano</td>\
               <td rowspan="2">30ml</td>\
               </tr>\
               <tr>\
               <td>Macchiatto</td>\
               </tr>\
               </table>'



            
    elif title_str==''and css_file_str!='':
        title_str='A dynamically generated webpage';
        print '<!DOCTYPE html>'
        print '<head>'
        print '<link rel="stylesheet" type="text/css" title="Default" media="all" href="',css_file_str,'"/>'
        print '<title>',title_str,'</title>'
        print '</head>'
        print '<body>'
        print '<h1>',title_str,'</h1>'
        print '<table>\
               <tr>\
               <td>Coffee</td>\
               <td>Amount of milk to<br>make 1 cup (236 ml)</td>\
               </tr>\
               <tr>\
               <td>Espresso</td>\
               <td>0 ml</td>\
               </tr>\
               <tr>\
               <td>Latte</td>\
               <td rowspan="2">100ml</td>\
               </tr>\
               <tr>\
               <td>Cappuccino</td>\
               </tr>\
               <tr>\
               <td>Americano</td>\
               <td rowspan="2">30ml</td>\
               </tr>\
               <tr>\
               <td>Macchiatto</td>\
               </tr>\
               </table>'


            
    elif title_str!=''and css_file_str!='':
        print '<!DOCTYPE html>'
        print '<head>'
        print '<link rel="stylesheet" type="text/css" title="Default" media="all" href="',css_file_str,'"/>'
        print '<title>',title_str,'</title>'
        print '</head>'
        print '<body>'
        print '<h1>',title_str,'</h1>'
        print '<table>\
               <tr>\
               <td>Coffee</td>\
               <td>Amount of milk to<br>make 1 cup (236 ml)</td>\
               </tr>\
               <tr>\
               <td>Espresso</td>\
               <td>0 ml</td>\
               </tr>\
               <tr>\
               <td>Latte</td>\
               <td rowspan="2">100ml</td>\
               </tr>\
               <tr>\
               <td>Cappuccino</td>\
               </tr>\
               <tr>\
               <td>Americano</td>\
               <td rowspan="2">30ml</td>\
               </tr>\
               <tr>\
               <td>Macchiatto</td>\
               </tr>\
               </table>'


def get_closing_markup():
        print '</body>'
        print '</html>'


opening_markup = get_standard_opening_markup("My first dynamically generated webpage, GG Thomas", "styles.css");
closing_markup = get_closing_markup();

opening_markup;
closing_markup;
        
