# A Guide to Autonomy

Fonts bundled in this folder, both under the SIL Open Font License 1.1. The full official notice of each family (copyright line and complete licence text) sits next to the files:

- jetbrainsmono-latin.woff2, jetbrainsmono-latin-ext.woff2: JetBrains Mono, Copyright 2020 The JetBrains Mono Project Authors (https://github.com/JetBrains/JetBrainsMono). OFL-1.1. Full notice: `OFL-JetBrainsMono.txt`.
- righteous-latin.woff2, righteous-latin-ext.woff2: Righteous, Copyright (c) 2011 by Brian J. Bonislawsky DBA Astigmatic (AOETI), with Reserved Font Name "Righteous". OFL-1.1. Full notice: `OFL-Righteous.txt`.

The 2 `OFL-*.txt` files are byte-identical copies of the `OFL.txt` files published in https://github.com/google/fonts (`ofl/jetbrainsmono/`, `ofl/righteous/`); the build checks their SHA-256 and stops if they differ. When an edition uses one of these fonts, the build copies its full notice into the site (`legal/fonts/`) and into the source archive, and lists it on the page "Licences, credits and source".

The default edition uses no bundled font (system fonts). If you modify a font, the OFL applies to the result, and a Modified Version may not use a Reserved Font Name (Righteous has one) without the holder's written permission. Keep the full notice with any copy.
