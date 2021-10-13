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


Using all of the confusable characters of unicode (see [the unicode confusable characters][1]), we can generate weird looking text worthy of old spam messages:

`𝖧‌𝘦‌ꭇ‍m‌𝒂‌ռ‍ ‍Ꮇ‌𝗲‌𝟭‌𑜆‍𝘪‍𝐥‌𝓵‍e‌ ‍❨‌𝜜‍𝞄‍ƍ‍𝖚‌𐑈‌𝗍‍ ‍1‌؍‍ ‍1‍ȣ‍1‌൭‌ ‌–‌ ‌𝓢‍e‍𝜚‍𝘁‌𝔢‍m‍b‌е‍𝒓‌ ‍Ϩ‌🯸‍‚‌ ‍1‌𝟴‌🯹‍1‌〕‍ ‍𝓌‌𝒶‍𝒔‌ ‌𝕒‍𝑛‍ ‍𝘈‍m‍𝗲‍𝗿‌ⅈ‌ϲ‍a‌𝙣‌ ‌𝗻‍𝗈‍v‌ⅇ‍Ⲓ‍𝜾‍𝓈‌𝔱‍¸‍ ‌ѕ‌𝕙‍ο‌𝙧‍𝘁‌ ‍𝖘‌𝗍‌ᴑ‌ᴦ‌𑣜‍ ‍𝗐‌𝓇‌ı‍t‍𝗲‌г‍ꓹ‌ ‌𝛼‌𝑛‌ⅆ‌ ‌𝛠‍𝔬‌𝕖‍𝘵‌ ‍ہ‍f‌ ‌𝐭‌𝔥‌𝕖‌ ‌𝛢‌m‌℮‍𝓇‌𝞲‍с‍𝒂‌𝕟‌ ‍ℝ‍𝑒‍𝒏‌𝕒‍ɩ‌𝓼‌𝓼‌𝓪‌𝒏‍𝒸‌𝕖‌ ‍ｐ‍𝑒‍𝗿‌⍳‌ﮦ‌𝒅‍٠‍ ‌𝛢‌m‍𝝈‌𝕟‌𝗴‌ ‍𝓱‌ι‍𝗌‌ ‍𝑏‍ҽ‌𝖘‌𝖙‌‒‌𝐤‌𝔫‌೦‍𝘸‍𝐧‍ ‌𝘸‌𝞼‌𝔯‍𝐤‌s‌ ‌𝐚‌𝕣‍ℯ‌ ‍𝘔‍𝜎‌b‍ү‌⁃‍ꓓ‌𝗂‍с‍𝚔‌ ‍﴾‌1‌ଃ‌𑢻‌1‍﴿‍,‌ ‍Τ‍𝘺‌ｐ‌𝖾‍ℯ‌ ‌［‌1‌𞣋‌𝟦‌б‍］‌,‍ ‌𝝰‍ ‍ᴦ‌०‌m‍𝞪‍ո‍𝖙‍𝞲‍𐐽‌𝒾‍𝘇‍𝗲‍𝙙‍ ‌𝕒‍с‍ꮯ‍𞸤‍𝘶‌𝖓‌𝗍‌ ‍ο‌𝒇‍ ‍𝐡‌ι‍ѕ‍ ‍ｅ‌⨯‌𝞀‍𝐞‍ꭇ‍ӏ‍𝗲‌𝚗‌𝓬‌𝑒‍𝓼‌ ‌𝞲‌𝙣‌ ‌Ｐ‍𝒐‌𝜤‌𑣜‍𝗇‍ⅇ‍ѕ‍ℹ‌𝜶‌¸‍ ‌α‌𝔫‌𝖽‌ ‌𝕭‌ӏ‍ⅼ‍ⵏ‍γ‍ ‌𝔅‍𝖚‍ⅾ‍𝙙‌,‌ ‍𝙎‍⍺‍ӏ‌𝙸‍𝗈‌ⲅ‌‚‍ ‌𝞪‌ ‌𝘱‌𝔬‍𝖘‌𝓽‍𝖍‌𝞾‍m‍𝔬‌𝒖‌ꜱ‌𝘐‍𝕪‍ ‌𝕡‍ʋ‍𝖇‌𝜤‌Ꭵ‍𝓼‌𝔥‌𝒆‌𝔡‌ ‌ռ‍𝐨‌𝒗‍𝘦‍ا‍𝐥‍𝛼‌۰‌ ‌𝒜‍ﺍ‌𝕥‌𝒽‌𝜊‌𝘂‌𝕘‌𝘩‍ ‌𝒉‌ӏ‌𝓼‍ ‍𝓻‍𝙚‌𝜚‍𐓶‌𝚝‍𝐚‌𝚝‌𝙞‍𝙤‍n‌ ‌ԝ‍ａ‍ꮪ‍ ‌𝓃‌௦‍𝗍‌ ‌𝗵‍ι‍𝔤‌𝗵‍ ‌𝝰‍𝘵‌ ‌𝙩‌ｈ‍𝑒‍ ‌𝒕‌𝗶‌m‍𝖾‍ ‍ᴏ‌𝗳‌ ‍Ꮒ‍ι‌𐑈‌ ‌ᑯ‌𝗲‌𝙖‍𝘁‍Ꮒ‌¸‌ ‍𝓉‍𝗵‍𝙚‍ ‍𝔠‍ҽ‍𝗻‍𝓉‌e‌𝐧‌𝘯‌𝗶‌𝕒‍𝞘‍ ‍೦‌ẝ‌ ‍𝒽‌𑣃‌ƽ‌ ‍𝒃‌𝚤‍𝑟‍𝗍‌һ‌ ‌𑣃‍𝚗‌ ‌1‍Ⳋ‌1‌𑣖‌ ‍𝘸‌𝛼‍ꜱ‌ ‍t‍𝚑‍ⅇ‌ ‍𝘴‌𝗍‍𝘢‌𝘳‍𝑡‌𝓲‍𝐧‌𝒈‍ ‍𝟈‌ﮨ‍i‍ո‍𝓽‌ ‌𝘰‍ք‌ ‍𝛼‌ ‍𝐌‌ⅇ‍ꓲ‍ꮩ‍𝐢‍𝙡‍𝖨‍ｅ‍ ‍𝚛‌е‍ⅴ‌𝜾‍𝖛‍𝒂‍𝙸‌ ‌⍺‍𝗻‌𝓭‌ ‌𝑀‍o‌𝔟‍𝕪‍−‌ⅅ‍𝞲‍𝘤‌𝗄‌ ‌𝖌‍ᴦ‌𝔢‌𝐰‍ ‌𝑡‍၀‍ ‌𝙗‌𝚎‍ ‍𐐽‌೦‌𝑛‍𝚜‍𝜾‌ᑯ‍ⅇ‌𝒓‍𝓮‍𝖽‍ ‍𝙤‍𝗇‍е‌ ‍ჿ‌ꬵ‍ ‌𝗍‌ｈ‌ҽ‍ ‍ᶃ‌𝗿‌ℯ‍ａ‌𝓽‌ ‍𝝖‍m‌𝗲‌𝐫‌𝙞‍𐐽‌𝑎‍𝔫‌ ‍𝓷‍𝒐‍⋁‍ꬲ‍ℑ‌ꮪ‌.
`


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

See http://www.unicode.org/Public/security/revision-03/confusablesSummary.txt for the complete list of confusable.

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
