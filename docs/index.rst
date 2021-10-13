==============
text-scrambler
==============

Using the Unicode confusable characters and other tricks, we can transform a text into another that looks exactly like it but remains different from a machine view.

Examples
~~~~~~~~

Replacing randomly the Latin characters by Greek or Cyrillic letters and adding the ZW(N)J.


**Original text:**

`Herman Melville (August 1, 1819 – September 28, 1891) was an American novelist, short story writer, and poet of the American Renaissance period. Among his best-known works are Moby-Dick (1851), Typee (1846), a romanticized account of his experiences in Polynesia, and Billy Budd, Sailor, a posthumously published novella. Although his reputation was not high at the time of his death, the centennial of his birth in 1919 was the starting point of a Melville revival and Moby-Dick grew to be considered one of the great American novels.`

**Srambled text (looking the same but totally different):**

`Неrman Μelvillе (Аugust 1, 1819 – Sерtеmbеr 28, 1891) waѕ аn Amerіcan nοvеliѕt, shοrt stоry wrіtеr, and рoеt οf thе Amеriсаn Rеnaissаnсе реrіοd. Amοng his bеѕt-knοwn works arе Мoby-Diсk (1851), Τyрee (1846), а romаntiсized aсcοunt of his ехperienсеs in Pоlynеѕіа, and Віlly Βudd, Sаilоr, а роѕthumοuѕly рublіshed nοvella. Аlthοugh hiѕ rеputatiоn wаs nоt hіgh аt the tіme оf hіѕ dеath, thе centеnnіаl οf hіѕ bіrth іn 1919 was thе startіng pοint οf a Мelvillе rеvіval аnd Mοby-Dісk grеw to be cоnsіdеrеd оne οf thе grеаt Αmerican novеls.`


It is worth to notice that search engines can't find the original webpage (as free online plagiarism checkers). Searching for **Μelvillе** (copy-paste it) on Google doesn't return any match, though the original word **Melville** does.


Using all of the confusable characters of unicode, we can generate weird looking text worthy of old spam messages:

`H‍e‍ꭈ‌m‌ɑ‍𝙣‍ ‌𝐌‍𝗲‍𝝞‌𝘷‌𝖎‌𝕀‌𝜤‍𝕖‍ ‌(‍𝔄‌ᴜ‍𝚐‌𝓾‌𝓼‌𝙩‍ ‍1‌‚‌ ‌1‍🯸‌1‍𑢬‌ ‍–‌ ‍𝕾‌𝑒‍𝞺‍t‌𝑒‍m‍𝔟‍𝖊‌𝑟‍ ‍Ꙅ‍੪‌,‌ ‍1‌৪‍𝟵‍1‍)‌ ‌ԝ‌𝒶‍ｓ‌ ‍𝛼‍𝚗‌ ‍𖽀‍m‍℮‌𝗋‍𝞲‍𝗰‍𝑎‍𝐧‌ ‍𝗻‍ⲟ‌𝛎‌𝐞‍𞣇‍𝖎‍𑣁‌𝘵‍‚‍ ‌ѕ‍𝐡‍ｏ‍𝕣‍𝔱‌ ‍𝚜‍𝚝‌౦‌𝘳‍𝖞‍ ‍𑜏‍𝖗‍ｉ‍𝔱‌ｅ‌𝔯‍ꓹ‌ ‍𝖆‍𝙣‌Ꮷ‍ ‍𝗉‍𝜎‍𝘦‌𝘁‌ ‌ℴ‍𝙛‍ ‍𝔱‍𝗁‌𝗲‌ ‌𝔄‍m‍𝑒‍𝔯‍𝜄‍ϲ‌𝔞‍𝑛‍ ‌Ꭱ‍ℯ‍𝔫‍𝖺‌𝕚‌𝐬‍𐑈‌𝘢‍𝗻‌ꮯ‌𝔢‍ ‌𝛒‍𝗲‍𝖗‍𝒾‍ە‍𝓭‌٠‍ ‍ꓮ‌m‌𝗈‍ռ‍𝚐‌ ‌һ‌𝕚‍𐑈‍ ‍𝔟‍𝑒‍𝓼‌𝖙‌⁃‌𝗄‌𝗇‍၀‌𝔀‍𝗇‍ ‍𝖜‍ο‌𝙧‌𝓴‍s‍ ‍𝑎‍𝓻‍𝒆‍ ‍Ｍ‌۵‍𝗯‍ꭚ‍⁃‌ⅅ‌ⅰ‍ᴄ‍𝗄‍ ‍［‍1‍৪‌Ƽ‌1‌〕‍¸‍ ‍𝕋‌𝜸‌⍴‌𝕖‌𝖾‍ ‍❲‌1‌𐌚‍𝟜‌𝟲‍)‌‚‍ ‌ɑ‌ ‌𝚛‍𝛐‍m‌⍺‌𝙣‍t‍𝑖‍𝑐‍𝑖‌𝑧‍𝖾‍𝖉‌ ‍𝛼‌𝕔‍𝚌‍𝘰‍𝑢‍ո‍𝓽‍ ‌໐‌ꬵ‍ ‌𝒉‌ι‍𝐬‌ ‌𝚎‍𝑥‌𝖕‍ꬲ‍r‍𝙞‌ҽ‌𝕟‌𐐽‌e‍𝐬‌ ‍𝓲‌ո‍ ‍Ρ‍𝖔‍𝐼‌𝑦‍𝓷‌ℯ‍𝔰‌ͺ‍𝖆‌؍‍ ‍𝗮‌𝘯‍d‌ ‍𐌁‌𝛊‌𝙄‍𝕴‌𝞬‍ ‍𝓑‌𝑢‌𝘥‌ꓒ‍ꓹ‍ ‌𐊖‍𝛂‌˛‌І‍ഠ‍𝓇‍٫‍ ‌𝜶‌ ‍𝐩‌ﮫ‌𝖘‌𝓽‌ℎ‌ꭒ‌m‍ⲟ‍ꞟ‍𝕤‌𝐼‍𝚢‍ ‌ｐ‍𝘶‍𝒷‌𝓁‍ｉ‌𝔰‍𝚑‍𝗲‌𝖉‌ ‌𝙣‌๐‌𝒗‌ҽ‍𝓵‌𝞘‌a‌꘎‌ ‌A‌𝐈‍𝑡‌Ꮒ‍𑣗‍ս‌ƍ‌𝚑‌ ‍𝒉‍і‍𝘴‌ ‍𝒓‌ｅ‌𝗽‌𝗎‍𝙩‌𝘢‌𝖙‍𝚒‌ο‌𝖓‍ ‍𝐰‌𝒂‍𝚜‌ ‍𝔫‌٥‌𝐭‍ ‍𝙝‌𝜾‌𝔤‍h‍ ‍⍺‌𝐭‍ ‌𝚝‍𝓱‌𝗲‍ ‍𝘁‍𝜾‍m‌𝔢‍ ‌ه‍ẝ‌ ‌𝐡‌𝘪‍𝖘‍ ‌𝙙‍𝒆‍𝜶‌𝖙‍𝐡‌ꓹ‌ ‌𝖙‍𝙝‌ℯ‌ ‌𝘤‌℮‌𝙣‍𝖙‌𝐞‌𝒏‌𝑛‌𝒾‍𝒂‌𝖨‌ ‍ﻬ‌ẝ‍ ‌𝔥‍ι‍ｓ‍ ‍𝒃‌𝕚‍𝓇‌𝓽‌𝘩‌ ‌ⅰ‍𝐧‌ ‍1‍੧‌1‍𝟫‍ ‌𝘄‍ａ‌𝘴‍ ‍𝐭‍𝒽‍𝚎‍ ‌s‌𝗍‌𝒂‍𝓇‍𝕥‍𝜄‍𝗻‌𝐠‍ ‌𝝔‍𐐬‍𝐢‌𝔫‍𝐭‍ ‍𝛔‌𝗳‌ ‌α‌ ‌Μ‌ℯ‌𝙡‍𝛎‌ⅈ‌𝟏‌ا‍𝓮‌ ‍𝘳‍℮‌ѵ‌𝙞‌𑣀‌𝛼‌Ι‍ ‌𝕒‌𝒏‌ⅾ‌ ‍ℳ‌ס‍ᑲ‍𝝲‌˗‍𝐷‍𝜾‍𝒸‌𝔨‌ ‍𝖌‍𝗿‌ҽ‌𝑤‍ ‌𝑡‌𑣗‍ ‍b‌𝚎‍ ‍ⅽ‍𑣗‍𝗻‍𝐬‌˛‍ꓒ‌℮‍ᴦ‍ｅ‌𝔡‍ ‍०‌n‍ｅ‍ ‌𝝄‍𝐟‍ ‌t‌𝚑‌𝘦‍ ‌𝗀‌𝚛‍ｅ‍𝒶‌𝓽‍ ‌Ꭺ‍m‍ⅇ‌𝒓‍𝗂‌𐐽‌𝖺‍𝔫‍ ‌𝐧‍𝗈‍𝚟‌𝘦‌𝐥‍𝔰‍`


===
API
===

Python
~~~~~~

  .. code:: python

      >>> from text_scrambler import Scrambler
      >>> scr = Scrambler()
      >>> text = "This is an example"
      >>> text_1 = scr.scramble(text, level=1)
      >>> # adding only zwj/zwnj characters
      >>> print(text, text_1)
      This is an example T‍h‍i‍s‍ ‌i‍s‍ ‍a‍n‌ ‍e‌x‍a‌m‍p‍l‍e
      >>> assert text != text_1
      >>> print(text_1)
      T‍h‍i‍s‍ ‌i‍s‍ ‍a‍n‌ ‍e‌x‍a‌m‍p‍l‍e
      >>> print(len(text), len(text_1))
      18 35
      >>> text_2 = scr.scramble(text, level=2)
      >>> # replacing some latin letters by their cyrilic/greek equivalent
      >>> print(text_2)
      Тhіѕ iѕ an еxample
      >>> for char, char_2 in zip(text, text_2):
      ...     if char != char_2:
      ...             print(char, char_2)
      ...
      T Т
      i і
      s ѕ
      s ѕ
      e е
      >>> text_4 = scr.scramble(text, level=4)
      >>> # replacing all characters by any
      >>> unicode looking like character
      >>> print(text_4)
      𝕋‌h‌ⅰ‌𝗌‌ ‌𝝸‍𝘴‍‍ 𝛼‌n‍‍ 𝖊‍𝙭‌𝐚‍m‌𝜌‍Ｉ‌𝐞
      >>> versions = scr.generate(text, 10, level=4)
      >>> for txt in versions:
      ...     print(txt)
      ...
      𝘛‌h‌𝚒‌𝓼‍‌ͺ‌s‌ ‍𝛂‌ո‌ ‍ҽ‍𝕩‌𝚊‍m‍𝒑‌𞣇‍𝒆
      𐊗‍𝘩‍ı‍𝚜‌ ‌𝚒‍𐑈‌ ‌𝚊‌𝓃‌ ‍𝔢‌ᕁ‌𝖺‍m‍𝗉‍𝟣‍𝑒
      𝕿‍𝓱‌𝚒‍ꜱ‌ ‍𝗂‌ꮪ‌ ‌𝗮‌𝙣‍ ‌𝖊‍𝑥‌𝛂‌m‌𝜌‍𝕴‍𝖾
      ⊤‍𝐡‍𝓲‍ｓ‍ ‍𝞲‌𝔰‍ ‌𝐚‍𝚗‍ ‌ҽ‌𝓍‌𝚊‌m‌ρ‌׀‌ꬲ
      𝕿‍𝚑‍і‌s‌ ‌𝜾‌ѕ‌ ‍𝔞‌𝕟‍ ‌𝑒‍𝘹‍𝛼‍m‌𝟈‍ﺍ‌℮
      𝗧‌𝐡‍𝚒‍ｓ‍ ‌𝘪‍𝗌‌ ‍𝔞‍ո‍ ‍𝕖‍𝘹‌𝘢‍m‍𝜌‌𝗅‍ⅇ
      𝕋‍𝗁‍ι‍𝔰‌ ‌𝕚‍𝒔‌ ‍𝓪‍𝘯‌ ‌𝙚‍ᕁ‍𝗮‍m‌𝝔‌۱‌ｅ
      𝖳‍𝖍‌ӏ‌𝗌‍ ‍ι‍𑣁‍ ‍α‌𝒏‌ ‍𝖊‍𝘹‌𝛼‍m‌𝗽‍𝜤‌e
      𝔗‌𝓱‍ɪ‍𑣁‍ ‍𝒾‍𝒔‍ ‌𝛼‍𝓷‌‍𝖾‌𝔵‍𝖺‌m‍𝝔‍𝒍‍e
      𝚻‍𝕙‌ɪ‌𝕤‍ ‍ⅈ‍𝕤‍‌𝛂‌𝔫‍ ‍𝓮‍ｘ‌⍺‍m‌⍴‍𝐈‌𝒆
      >>> versions = scr.generate(text, 1000, level=2)
      >>> assert len(versions) == len(set(versions))
      >>> # all unique

      >>> text = "A cranial nerve nucleus is a collection of neurons in the brain stem that is associated with one or more of the cranial nerves."
      >>> texts = scr.generate(text, 1000, level=1)
      >>> assert texts[0] != text
      >>> for scrambled_text in texts:
      ...     assert text != scrambled_text
      ...
      >>> print(texts[0])
      A‍ ‌c‍r‌a‌n‍i‍a‌l‌ ‌n‌e‍r‍v‍e‌ ‍n‌u‌c‍l‌e‌u‌s‌ ‍i‌s‌ ‌a‍ ‌c‍o‌l‍l‌e‍c‌t‌i‌o‍n‍ ‌o‍f‍ ‍n‌e‌u‌r‍o‍n‍s‌ ‍i‌n‌ ‍t‌h‍e‍ ‍b‍r‍a‍i‍n‌ ‌s‍t‍e‌m‍ ‍t‍h‍a‍t‍ ‍i‍s‌ ‌a‌s‍s‍o‌c‌i‌a‌t‌e‍d‍ ‌w‌i‌t‌h‍ ‌o‍n‍e‍ ‍o‍r‍ ‌m‌o‍r‍e‌ ‍o‍f‌ ‍t‍h‌e‌ ‍c‍r‌a‍n‍i‌a‍l‌ ‍n‌e‍r‍v‌e‌s‌.
      >>> # different from the original text



Command line interface (CLI)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To get words from input words through CLI, run


  .. code:: bash

      $ python -m text_scrambler
      usage: Usage : python -m text_scrambler file

      Replace/insert the charaters of the file using the unicode confusable characters

      positional arguments:
        file                  encoded in UTF-8

      optional arguments:
        -h, --help            show this help message and exit
        -l LEVEL, --level LEVEL

                                      1: insert non printable characters within the text
                                      2: replace some latin letters to their Greek or Cyrilic equivalent
                                      3: insert non printable characters and change the some latin  to their Greek or Cyrilic equivalent
                                      4: insert non printable chraracters change all possible letter to a randomly picked unicode letter equivalent
                                      default=1
        -n N, --generate N
                                      Scramble n times the string
                                      default=1





=====
Links
=====

See https://en.wikipedia.org/wiki/Word_joiner for more info on word joiners

See https://unix.stackexchange.com/questions/469347/using-uniq-on-unicode-text for why in this case the `sort` command wouldn't work well to check the uniqueness of those strings

See http://www.unicode.org/Public/security/revision-03/confusablesSummary.txt for the complete list of confusable characters.

Contents
========

.. toctree::
   :maxdepth: 2

   License <license>
   Authors <authors>
   Changelog <changelog>
   Module Reference <api/modules>


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _toctree: http://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html
.. _reStructuredText: http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
.. _references: http://www.sphinx-doc.org/en/stable/markup/inline.html
.. _Python domain syntax: http://sphinx-doc.org/domains.html#the-python-domain
.. _Sphinx: http://www.sphinx-doc.org/
.. _Python: http://docs.python.org/
.. _Numpy: http://docs.scipy.org/doc/numpy
.. _SciPy: http://docs.scipy.org/doc/scipy/reference/
.. _matplotlib: https://matplotlib.org/contents.html#
.. _Pandas: http://pandas.pydata.org/pandas-docs/stable
.. _Scikit-Learn: http://scikit-learn.org/stable
.. _autodoc: http://www.sphinx-doc.org/en/stable/ext/autodoc.html
.. _Google style: https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings
.. _NumPy style: https://numpydoc.readthedocs.io/en/latest/format.html
.. _classical style: http://www.sphinx-doc.org/en/stable/domains.html#info-field-lists
