# publications.html vs Crossref discrepancies

Generated from Crossref REST records fetched 2026-11-25. "Page" = current `publications.html`. Pure initials formatting (e.g. "J.A." vs "J. A.", "Norskov" vs "Nørskov", "T.K. Ludwig" vs Crossref "T. Ludwig", "J.H. Stenlid" vs Crossref family "Halldin Stenlid") is not listed.

## Link / DOI (wrong DOI on the page; corrected in publications.yml)

| paper (DOI used in yml) | field | page says | Crossref says |
|---|---|---|---|
| Rutile oxides, JPCC 2026 (10.1021/acs.jpcc.5c08777) | link | 10.1021/acs.jpcc.5c00811 | correct DOI resolves to "Unraveling Fundamental Activity-Stability Relationships in Rutile Oxides" |
| Force-Based Method, JPCL 2022 (10.1021/acs.jpclett.2c01367) | link | 10.1021/acs.jpclett.2c00883 | correct DOI resolves to the Force-Based Method paper |
| Intricacies of Computational Electrochemistry, ACS Energy Lett. 2025 (10.1021/acsenergylett.5c00748) | link | 10.1021/acsenergylett.5c01574 | correct DOI resolves to that title |
| Acetate formation (Heenen), EES 2022 (10.1039/d2ee01485h) | link | 10.1039/D1EE03914C | correct DOI resolves to the acetate paper |
| Dinitrogen Activation, EES Catal. 2025 (10.1039/d5ey00033e) | link | 10.1039/D4EY00191E | correct DOI resolves to that title |
| Atomic Origins of Roughness, ACS Energy Lett. 2025 (10.1021/acsenergylett.5c02126) | link | 10.1021/acsenergylett.5c01927 | correct DOI resolves to that title |
| Nonaqueous Reactive CO2 Capture, Chem. Eng. J. 2025 (10.1016/j.cej.2025.171274) | link | 10.1016/j.cej.2025.160768 | that DOI is a different paper ("Facet-dependent activation of peroxonosulfate on C...", vol 507); the Sartape paper is 10.1016/j.cej.2025.171274 (vol 526, art. 171274) |
| Magnetically enhanced CO2 to formate, Chem. Eng. J. 2025 (10.1016/j.cej.2025.163614) | link | 10.1016/j.cej.2024.158581 | that DOI is a different paper ("Constructing ionic conductive channels with zwitte...", vol 503); the Abarca paper is 10.1016/j.cej.2025.163614 (vol 515, art. 163614) |
| Polyolefin model molecule, PCCP 2025 (10.1039/d4cp04663c) | link | 10.1039/D5CP00374A | that DOI is a different paper ("Influence of substitution patterns on isomer preference...", vol 27, 7826-7832); the Ortega-Ramos paper is 10.1039/d4cp04663c (vol 27, 11405-11412) |
| CoO nanoclusters nitrate reduction, Adv. Energy Mater. 2023 (10.1002/aenm.202204236) | link | 10.1002/aenm.202370069 | that DOI is the cover item ("... (Adv. Energy Mater. 17/2023)", article no. 2370069); the research article is 10.1002/aenm.202204236 (vol 13, issue 17, art. 2204236, online 2023-03-11) |

## (a) Year section vs Crossref print / online year

| paper (DOI) | field | page says | Crossref says |
|---|---|---|---|
| Challenges in Modeling Electrochemical Reaction Energetics with PCMs (10.1021/acscatal.8b02793) | year | filed under 2018, cited "ACS Catalysis, 2018" | published online 2018-11-28; print/issue 2019-02-01 (vol 9, issue 2, pp 920-931) |
| Achievements, Challenges, and Perspectives on Nitrogen Electrochemistry (10.1002/anie.202215938) | year | filed under 2023 | print/issue 2023-03 (vol 62, issue 10); online 2022-12-29. Page agrees with print year. |
| CoO nanoclusters (10.1002/aenm.202204236) | year | 2023 | print 2023-05; online 2023-03-11. Consistent. |

All other entries: page year equals both Crossref print and online year (RSC/other entries with no print date use the online year).

## (b) Volume / pages / article number

| paper (DOI) | field | page says | Crossref says |
|---|---|---|---|
| Sartape CEJ (10.1016/j.cej.2025.171274) | volume / article | 526, 171274 | 526, 171274 (agrees). The page's error was the DOI, not the volume/article number. |
| Abarca CEJ (10.1016/j.cej.2025.163614) | volume / article | 515, 163614 | 515, 163614 (agrees). Again only the DOI was wrong. |

No other printed volume/page value on the page differs from Crossref. Entries that print only the year (most 2017-2021 and 2024 entries) have no volume/pages to compare.
For reference, the two wrong CEJ DOIs on the page would have given vol 507 art. 160768 and vol 503 art. 158581 (other papers).

## (c) Title differences beyond case and sub/superscript markup

| paper (DOI) | field | page says | Crossref says |
|---|---|---|---|
| Acetate formation (10.1039/d2ee01485h) | title | "Mechanism for acetate formation in CO(2) reduction on Cu: Selectivity trends with pH and nanostructuring derive from mass transport" | "The mechanism for acetate formation in electrochemical CO(2) reduction on Cu: selectivity with potential, pH, and nanostructuring" |
| Roughening (10.1021/acsenergylett.1c01485) | title | "The role of roughening in enhancing selectivity to C2+ products during CO2 electroreduction on copper." | "The Role of Roughening to Enhance Selectivity to C2+ Products during CO2 Electroreduction on Copper" |
| Polyolefin model molecule (10.1039/d4cp04663c) | title | "...catalytic upcycling of polyolefins" (the chemrxiv preprint title) | "...catalytic upcycling of polyethylene and polypropylene" |
| Screening TM electrodes, SEF 2025 (10.1039/d4se00841c) | title | "...urea via electroreduction of NO 3− and CO 2 at 100 mA cm− 2..." (broken spacing) | same wording with proper sub/superscripts and italic "via" (formatting only; noted) |

## (d) Author-list differences

| paper (DOI) | field | page says | Crossref says |
|---|---|---|---|
| Sartape CEJ (10.1016/j.cej.2025.171274) | authors | 6: R. Sartape, V.V. Gande, R.R. Bhawnani, L. H-Z. Feistel, J.A. Gauthier, M.R. Singh | 8: R. Sartape, L. F. Zimmermann, P. Sharan, V. V. Gande, R. R. Bhawnani, S. Johnson, J. A. Gauthier, M. R. Singh. Page omits Sharan and Johnson; the group member appears in Crossref as "Luis F. Zimmermann" (page: "L. H-Z. Feistel") and in a different position. |
| Acetate formation (10.1039/d2ee01485h) | author order | Heenen, Kastlunger, Shin, Overa, Gauthier, Jiao, Chan | Heenen, Shin, Kastlunger, Overa, Gauthier, Jiao, Chan (Shin and Kastlunger swapped) |
| Ni-Mo cathodes ChemSusChem (10.1002/cssc.201900617) | authors | "J.H.J. Witjen" (typo) | "Wijten"; also Crossref has the PI as "Joseph Gauthier" (no middle initial) |
| Polyolefin PCCP (10.1039/d4cp04663c) | first author | "J. Ortega" | "Jessica Ortega-Ramos" (surname form) |

All other author lists agree in length, order and family names.

## Could not confirm / other things that look wrong

- Every DOI in publications.yml resolved in Crossref and the title matched the page title (modulo the title differences above). The three non-lead corrections (two CEJ DOIs, PCCP polyolefins) and the AEM cover/article swap were found by Crossref title search (title and first author agree); they were not on the verified list, so they merit a quick look.
- Entries whose page link was a journal homepage (2017-2021) had DOIs derived from the citation link (publisher URL or doi.org); all matched on title and authors.
- Thumbnail for the new Ludwig 2019 record (`thumbs/jpcc.jpg`) is assumed (same journal thumbnail as other JPCC entries), not taken from the page.
- Both Chem. Eng. J. entries use `thumbs/jpcc.jpg` on the page (a JPCC thumbnail on a CEJ paper).
- Several entries print only "Journal, year" with no volume or pages (2024 ACS Catal., ACS Energy Lett., etc.); yml carries Crossref values.
- Crossref gives hyphens as U+2010 in the two Wiley titles (aenm, angew) and an en dash in some ACS titles; kept as Crossref has them.
- AIChE 2021 session entry excluded; commented-out duplicate Lininger entry ignored.
- Crossref gives Verhoeven's given name as "Marcel W. G. M. (Tiny)"; recorded as "M. W. G. M. Verhoeven".
