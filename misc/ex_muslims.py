#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Format: (UserID, NickName, Gender, Location, Belief, ("Three", "Reasons", "ForApostasy"), OptionalAnnotation)
users = [
  # (2671, "LondonGirl", "♀", "UK", "", ()), # Doubting.
  (1470, "noallah", "♂", "UK", "Atheist", (), "⚤⚣"),
  (2648, "muddy", "♂", "Canada", "", ("Muslims bash gays", "Quran has many contradictions among different verses. I have always questioned them.", "Islam is very anti women")),
  (2649, "Zeeman", "♂", "Canada", "", ()),
  (2491, "Sameh", "♂", "UK", "Agnostic", ("Lack of evidence", "eternal punishment", "immoral teachings")),
  (2693, "infidelicious", "♂", "", "", ()),
  (2743, "musivore", "♂", "UK", "", ()),
  (2901, "Madig", "♂", "UK", "Atheist", ()),
  (2328, "Damian_Gray", "♂", "UK", "Atheist", ("Because it is a hateful religion which worships the waste of sperm that is Mohammed", "It's incompatible with science", "Has barbaric punishments for miniscule things that it considers sins.")),
  (2784, "Kafir", "♂", "Norway", "", ()),
  (2811, "Planetlestar", "♂", "Algeria", "", ()),
  (2973, "Mount A Bison", "♂", "UK", "", ()),
  (2375, "armanduk2010", "♂", "UK", "Christian", ()),
  (2975, "Lukatic", "♀", "Malaysia", "", ()),
  # Users below are sorted alphabetically:
  (658, "[C*]", "♂", "UK", "Atheist", ()),
  (1108, "_truth_", "♂", "USA", "Atheist", (), "Was raised as a Sunni Salafi"),
  (558, "a.ghazali", "♂", "UK", "Atheist", ()),
  #(359, "A_G", "♂", "", "", ()), # Got banned.
  (925, "Aa", "♂", "Bangladesh", "Atheist", (), "Reading COEM helped him to apostatize"),
  (1068, "AbbasMerali", "♂", "UK", "Atheist", (), '<a href="http://www.councilofexmuslims.com/index.php?topic=7495">His story</a>'),
  (469, "abdalwali", "♂", "USA", "", ()),
  (1300, "Abood", "♂", "Canada", "Atheist", ("Incompatibility with science",)),
  (887, "abuk", "♂", "UK", "", ()),
  (1558, "abz", "♂", "Australia", "", ()),
  (289, "afghan_exmuslim", "♂", "Afghanistan", "", ()),
  (884, "AisaLagtaHAI", "♂", "Canada", "Agnostic", ()),
  (975, "aj566", "♂", "UK", "Atheist", ()),
  (370, "Al Razi", "♂", "UK", "Atheist", (), "Occasionally writes funny, Arabic revelations"),
  (2101, "Al-Razi", "♂", "Egypt", "", ()),
  (668, "al-uzza", "♀", "", "", ()),
  (1825, "algebra", "", "Canada", "Theist", ()),
  (1023, "Ali Marwa", "♂", "", "Christian", ()),
  (657, "aliadiere", "♂", "UK", "Agnostic", ()),
  (56, "All_Brains", "♂", "", "Atheist", (), "Psychologist"),
  (416, "allat", "♀", "Canada", "Atheist", ("Lack of women's rights & LGBT rights in Islam", 'Muhammad\'s bad character as an "infallible prophet"', "the ruthless, sadistic, invisible Allah"), "⚢⚤; Atheist-Pantheist to be exact"),
  (684, "AlmostAisha", "♀", "Canada", "Atheist", (), "Ex-Convert"),
  (815, "Alprh", "♂", "Iran", "Atheist", ()),
  (790, "Angel54", "♀", "Canada", "Agnostic", (), "Agnostic deist"), # Guessed gender.
  (169, "Anisah", "♀", "USA", "Agnostic", (), 'Muslim Convert for 12 years, now Agnostic Unitarian<br/><a href="http://notmuslimanymore.blogspot.com">Her Blog</a>'),
  (930, "arabie", "♂", "Netherlands", "", ()),
  (1376, "ateapotist", "♂", "UK", "Atheist", ("Incompatible with science", "anti-freedom", "barbaric punishments under Sharia"), '<a href="http://www.councilofexmuslims.com/index.php?topic=9976">His intro</a>'),
  (747, "atheist.pk", "♂", "Pakistan", "Atheist", ()),
  (1356, "Aurora", "♀", "Saudi Arabia", "Atheist", ()),
  (1302, "ausath", "♀", "Australia", "", ()),
  (1025, "aussieexmuslim", "", "Australia", "", ()),
  (564, "automan", "♂", "", "", ()),
  (342, "awais", "♂", "USA", "Spiritual Agnostic", ("Etymology",)),
  (462, "Ayaz", "♂", "Pakistan", "Atheist", ()),
  (1061, "azgyl", "♂", "Austria", "Atheist", ()),
  (9, "Aziz", "♂", "Austria", "Atheist", ("Hell", "slavery", "4:34"), '<a href="http://www.youtube.com/user/AlsanaAziz">YouTube channel</a>'),
  (686, "Balthier", "♂", "", "", ()),
  (1163, "Barayev", "♂", "Singapore", "", ()),
  (613, "belladonnasix", "♀", "Canada", "Pantheist", ()),
  (6, "BerberElla", "♀", "UK", "Atheist", (), "Our Great Goddess and one of the founders of the forum"),
  (1224, "BeyT", "♀", "UAE", "Sceptic", ("lack of women's rights", "incompatibility with science and reason", "penalty for apostasy")),
  (1110, "BlackDog", "♂", "Canada", "Pantheist", (), "Was a Shia-Muslim; speaks Arabic; raised in Europe"),
  (409, "BluLox", "♀", "", "", ()),
  (970, "Bobonaut", "♂", "USA", "Atheist", (), "Apostatized because of good, atheist YouTube videos"),
  (1467, "brummie", "♂", "UK", "", (), "ex-Shia"),
  (1944, "burdenofbeing", "♂", "Turkey", "Atheist", ("The notion that the god of the reality we live in puts blind faith over anything else, in spite of the rest of its creation", "The notion that humans are being tested, when the rules and the aspect of the test is so vague and nonsensical", "The impossibility of the proposed god, based on the contradicting nature of its specifications")),
  (1274, "CahitKaya", "♂", "Austria", "Atheist", (), 'Head of the Austrian Council of Ex-Muslims; <a href="http://www.facebook.com/kayacahit">Facebook</a>'),
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
  (1553, "Dreamer", "♀", "USA", "Agnostic", (), "Convert Muslimah for 1 1/2 years."),
  #(1161, "Eazy", "♂", "Egypt", "", ()), # Wavering Muslim.
  (510, "Eddy", "♂", "Turkey", "", ()),
  (1370, "Eliphaz", "♂", "", "", ()),
  (255, "Emerald", "♂", "Saudi Arabia", "Spiritual Agnostic", ("Women's rights", "Jihad", "negative effects of Islam on Muslims")),
  (1002, "Ennis", "♂", "USA", "Agnostic", ()),
  (1369, "Ephemeral", "♀", "Canada", "Atheist", ()),
  (1028, "ExKimDonesia", "♀", "Australia", "Agnostic", (), 'She was a little Internet celebrity as a convert to Islam; "<a href="http://www.councilofexmuslims.com/index.php?topic=7423">Famous Muslim to infamous Murtad</a>"; <a href="http://my.muxlim.com/kimdonesia/">Her Muslim website</a>; <a href="http://www.youtube.com/user/ExKimDonesia">Her YouTube channel</a>'),
  (1442, "exmuslimenoc", "♂", "India", "", ()),
  (1107, "ExMuslimGirl8", "♀", "", "", ()),
  (1139, "Eyad", "♂", "UK", "Atheist", ()),
  (1087, "Farhad", "♂", "USA", "", ()),
  (785, "Farid92", "♂", "Netherlands", "Deist", ()),
  (756, "Ferrero", "♀", "UK", "", ()),
  (725, "freakzilla", "♂", "UK", "Sceptic", ()),
  (1987, "GAIMANPALMERR", "♀", "UK", "Agnostic", ()),
  (1155, "Gallasadeq", "♂", "Kuwait", "Atheist", (), "Ex-Shia"),
  (1807, "GodIsNotGreat", "♂", "UK", "Atheist", ()),
  (980, "Godot", "♂", "UK", "Atheist", ("Violent punishments", "slavery", "gender inequality"), "Wasn't really devout, but took faith seriously. Strong existentialist, and a secular humanist."),
  (397, "Goldie", "♂", "UK", "", (), "Apostatized in our forum; ⚣"),
  (150, "green_eyes", "♀", "UK", "Atheist", ()),
  (2426, "grudgydiablo", "♂", "UK", "", ()),
  (909, "Hadugh", "♂", "UK", "Atheist", ()),
  (1582, "hafiz", "♂", "India", "Agnostic", ()),
  (219, "Haji Murad", "♂", "", "", ()),
  (1575, "Hanan_x3", "♀", "USA", "Agnostic Theist", ()),
  (1494, "Haroon", "♂", "Pakistan", "Atheist", ()),
  (1024, "Haroun", "♂", "USA", "Atheist", (), "Ex-Salafi"),
  (8, "Hassan", "♂", "UK", "Agnostic", ("Hell", "slavery", "4:34"), 'Former teacher at an Islamic school; studied Arabic; <a href="http://www.youtube.com/user/discussislam">YouTube channel</a>'),
  (383, "Hedaya", "♀", "", "Agnostic", ()),
  (638, "HenriMonier", "♂", "UK", "Atheist", ("Ideology", "fallacies", "barbaric practices")),
  (561, "henrypage", "♂", "UK", "Atheist", ("Muslim reactions to 9/11",)),
  (935, "Heyjustlooking", "♂", "UK", "Agnostic", (), "Came as an open-minded, doubting Muslim, apostatized later on"),
  (898, "HighOctane", "♂", "UK", "Atheist", ()),
  (918, "Human", "♀", "Bangladesh", "", ()),
  (114, "Humanoid", "♂", "UK", "Apatheist", ()),
  (826, "humblesoul", "♂", "Nigeria", "Sceptic", (), "Was a devout Sunni. Dawkins, YouTube atheists and COEM forum helped him become an apostate"),
  (1082, "Iblis", "♂", "Canada", "Atheist", (), "Born to Bengali family; was a devout Muslim, now atheist/agnostic"),
  (80, "ibnishaq", "♂", "USA", "", (), "Apostatized in our forum"),
  (594, "identitas", "♂", "UK", "Agnostic", ()),
  (77, "Iggy", "♀", "Canada", "Ignostic", ()),
  (724, "indiana", "♂", "", "", ()),
  (936, "Infidel", "♂", "UK", "Atheist", ()),
  (453, "InfidelAussieLeb", "♂", "Australia", "", ()),
  (917, "insiaiftiqhar", "♂", "USA", "", ()),
  (1141, "Iraqi Atheist", "♂", "UK", "Atheist", (), "Fled Iraq because of the war and settled in the UK; became atheist thanks to the popular ('new') atheists"),
  (141, "Iris", "♀", "UK", "", ()),
  (2452, "Irzyad", "♂", "Indonesia", "Atheist", ()),
  (194, "Isaac Schrodinger", "♂", "Canada", "", ()),
  (2366, "Ishina", "♀", "UK", "Atheist", ()),
  (574, "IsLame", "♂", "UK", "Humanist", ("God's invisibility and cruelty", "existence of polytheism", "net effect of the Qur'an on Muslims"), '<a href="http://www.youtube.com/user/ExMuslimUK">YouTube channel</a>'),
  (1111, "iThink", "♂", "Syria", "Atheist", ()),
  (336, "ItStartedInCollege", "♂", "USA", "", ()),
  (738, "J4m3z", "♂", "UK", "", ()),
  (26, "Jack Torrance", "♂", "UK", "Anti-Labelist", ()),
  (727, "jamshed raja", "♂", "UK", "Atheist", ()),
  (969, "Kafir-Supersta", "♂", "UK", "", ()),
  (1353, "Kansuke", "♂", "UK", "", ()),
  (1353, "kero-zen", "♂", "", "Humanist", ("Islam is immoral", "and illogical", "desire to be free to think for himself")),
  (819, "khalid saeed", "♂", "Pakistan", "", (), "His brother is also an ex-Muslim, humanist atheist"),
  #(641, "KhalilF", "♂", "", "", ()), # Same account as Haji Murad.
  (93, "Kid A", "♂", "UK", "", ()),
  (801, "kimo", "♂", "Egypt", "Atheist", (), '<a href="http://www.councilofexmuslims.com/index.php?topic=9798">His story</a>'),
  (1382, "Kod", "♂", "USA", "Atheist", ()),
  (317, "KraziKuri", "♀", "UK", "", ()),
  (153, "KunstInFlammen", "♂", "UK", "Agnostic", ()),
  (381, "ladyofshalott", "♀", "UK", "Atheist", ()),
  (634, "li", "♂", "Singapore", "Atheist", ()),
  (1126, "liberated", "♂", "Pakistan", "Agnostic", ()),
  (760, "Loki", "♀", "UK", "Agnostic", ()),
  (215, "Luthiel", "♀", "USA", "Atheist", ()),
  (197, "Maghrebi", "♂", "Morocco", "", ()),
  (854, "Malik", "♂", "UK", "Atheist", ()),
  (450, "Manat", "♀", "", "", ()),
  (557, "mangostan", "", "", "", ()), # Registered long time ago. First posting 28.9.2009.
  (1057, "MangoStar", "♀", "USA", "", (), "Raised Southern Baptist. Converted when she was 17, apostatized when she was 18."), # Guessed country.
  (32, "Marmalade-Lady", "♀", "UK", "", ()),
  (1453, "Marxist", "♂", "USA", "", ()),
  (11, "Maryam Namazie", "♀", "UK", "Atheist", (), "Head of the Council of Ex-Muslims of Britain"),
  (1194, "mateen", "♂", "Pakistan", "", ()),
  (960, "mattb", "♂", "", "", ()),
  (325, "Mia Bella", "♀", "Canada", "", ()),
  (1255, "MoeAlharbi", "♂", "Canada", "Atheist", ()),
  (2076, "mohsinali32", "♂", "UK", "", ()),
  (1410, "Morpheus", "♂", "", "", ()),
  (1131, "Mowgli", "♂", "UK", "", (), "⚣"),
  (1436, "msshama", "♀", "Egypt", "", (), '<a href="http://www.councilofexmuslims.com/index.php?topic=10382">Her story</a>.'),
  (1695, "mufa9a", "♀", "Saudi Arabia", "", ()),
  (1235, "Mughal", "♂", "UK", "", ()),
  (1243, "mujahid", "♀", "UK", "", (), '<a href="http://www.councilofexmuslims.com/index.php?topic=8959">Her introduction</a>'),
  (1188, "Naerys", "♀", "North-Africa", "Atheist", ("Coming to the realization that Islam is merely a bad rip-off of other religions", "Women's status in Islam", "God's pettiness and irrational punishment")),
  (1630, "Naija Infidel", "♂", "Nigeria", "Deist", ()),
  (710, "ned", "♀", "Pakistan", "Panentheist", (), '"Strictly speaking, I\'m a non-religious, neo-Vedantist, panentheistic mystic."'),
  (1297, "nessrriinn", "♀", "Canada", "", ()),
  (2483, "newsoul", "♀", "USA", "", ()),
  (712, "Nite Owllll", "♂", "USA", "Atheist", ()),
  (623, "Nizar", "♂", "Sweden", "Agnostic", ()),
  (880, "nothingthere", "♂", "", "Atheist", ()), # Guessed the gender.
  (430, "Nour", "♀", "UK", "Agnostic", ()),
  (1280, "nugzy", "♂", "", "", ()),
  (846, "Nuppar", "♂", "USA", "Atheist", ()),
  (1656, "olweasel", "♂", "USA", "", ()),
  (787, "Omaar Khayaam", "♂", "UK", "Atheist", (), "Apostatized after struggling with doubts for many years"),
  (868, "omarinbox", "♂", "UK", "Atheist", (), 'When still a Muslim, he was addressed in a "<a href="http://tariqali.org/ExtractClashLetter.html">Letter To A Young Muslim</a>" by <a href="http://en.wikipedia.org/wiki/Tariq_Ali">Tariq Ali</a>'),
  (786, "onlyme", "♂", "UK", "", ()),
  (414, "open_thinking", "♂", "UK", "", ()),
  (408, "Orion", "♂", "", "", ()),
  (260, "pakman", "♂", "", "", ()), # UK?
  (249, "panoptic", "♂", "UK", "Atheist", ()),
  (734, "Pariah", "♀", "UK", "Atheist", ("I bow to no one",), "Wife of thinkfree"),
  (160, "Pazuzu", "♂", "UK", "Atheist", ()),
  (554, "PeruvianSkies", "♀", "UK", "Atheist", ()),
  (1828, "pierced_beauty", "♀", "USA", "Spiritual", ()),
  (1312, "Prince Spinoza", "♂", "UK", "Pantheist", ()),
  (870, "Prosaic", "♀", "Egypt", "Atheist", (), "Came as a wavering Muslim to the forum"),
  (1043, "Psychologist", "♂", "UK", "", (), "Invited ex-Muslims to an interview for a psychological study at the University of Westminster"),
  (1135, "pure.virtual", "♂", "Palestine", "Atheist", ()),
  (121, "quratulain", "♂", "Pakistan", "Atheist", ()),
  (757, "Ramadulla", "♂", "UK", "", ()),
  (715, "Raqsi", "♀", "", "", ()),
  (919, "reemz83", "♀", "Canada", "", ()),
  (31, "Reza Moradi", "♂", "UK", "Atheist", ()),
  (735, "RIBS", "♂", "", "Atheist", ()),
  (592, "rooblee", "♂", "", "", ()),
  (1012, "Rubaiyat", "♂", "", "Atheist", ()),
  (57, "Rubina", "♀", "", "", ()),
  (616, "Saima", "♀", "", "", ()),
  (628, "SalahuddinR", "♂", "USA", "Atheist", ()),
  (707, "salim munqith", "♂", "Syria", "Atheist", ()),
  (1602, "sAllah Eldream", "♂", "Canada", "Atheist", ()),
  (855, "Sameer", "♂", "India", "Atheist", ()),
  (435, "sbmuse", "♂", "", "", (), "Ex-Convert; was/is friends with Hamza Yusuf, Nuh Ha Mim Keller, Suhaib Webb..."),
  (1250, "scousepk", "♂", "UK", "", ()),
  #(1147, "SeekTruth", "♂", "USA", "", ()), #Pretty much an ex-Muslim (soon).
  (1684, "serrated_colon", "♂", "UK", "Atheist", ("God's existence isn't a definitive fact, therefore I cannot believe in Islam as it treats Allah's existence as a fact",), "Agnostic atheist"),
  (966, "shaft4038", "♂", "USA", "Atheist", ()),
  (65, "Shahid Raza", "♂", "UK", "Deist", ()),
  (675, "Shahzad", "♂", "", "Panentheist", ()),
  (831, "sharkheart", "♂", "UK", "Atheist", ()),
  (1201, "Shirdon", "♂", "UK", "Atheist", (), "⚣⚤"),
  (1174, "sku", "♀", "UK", "Atheist", ()),
  (944, "smudge59", "♂", "UK", "", ()),
  (1027, "smy890", "♂", "UAE", "", ()),
  (1137, "SojournerTruth", "♀", "Netherlands", "Agnostic", ()),
  (1963, "Solarjaaz", "♀", "USA", "Atheist", ("Allah is barbaric an unjust", "the Qur'an contradicts itself and Science", "Lack of evidence for the claims made in Islam")),
  (3, "Spasm", "♀", "", "", ()),
  (495, "spiral dive", "♀", "UK", "Atheist", ()),
  (544, "stardust", "♀", "", "Atheist", ()),
  (369, "Starnexus", "♂", "", "Atheist", ()),
  (1429, "stifleddoubt", "♀", "Egypt", "Atheist", ()),
  (926, "stranger", "♂", "UK", "", ()),
  (1173, "taraC", "♂", "Pakistan", "", ()),
  (1214, "the_revivor", "♂", "Australia", "Atheist", ()),
  (1328, "thinkfree", "♂", "UK", "Atheist", (), "Husband of Pariah"),
  (562, "Tommy", "♂", "USA", "Atheist", ()),
  (244, "Uppercut", "♂", "UK", "Humanist", ()),
  (1694, "Urahara Kissuk", "♂", "Oman", "Humanist", ()),
  (1103, "virav5", "♀", "Indonesia", "Agnostic", ()),
  (485, "whatabastor", "♂", "Saudi Arabia", "", ()),
  (2516, "whyabadi", "♂", "UAE", "Atheist", (), "⚣"),
  #(2444, "whyme89", "♀", "", "", ()),
  (19, "Witzbold", "♂", "Pakistan", "Atheist", ()),
  (1898, "xantar", "♂", "Belgium", "Atheist", ()),
  (924, "youcansee", "♀", "UK", "Atheist", ()),
  (1138, "z10", "♂", "Canada", "Atheist", (), "Was raised in a British Pakistani home with Muslim values"),
  (42, "Zaephon", "♂", "Turkey", "Atheist", ()),
  (888, "ZBS", "♂", "USA", "Atheist", ()),
  (58, "ZiaZ", "♂", "UK", "Humanist", ()),
  (1013, "zizo", "♂", "Egypt", "Atheist", ()),
  (2494, "Zodiac", "♂", "Kuwait", "Atheist", ()),
  (913, "Zuber", "♂", "New Zealand", "Atheist", ()),
]

def sort_user_list():
  # Sort the list by user name in lower case.
  users.sort(key=lambda x: x[1].lower())
sort_user_list()


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
  body { background-color: white; }
  tbody > tr:nth-child(odd) { background-color: #D0E4DE; }
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
      var parag = $('<p class="stats_closed"><a href="#stats">Statistics</a></p>');
      xmlist.before(parag);
      var $a = $("a", parag), a = $a[0];
      a.clickHandler = function(e) {
        e && e.preventDefault();
        document.location = this.href;
        this.href = (this.href.slice(-1) == "#") ? "#stats" : "#";
        showStatistics(parag);
      };
      $a.click(a.clickHandler);
      if (/#stats$/.test(document.location.href))
        a.clickHandler();
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
  import re
  from sys import stdout
  def out(text, nl= "\n"):
    text = unicode(text) + nl
    out.write(text.encode("utf-8"))
  out.write = stdout.write

  rx = re.compile('<a .*?href="([^"]+)"[^>]*>(.+?)</a>')

  out('{| width=100% border=1 class="wikitable"\n'
    "!Nick!!Gender!!Country!!Current views!!"
    "Top 3 reasons for leaving Islam!!Annotations")
  for u in users:
    u = list(u)
    if len(u) < 7:
      u += [""]
    u[5] = "''';''' ".join(u[5])
    u[6] = rx.sub(r"[\1 \2]", u[6])
    out("|-\n|[[coem_user:{0}|{1}]]||{2:1}||{3:1}||{4:1}||{5:1}||{6}".format(*u))
  out("|}")

def escape(s):
  return s.replace("&", "&amp;")

def write_XHTML(dest):
  def write(text):
    xhtml.write(text.encode("utf-8"))

  xhtml = open(dest, "w")
  write(get_xhtml_head())

  for u in users:
    annot = u[6] if len(u) >= 7 else ""
    reasons = "<b>;</b> ".join(['<span class="reason">%s</span>' % escape(r) for r in u[5]])
    user = '<a href="http://www.councilofexmuslims.com/index.php?action=profile;u='+str(u[0])+'">'+u[1]+"</a>"
    row = dict(id=u[0], name=u[1], user=user, gndr=u[2], cntry=u[3],
      views=escape(u[4]), reasons=reasons, annot=annot)
    write(('<tr id="u%(id)s"><td>%(user)s</td><td>%(gndr)s</td><td>%(cntry)s</td>'
      '<td>%(views)s</td><td>%(reasons)s</td><td>%(annot)s</td></tr>\n') % row)

  write("</tbody>\n</table>\n</body>\n</html>")

def check_list():
  # Check for correct alphabetic order.
  # NB: not necessary any more; see sort_user_list().
  names = [u[1] for u in users]
  names_ = names[:]
  names.sort(lambda a, b: cmp(a.lower(), b.lower()))
  for n1, n2 in zip(names, names_):
    if n1 != n2:
      print n1, "<", n2
      break

def main():
  from sys import argv
  if "--wiki" in argv:
    print_Wiki()
  elif "--bbc" in argv:
    print_BBC()
  elif "--check" in argv:
    check_list()
  else:
    dest = "COEM_ex-Muslims.xhtml"
    if len(argv) > 1: dest = argv[1]
    write_XHTML(dest)

if __name__ == '__main__':
  main()
