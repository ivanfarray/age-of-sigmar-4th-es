# Erratas oficiales pendientes de BSData

## Correcciones de datos pendientes de BSData

No son erratas de Games Workshop, sino fallos de los datos de BSData que el
fork corrige mientras BSData no los publica. Cada una tiene su prueba en
`tools/test-official-errata.py`.

- **Knight-Zephyros es Legends** (4 de noviembre de 2026). Pasó a Warhammer
  Legends el 1 de junio de 2025, pero su entrada de `Stormcast Eternals -
  Library.cat` no lleva la categoría `Legends` que tienen los demás héroes
  retirados. BSData cerró el aviso
  [#1075](https://github.com/BSData/age-of-sigmar-4th/issues/1075) sin
  añadirla. Al integrar BSData, comprueba si ya la incluye; si es así, quita
  la corrección local y adopta su ID.

## Decisiones del equipo que se apartan de los perfiles oficiales

Valores que el fork cambia a propósito, aunque Battle Profiles diga otra cosa.
No los «corrijas» al integrar BSData: conserva el valor del fork.

- **Kurnoth Hunters with Kurnoth Greatswords: 220 puntos** (4 de noviembre de
  2026). Battle Profiles de septiembre de 2026 da 210 a la versión normal y
  220 a la de Scourge of Aqshy. Por decisión del equipo, las dos cuestan 220
  en `Sylvaneth.cat`, `Sylvaneth - Lords of the Clan.cat` y `Sylvaneth - The
  Evergreen Hunt.cat`.

## Reconciliación con BSData del 4 de noviembre de 2026

BSData publicó su versión de estas erratas el 28 de septiembre (`4ac427f`,
«September 2026 battle profiles and rules updates (#1368)») y el fork la ha
integrado con un merge hasta `d2334be`. De las 688 entradas del manifiesto,
649 quedan resueltas: 433 porque BSData publica el mismo contenido y 216
porque se adopta su implementación, que a veces usa otros IDs (por ejemplo,
las categorías Thaumaturgical Specialist y Mortisan Vizier). Están archivadas
en la lista `resolved` del manifiesto, con el commit que las absorbió.

Siguen siendo locales 39 entradas, rebasadas sobre la versión de BSData:

- **Puntos de Ejércitos de Renombre.** BSData considera que Pyrofane Cult y
  The Roving Maw tienen precios propios y no los actualiza. Battle Profiles no
  publica precios aparte para ellos, así que se mantiene el de la facción:
  Gaunt Summoner on Disc of Tzeentch 190, Ogroid Thaumaturge 120,
  Slaughtermaster 160, Butcher 170 y Gluttons 210. También Ogor Gluttons en
  Ironsunz: 210.
- **Campeones con refuerzo.** Se mantienen los límites del fork en las unidades
  que pasan a poder reforzarse: 10 de Slaves to Darkness, Khainite
  Shadowstalkers, Kruleboyz Monsta-killaz, Teratic Cohort, Hunters of Huanchi y
  Askurgan Trueblades. Pyregheists sigue con un único campeón aunque se
  refuerce; BSData lo duplica.
- **Regimientos.** Gunnar Brand admite Oathsworn y Bloodwrack Shrine admite
  Coven Matriarch. El Saurus Scar-Veteran on Aggradon (Scourge of Aqshy) sigue
  pudiendo unirse como Favoured Spawning: BSData retira esa nota, pero la
  página 18 del Battle Profiles de septiembre la conserva.
- Las revisiones de los catálogos que llevan alguno de estos cambios.

Las pruebas de `tools/test-official-errata.py` comprueban ahora la
implementación de BSData para Skink Starpriest, Skink Starseer y Favoured
Spawning, y el caso del Aggradon de Aqshy.

## Actualización del 23 de septiembre de 2026

Aplicada al fork el 25 de septiembre, sobre BSData
`d1f97bc9a3c4d65a13add36ed48082866c4e7942`. La integración previa de BSData
es un merge real (`18feb42`); las correcciones anticipadas de Games Workshop
se mantienen como cambios locales identificables.

Las fuentes son las [descargas oficiales de Age of Sigmar](https://www.warhammer-community.com/en-gb/downloads/warhammer-age-of-sigmar/),
actualizadas el 23 de septiembre:

- [Battle Profiles](https://assets.warhammer-community.com/eng_23-09_aos_core&key_battle_profiles-0amt68pt5c-vjtgulelgr.pdf): puntos, mejoras con coste, opciones de regimiento y unidades que ahora se pueden reforzar.
- [Rules Updates](https://assets.warhammer-community.com/eng_23-09_aos_core&key_rule_updates-eu6fu82jl3-dlyuiignte.pdf): comprobación de las correcciones de reglas representadas en los catálogos.
- Los documentos de Scourge of Aqshy de Slaves to Darkness, Fyreslayers,
  Sons of Behemat, Idoneth Deepkin, Soulblight Gravelords y Ogor Mawtribes,
  y el suplemento de Cities of Sigmar. Sus archivos exactos están registrados
  en el manifiesto enlazado abajo.

Se han actualizado los costes y las restricciones que faltaban, incluidas sus
copias en otros catálogos cuando representan la misma unidad. Los tamaños
reducidos conservan su coste propio. Los nuevos refuerzos duplican los modelos
y los puntos; los campeones siguen los límites de su warscroll.

También se han corregido Oracular Visions del Chaos Sorcerer Lord a pie y el
warscroll de Gatebreaker Mega-Gargant de Aqshy, incluida su selección de armas.
Las variantes de Aqshy de Gatebreaker y Mancrusher usan BIG y LITTLE,
respectivamente. No se vuelve a aplicar lo que ya estaba incorporado en BSData,
como las correcciones recientes de Nighthaunt, Tzeentch, Skaven y Ogors.

Ejemplos de los valores actuales de Ogors: Redd 420 puntos, Morga 420,
Gluttons 210, Hunters with Sabrefangs 170 y Maw-Cult Fanatics 10. Conviene volver
a validar las listas guardadas después de actualizar los datos.

Las FAQ generales y los planes de batalla que no tienen representación en los
catálogos se consultan en el PDF. La corrección de Rotmire Creed en **Spearhead:
Bubonic Cell** pertenece a ese modo de juego, que este repositorio no modela;
no se ha trasladado a la unidad de batalla campal. Stumblefoot Gargant ya
estaba ausente del catálogo de BSData.

## Registro de las diferencias

[El manifiesto del 23 de septiembre](erratas/2026-09-23.json) conserva la revisión
base, las fuentes, los archivos, los identificadores y las huellas del contenido
anterior y corregido. No contiene copias de los PDF. Las revisiones de los
catálogos modificados se incrementan para distribuir la actualización.

Los originales ingleses contienen la corrección de reglas; los diccionarios de
`translations/` contienen el español. Los archivos `_es.cat` y `_es.gst` se
generan con las herramientas habituales. Esta es una excepción documentada a
la regla habitual de no modificar originales: el fork difiere temporalmente
de BSData para adelantar una corrección oficial.

Desde la raíz del repositorio, en PowerShell:

```powershell
python tools/verify-official-errata.py
git fetch upstream
python tools/verify-official-errata.py --upstream upstream/main --details
```

El primer comando comprueba que los cambios locales siguen como se registraron.
El segundo comparador clasifica cada entrada:

| Resultado | Qué significa | Qué revisar |
| --- | --- | --- |
| `coincide` | BSData tiene el mismo ID y contenido corregido. | Confirmar la regla y conservar su implementación. |
| `pendiente` | BSData mantiene el contenido anterior, o aún no tiene el ID nuevo. | Mantener la corrección local y buscar también por nombre: BSData puede usar otro ID. |
| `revisar` | El contenido de BSData es distinto de ambas versiones. | Comparar las reglas y la estructura manualmente. |

La comparación ignora diferencias de formato XML, pero no reorganizaciones de
los elementos. Una coincidencia de huellas no valida por sí sola la legalidad
de una lista. Las revisiones del catálogo son metadatos y pueden requerir una
decisión independiente del contenido de las reglas.

## Cuando BSData publique su versión

1. Trabaja con el árbol limpio. Ejecuta la comparación anterior **antes del
   merge** y guarda su resultado para revisar las entradas afectadas.
2. Sigue [la guía de actualización](../ACTUALIZAR-DESDE-BSDATA.md) e integra
   `upstream/main` con un merge real. No reviertas todo el commit de erratas:
   podrías perder correcciones que BSData aún no haya publicado.
3. Revisa todas las entradas pendientes, aunque Git no señale conflictos.
   Un cambio equivalente con otro ID puede producir dos opciones duplicadas
   sin conflicto textual. Comprueba unidades, armas, mejoras, categorías,
   límites y referencias al sustituirlas.
4. Cuando ambas implementaciones representen la misma regla, adopta los IDs y
   la estructura de BSData y elimina la implementación temporal duplicada.
   Si BSData solo incorpora una parte, conserva el resto del parche local.
5. Actualiza el registro explícitamente después de revisar el cambio: ajusta
   IDs y huellas a la implementación aceptada, o archiva las entradas ya
   resueltas indicando el commit de BSData que las absorbió. No regeneres las
   huellas a ciegas para silenciar una diferencia. Adapta las pruebas si BSData
   cambia los IDs, conservando la comprobación del comportamiento.
6. Extrae y traduce las cadenas nuevas, archiva las sustituidas y regenera los
   archivos españoles según la guía. No edites los `_es` a mano.
7. Ejecuta las comprobaciones y revisa el diff antes de hacer commit y push:

```powershell
python tools/verify-official-errata.py
python tools/test-official-errata.py
python tools/verify-translation.py
python tools/verify-name-coverage.py
python tools/test-name-translation.py
git diff --check
```

El objetivo al cerrar cada errata es que los originales vuelvan a seguir la
implementación de BSData, manteniendo las traducciones y herramientas del fork.
El verificador es de solo lectura: no resuelve conflictos ni elimina parches.
