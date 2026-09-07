# Estado de la traducción — 7 de septiembre de 2026

**Completada la prosa pendiente de todos los catálogos actuales.**

## Resultado

- 133 archivos originales y sus 133 versiones españolas generadas y verificadas.
- 9.862 entradas de texto en los JSON: **9.165 con traducción** y **697 conservadas intencionadamente en inglés** (264 cadenas distintas).
- Revisadas todas las cadenas vacías: contienen claves, habilidades de arma, medidas de peanas, expresiones de dados o nombres de ingredientes con sus cantidades. No queda prosa pendiente en los valores vacíos.
- Completados los 17 archivos que seguían pendientes tras el primer bloque: Cities of Sigmar, Daughters of Khaine, Disciples of Tzeentch, Flesh-eater Courts, Gloomspite Gitz, Hedonites of Slaanesh, Lores, Lumineth Realm-lords, Maggotkin of Nurgle, Ossiarch Bonereapers, los suplementos Blighted Wilds y Ravaged Coast, Regiments of Renown, Skaven, Slaves to Darkness, Soulblight Gravelords y Stormcast Eternals.
- Estos 17 archivos incorporan **3.500 traducciones** adicionales a entradas antes vacías respecto al commit `04a747d`, además del trabajo anterior.
- Se ha mantenido el método del proyecto: editar solo los valores de traducción de los JSON y generar los XML con las herramientas existentes. No se han enviado las reglas a un traductor externo.

## Verificación

- `python tools/verify-translation.py`: las 133 parejas pasan la comprobación de estructura XML y atributos.
- Los originales ingleses no han cambiado. Las claves y el orden de las entradas JSON se conservan.
- Cada catálogo modificado se ha contrastado con su JSON al generarlo.
- Revisadas las cifras de las 3.500 traducciones añadidas. La única diferencia numérica detectada corresponde a una frase duplicada en el original de Disciples of Tzeentch sobre el valor 6: se ha eliminado la repetición sin cambiar la regla.
- Revisadas las referencias a habilidades citadas y la ausencia de caracteres de sustitución o signos de interrogación incrustados en palabras en las traducciones añadidas.
- Corregidas siete referencias recientes que usaban «Curar» para conservar el nombre `Heal`, tal como exige `TRADUCIR.md`.

La comprobación técnica protege la estructura y las referencias de los datos; no sustituye una revisión editorial independiente ni pruebas en una aplicación de listas de ejército. Los nombres y claves ingleses que aparecen en el texto son deliberados, para coincidir con los atributos `name` del catálogo.

## Mantenimiento

El contenido actual ya no tiene bloques pendientes de traducción. Al incorporar nuevas versiones de los originales, extraer las nuevas cadenas, traducirlas siguiendo `TRADUCIR.md`, regenerar las versiones españolas y ejecutar la verificación. Por preferencia del usuario, hacer commit y push tras completar y verificar cada ejército.

## Cobertura por archivo

El porcentaje bruto de valores no vacíos no representa la completitud: las entradas de la última columna deben conservarse en inglés.

| Original | Entradas traducidas | Conservadas en inglés |
| --- | ---: | ---: |
| Age of Sigmar 4.0.gst | 124 | 13 |
| Beasts of Chaos - Library.cat | 61 | 14 |
| Beasts of Chaos.cat | 27 | 1 |
| Big Waaagh!.cat | 18 | 1 |
| Blades of Khorne - Gorechosen Champions.cat | 15 | 0 |
| Blades of Khorne - Library.cat | 218 | 27 |
| Blades of Khorne - The Baleful Lords.cat | 23 | 1 |
| Blades of Khorne.cat | 57 | 1 |
| Bonesplitterz - Library.cat | 34 | 8 |
| Bonesplitterz.cat | 24 | 1 |
| Cities of Sigmar - Allies of the Free Cities.cat | 17 | 6 |
| Cities of Sigmar - Greywater Fastness [LEGENDS].cat | 37 | 2 |
| Cities of Sigmar - Lethis [LEGENDS.cat | 17 | 1 |
| Cities of Sigmar - Library.cat | 352 | 33 |
| Cities of Sigmar - The Duardin Ascendant [LEGENDS].cat | 0 | 0 |
| Cities of Sigmar - The Iron March.cat | 27 | 4 |
| Cities of Sigmar.cat | 68 | 2 |
| Daughters of Khaine - Champions of the Arena.cat | 12 | 0 |
| Daughters of Khaine - Library.cat | 180 | 18 |
| Daughters of Khaine - The Croneseer's Pariahs.cat | 16 | 0 |
| Daughters of Khaine - Zainthar Kai.cat | 13 | 0 |
| Daughters of Khaine.cat | 50 | 0 |
| Disciples of Tzeentch - Change-cult Uprising.cat | 18 | 0 |
| Disciples of Tzeentch - Library.cat | 196 | 24 |
| Disciples of Tzeentch - Pyrofane Cult.cat | 27 | 4 |
| Disciples of Tzeentch - The Oracles of Fate.cat | 10 | 0 |
| Disciples of Tzeentch.cat | 61 | 0 |
| Flesh-eater Courts - Legions of Nagash [LEGENDS].cat | 0 | 0 |
| Flesh-eater Courts - Library.cat | 194 | 23 |
| Flesh-eater Courts - New Summercourt.cat | 20 | 1 |
| Flesh-eater Courts - The Equinox Feast.cat | 12 | 0 |
| Flesh-eater Courts.cat | 59 | 1 |
| Fyreslayers - Library.cat | 81 | 12 |
| Fyreslayers - Lofnir Drothkeepers.cat | 13 | 1 |
| Fyreslayers - The Duardin Ascendant [LEGENDS].cat | 0 | 0 |
| Fyreslayers.cat | 34 | 1 |
| Gloomspite Gitz - Da King's Gitz.cat | 18 | 0 |
| Gloomspite Gitz - Droggz's Gitmob.cat | 18 | 1 |
| Gloomspite Gitz - Library.cat | 229 | 19 |
| Gloomspite Gitz - Trugg's Troggherd.cat | 14 | 1 |
| Gloomspite Gitz.cat | 38 | 2 |
| Hedonites of Slaanesh - Court of the Godlings.cat | 21 | 0 |
| Hedonites of Slaanesh - Library.cat | 226 | 21 |
| Hedonites of Slaanesh - The Decadent Host.cat | 17 | 0 |
| Hedonites of Slaanesh.cat | 69 | 2 |
| Helsmiths of Hashut - Library.cat | 128 | 15 |
| Helsmiths of Hashut - Taar's Grand Forgehost.cat | 8 | 0 |
| Helsmiths of Hashut - Ziggurat Stampede.cat | 8 | 0 |
| Helsmiths of Hashut.cat | 48 | 0 |
| Idoneth Deepkin - Library.cat | 163 | 18 |
| Idoneth Deepkin - The First Phalanx of Ionrach.cat | 20 | 1 |
| Idoneth Deepkin - Wardens of the Chorrileum.cat | 15 | 2 |
| Idoneth Deepkin.cat | 53 | 1 |
| Ironjawz - Big Waaagh!.cat | 0 | 0 |
| Ironjawz - Ironsunz [LEGENDS].cat | 26 | 4 |
| Ironjawz - Krazogg's Grunta Stampede.cat | 17 | 1 |
| Ironjawz - Library.cat | 127 | 15 |
| Ironjawz - Zoggrok's Ironmongerz.cat | 9 | 0 |
| Ironjawz.cat | 45 | 2 |
| Kharadron Overlords - Grundstok Expeditionary Force.cat | 14 | 0 |
| Kharadron Overlords - Library.cat | 181 | 7 |
| Kharadron Overlords - Pioneer Outpost.cat | 21 | 1 |
| Kharadron Overlords - The Duardin Ascendant [LEGENDS].cat | 0 | 0 |
| Kharadron Overlords - The Magnate's Crew.cat | 23 | 1 |
| Kharadron Overlords.cat | 66 | 1 |
| Kruleboyz - Big Waaagh!.cat | 0 | 0 |
| Kruleboyz - Library.cat | 158 | 14 |
| Kruleboyz - Murkvast Menagerie.cat | 11 | 1 |
| Kruleboyz.cat | 52 | 2 |
| Legions of Nagash [LEGENDS].cat | 20 | 1 |
| Lores.cat | 734 | 10 |
| Lumineth Realm-lords - Aelementiri Conclave.cat | 17 | 0 |
| Lumineth Realm-lords - Library.cat | 196 | 18 |
| Lumineth Realm-lords - Vanari Paragons.cat | 21 | 0 |
| Lumineth Realm-lords.cat | 40 | 2 |
| Maggotkin of Nurgle - Cycle of Corruption.cat | 14 | 1 |
| Maggotkin of Nurgle - Library.cat | 225 | 21 |
| Maggotkin of Nurgle - The Gardeners of Nurgle.cat | 16 | 0 |
| Maggotkin of Nurgle.cat | 44 | 0 |
| Nighthaunt - Legions of Nagash [LEGENDS].cat | 0 | 0 |
| Nighthaunt - Library.cat | 197 | 14 |
| Nighthaunt - The Clattering Procession.cat | 15 | 1 |
| Nighthaunt - The Eternal Nightmare.cat | 10 | 1 |
| Nighthaunt.cat | 51 | 1 |
| Ogor Mawtribes - Beastclaw Alfrostun.cat | 13 | 0 |
| Ogor Mawtribes - Library.cat | 199 | 21 |
| Ogor Mawtribes - Mawseeker Gollop.cat | 22 | 0 |
| Ogor Mawtribes - Meatfist Mawtribe.cat | 28 | 0 |
| Ogor Mawtribes - The Roving Maw.cat | 11 | 0 |
| Ogor Mawtribes.cat | 54 | 4 |
| Orruk Warclans - Library.cat | 18 | 2 |
| Ossiarch Bonereapers - Legions of Nagash [LEGENDS].cat | 0 | 0 |
| Ossiarch Bonereapers - Library.cat | 187 | 17 |
| Ossiarch Bonereapers - Petrifex Elite [LEGENDS].cat | 20 | 3 |
| Ossiarch Bonereapers - The Lance of Ossia.cat | 18 | 1 |
| Ossiarch Bonereapers - The Null Myriad.cat | 10 | 0 |
| Ossiarch Bonereapers.cat | 51 | 1 |
| Path to Glory - Ascension.cat | 60 | 2 |
| Path to Glory - Blighted Wilds.cat | 259 | 18 |
| Path to Glory - Ravaged Coast.cat | 211 | 6 |
| Regiments of Renown.cat | 323 | 12 |
| Seraphon - Library.cat | 129 | 20 |
| Seraphon.cat | 51 | 2 |
| Skaven - Library.cat | 254 | 36 |
| Skaven - Thanquol's Mutated Menagerie.cat | 15 | 1 |
| Skaven - The Great-grand Gnawhorde.cat | 12 | 1 |
| Skaven.cat | 60 | 1 |
| Slaves to Darkness - Legion of the First Prince.cat | 37 | 4 |
| Slaves to Darkness - Library.cat | 237 | 38 |
| Slaves to Darkness - The Swords of Chaos.cat | 14 | 1 |
| Slaves to Darkness - Tribes of the Snow Peaks.cat | 20 | 1 |
| Slaves to Darkness.cat | 61 | 1 |
| Sons of Behemat - King Brodd's Stomp.cat | 19 | 1 |
| Sons of Behemat - Library.cat | 49 | 9 |
| Sons of Behemat.cat | 46 | 1 |
| Soulblight Gravelords - Barrow Legion.cat | 28 | 1 |
| Soulblight Gravelords - Knights of the Crimson Keep.cat | 17 | 2 |
| Soulblight Gravelords - Legions of Nagash [LEGENDS].cat | 0 | 0 |
| Soulblight Gravelords - Library.cat | 268 | 20 |
| Soulblight Gravelords - Scions of Nulahmia.cat | 13 | 1 |
| Soulblight Gravelords.cat | 51 | 1 |
| Stormcast Eternals - Astral Templars.cat | 16 | 1 |
| Stormcast Eternals - Draconith Skywing.cat | 12 | 1 |
| Stormcast Eternals - Heroes of the First-Forged.cat | 17 | 1 |
| Stormcast Eternals - Library.cat | 312 | 34 |
| Stormcast Eternals - Ruination Brotherhood.cat | 13 | 1 |
| Stormcast Eternals.cat | 59 | 1 |
| Sylvaneth - Library.cat | 189 | 23 |
| Sylvaneth - Lords of the Clan.cat | 14 | 1 |
| Sylvaneth - Soulpod Guardians.cat | 11 | 1 |
| Sylvaneth - The Evergreen Hunt.cat | 25 | 0 |
| Sylvaneth.cat | 53 | 1 |
| The Duardin Ascendant [LEGENDS].cat | 21 | 1 |
