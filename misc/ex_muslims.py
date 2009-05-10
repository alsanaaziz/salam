#!/usr/bin/env python
# -*- coding: utf-8 -*-

users = [
  (658, "[C*]", "♂", "UK", "Atheist", ()),
  (558, "a.ghazali", "♂", "USA", "", ()),
  (359, "A_G", "♂", "", "", ()),
  (469, "abdalwali", "♂", "USA", "", ()),
  (289, "afghan_exmuslim", "♂", "Afghanistan", "", ()),
  (668, "al-uzza", "♀", "", "", ()),
  (684, "AlmostAisha", "♀", "", "", ()),
  (657, "aliadiere", "♂", "", "", ()),
  (56, "All_Brains", "♂", "", "Atheist", ()),
  (416, "allat", "♀", "", "", ()),
  (564, "automan", "♂", "", "", ()),
  (342, "awais", "♂", "USA", "Agnostic", ("Etymology",)),
  (462, "Ayaz", "♂", "Pakistan", "Atheist", ()),
  (9, "Aziz", "♂", "Austria", "Atheist", ("Hell", "slavery", "4:34")),
  (686, "Balthier", "♂", "", "", ()),
  (613, "belladonnasix", "♀", "Canada", "Pantheist", ()),
  (6, "BerberElla", "♀", "UK", "Atheist", ()),
  (187, "Charles", "♂", "Australia", "", ()),
  (615, "coolred38", "♀", "", "", ()),
  (733, "crueljewel", "♀", "", "", ()),
  (345, "DivineMercy", "♀", "", "", ()),
  (346, "Dr Diavolo", "♂", "UK", "Atheist", ()),
  (510, "Eddy", "♂", "Turkey", "", ()),
  (450, "Fading", "♀", "", "", ()),
  (756, "Ferrero", "♀", "", "", ()),
  (638, "FinallyFree", "♂", "UK", "Karma &amp; Luck", ("Ideology", "fallacies", "barbaric practices")),
  (725, "freakzilla", "♂", "UK", "Skeptic", ()),
  (397, "Goldie", "♂", "UK", "", ()),
  (219, "Haji Murad", "♂", "", "", ()),
  (8, "Hassan", "♂", "UK", "Deist", ("Hell", "slavery", "4:34")),
  (495, "heartbomb", "♀", "Australia", "Agnostic", ()),
  (383, "Hedaya", "♀", "", "Agnostic", ()),
  (561, "henrypage", "♂", "UK", "Atheist", ("Muslim reactions to 9/11",)),
  (114, "Humanoid", "♂", "UK", "Apatheist", ()),
  (409, "Humra", "♀", "", "", ()),
  (594, "identitas", "♂", "UK", "Agnostic", ()),
  (77, "Iggy", "♀", "Canada", "Ignostic", ()),
  (141, "Iris", "♀", "UK", "", ()),
  (574, "IsLame", "♂", "UK", "Humanist", ("God's invisibility and cruelty", "existance of polytheism", "net effect of the Qur'an on Muslims")),
  (738, "J4m3z", "♂", "", "", ()),
  (26, "Jack Torrance", "♂", "UK", "Agnostic", ()),
  (727, "jamshed raja", "♂", "UK", "Atheist", ()),
  (93, "Kid A", "♂", "UK", "", ()),
  (317, "KraziKuri", "♀", "UK", "", ()),
  (381, "ladyofshalott", "♀", "UK", "Atheist", ()),
  (16, "li", "♂", "Singapore", "Atheist", ()),
  (197, "Maghrebi", "♂", "Morocco", "", ()),
  (32, "Marmalade-Lady", "♀", "UK", "", ()),
  (11, "Maryam Namazie", "♀", "UK", "Atheist", ()),
  (760, "Meredith", "♀", "", "", ()),
  (710, "ned", "♀", "", "Agnostic", ()),
  (712, "Nite Owllll", "♂", "USA", "Atheist", ()),
  (623, "Nizar", "♂", "Sweden", "Agnostic", ()),
  (430, "Nour", "♀", "", "", ()),
  (408, "Orion", "♂", "", "", ()),
  (260, "Pakman", "♂", "Pakistan", "", ()),
  (249, "panoptic", "", "UK", "Atheist", ()),
  (734, "Pariah", "♀", "", "", ()),
  (160, "Pazuzu", "♂", "UK", "Atheist", ()),
  (554, "PeruvianSkies", "♀", "UK", "Atheist", ()),
  (757, "Ramadulla", "♂", "UK", "", ()),
  (215, "Rational1", "♀", "USA", "Atheist", ()),
  (31, "Reza Moradi", "♂", "UK", "Atheist", ()),
  (592, "rooblee", "♂", "", "", ()),
  (57, "rubina", "♀", "", "", ()),
  (628, "SalahuddinR", "♂", "USA", "Atheist", ()),
  (65, "Shahid Raza", "♂", "", "Atheist", ()),
  (675, "Shahzad", "♂", "", "Panentheist", ()),
  (3, "Spasm", "♀", "", "", ()),
  (544, "stardust", "♀", "", "Deist", ()),
  (369, "Starnexus", "♂", "", "Atheist", ()),
  (747, "Suprah", "♂", "Pakistan", "Atheist", ()),
  (562, "Tommy", "♂", "USA", "Atheist", ()),
  (244, "Uppercut", "", "UK", "Humanist", ()),
  (485, "whatabastor", "♂", "Saudi Arabia", "", ()),
  (255, "WiSsAm", "♂", "Saudi Arabia", "Spiritual Agnostic", ("Women's rights", "Jihad", "negative effects of Islam on Muslims")),
  (19, "Witzbold", "♂", "Pakistan", "Atheist", ()),
  (42, "Zaephon", "♂", "Turkey", "Atheist", ()),
  (58, "ZiaZ", "♂", "UK", "Humanist", ()),
]

from os import path as path
jquery = open(path.join(path.dirname(path.dirname(__file__)), "js", "jquery.js")).read()

head = r"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
  <style type="text/css">
  tbody > tr:nth-child(odd) { background-color: #DFFFCF; }
  .odd_row { background-color: #DFFFCF; }
  .xmlist .male { background-color: #CDE; text-align: center; }
  .xmlist .female { background-color: #EDC; text-align: center; }
  .xmlist a { text-decoration: none; color: darkblue; }
  th.sortable { cursor: pointer; }
  th.sorted_d:after { content: " ▾"; color: darkgreen; }
  th.sorted_u:after { content: " ▴"; color: darkgreen; }
  p.stats_closed:before { content: "▸ "; }
  p.stats_opened:before { content: "▾ "; }
  </style>
  <script type="text/javascript"><![CDATA[
""" + jquery + """
  ]]>
  </script>
  <script type="text/javascript"><![CDATA[
    function obj_items(dict) {
      var items = [];
      for (key in dict)
        items.push([key, dict[key]]);
      return items;
    }
    function xmlescape(str) {
      var dict = {"&":"&amp;", "<":"&lt;", ">":"&gt;"};
      return str.replace(/&|<|>/g, function(m) { return dict[m] });
    }
    function cmp_ascending(a, b)  { return (a < b) ? -1 : a != b; }
    function cmp_descending(a, b) { return (a > b) ? -1 : a != b; }
    function sort_column(tbody, th, order) {
      var column_nr = $("th", th.parentNode).index(th);
      var rows = $(">tr", tbody).get();
      order = order ? 1 : -1;
      function cmp(a, b) {
        a = a.childNodes[column_nr].textContent.toLowerCase();
        b = b.childNodes[column_nr].textContent.toLowerCase();
        if (a == "") return 1;  // Sink to the bottom.
        if (b == "") return -1; // ditto
        if (!isNaN((tmp = Number(a)))) a = tmp;
        if (!isNaN((tmp = Number(b)))) b = tmp;
        return ((a < b) ? -1 : a != b) * order;
      }
      rows.sort(cmp);
      $(tbody).append(rows);
    }
    function handle_title_click(e) {
      var this_ = $(this);
      var thead = this.parentNode.parentNode, tbody = $(thead).next()[0];
      if (this_.hasClass("sorted"))
        this_.toggleClass("sorted_u").toggleClass("sorted_d");
      else
        this_.siblings().add(this).removeClass("sorted sorted_u sorted_d"),
        this_.addClass("sorted sorted_d");
      sort_column(tbody, this, this_.hasClass("sorted_u"));
      if (!window.opera)
        $(">tr", tbody).each(function(i, tag) {
          if (i % 2 == 0) $(tag).addClass("odd_row");
          else $(tag).removeClass("odd_row");
        });
    }
    function add_class_odd_rows(tbody) {
      if (!window.opera)
        $(">tr:nth-child(odd)", tbody).addClass("odd_row");
    }
    // Executed when the document is ready.
    $(function() {
      var xmlist = $(".xmlist");
      var rows = xmlist[0].getElementsByTagName("tr");
      for (var i = 1, len = rows.length; i < len; i++)
      {
        var row = rows[i];
        var first_td = row.childNodes[0], second_td = row.childNodes[1];
        if (second_td.textContent == "♂")
          second_td.className = "male";
        if (second_td.textContent == "♀")
          second_td.className = "female";
        if (!window.opera) {
          if (i % 2 == 0) row.className = "odd_row";
          first_td.className = "username";
        }
      }
      // Add sorting functionality.
      var th_s = $("tr:first th", xmlist);
      th_s.addClass("sortable").click(handle_title_click);
      // Statistics:
      var parag = $("<p class='stats_closed'><a href='#stats'>Statistics</a></p>");
      xmlist.before(parag);
      $("a", parag).click(function(e) {
        e.preventDefault();
        parag.toggleClass("stats_opened").toggleClass("stats_closed");
        if (parag.hasClass("stats_closed"))
          return parag.table.hide();
        if (parag.table)
          return parag.table.show();

        function make_thead(t1, t2) { return "<thead><tr><th>"+t1+"</th><th>"+t2+"</th></tr></thead>"; }
        function make_rows(tbody, items) {
          for (var i = 0, len = items.length; i < len; i++)
            tbody.append("<tr><td>"+xmlescape(items[i][0])+"</td><td>"+items[i][1]+"</td></tr>");
        }
        function count(i, elem) {
          var c = count.dict[elem.textContent];
          c = c ? c + 1 : 1;
          count.dict[elem.textContent] = c;
        }
        function cmp_items(a, b) { return cmp_ascending(a[0].toLowerCase(), b[0].toLowerCase()) }

        var columns = [[2, "Gender"], [3, "Country"], [4, "Current Views"]];
        var table = $("<table class='stats_table'/>"), thead, tbody, items;
        parag.after(table);
        parag.table = table;
        for (var i = 0; i < 3; i++)
        {
          var column = columns[i][0], title = columns[i][1];
          rows = $("td:nth-child("+column+")", xmlist);
          count.dict = {}
          rows.each(count);
          if (rows.length == 0)
            continue;
          items = obj_items(count.dict);
          items.sort(cmp_items);
          if (items[0][0] == "")
            items[0][0] = "N/A";
          thead = $(make_thead(title, "Count"));
          $("th", thead).addClass("sortable").click(handle_title_click);
          table.append(thead).append(tbody = $("<tbody/>"));
          make_rows(tbody, items);
          add_class_odd_rows(tbody);
        }
      });
    });
  ]]>
  </script>
</head>
<body>
<p>This is a list of former Muslims on <a href="http://www.councilofexmuslims.com">councilofexmuslims.com</a>:</p>
<table class="xmlist">
<thead>
<tr><th>Nick</th><th>Gender</th><th>Country</th><th>Current views</th><th>Top 3 reasons for leaving Islam</th></tr>
</thead>
<tbody>"""

xhtml = open("COEM_ex-Muslims.xhtml", "w")
xhtml.write(head)

for u in users:
  reasons = ", ".join(['<span class="reason">%s</span>' % r for r in u[5]])
  link = '<a href="http://www.councilofexmuslims.com/index.php?action=profile;u='+str(u[0])+'">'+u[1]+"</a>"
  row = dict(id=u[0], name=u[1], link=link, gndr=u[2], cntry=u[3], views=u[4], reasons=reasons)
  xhtml.write(('<tr id="%(id)s"><td>%(link)s</td><td>%(gndr)s</td><td>%(cntry)s</td><td>%(views)s</td><td>%(reasons)s</td></tr>\n' % row))#.encode("utf-8"))

xhtml.write("</tbody>\n</table>\n</body>\n</html>")
