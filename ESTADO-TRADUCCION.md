# Estado de la traducción — 9 de septiembre de 2026

**Completadas la prosa, las etiquetas y los nombres de unidades, armas y habilidades.**

- Los 133 JSON de prosa contienen 9.862 entradas resueltas y **0 valores vacíos**.
- Se han rellenado las 697 entradas que antes se conservaban vacías: claves,
  habilidades de arma, etiquetas de peanas e ingredientes, además de registrar
  las expresiones numéricas y los nombres propios sin traducción.
- 24 valores de prosa son idénticos al original porque contienen datos, nombres
  propios u otras expresiones que no cambian.
- Las **133 parejas de archivos** pasan la verificación completa de texto,
  nombres, estructura XML y atributos técnicos. Los originales ingleses y los
  diccionarios de prosa no han cambiado durante la traducción de nombres.
- Pasan las siete pruebas del generador, incluidos los nombres de habilidades
  en reglas y perfiles y los alias que enlazan catálogos diferentes.
- Las equivalencias son traducciones de aficionado, no nomenclatura oficial.

## Cobertura de nombres

La comprobación ampliada revisa **8.488 nombres distintos**:
8.303 tienen equivalencia española, 185 mantienen
su denominación y **0 están pendientes**. Incluye unidades, miniaturas,
armas, manifestaciones, habilidades, reglas, selectores y modificadores de nombre.

El bloque inicial de unidades y armas cubría 3.248 nombres: 3.077 traducidos
y 171 conservados. La ampliación cubre los **4.511 títulos distintos
de perfiles de habilidades y tácticas de batalla** (4.497 traducidos
y 14 conservados), así como 784 nombres adicionales
de reglas, formaciones, sendas y alias. Hay 666 títulos distintos de reglas
registrados; algunos ya figuraban en los perfiles o en el bloque de unidades.
Estas cifras se solapan y no deben sumarse para obtener el total.

Además se han registrado 293 nombres citados dentro de la prosa:
órdenes básicas sin perfil local, variantes de escritura y títulos de efectos.
Se han revisado también los encabezados de efectos que seguían en inglés en
las traducciones existentes. Este bloque incluye referencias como `Rally`,
`Redeploy`, `Power Through` y `Banish Manifestation`.

Las equivalencias se documentan en [GLOSARIO-NOMBRES.md](GLOSARIO-NOMBRES.md),
[GLOSARIO-HABILIDADES.md](GLOSARIO-HABILIDADES.md) y
[GLOSARIO-ETIQUETAS.md](GLOSARIO-ETIQUETAS.md).

## Alcance

Se traduce el contenido de `description` y `characteristic`, además de los
nombres visibles registrados en `translations/names/`. Se incluyen personajes,
variantes, Legends, hechizos, plegarias, rasgos, artefactos, formaciones,
Regimientos de Renombre y opciones de Sendero a la Gloria.

El generador actualiza las referencias a esos nombres dentro de las reglas.
Los nombres propios sin equivalente se conservan. Los atributos de nombre
autorizados pertenecen a entradas, grupos, perfiles, reglas y enlaces; también
se traducen valores de modificadores cuyo `field` es `name`.
Los identificadores, tipos de perfil, categorías, nombres de características,
valores técnicos y estructura permanecen intactos.

No se han enviado las reglas a un traductor externo. La verificación técnica
no sustituye una revisión editorial independiente ni pruebas en una aplicación
de listas de ejército.

## Mantenimiento

Al incorporar nuevas versiones de los originales, extraer las nuevas cadenas,
traducirlas siguiendo `TRADUCIR.md`, generar las versiones españolas y ejecutar
la verificación y la comprobación de cobertura de nombres. Un valor vacío
representa trabajo pendiente. Por preferencia del usuario, hacer commit y push
tras completar y verificar cada ejército.

## Cobertura por archivo

| Original | Entradas resueltas | Valores idénticos al original |
| --- | ---: | ---: |
| Age of Sigmar 4.0.gst | 137 | 1 |
| Beasts of Chaos - Library.cat | 75 | 1 |
| Beasts of Chaos.cat | 28 | 0 |
| Big Waaagh!.cat | 19 | 0 |
| Blades of Khorne - Gorechosen Champions.cat | 15 | 0 |
| Blades of Khorne - Library.cat | 245 | 0 |
| Blades of Khorne - The Baleful Lords.cat | 24 | 0 |
| Blades of Khorne.cat | 58 | 0 |
| Bonesplitterz - Library.cat | 42 | 0 |
| Bonesplitterz.cat | 25 | 1 |
| Cities of Sigmar - Allies of the Free Cities.cat | 23 | 1 |
| Cities of Sigmar - Greywater Fastness [LEGENDS].cat | 39 | 0 |
| Cities of Sigmar - Lethis [LEGENDS.cat | 18 | 0 |
| Cities of Sigmar - Library.cat | 385 | 2 |
| Cities of Sigmar - The Duardin Ascendant [LEGENDS].cat | 0 | 0 |
| Cities of Sigmar - The Iron March.cat | 31 | 0 |
| Cities of Sigmar.cat | 70 | 0 |
| Daughters of Khaine - Champions of the Arena.cat | 12 | 0 |
| Daughters of Khaine - Library.cat | 198 | 0 |
| Daughters of Khaine - The Croneseer's Pariahs.cat | 16 | 0 |
| Daughters of Khaine - Zainthar Kai.cat | 13 | 0 |
| Daughters of Khaine.cat | 50 | 0 |
| Disciples of Tzeentch - Change-cult Uprising.cat | 18 | 0 |
| Disciples of Tzeentch - Library.cat | 220 | 2 |
| Disciples of Tzeentch - Pyrofane Cult.cat | 31 | 0 |
| Disciples of Tzeentch - The Oracles of Fate.cat | 10 | 0 |
| Disciples of Tzeentch.cat | 61 | 0 |
| Flesh-eater Courts - Legions of Nagash [LEGENDS].cat | 0 | 0 |
| Flesh-eater Courts - Library.cat | 217 | 0 |
| Flesh-eater Courts - New Summercourt.cat | 21 | 0 |
| Flesh-eater Courts - The Equinox Feast.cat | 12 | 0 |
| Flesh-eater Courts.cat | 60 | 0 |
| Fyreslayers - Library.cat | 93 | 1 |
| Fyreslayers - Lofnir Drothkeepers.cat | 14 | 0 |
| Fyreslayers - The Duardin Ascendant [LEGENDS].cat | 0 | 0 |
| Fyreslayers.cat | 35 | 0 |
| Gloomspite Gitz - Da King's Gitz.cat | 18 | 0 |
| Gloomspite Gitz - Droggz's Gitmob.cat | 19 | 0 |
| Gloomspite Gitz - Library.cat | 248 | 4 |
| Gloomspite Gitz - Trugg's Troggherd.cat | 15 | 0 |
| Gloomspite Gitz.cat | 40 | 0 |
| Hedonites of Slaanesh - Court of the Godlings.cat | 21 | 0 |
| Hedonites of Slaanesh - Library.cat | 247 | 0 |
| Hedonites of Slaanesh - The Decadent Host.cat | 17 | 0 |
| Hedonites of Slaanesh.cat | 71 | 0 |
| Helsmiths of Hashut - Library.cat | 143 | 0 |
| Helsmiths of Hashut - Taar's Grand Forgehost.cat | 8 | 0 |
| Helsmiths of Hashut - Ziggurat Stampede.cat | 8 | 0 |
| Helsmiths of Hashut.cat | 48 | 0 |
| Idoneth Deepkin - Library.cat | 181 | 0 |
| Idoneth Deepkin - The First Phalanx of Ionrach.cat | 21 | 1 |
| Idoneth Deepkin - Wardens of the Chorrileum.cat | 17 | 0 |
| Idoneth Deepkin.cat | 54 | 0 |
| Ironjawz - Big Waaagh!.cat | 0 | 0 |
| Ironjawz - Ironsunz [LEGENDS].cat | 30 | 1 |
| Ironjawz - Krazogg's Grunta Stampede.cat | 18 | 0 |
| Ironjawz - Library.cat | 142 | 0 |
| Ironjawz - Zoggrok's Ironmongerz.cat | 9 | 0 |
| Ironjawz.cat | 47 | 1 |
| Kharadron Overlords - Grundstok Expeditionary Force.cat | 14 | 0 |
| Kharadron Overlords - Library.cat | 188 | 0 |
| Kharadron Overlords - Pioneer Outpost.cat | 22 | 0 |
| Kharadron Overlords - The Duardin Ascendant [LEGENDS].cat | 0 | 0 |
| Kharadron Overlords - The Magnate's Crew.cat | 24 | 0 |
| Kharadron Overlords.cat | 67 | 0 |
| Kruleboyz - Big Waaagh!.cat | 0 | 0 |
| Kruleboyz - Library.cat | 172 | 0 |
| Kruleboyz - Murkvast Menagerie.cat | 12 | 0 |
| Kruleboyz.cat | 54 | 1 |
| Legions of Nagash [LEGENDS].cat | 21 | 0 |
| Lores.cat | 744 | 0 |
| Lumineth Realm-lords - Aelementiri Conclave.cat | 17 | 0 |
| Lumineth Realm-lords - Library.cat | 214 | 0 |
| Lumineth Realm-lords - Vanari Paragons.cat | 21 | 0 |
| Lumineth Realm-lords.cat | 42 | 0 |
| Maggotkin of Nurgle - Cycle of Corruption.cat | 15 | 0 |
| Maggotkin of Nurgle - Library.cat | 246 | 0 |
| Maggotkin of Nurgle - The Gardeners of Nurgle.cat | 16 | 0 |
| Maggotkin of Nurgle.cat | 44 | 0 |
| Nighthaunt - Legions of Nagash [LEGENDS].cat | 0 | 0 |
| Nighthaunt - Library.cat | 211 | 0 |
| Nighthaunt - The Clattering Procession.cat | 16 | 0 |
| Nighthaunt - The Eternal Nightmare.cat | 11 | 0 |
| Nighthaunt.cat | 52 | 0 |
| Ogor Mawtribes - Beastclaw Alfrostun.cat | 13 | 0 |
| Ogor Mawtribes - Library.cat | 220 | 0 |
| Ogor Mawtribes - Mawseeker Gollop.cat | 22 | 0 |
| Ogor Mawtribes - Meatfist Mawtribe.cat | 28 | 0 |
| Ogor Mawtribes - The Roving Maw.cat | 11 | 0 |
| Ogor Mawtribes.cat | 58 | 0 |
| Orruk Warclans - Library.cat | 20 | 0 |
| Ossiarch Bonereapers - Legions of Nagash [LEGENDS].cat | 0 | 0 |
| Ossiarch Bonereapers - Library.cat | 204 | 1 |
| Ossiarch Bonereapers - Petrifex Elite [LEGENDS].cat | 23 | 0 |
| Ossiarch Bonereapers - The Lance of Ossia.cat | 19 | 0 |
| Ossiarch Bonereapers - The Null Myriad.cat | 10 | 0 |
| Ossiarch Bonereapers.cat | 52 | 0 |
| Path to Glory - Ascension.cat | 62 | 0 |
| Path to Glory - Blighted Wilds.cat | 277 | 0 |
| Path to Glory - Ravaged Coast.cat | 217 | 0 |
| Regiments of Renown.cat | 335 | 0 |
| Seraphon - Library.cat | 149 | 0 |
| Seraphon.cat | 53 | 0 |
| Skaven - Library.cat | 290 | 4 |
| Skaven - Thanquol's Mutated Menagerie.cat | 16 | 0 |
| Skaven - The Great-grand Gnawhorde.cat | 13 | 0 |
| Skaven.cat | 61 | 0 |
| Slaves to Darkness - Legion of the First Prince.cat | 41 | 0 |
| Slaves to Darkness - Library.cat | 275 | 1 |
| Slaves to Darkness - The Swords of Chaos.cat | 15 | 0 |
| Slaves to Darkness - Tribes of the Snow Peaks.cat | 21 | 0 |
| Slaves to Darkness.cat | 62 | 0 |
| Sons of Behemat - King Brodd's Stomp.cat | 20 | 0 |
| Sons of Behemat - Library.cat | 58 | 0 |
| Sons of Behemat.cat | 47 | 0 |
| Soulblight Gravelords - Barrow Legion.cat | 29 | 0 |
| Soulblight Gravelords - Knights of the Crimson Keep.cat | 19 | 0 |
| Soulblight Gravelords - Legions of Nagash [LEGENDS].cat | 0 | 0 |
| Soulblight Gravelords - Library.cat | 288 | 1 |
| Soulblight Gravelords - Scions of Nulahmia.cat | 14 | 0 |
| Soulblight Gravelords.cat | 52 | 0 |
| Stormcast Eternals - Astral Templars.cat | 17 | 0 |
| Stormcast Eternals - Draconith Skywing.cat | 13 | 0 |
| Stormcast Eternals - Heroes of the First-Forged.cat | 18 | 0 |
| Stormcast Eternals - Library.cat | 346 | 0 |
| Stormcast Eternals - Ruination Brotherhood.cat | 14 | 0 |
| Stormcast Eternals.cat | 60 | 0 |
| Sylvaneth - Library.cat | 212 | 0 |
| Sylvaneth - Lords of the Clan.cat | 15 | 0 |
| Sylvaneth - Soulpod Guardians.cat | 12 | 0 |
| Sylvaneth - The Evergreen Hunt.cat | 25 | 0 |
| Sylvaneth.cat | 54 | 0 |
| The Duardin Ascendant [LEGENDS].cat | 22 | 0 |
