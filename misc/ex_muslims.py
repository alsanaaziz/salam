#!/usr/bin/env python
# -*- coding: utf-8 -*-

users = [
  (658, "[C*]", "♂", "UK", "Atheist", ()),
  (1108, "_truth_", "♂", "USA", "Atheist", (), "Was raised as a Sunni Salafi"),
  (558, "a.ghazali", "♂", "USA", "", ()),
  #(359, "A_G", "♂", "", "", ()), # Got banned.
  (925, "Aa", "♂", "Bangladesh", "Atheist", (), "Reading COEM helped him to apostatize"),
  (1068, "AbbasMerali", "♂", "UK", "Atheist", (), '<a href="http://www.councilofexmuslims.com/index.php?topic=7495">His story</a>'),
  (469, "abdalwali", "♂", "USA", "", ()),
  (887, "abuk", "♂", "UK", "", ()),
  (289, "afghan_exmuslim", "♂", "Afghanistan", "", ()),
  (884, "AisaLagtaHAI", "♂", "Canada", "Agnostic", ()),
  (975, "aj566", "♂", "UK", "Atheist", ()),
  (370, "Al Razi", "♂", "UK", "Atheist", (), "Occasionally writes funny, Arabic revelations"),
  (668, "al-uzza", "♀", "", "", ()),
  (657, "aliadiere", "♂", "UK", "Agnostic", ()),
  (1023, "Ali Marwa", "♂", "", "Christian", ()),
  (56, "All_Brains", "♂", "", "Atheist", (), "Psychologist"),
  (416, "allat", "♀", "Canada", "Atheist", ("Lack of women's rights & LGBT rights in Islam", 'Muhammad\'s bad character as an "infallible prophet"', "the ruthless, sadistic, invisible Allah"), "⚢⚤; Atheist-Pantheist to be exact"),
  (684, "AlmostAisha", "♀", "Canada", "Atheist", (), "Ex-Convert"),
  (815, "Alprh", "♂", "Iran", "Atheist", ()),
  (790, "Angel54", "♀", "Canada", "Agnostic", (), "Agnostic deist"), # Guessed gender.
  (169, "Anisah", "♀", "USA", "Agnostic", (), 'Muslim Convert for 12 years, now Agnostic Unitarian<br/><a href="http://notmuslimanymore.blogspot.com">Her Blog</a>'),
  (930, "arabie", "♂", "Netherlands", "", ()),
  (747, "atheist.pk", "♂", "Pakistan", "Atheist", ()),
  (564, "automan", "♂", "", "", ()),
  (342, "awais", "♂", "USA", "Spiritual Agnostic", ("Etymology",)),
  (462, "Ayaz", "♂", "Pakistan", "Atheist", ()),
  (9, "Aziz", "♂", "Austria", "Atheist", ("Hell", "slavery", "4:34"), '<a href="http://www.youtube.com/user/AlsanaAziz">YouTube channel</a>'),
  (686, "Balthier", "♂", "", "", ()),
  (1163, "Barayev", "♂", "Singapore", "", ()),
  (613, "belladonnasix", "♀", "Canada", "Pantheist", ()),
  (6, "BerberElla", "♀", "UK", "Atheist", (), "Our Great Goddess and one of the founders of the forum"),
  (1224, "BeyT", "♀", "UAE", "", (), "Wavering Muslim"),
  (1110, "BlackDog", "♂", "Canada", "Pantheist", (), "Was a Shia-Muslim; speaks Arabic; raised in Europe"),
  (970, "Bobonaut", "♂", "USA", "Atheist", (), "Apostatized because of good, atheist YouTube videos"),
  (1189, "canex", "♂", "Canada", "", ()),
  (180, "carolineislands", "♀", "USA", "", (), "Converted but flip-flopped shortly after"),
  (187, "Charles", "♂", "Australia", "", ()),
  (79, "cherry", "♀", "UK", "", ()),
  (552, "chickpea", "♀", "USA", "", (), '<a href="http://chickpealove.com/blog/">Blog</a>'), # Has no postings. Guessed her being an ex-Muslim from her blog.
  (839, "Cliodna", "♀", "India", "", ()),
  (555, "Cool Canadian", "♂", "Canada", "", (), "Ex-Convert"),
  (615, "coolred38", "♀", "", "", (), "Ex-Convert"),
  (733, "crueljewel", "♀", "", "", ()),
  (851, "cwar068", "♂", "Australia", "Atheist", (), '<a href="http://charleswardle.com/">His website</a>; <a href="http://www.youtube.com/user/cwar068">YouTube Channel</a>'),
  #(1186, "Dain Bramaged", "♂", "", "Atheist", ()), # Double account for his anonymous autobiography.
  (850, "darkone", "♂", "UK", "Agnostic", ()),
  (842, "Diem", "♀", "Canada", "", ()),
  (345, "DivineMercy", "♀", "USA", "Christian", ()),
  (346, "Dr Diavolo", "♂", "UK", "Atheist", (), "Real Doctor"),
  #(1161, "Eazy", "♂", "Egypt", "", ()), # Wavering Muslim.
  (510, "Eddy", "♂", "Turkey", "", ()),
  (255, "Emerald", "♂", "Saudi Arabia", "Spiritual Agnostic", ("Women's rights", "Jihad", "negative effects of Islam on Muslims")),
  (1002, "Ennis", "♂", "USA", "Agnostic", ()),
  (1028, "ExKimDonesia", "♂", "Australia", "Agnostic", (), 'She was a little Internet celebrity as a convert to Islam; "<a href="http://www.councilofexmuslims.com/index.php?topic=7423">Famous Muslim to infamous Murtad</a>"; <a href="http://my.muxlim.com/kimdonesia/">Her Muslim website</a>; <a href="http://www.youtube.com/user/ExKimDonesia">Her YouTube channel</a>'),
  (1107, "ExMuslimGirl8", "♀", "", "", ()),
  (1139, "Eyad", "♂", "UK", "Atheist", ()),
  (785, "Farid92", "♂", "Netherlands", "Deist", ()),
  (1087, "Farhad", "♂", "USA", "", ()),
  (756, "Ferrero", "♀", "UK", "", ()),
  (725, "freakzilla", "♂", "UK", "Skeptic", ()),
  (1155, "Gallasadeq", "♂", "Kuwait", "Atheist", (), "Ex-Shia"),
  (980, "Godot", "♂", "", "", (), "Wasn't really devout, but took faith seriously."),
  (397, "Goldie", "♂", "UK", "", (), "Apostatized in our forum; ⚣"),
  (150, "green_eyes", "♀", "UK", "Atheist", ()),
  (909, "Hadugh", "♂", "UK", "Atheist", ()),
  (219, "Haji Murad", "♂", "", "", ()),
  (8, "Hassan", "♂", "UK", "Deist", ("Hell", "slavery", "4:34"), 'Former teacher at an Islamic school; studied Arabic; <a href="http://www.youtube.com/user/discussislam">YouTube channel</a>'),
  (1024, "Haroun", "♂", "USA", "Atheist", (), "Ex-Salafi"),
  (383, "Hedaya", "♀", "", "Agnostic", ()),
  (638, "HenriMonier", "♂", "UK", "Atheist", ("Ideology", "fallacies", "barbaric practices")),
  (561, "henrypage", "♂", "UK", "Atheist", ("Muslim reactions to 9/11",)),
  (935, "Heyjustlooking", "♂", "UK", "Agnostic", (), "Came as an open-minded, doubting Muslim, apostatized later on"),
  (898, "HighOctane", "♂", "UK", "Atheist", ()),
  (717, "Homer", "♂", "", "", ()),
  (918, "Human", "♀", "Bangladesh", "", ()),
  (114, "Humanoid", "♂", "UK", "Apatheist", ()),
  (826, "humblesoul", "♂", "Nigeria", "Deist", (), "Apostatized in our forum; Considers himself an agnostic deist"),
  (409, "BluLox", "♀", "", "", ()),
  (80, "ibnishaq", "♂", "", "", (), "Apostatized in our forum"),
  (594, "identitas", "♂", "UK", "Agnostic", ()),
  (77, "Iggy", "♀", "Canada", "Ignostic", ()),
  (724, "indiana", "♂", "", "", ()),
  (936, "Infidel", "♂", "UK", "Agnostic", ()),
  (453, "InfidelAussieLeb", "♂", "Australia", "", ()),
  (917, "insiaiftiqhar", "♂", "USA", "", ()),
  (1141, "Iraqi Atheist", "♂", "UK", "Atheist", (), "Fled Iraq because of the war and settled in the UK; became atheist thanks to the popular ('new') atheists"),
  (141, "Iris", "♀", "UK", "", ()),
  (194, "Isaac Schrodinger", "♂", "Canada", "", ()),
  (574, "IsLame", "♂", "UK", "Humanist", ("God's invisibility and cruelty", "existence of polytheism", "net effect of the Qur'an on Muslims"), '<a href="http://www.youtube.com/user/ExMuslimUK">YouTube channel</a>'),
  (1111, "iThink", "♂", "Syria", "Atheist", ()),
  (336, "ItStartedInCollege", "♂", "USA", "", ()),
  (738, "J4m3z", "♂", "UK", "", ()),
  (26, "Jack Torrance", "♂", "UK", "Anti-Labelist", ()),
  (727, "jamshed raja", "♂", "UK", "Atheist", ()),
  (969, "Kafir-Supersta", "♂", "UK", "", ()),
  (1082, "Kafirist", "♂", "Canada", "Atheist", (), "Born to Bengali family; was a devout Muslim, now atheist/agnostic"),
  (819, "khalid saeed", "♂", "Pakistan", "", (), "His brother is also an ex-Muslim, humanist atheist"),
  (641, "KhalilF", "♂", "", "", ()),
  (93, "Kid A", "♂", "UK", "", ()),
  (317, "KraziKuri", "♀", "UK", "", ()),
  (153, "KunstInFlammen", "♂", "UK", "Agnostic", ()),
  (381, "ladyofshalott", "♀", "UK", "Atheist", ()),
  (16, "li", "♂", "Singapore", "Atheist", ()),
  (1126, "liberated", "♂", "Pakistan", "Agnostic", ()),
  (197, "Maghrebi", "♂", "Morocco", "", ()),
  (854, "Malik", "♂", "UK", "Atheist", ()),
  (450, "Manat", "♀", "", "", ()),
  (557, "mangostan", "", "", "", ()), # Registered long time ago. First posting 28.9.2009.
  (1057, "MangoStar", "♂", "USA", "", (), "Raised Southern Baptist. Converted when she was 17, apostatized when she was 18."), # Guessed country.
  (32, "Marmalade-Lady", "♀", "UK", "", ()),
  (11, "Maryam Namazie", "♀", "UK", "Atheist", (), "Head of the Council of Ex-Muslims of Britain"),
  (1194, "mateen", "♂", "Pakistan", "", ()),
  (960, "mattb", "♂", "", "", ()),
  (760, "Meredith", "♀", "UK", "", ()),
  (325, "Mia Bella", "♀", "Canada", "", ()),
  (1255, "MoeAlharbi", "♂", "Canada", "Atheist", ()),
  (1131, "Mowgli", "♂", "UK", "", (), "⚣"),
  (1235, "Mughal", "♂", "UK", "", ()),
  (1243, "mujahid", "♀", "UK", "", (), '<a href="http://www.councilofexmuslims.com/index.php?topic=8959">Her introduction</a>'),
  (1188, "Naerys", "♀", "North-Africa", "", ()),
  (710, "ned", "♀", "Pakistan", "Panentheist", (), '"Strictly speaking, I\'m a non-religious, neo-Vedantist, panentheistic mystic."'),
  (712, "Nite Owllll", "♂", "USA", "Atheist", ()),
  (623, "Nizar", "♂", "Sweden", "Agnostic", ()),
  (880, "nothingthere", "♂", "", "Atheist", ()), # Guessed the gender.
  (430, "Nour", "♀", "UK", "Agnostic", ()),
  #(846, "Nuppar", "", "", "", ()), # Probably ex-Muslim.
  (787, "Omaar Khayaam", "♂", "UK", "Atheist", (), "Apostatized after struggling with doubts for many years"),
  (868, "omarinbox", "♂", "UK", "Atheist", (), 'When still a Muslim, he was addressed in a "<a href="http://tariqali.org/ExtractClashLetter.html">Letter To A Young Muslim</a>" by <a href="http://en.wikipedia.org/wiki/Tariq_Ali">Tariq Ali</a>'),
  (786, "onlyme", "♂", "UK", "", ()),
  (414, "open_thinking", "♂", "UK", "", ()),
  (408, "Orion", "♂", "", "", ()),
  (260, "pakman", "♂", "", "", ()), # UK?
  (249, "panoptic", "♂", "UK", "Atheist", ()),
  (734, "Pariah", "♀", "UK", "Agnostic", ()), # Guessed beliefs.
  (160, "Pazuzu", "♂", "UK", "Atheist", ()),
  (554, "PeruvianSkies", "♀", "UK", "Atheist", ()),
  (870, "Prosaic", "♀", "Egypt", "Atheist", (), "Came as a wavering Muslim to the forum"),
  (1043, "Psychologist", "♂", "UK", "", (), "Invited ex-Muslims to an interview for a psychological study at the University of Westminster"),
  (1135, "pure.virtual", "♂", "Palestine", "Atheist", ()),
  (121, "quratulain", "♂", "Pakistan", "Atheist", ()),
  (1012, "Rubaiyat", "♂", "", "Atheist", ()),
  (757, "Ramadulla", "♂", "UK", "", ()),
  (715, "Raqsi", "♀", "", "", ()),
  (215, "Rational1", "♀", "USA", "Atheist", ()),
  (919, "reemz83", "♀", "Canada", "", ()),
  (31, "Reza Moradi", "♂", "UK", "Atheist", ()),
  (735, "RIBS", "♂", "", "Atheist", ()),
  (592, "rooblee", "♂", "", "", ()),
  (57, "Rubina", "♀", "", "", ()),
  (616, "Saima", "♀", "", "", ()),
  (920, "Saina.k", "♀", "Syria", "", ()),
  (628, "SalahuddinR", "♂", "USA", "Atheist", ()),
  (855, "Sameer", "♂", "India", "Atheist", ()),
  (435, "sbmuse", "♂", "", "", (), "Ex-Convert; was/is friends with Hamza Yusuf, Nuh Ha Mim Keller, Suhaib Webb..."),
  (1250, "scousepk", "♂", "UK", "", ()),
  #(1147, "SeekTruth", "♂", "USA", "", ()), #Pretty much an ex-Muslim (soon).
  (966, "shaft4038", "♂", "USA", "Atheist", ()),
  (65, "Shahid Raza", "♂", "UK", "Deist", ()),
  (675, "Shahzad", "♂", "", "Panentheist", ()),
  (831, "sharkheart", "♂", "UK", "Atheist", ()),
  (1201, "Shirdon", "♂", "UK", "Atheist", (), "⚣⚤"),
  (1174, "sku", "♀", "UK", "Atheist", ()),
  (944, "smudge59", "♂", "UK", "", ()),
  (1027, "smy890", "♂", "UAE", "", ()),
  (3, "Spasm", "♀", "", "", ()),
  (495, "spiral dive", "♀", "UK", "Atheist", ()),
  (544, "stardust", "♀", "", "Deist", ()),
  (369, "Starnexus", "♂", "", "Atheist", ()),
  (1137, "SojournerTruth", "♀", "Netherlands", "Agnostic", ()),
  (926, "stranger", "♂", "UK", "", ()),
  (1173, "taraC", "♂", "Pakistan", "", ()),
  (1214, "the_revivor", "♂", "Australia", "Atheist", ()),
  (562, "Tommy", "♂", "USA", "Atheist", ()),
  (244, "Uppercut", "♂", "UK", "Humanist", ()),
  (485, "whatabastor", "♂", "Saudi Arabia", "", ()),
  (19, "Witzbold", "♂", "Pakistan", "Atheist", ()),
  (924, "youcansee", "♀", "UK", "Atheist", ()),
  (1138, "z10", "♂", "UK", "Atheist", (), "Was raised in a British Pakistani home with Muslim values"),
  (42, "Zaephon", "♂", "Turkey", "Atheist", ()),
  (888, "ZBS", "♂", "USA", "Atheist", ()),
  (58, "ZiaZ", "♂", "UK", "Humanist", ()),
  (913, "Zuber", "♂", "New Zealand", "Atheist", ()),
]


def get_xhtml_head(copy_jquery=False):
  from datetime import datetime
  date = datetime.utcnow().strftime("%A, %d. %B %Y")

  if copy_jquery:
    from os import path as path
    jquery = open(path.join(path.dirname(path.dirname(__file__)), "js", "jquery.js")).read()
    jquery = '<script type="text/javascript">//<![CDATA[\n' + jquery + '\n//]]>\n</script>'
  else:
    jquery = '<script type="text/javascript" src="http://code.jquery.com/jquery-1.4.1.min.js"></script>'

  head = (r"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
  <title>List of ex-Muslims</title>
  <style type="text/css">
  tbody > tr:nth-child(odd) { background-color: HoneyDew; }
  .xmlist .male { background-color: #CDE; text-align: center; }
  .xmlist .female { background-color: #EDC; text-align: center; }
  .xmlist a { text-decoration: none; color: darkblue; }
  th.sortable { cursor: pointer; }
  th.sorted_d:after { content: " ▾"; color: darkgreen; }
  th.sorted_u:after { content: " ▴"; color: darkgreen; }
  p.stats_closed:before { content: "▸ "; }
  p.stats_opened:before { content: "▾ "; }
  </style>
  """ + jquery + """
  <script type="text/javascript">//<![CDATA[
    function obj_items(dict) {
      var items = [];
      for (key in dict)
        items.push([key, dict[key]]);
      return items;
    }
    function xmlescape(str) {
      var dict = {"&":"&amp;", "<":"&lt;", ">":"&gt;"};
      return str.replace(/[&<>]/g, function(m) { return dict[m] });
    }
    function cmp_ascending(a, b)  { return (a < b) ? -1 : a != b; }
    function cmp_descending(a, b) { return (a > b) ? -1 : a != b; }
    function sort_column(tbody, th, order) {
      var column_nr = $("th", th.parentNode).index(th);
      var rows = $(">tr", tbody).get();
      order = order ? 1 : -1;
"""
#      function convert_numbers(list) {
#        for (var i=0, len=list.length; i < len; i++)
#          //if ((x = list[i].charCodeAt(0) - 48) >= 0 && x < 10); // '0'.charCodeAt(0) == 48
#          if (!isNaN(x = Number(list[i])))
#            list[i] = x;
#        return list;
#      }
"""      function cmp(a, b) {
        a = a.childNodes[column_nr].textContent.toLowerCase();
        b = b.childNodes[column_nr].textContent.toLowerCase();
        if (a == "") return 1;  // Sink to the bottom.
        if (b == "") return -1; // ditto
        if (!isNaN((tmp = Number(a)))) a = tmp;
        if (!isNaN((tmp = Number(b)))) b = tmp;
"""
#        /*if (/\d/.test(a) || /\d/.test(b)) {
#          // TRY: Handle alphanumerical strings by comparing their parts.
#          a = convert_numbers(a.match(/\d+|[^\d]+/g));
#          b = convert_numbers(b.match(/\d+|[^\d]+/g));
#        }*/
"""        return ((a < b) ? -1 : a != b) * order;
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
    }
    // Executed when the document is ready.
    $(function main() {
      var xmlist = $(".xmlist");
      var rows = xmlist[0].getElementsByTagName("tr"),
          m_or_f = ["male", "female"];
      for (var i = 1, len = rows.length; i < len; i++)
      {
        var second_td = rows[i].childNodes[1];
        second_td.className = m_or_f["♂♀".indexOf(second_td.textContent)];
      }
      // Add sorting functionality.
      var th_s = $("tr:first th", xmlist);
      th_s.addClass("sortable").click(handle_title_click);
      // Statistics:
      var parag = $("<p class='stats_closed'><a href='#stats'>Statistics</a></p>");
      xmlist.before(parag);
      $("a", parag).click(function(){showStatistics(parag)});
      if (/#stats$/.test(document.location.href))
        showStatistics(parag);
    });
    function showStatistics(parag)
    {
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
        rows = $(".xmlist td:nth-child("+column+")");
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
      }
    }
  //]]>
  </script>
</head>
<body>
<p>This is a list of former Muslims registered at <a href="http://www.councilofexmuslims.com">councilofexmuslims.com</a> (last updated: """ + date + """):</p>
<table class="xmlist">
<thead>
<tr><th>Nick</th><th>Gender</th><th>Country</th><th>Current views</th><th>Top 3 reasons for leaving Islam</th><th>Annotations</th></tr>
</thead>
<tbody>""")
  return head

def print_BBC():
  print "[table]"
  print "[tr][td][b]%s[/b][/td][/tr]" % "Nick;Gender;Country;Belief".replace(";", "[/b][/td][td][b]")
  for u in users:
    print "[tr][td][b][url=/index.php?action=profile;u=%d]%s[/url][/b][/td][td]%s[/td][td]%s[/td][td]%s[/td][/tr]" % (u[0], u[1], u[2], u[3], u[4])

  print "[/table]"
  class Table(dict):
    def inc(self, item):
      if item not in self:
        self[item] = 0
      self[item] += 1

  gender_table = Table()
  country_table = Table()
  belief_table = Table()
  for u in users:
    gender_table.inc(u[2])
    country_table.inc(u[3])
    belief_table.inc(u[4])
  print "[table]"
  for table, title in [(gender_table, "Gender"), (country_table, "Country"), (belief_table, "Belief")]:
    print "[tr][td][b]%s[/b][/td][td][b]Count[/b][/td][/tr]" % title
    keys = table.keys()
    keys.sort()
    if keys[0] == "":
      keys[0] = "N/A"
      table["N/A"] = table[""]
    for key in keys:
      print "[tr][td]%s[/td][td]%d[/td][/tr]" % (key, table[key])
  print "[/table]"

def print_Wiki():
  """ Prints the list in wiki markup. """
  #TODO:
  pass

def escape(s):
  return s.replace("&", "&amp;")

def main():
  #print_BBC()
  #return
  head = get_xhtml_head()
  xhtml = open("COEM_ex-Muslims.xhtml", "w")
  xhtml.write(head)

  # Check for correct alphabetic order.
  #names = [u[1] for u in users]
  #names_ = names[:]
  #names.sort(lambda a, b: cmp(a.lower(), b.lower()))
  #assert names == names_
  #for n1, n2 in zip(names, names_):
    #print n1, n2

  for u in users:
    annot = u[6] if len(u) >= 7 else ""
    reasons = "<b>;</b> ".join(['<span class="reason">%s</span>' % escape(r) for r in u[5]])
    link = '<a href="http://www.councilofexmuslims.com/index.php?action=profile;u='+str(u[0])+'">'+u[1]+"</a>"
    row = dict(id=u[0], name=u[1], link=link, gndr=u[2], cntry=u[3],
      views=escape(u[4]), reasons=reasons, annot=annot)
    xhtml.write(('<tr id="u%(id)s"><td>%(link)s</td><td>%(gndr)s</td>'
      '<td>%(cntry)s</td><td>%(views)s</td><td>%(reasons)s</td><td>%(annot)s</td></tr>\n') % row)
      #.encode("utf-8"))

  xhtml.write("</tbody>\n</table>\n</body>\n</html>")

if __name__ == '__main__':
  main()
